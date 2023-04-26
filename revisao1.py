from gtts import gTTS
from playsound import playsound

msg = "Testando 1 2 3"

audio = gTTS(msg, lang='pt')
audio.save('teste.mp3')
playsound('teste.mp3')