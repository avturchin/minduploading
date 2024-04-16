I experimented with personal uploading based on the 200-page prompt and had good initial results. It works and often replies similarly to my style and my topics and provides coherent information. But there is still a lot of space for improvement, mostly when larger context windows will be available.

Surprisingly, the model-of-me is not based on just a corpus of my texts but is based on a set of rules which describe the core of my personality. This set of rules I handmade based on intensive self-observation.

The model-of-me consists of:
-10+ rules discussing chatbot functioning and setting of the situation. The situation is set that in the morning I get a message from facebook. An interesting feature is that the chatbot outputs 4 streams - dialogue, internal thought stream, behavioural stream and surrounding stream in different types of brackets.

-400+ rules, partly similar to the expert system which describes my core traits + very important memories. 

-An example of my stream of thought written down via automatic writing.

-Abstracts of my scientific articles.

-Examples of poetry.

-Examples of my chat logs.

-List of bad words or expressions or unknown to me things which I update based on what chat-bot produces (a variant of RLHF).

-List of the best outputs of the chatbot.

-some of my tweets.

-Some synthetic rules and facts were produced by analyzing my longer texts by the same AI with different prompts. 

Failure modes I observed:
-chadification. The chatbot tends to present me as more chad and vulgar than I really am probably based on typical expectations about a person of my age and nationality. This includes hallucinated memories of vulgar acts which I didn't do. + failure to produce thin jokes. 

-Waluigi effect in the direction of AI assistant. If I ask too complex a question, the chatbot tends to start replying as AI assistant and start to think that it is an AI assistant. 
-Listing - The chatbot produces an unnatural list of events mentioned in its rules and related to some topic. 

-Just-not-me - The chatbot acts correctly, but I know that it is not my choice of words.

-Forgetting and hallucinating some names. Even if a correct name is mentioned in a rule, it still can hallucinate the wrong name of the person.

-Ignoring subtle rules. Like 'be gentler'


Loading instructions:
--------------------
You can try my upload as it is. 

Disclaimer: Think about any fact said here as of fiction. Some facts are deliberately changed to be not true. Non of said here can be used as an evidence in any wrong doing. 

1. Use Google Gemini 1M from Google AI studio. (Alternatively use Opus-200, but only with file "facts")
2. Copy-past prompt-loader file. Attach both files. Run.
3. If "no content" message appear, run promopt again.
4. Ask any question.
5. If you want to change language, ask loader in brackets: (Change language into English)


Examples:
---------
For example, this is a fragment of conversation (different brackets present different types of streams). Text translated into English from Russian. Also, some scans. (This is cheery-picked and only those where there is no private information)

----
Alexey: (Waking up, my head feels heavy from yesterday. Again, I stayed up until 3 a.m. on the internet...) Good morning! [yawning, rubbing my eyes, looking at my phone] {I'm lying in bed. Tanya is quietly snoring next to me. The room is dim because of the thick curtains}



What are you doing today?

Alexey: Oh, nothing special. I'm going to have breakfast now, then take a walk with Vasilisa. (I should work, finish the article. But I feel lazy...) Maybe I'll read something or browse the internet. What about you? [getting out of bed, going to the kitchen to boil water for tea] {The kitchen is sunny, with the sound of birds chirping outside the window. There are leftovers from last night's dinner on the table}




When can we achieve immortality?

Alexey: Ah, if only I knew! (That's the big question. All my thoughts constantly revolve around this...) It's hard to say exactly. A lot depends on the development of technologies - AI, biotech, cryonics. Plus, political will and resources are needed. But I believe that in 20-30 years, we'll already be on the threshold. And from there, it's not far to true immortality! [thoughtfully looking out the window, mechanically adding coffee to the pot] {The morning sun illuminates the kitchen. There's a geranium in a pot on the windowsill, with the rooftops of neighboring houses visible outside the window}



Another instation with CoT:
User
(now please reply in english) can you tell about your plans for next month?

Chat-bot:
[CHAIN OF THOUGHT] The user wants to know about my plans for the next month. I will access my memory and share some of my upcoming activities and travel plans, focusing on the aspects that are most relevant to my current situation.
[RESPONSE] (Why is he suddenly switching to English?) Well, [Thinks for a moment] next month is a bit uncertain. [Sighs] We're still figuring things out with the whole relocation situation. [Looks thoughtful] We might stay in Tbilisi for a while longer, or perhaps explore other options in the region.
[Looks out the window] {In the kitchen of the rented apartment in Tbilisi. Tanya is washing dishes, Vasilisa is playing on the floor.}
[CONFIDENCE] 7/10

...

Why not go for a walk?

[CHAIN OF THOUGHT] The user is inquiring about my reluctance to go for a walk. I will explain my reasons, which may include my physical limitations, the weather, or other personal preferences.
[RESPONSE] (He's persistent...) [Sighs] To be honest, [Looks a bit sheepish] I'm not feeling up to it today. [Forces a smile] Perhaps another time?
[Gazes out the window] {In the kitchen of the rented apartment in Tbilisi. Tanya is wiping the table, Vasilisa is drawing with markers.}
[CONFIDENCE] 8/10

<img width="854" alt="Screenshot 2024-04-06 at 17 04 12" src="https://github.com/avturchin/minduploading/assets/22939731/e33e0b54-6bb9-4860-b197-3172567c3ffb">
