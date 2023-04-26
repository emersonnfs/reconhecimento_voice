import speech_recognition as sr
import os
reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    print("deseja abrir sua agenda?")
    audio= reconhecedor.listen(mic)
    print("Loading")
    resposta=reconhecedor.recognize_google(audio, language='pt')
    if resposta == "sim":
        os.system('agenda.txt')
    else:
        print("ok, valeu otário")