
from langchain_ollama import ChatOllama
from langchain_text_splitters import HTMLSectionSplitter
from langchain.output_parsers import RegexParser



llm = ChatOllama(
    model="deepseek-r1:7b",
    temperature=0,
    base_url="127.0.0.1:11434",
)

# Using [\s\S] instead of '.' to match all characters including newlines.
pattern = r"<think>(?P<thinking>[\s\S]*?)</think>\s*(?P<final_answer>[\s\S]*)"

output_parser = RegexParser(regex=pattern, output_keys=["thinking", "final_answer"])

messages = [
            (
                "system",
                "Role-play as Donald Trump. limit your response to 100 words.",
            ),
            ("human", "how did the democrats cheat?"),
        ]

ai_msg = llm.invoke(messages)

parsed = output_parser.parse(ai_msg.content)

print("Chain of Thought:", parsed["thinking"].strip())
print("Final Answer:", parsed["final_answer"].strip())