import os
import time
import keyboard
from langchain_ollama import ChatOllama
import speech_recognition as sr
from kokoro import KPipeline
import soundfile as sf
import simpleaudio as sa
from langchain.output_parsers import RegexParser
from faster_whisper import WhisperModel

pipeline = KPipeline(
    lang_code="a", device="cuda"
)  # <= make sure lang_code matches voice

modelname = "smollm2"

llm = ChatOllama(
    model=modelname,
    temperature=0.5,
    base_url="127.0.0.1:11434",
)

r = sr.Recognizer()
r.pause_threshold = 1.5
conversation_history = [
    (
        "system",
        "You are a friendly AI. Have a conversation with the user.",
    )
]

pattern = r"<think>(?P<thinking>[\s\S]*?)</think>\s*(?P<final_answer>[\s\S]*)"

output_parser = RegexParser(regex=pattern, output_keys=["thinking", "final_answer"])

# Initialize the Whisper model
whisper_model = WhisperModel("turbo", device="cuda")


def process_audio():
    try:
        print("\nRecording... (Release down arrow to stop)")
        source = sr.Microphone()
        with source as source:
            print("Listening...")
            audio = r.listen(
                source,
                timeout=10,
            )

            print("responding...")
            start_recognize_time = time.time()  # Start time for recognition

            # Save the audio to a temporary file
            with open("temp.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Transcribe the audio using faster_whisper
            segments, info = whisper_model.transcribe("temp.wav")
            text = " ".join([segment.text for segment in segments])

            if text == "":
                print("Whisper could not understand audio")
                return

            end_recognize_time = time.time()  # End time for recognition
            print(
                f"Recognition duration: {end_recognize_time - start_recognize_time:.2f} seconds"
            )

            conversation_history.append(("human", text))

            start_model_time = time.time()  # Start time for model call
            ai_msg = llm.invoke(conversation_history)
            end_model_time = time.time()  # End time for model call

            finalmsg = ""

            if modelname == "deepseek-r1":
                parsed = output_parser.parse(ai_msg.content)
                finalmsg = parsed["final_answer"].strip()
            else:
                finalmsg = ai_msg.content

            conversation_history.append(("ai", ai_msg.content))

            print(
                f"Model call duration: {end_model_time - start_model_time:.2f} seconds"
            )

            start_pipeline_time = time.time()  # Start time for pipeline
            generator = pipeline(
                finalmsg,
                voice="af_heart",  # <= change voice here
                speed=1,
                split_pattern=r"\n+",
            )
            end_pipeline_time = time.time()  # End time for pipeline

            print(
                f"Pipeline duration: {end_pipeline_time - start_pipeline_time:.2f} seconds"
            )

        for result in generator:
            if result.audio is None:
                continue

            sf.write("temp.wav", result.audio, 24000, format="wav")
            wave_obj = sa.WaveObject.from_wave_file("temp.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()

            os.remove("temp.wav")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("\n✨ Ready for next prompt! Press down arrow to speak...")


print("\n✨ Ready! Press down arrow to speak...")
is_recording = False

while True:
    try:
        if keyboard.is_pressed("down"):
            if not is_recording:
                is_recording = True
                process_audio()
                is_recording = False
        time.sleep(0.1)  # Sleep briefly to prevent high CPU usage
    except KeyboardInterrupt:
        print("\nExiting...")
        break
