import speech_recognition as sr
reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

with microfone as mic:
    print("Fale algo...")
    audio = reconhecedor.listen(mic)
    print("Aguarde... reconhecendo audio...")
    print(reconhecedor.recognize_google(audio, language='pt'))

