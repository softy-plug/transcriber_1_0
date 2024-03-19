import os

os.system("pip install SpeechRecognition moviepy")
os.system("pip install SpeechRecognition")
os.system("pip install moviepy")

import speech_recognition as sr
from moviepy.editor import AudioFileClip

def transcribe_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    
    # Transcribe the audio
    try:
        text = recognizer.recognize_google(audio_data, show_all=True)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def get_audio_duration(audio_file):
    audio = AudioFileClip(audio_file)
    return audio.duration

def save_transcript_with_timecodes(transcript, audio_duration, output_file):
    with open(output_file, 'w') as file:
        for result in transcript['alternative']:
            for word_info in result['words']:
                start_time = word_info['startTime']
                end_time = word_info['endTime']
                duration = end_time - start_time
                file.write(f"{start_time} - {end_time} ({duration}s): {word_info['word']}\n")

# Specify the path to the audio file
audio_file_path = "audio_file.wav"

# Transcribe the audio file
transcript = transcribe_audio_to_text(audio_file_path)

# Get the duration of the audio file
audio_duration = get_audio_duration(audio_file_path)

# Save the transcript with timecodes to a text file
output_file_path = "transcript.txt"
save_transcript_with_timecodes(transcript, audio_duration, output_file_path)

# softy_plug