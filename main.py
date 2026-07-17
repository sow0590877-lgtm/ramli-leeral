# 1. Installer xaralay AI Whisper ak tools yi koy jàpple
!pip install git+https://github.com 
!pip install ffmpeg-python

import whisper
from google.colab import files

print("--- TÀMBALI LIGGÉEY BI ---")

# 2. Lii day ubbé sa dossier téléphone/ordinateur ngir nga tann sa video dëgg dëgg
uploaded = files.upload()
video_path = list(uploaded.keys())[0]
print(f"Sufé! Video bi duggu na, turam mooy: {video_path}")

# 3. Mu ngi jël sa xarala bi gëna dëggër (Model AI bu Whisper)
print("Maa ngi sàkk xaralay AI bi...")
model = whisper.load_model("base")

# 4. AI bi mu ngi tàmbalee déglu video bi, firi ko ci Angale baat par baat
print("Maa ngi déglu video bi ak simili yi (Loolu mën na jël tuuti minit)...")
result = model.transcribe(video_path, task="translate")

# 5. Mbindu faylu SRT bu am simili yi par minit
srt_filename = "subtitles.srt"
with open(srt_filename, "w", encoding="utf-8") as srt_file:
    for i, segment in enumerate(result['segments'], start=1):
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text'].strip()
        
        # Fexal simili yi ci anam bu dëppoo
        def format_time(seconds):
            hrs = int(seconds // 3600)
            mins = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            ms = int((seconds % 1) * 1000)
            return f"{hrs:02d}:{mins:02d}:{secs:02d},{ms:03d}"
        
        srt_file.write(f"{i}\n{format_time(start_time)} --> {format_time(end_time)}\n{text}\n\n")

print(f"Sufé! Sa simili mat na sekk ci {srt_filename}")

# 6. Lii day télé sargé (download) faylu SRT bi ci sa téléphone/ordinateur ci saasa rekk!
files.download(srt_filename)
print("Faylu SRT bi wàcc na ci sa téléphone!")
