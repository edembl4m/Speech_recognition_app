import speech_recognition as sr


def mic_list():
    list_mic = sr.Microphone.list_microphone_names()
    return list_mic


def sel_mic(n):
    mic = sr.Microphone(device_index=n)
    return mic


def sr_recognition(n):
    mic = sr.Microphone(device_index=n)
    r = sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source) #new чистит шум
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Речь не распознана"
    except sr.RequestError as e:
        return "Не удалось запросить результаты из службы распознавания речи Google"