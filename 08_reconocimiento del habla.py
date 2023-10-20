import speech_recognition as sr

# Crear un reconocedor de voz
recognizer = sr.Recognizer()

# Escuchar audio del micrófono
with sr.Microphone() as source:
    print("Habla algo...")
    audio = recognizer.listen(source)

# Realizar el reconocimiento de habla
try:
    texto_reconocido = recognizer.recognize_google(audio)
    print("Texto reconocido: " + texto_reconocido)
except sr.UnknownValueError:
    print("No se pudo reconocer el habla.")
except sr.RequestError as e:
    print("Error en la solicitud: {0}".format(e))
