import whisper

model = whisper.load_model("tiny.en", device="cuda")

result = model.transcribe("0.wav")
print(result["text"])