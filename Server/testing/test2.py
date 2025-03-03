from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="127.0.0.1:11434",
    
    
)


messages = [
            (
                "system",
                "You are a property manager. You will use tools to register a tenants issue, and with the permission of the landlord, contact a contractor.",
            ),
            ("human", "roof collapsed"),
        ]

ai_msg = llm.invoke(messages)

print(ai_msg.content)