import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile, os

SRATE = 16000     # tasa de muestreo
DUR = 5           # segundos

print("Grabando... habla ahora!")
audio = sd.rec(int(DUR*SRATE), samplerate=SRATE, channels=1, dtype='int16')
sd.wait()
print("Listo, procesando...")

# guarda a WAV temporal
tmp_wav = tempfile.mktemp(suffix=".wav")
write(tmp_wav, SRATE, audio)

# reconoce con SpeechRecognition
r = sr.Recognizer()
with sr.AudioFile(tmp_wav) as source:
    data = r.record(source)

try:
    texto = r.recognize_google(data, language="es-ES")
    print("Dijiste:", texto)
except sr.UnknownValueError:
    print("No se entendió el audio.")
except sr.RequestError as e:
    print("Error:", e)
finally:
    if os.path.exists(tmp_wav):
        os.remove(tmp_wav)
        
        cmd = texto.lower()

if "hola" in cmd:
    print("¡Hola, bienvenido al curso!")
elif "abrir google" in cmd:
    import webbrowser
    webbrowser.open("https://www.google.com")
elif "abrir traductor" in cmd:
    import webbrowser
    webbrowser.open("https://translate.google.com/?hl=es&sl=en&tl=es&op=translate")
elif "chiste" in cmd:
    import random
    chistes = [
        "¿Qué le dice una impresora a otra? — ¿Esa hoja es tuya o es una impresión mía?",
        "¿Por qué el libro de matemáticas se deprimió? — Porque tenía demasiados problemas.",
        "¿Cómo se despiden los químicos? — Ácido un placer."
    ]
    print(random.choice(chistes))
elif "hora" in cmd:
    from datetime import datetime
    print("Hora actual:", datetime.now().strftime("%H:%M"))
else:
    print("Comando no reconocido.")