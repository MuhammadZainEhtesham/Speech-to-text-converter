#necessary imports
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def recorder(duration,freq):
    print('start')
    recorder = sd.rec(int(duration*freq), samplerate = freq, channels = 2)
    sd.wait()
    print('stop')
    #save recording
    wv.write("record.wav", recorder, freq, sampwidth=2)

def speech_to_text(energy_threshold):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = energy_threshold
    #Audio prepsocessing
    audio_file = sr.AudioFile('record.wav')
    with audio_file as source:
        audio_file = recognizer.record(source)
    #text detection
    result = recognizer.recognize_google(audio_data = audio_file,language = 'en-IN')
    print(result)

def main():
    recorder(3,44100)
    speech_to_text(300)

main()
