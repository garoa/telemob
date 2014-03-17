#!/bin/bash
# rename this file to ./mng.sh for an easy way to run manage.py for
# this project in a development environment, setting all needed variables

export SECRET_KEY=VALOR-RANDOMICO-QUE-O-STARTPROJECT-GERA-PRA-VC
export RECAPTCHA_PUBLIC_KEY=CHAVE-PUBLICA-DO-RECAPTCHA
export RECAPTCHA_PRIVATE_KEY=CHAVE-PRIVADA-DO-RECAPTCHA

./manage.py $1 $2 $3 $4 $5
