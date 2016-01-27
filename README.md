#Como Contribuir

**Ao fazer um pull-request, assegure-se de que os mantenedores do projeto sabem o seu nome e o seu e-mail. Se não tivermos essas informações, não aceitaremos seu pull-request, por melhor que seja.**

##Clonar código e instalar dependências
```
git clone https://github.com/garoa/telemob.git
cd telemob
pip install -r requirements
python manage.py syncdb --migrate
```

##Configurar ambiente
```
mv .rename-to-dotenv .env
```
Coloque no arquivo .env as credenciais do reCaptcha (http://www.google.com/recaptcha)

##Vagrant

Se você usa vagrant, basta digitar:

```
vagrant up
vagrant ssh
```

##Rodando o projeto
```
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
heroku config:set 'GTM_CONTAINER=CONTAINER-DO-GOOGLE-TAG-MANAGER'
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

#Configurar o Google Tag Manager
Através do Google Tag Manager é possível configurar o Google Analytics e outras ferramentas externas. Para configurar uma conta acesse: https://www.google.com/tagmanager
