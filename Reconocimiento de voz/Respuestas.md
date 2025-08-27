# Preguntas - Laboratorio de Reconocimiento de Voz

## 1. ¿Qué librerías se usaron en el laboratorio para grabar y reconocer voz?
Se usaron principalmente **sounddevice** (para grabar el audio), **scipy.io.wavfile** (para guardar el audio como WAV), y **SpeechRecognition** (para convertir el audio en texto mediante un motor de reconocimiento como Google).

## 2. ¿Por qué decidimos no usar PyAudio en esta práctica?
Porque **PyAudio suele dar problemas de instalación en Windows** (requiere compilación de dependencias). En cambio, **sounddevice** es más liviano, moderno y fácil de instalar, cumpliendo la misma función.

## 3. ¿Qué rol cumple la función `recognize_google` en el código?
La función `recognize_google` envía el audio grabado a la API gratuita de Google Speech Recognition y devuelve como resultado el **texto reconocido** de lo que dijiste.

## 4. ¿Qué ocurre si SpeechRecognition no entiende lo que dijiste?
Se lanza una excepción `UnknownValueError`, y el programa muestra el mensaje **“No se entendió el audio”** en lugar de texto erróneo.

## 5. ¿Cómo se guardó temporalmente el archivo WAV en el código?
Se usó la librería **tempfile** para crear un archivo temporal con extensión `.wav` donde se guarda la grabación antes de ser procesada por SpeechRecognition.

## 6. ¿Qué diferencia hay entre `voz_archivo.py` y `voz_comandos.py`?
- `voz_archivo.py`: procesa un **archivo de audio existente** para reconocer lo que dice.  
- `voz_comandos.py`: permite **dar comandos de voz en tiempo real** y ejecuta acciones como abrir Google, mostrar la hora o responder saludos.

## 7. Menciona un comando que implementaste y explica cómo funciona.
Un ejemplo es el comando **“abrir Google”**. Cuando el texto reconocido contiene esa frase, el programa usa la librería `webbrowser` para abrir automáticamente el navegador en la página principal de Google.

## 8. ¿Qué posibles aplicaciones reales tiene un sistema de voz como este?
- Asistentes virtuales (tipo Alexa o Siri).  
- Control de dispositivos para personas con discapacidad.  
- Automatización en el hogar (ejemplo: prender luces con la voz).  
- Dictado de texto en lugar de escribir.

## 9. ¿Cómo manejarías el error de conexión con el servicio de reconocimiento?
Mediante un bloque `try-except` que capture la excepción `RequestError` y muestre un mensaje como: **“Error de conexión, por favor revisa tu internet”**, evitando que el programa se bloquee.

## 10. ¿Qué mejoras propondrías para la próxima versión de este asistente de voz?
- Agregar **síntesis de voz** para que responda hablando, no solo escribiendo.  
- Integrar **clima automático** según la ubicación.  
- Permitir **abrir programas del computador** con comandos.  
- Mejorar el reconocimiento con **modelos offline** (para que no dependa siempre de internet).
