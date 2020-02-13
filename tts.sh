#!/bin/bash


# Проверяем IAM_TOKEN
if [ -z "${IAM_TOKEN}" ] ; then
    echo "Please set IAM_TOKEN"
    exit 1
fi


text=$@

# Проверяем на пустоту текста
if [ -z "${text}" ] ; then
    echo "You should provide some text"
    exit 1
else
    echo "Processing ..."
fi
# Обрезаем строку
filename="${text:0:32}"
# Образуем имя файла удаляя запрещенные симводы
filename="${filename//[ !\'\"\/\\]/_}.ogg"

curl -X POST -H "Authorization: Bearer ${IAM_TOKEN}" \
    --data-urlencode "text=${text}" \
    -d "voice=alena&lang=ru-RU&folderId=b1g28lfpue6ck5imgne3" \
    "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize" > "${filename}"

# mplayer -really-quiet 
mplayer  "${filename}"


