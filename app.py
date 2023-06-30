import eel
import vosk_script as vs
import sr_script as srs

eel.init("gui")


@eel.expose
def get_microphone_list():
    list_mic = srs.mic_list()
    eel.display_mic_list(list_mic)


@eel.expose
def recv_settings(mic, type):
    settings_list = [mic, type]
    return settings_list


@eel.expose
def vosk_script():
    result = vs.vosk_recognition()
    eel.output_to_display(result)


@eel.expose
def sr_script(mic):
    result = srs.sr_recognition(mic)
    eel.output_to_display(result)


@eel.expose
def main(mic, type_rec):
    print(mic)
    print(type_rec)

    if type_rec == "0":
        vosk_script()
    else:
        sr_script(int(mic))



eel.start("index.html", size=(500, 500))