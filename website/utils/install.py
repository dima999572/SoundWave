import pytube
from pydub import AudioSegment
import os

def install(url):
    save_path = "website/utils/audios/"

    yt = pytube.YouTube(url)
    title = yt.title.replace(".", "").replace(",", "")
    author = yt.author

    audio_stream = yt.streams.get_audio_only()
    audio_file = audio_stream.download(output_path=save_path)

    audio = AudioSegment.from_file(audio_file)
    output_path = audio_file[:-4] + ".mp3"
    audio.export(output_path, format="mp3")
    os.remove(f"{save_path}{title}.mp4")

    end_data = [f"{save_path}{title}.mp3", title, author]

    return end_data