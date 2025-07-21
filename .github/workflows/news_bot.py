import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import time

# Настройка Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_news():
    """Получает последние новости с новостных сайтов"""
    news_items = []
    
    sources = [
        {
            'url': 'https://lenta.ru/rss/news',
            'name': 'Lenta.ru'
        },
        {
            'url': 'https://ria.ru/export/rss2/archive/index.xml',
            'name': 'РИА Новости'
        }
    ]
    
    for source in sources:
        try:
            print(f"Получаем новости с {source['name']}...")
            response = requests.get(source['url'], timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'xml')
            
            for item in soup.find_all('item')[:3]:  # По 3 новости с каждого источника
                title = item.title.text if item.title else ""
                description = item.description.text if item.description else ""
                link = item.link.text if item.link else ""
                pub_date = item.pubDate.text if item.pubDate else ""
                
                # Очищаем от HTML тегов в описании
                if description:
                    desc_soup = BeautifulSoup(description, 'html.parser')
                    description = desc_soup.get_text()
                
                news_items.append({
                    'title': title,
                    'description': description[:300],  # Ограничиваем длину
                    'link': link,
                    'source': source['name'],
                    'pub_date': pub_date
                })
                
        except Exception as e:
            print(f"Ошибка получения новостей с {source['name']}: {e}")
            continue
    
    return news_items

def generate_commentary(news_items):
    """Генерирует комментарий к новостям через Gemini"""
    if not news_items:
        return None
        
    # Формируем список новостей для промпта
    news_text = ""
    for i, item in enumerate(news_items, 1):
        news_text += f"{i}. {item['title']}\n"
        if item['description']:
            news_text += f"   {item['description']}\n"
        news_text += f"   Источник: {item['source']}\n\n"
    
    prompt = f"""
Проанализируй следующие новости и напиши аналитический комментарий на русском языке (300-400 слов):

{news_text}

Требования к комментарию:
- Выдели основные тренды и связи между событиями
- Проанализируй возможные последствия
- Дай контекст происходящего
- Пиши как опытный журналист-аналитик
- Будь объективным и взвешенным
- Структурируй текст с подзаголовками

Формат ответа: чистый текст без markdown разметки.
"""
    
    try:
        # Используем Gemini Pro
        model = genai.GenerativeModel('gemini-pro')
        
        # Настройки генерации
        generation_config = genai.types.GenerationConfig(
            temperature=0.7,
            top_p=0.8,
            top_k=40,
            max_output_tokens=1000,
        )
        
        print("Отправляем запрос к Gemini...")
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        # Проверяем на блокировку контента
        if response.candidates[0].finish_reason.name == "SAFETY":
            print("Контент заблокирован системой безопасности")
            return "Комментарий не может быть сгенерирован из-за ограничений безопасности."
        
        return response.text
        
    except Exception as e:
        print(f"Ошибка генерации комментария: {e}")
        return None

def save_commentary(commentary, news_items):
    """Сохраняет комментарий в файл"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    date_formatted = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # Создаем папку если её нет
    os.makedirs('commentary', exist_ok=True)
    
    # Сохраняем комментарий
    filename = f'commentary/news_commentary_{timestamp}.md'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Комментарий к новостям - {date_formatted}\n\n")
        f.write(f"{commentary}\n\n")
        f.write("---\n\n")
        f.write("## Проанализированные новости:\n\n")
        
        for i, item in enumerate(news_items, 1):
            f.write(f"**{i}. {item['title']}**\n")
            if item['description']:
                f.write(f"{item['description']}\n")
            f.write(f"*Источник: {item['source']}*\n")
            if item['link']:
                f.write(f"[Читать полностью]({item['link']})\n")
            f.write("\n")
    
    print(f"Комментарий сохранен в {filename}")

def main():
    print("=== Запуск бота комментариев новостей ===")
    print(f"Время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    
    # Проверяем API ключ
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("ОШИБКА: Не найден GEMINI_API_KEY в переменных окружения")
        return
    
    print("Получаем новости...")
    news_items = get_news()
    
    if not news_items:
        print("Не удалось получить новости")
        return
    
    print(f"Получено {len(news_items)} новостей")
    
    # Добавляем задержку для соблюдения лимитов API
    time.sleep(2)
    
    print("Генерируем комментарий...")
    commentary = generate_commentary(news_items)
    
    if commentary:
        save_commentary(commentary, news_items)
        print("✅ Комментарий успешно сгенерирован и сохранен!")
    else:
        print("❌ Не удалось сгенерировать комментарий")

if __name__ == "__main__":
    main()
