import os
import whisper
import subprocess

# Step 2: Transcribe with Whisper
print("🎙️ Transcribing with Whisper...")
model = whisper.load_model("medium")
result = model.transcribe("recruter_audio.mp3")  # <-- fixed extension

# Step 3: Save transcript
with open("recruter_transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Done! Transcript saved to 'recruter_transcript.txt'")
