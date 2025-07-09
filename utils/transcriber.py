import whisper

def transcribe(audio_path):
    try:
        model = whisper.load_model("base", device="cpu")
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"{e}")
