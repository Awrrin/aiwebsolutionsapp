import speech_recognition as sr

def capturar_e_transcrever():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Fale algo...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"📝 Transcrição: {texto}")
        return texto
    except sr.UnknownValueError:
        return "Não foi possível entender o áudio."
    except sr.RequestError:
        return "Erro ao conectar com o serviço de transcrição."
