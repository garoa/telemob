To run:
./manage.py '--settings=telemob.settings.local'

Veja mais em: https://docs.djangoproject.com/en/dev/topics/settings/#envvar-DJANGO_SETTINGS_MODULE

Uma dica para que usa virtualenvwrapper é colocar no postactivate o seguinte:
```
export DJANGO_SETTINGS_MODULE=telemob.settings.local
```

Assim quando você ativar o virtual env essa variável de ambiente é setada
não precisando passar o parâmetro --settings para rodas os comando do manage.py

coloque também no postdeactivate a seguinte linha:
```
unset DJANGO_SETTINGS_MODULE
```
