# Prompt engineering roadmap

prompt engineers uses standard English to give instructions, set rules and structure the data to LLM because LLM understand human language. 
There also use specific formatting tricks and logical frameworks to make sure the chatbot follows directions perfectly.
1. While the text is english,prompts engineers structure it using clean layout so the AI can easily seperate structions from data. There also often use markdown (like headers and bullet points) and delimiters(like --- or ###).

# Example
* "The persona: you'are an expact financial advisor..."
* The constraints: "Never give specific stock tickers only use the data below..."
* The context tags: "[START OF CONTEXT] ...data... [END OF CONTEXT]"

2. A Trick You Should Know: "Variable Placeholders"
When building software, a prompt engineer doesn't type out the document chunks by hand every time. They write a template in English, using curly brackets {} as placeholders.

## text
"You are a customer support bot. Answer the question using only the context below."

context:
{retrieved_document_chunks}

Question:
{user_question}

Answer:
...

when a user types a question, the software automatically replaces {user_question} with the text found in the database. The final product sent to the AI is 100% plain English.

3. What does a promt engineer need to learn?
Instead of learning python or c++ a prompt engineer focuses on learning advanced communication strategies, such as:
* Chain-of-thought: Telling the AI, "Think step by step before writing the final answer."
* Few-shot-prompting: Giving the AI 2 or 3 English example of a perfect answer within the prompt so it can copy the tone.
* Negative prompting: Explicitly telling the AI what not to do (e.g., "Do not use technical jargon").

## Prompt engineering is a design skill, not a coding skill.
You learn by understanding how AI thinks and by practicing structured communication.

## Structural blueprint, and learning path you need to master prompt engineering
1. The Right Mindset: The "Smart Intern" Analogy
Treat the AI like a highly intelligent, infinitely fast intern who has zero context about your world.
* if you are vague, there will guess: if you tell the intern fix the report, there won't know what style, length, or tone you want, So they will guess(right/wrong).
* if you give guardrails, the succeed: if you tell them, "Rewrite this report. keep it under 200 words, use bullet points, and do not use technical jagorn," There will deliver exactly what you need.
* The AI doesn't know your intent: you must explicitly state your goals, rules and boundaries.

2. How to Structure Any Prompt(The CRATE Framework)
Prompt engineers use structural frameworks to organize their English text, A highly effective framework is CRATE

|___|___|___|
|component | what it does | example |
| context/ Role | defines the AI's persona and target audience. | "You are a senior UX designer reviewing a junior portfolio." |
| Request/Task | clearly states what the AI needs to do. | "Analyze the layout and list three specific areas for improvement." |
| Attribute/Constraints | sets rules, length, formatting, and tone. | "Use a supportive tone. Keep the feedback under 300 words. Format as a bullected list." |
| Template/Example | Gives a pattern to follow (few-shot prompting). | "Format your review like this: 1. Praise, 2. Critique, 3. Next steps." |
| Execution Input | The actual data or question to process. | "Here is the text describing the portfolio website: [insert text]" |


























# campus
build a campus Resources Management System

List the problems out
1. func that stores resource inventory, issue item(give), accepts return, search inventory and produces accurate reports.

data needed:
1. resource inventory; should have unique ID number, name(string), category(string), total unit(int), and availabe unit(int), Add and list, reject duplicates IDs(err).

2. Borrowing; check fellow and resource ID(auth), quantity only possitive numbers and not less than stock, log(write) a successful borrow record, regect attemp must not mutate(change) state

3. Returns; Only return quantity(int) a fellow only has as loan; update both borrowing record and invetory.

4. search/filter; case sensitive name search; filter by category.

5. Reports; show total units(int), available units(int), units(int) currently borrowed, resources with fewer than 3 available unit and resources with most units currently borrowed. if tied(same unit number of currently borrowed item), identify all tied leaders

6. structure/robustness; meaningfull functions, menu that loops until exit, input validation and helpful errors. 