#Como Contribuir

```
git clone https://github.com/garoa/telemob.git
cd telemob
mv .rename-to-dotenv .env
python manage.py syncdb --migrate
python manage.py runserver
```

#Para instalar no Heroku

```
heroku create telemob
heroku labs:enable user-env-compile
heroku config:set 'SECRET_KEY=VALOR-RANDOMICO-QUE-O-STARTPROJECT-GERA-PRA-VC'
heroku config:set DEBUG=False
heroku config:set 'RECAPTCHA_PUBLIC_KEY=CHAVE-PUBLICA-DO-RECAPTCHA'
heroku config:set 'RECAPTCHA_PRIVATE_KEY=CHAVE-PRIVADA-DO-RECAPTCHA'
git push heroku master
heroku run python manage.py syncdb --migrate
```

#Para fazer deploy no Heroku

```
git push heroku master
heroku run python manage.py syncdb --migrate
```

#Gerar credenciais do reCaptcha
Para gerar as credenciais do reCaptcha acesse http://www.google.com/recaptcha 
