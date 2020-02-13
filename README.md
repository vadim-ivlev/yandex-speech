Yandex speech API
=============

https://cloud.yandex.ru/docs/speechkit/quickstart

Подготовка
---------

Получение идентификатора каталога
    
    yc resource-manager folder get default
    yc resource-manager folder list



Получить IAM-токен

    export IAM_TOKEN=`yc iam create-token`

или

    . get-iam-token.sh

Использование
--------

    ./tts.sh Привет Мир!



Notes
------
https://askubuntu.com/questions/44443/command-line-audio-players

for OGG/OPUS streams

    wget -qO- http://ai-radio.org/128.opus | opusdec - - | aplay -qfdat 
    be sure you have installed opus packages

for listen OGG/Vorbis radio stream just write

    ogg123 http://ai-radio.org


fish
-----
in `~/.config/Code/User/settings.json`

    "terminal.integrated.shell.linux": "/home/vadim/anaconda3/bin/fish",
