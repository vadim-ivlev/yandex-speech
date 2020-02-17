import sys
import re
import requests
import os


def read_text(txt, num):
    name = get_name(num, txt)
    if name == "":
        return
    save_sound_to_file(txt, name)


def get_name(num, txt):
    s = txt[0:32]
    s = s.strip()
    if s == "":
        return ""
    s = re.sub(r"[\s!,\"'].","_",s, flags=re.MULTILINE)
    return "{:0>3d} {}.ogg".format(num, s)


def save_sound_to_file(txt, file_name):
    # s = re.sub(r'[\s\n\r].',' ',txt, flags=re.MULTILINE )
    s = re.sub(r'\s.',' ',txt, flags=re.MULTILINE )
    s = s.strip()
    s = s+"."
    print(s)

    iam_token = os.environ.get('IAM_TOKEN')
    url = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
    header = {"Authorization":"Bearer "+iam_token}
    payload = {
        "voice":"alena",
        "lang":"ru-RU",
        "folderId":"b1g28lfpue6ck5imgne3",
        "text": s+"."
    }
    response = requests.post(url, data=payload, headers=header, stream=True)
    # Throw an error for bad status codes
    response.raise_for_status()
    with open(file_name, 'wb') as handle:
        for block in response.iter_content(1024):
            handle.write(block)   
    
    print("File written. ", file_name)
    os.system("mplayer '{}'".format(file_name))

 
# -------------------------------

if os.environ.get('IAM_TOKEN') is None:
    print("No IAM_TOKEN")
    exit(1)


if len(sys.argv) < 2:
    print("Please, provide a file name as the first argument.")
    exit(1)

file_name = sys.argv[1]

with open(file_name) as f:
    text = f.read()
    sentences = text.split(".")


counter = 0
for sentence in sentences :
    read_text(sentence, counter)
    counter += 1


