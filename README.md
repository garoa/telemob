Para rodar em ambiente de desenvolvimento:

```
./manage.py runserver --settings=telemob.settings.local
```

Veja mais em: https://docs.djangoproject.com/en/dev/topics/settings/#envvar-DJANGO_SETTINGS_MODULE

Uma dica para quem usa virtualenvwrapper é colocar no postactivate o seguinte:

```
export DJANGO_SETTINGS_MODULE=telemob.settings.local
```

Assim quando você ativar o virtual env essa variável de ambiente é setada
não precisando passar o parâmetro --settings para rodar os comandos do manage.py

Coloque também no postdeactivate a seguinte linha:

```
unset DJANGO_SETTINGS_MODULE
```
