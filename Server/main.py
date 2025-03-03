from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_community.utilities.twilio import TwilioAPIWrapper
from fastapi import FastAPI, Form
from langchain.output_parsers import RegexParser
from os import getenv

load_dotenv()
app = FastAPI()


model = "smollm2"
twilio = TwilioAPIWrapper(
    account_sid=getenv("TWILIO_ACCOUNT_SID"),
    auth_token=getenv("TWILIO_AUTH_TOKEN"),
    from_number=getenv("TWILIO_FROM_NUMBER"),
)

llm = ChatOllama(
    model=model,
    temperature=0,
    base_url="127.0.0.1:11434",
    max_tokens=100,
)

pattern = r"<think>(?P<thinking>[\s\S]*?)</think>\s*(?P<final_answer>[\s\S]*)"

output_parser = RegexParser(regex=pattern, output_keys=["thinking", "final_answer"])


@app.post(
    "/sms", summary="Webhook endpoint to receive incoming SMS messages from Twilio"
)
async def sms_webhook(
    From: str = Form(...),
    Body: str = Form(...),
):
    """
    This endpoint receives SMS messages from Twilio. Make sure you have configured your Twilio number's
    webhook URL to point to this endpoint (for example, https://yourdomain.com/sms).

    The Twilio wrapper from langchain_community is used to process the incoming message.
    """
    if Body:
        # Log incoming message details (for debugging)
        print(f"Received SMS from {From}: {Body}")

        messages = [
            (
                "system",
                "You are a helpful assistant. 160 characters limit",
            ),
            ("human", Body),
        ]
        ai_msg = llm.invoke(messages)

        print("AI Response:", ai_msg.content)

        if model == "deepseek-r1":
            parsed = output_parser.parse(ai_msg.content)
            print("Chain of Thought:", parsed["thinking"].strip())
            print("Final Answer:", parsed["final_answer"].strip())
            twilio.run(parsed["final_answer"].strip(), From)
        else:
            twilio.run(ai_msg.content.strip(), From)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
