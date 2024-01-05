from openai import OpenAI

client = OpenAI()

with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
    )
    print(transcript.text)