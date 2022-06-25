from pydub import AudioSegment
from pydub.playback import play


def get_audio_out_file(path, stem):
    p = path.rsplit(".", 1)
    return p[0] + stem + "." + p[1]


def create_blank_audio(audio_in_file, duration=1000 * 60 * 3):
    audio_out_file = get_audio_out_file(audio_in_file, "_out")
    # create 1 sec of silence audio segment
    one_sec_segment = AudioSegment.silent(duration)  # duration in milliseconds

    # read wav file to an audio segment
    song = AudioSegment.from_wav(audio_in_file)

    # Add above two audio segments
    final_song = song + one_sec_segment
    # Either save modified audio
    final_song.export(audio_out_file, format="wav")
    return audio_out_file
    # Or Play modified audio
    play(final_song)
