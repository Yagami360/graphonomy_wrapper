FILE_ID=18WiffKnxaJo50sCC9zroNyHjcnTxGCbk
FILE_NAME=deeplab_v3plus_v3.pth
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

mkdir -p ./data/pretrained_model
mv ${FILE_NAME} ./data/pretrained_model/