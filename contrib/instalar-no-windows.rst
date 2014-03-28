=======================================
Procedimento para instalar no Windows
=======================================

Baixar e instalar o virtualenv
================================

1. Baixe o *wheel* ``virtualenv*.whl`` de https://pypi.python.org/pypi/virtualenv/1.11.4

2. Abra o ``virtualenv*.whl`` com 7-zip ou outro utilitário de descompressão

Criar e ativar o ambiente virtual
===================================

1. Execute o script ``virtualenv.py`` com Python 2.7 informando o caminho completo do Python e do script. Use a opção ``--no-site-packages`` e informe o nome do ambiente a ser criado, neste exemplo usamos ``.venv``:

.. code-block::

  C:\Users\luciano\prj\telemob>c:\Python27\python.exe c:\Python27\virtualenv-1.11.4\virtualenv.py --no-site-packages .venv
  New python executable in .venv\Scripts\python.exe
  Installing setuptools, pip...done.

2. Execute o script ``.venv\Scripts\activate.bat``. Isso colocará o prefixo ``(.venv)`` no prompt:

.. code-block::

  C:\Users\luciano\prj\telemob>.venv\Scripts\activate.bat
  (.venv) C:\Users\luciano\prj\telemob>

3. Teste a instalação do Python. Note que a partir de agora você pode rodar o Python sem informar o caminho:

.. code-block::

  (.venv) C:\Users\luciano\prj\telemob>.venv\Scripts\activate.bat
  (.venv) C:\Users\luciano\prj\telemob>python
  Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import sys
  >>> for p in sys.path: print p
  ...

  C:\WINDOWS\SYSTEM32\python27.zip
  C:\Users\luciano\prj\telemob\.venv\DLLs
  C:\Users\luciano\prj\telemob\.venv\lib
  C:\Users\luciano\prj\telemob\.venv\lib\plat-win
  C:\Users\luciano\prj\telemob\.venv\lib\lib-tk
  C:\Users\luciano\prj\telemob\.venv\Scripts
  c:\Python27\Lib
  c:\Python27\DLLs
  c:\Python27\Lib\lib-tk
  C:\Users\luciano\prj\telemob\.venv
  C:\Users\luciano\prj\telemob\.venv\lib\site-packages
  C:\Users\luciano\prj\telemob\.venv\lib\site-packages\setuptools-0.6c11-py2.7.egg-info
  >>> ^Z
  (.venv) C:\Users\luciano\prj\telemob>


Baixar o Telemob
==================

1. Utilize o ``git`` ou um cliente ``git`` gráfico como o SourceTree para clonar o repositório https://github.com/garoa/telemob.git

1.1. Alternativamente, baixe o ``master.zip`` usando o botão **Download Zip** na coluna direita da página https://github.com/garoa/telemob, e descompacte o arquivo dentro do diretório onde quer instarlar. Neste exemplo, usamos ``C:\Users\luciano\prj\telemob\repo``.

Instalar o Telemob
====================

Com o ambiente virtual ativado você pode usar o ``pip``, e tudo o que instalar ficará dentro do diretório ``.venv``.

1. Abra o ``cmd.exe`` vá até o diretório onde encontra o arquivo ``manage.py``. Este é o diretório raiz de um projeto em Django. Em nosso exemplo, ``C:\Users\luciano\prj\telemob\repo``.

.. code-block::

  (.venv) C:\Users\luciano\prj\telemob>cd repo
  (.venv) C:\Users\luciano\prj\telemob\repo>


2. Para experimentar o projeto de uma forma simplificada, sem usar PostresSQL e sem o servidor ``gunicorn``, use o ``pip`` com o arquivo de requisitos ``simple-requirements.txt`` desta maneira:

.. code-block::

  (.venv) C:\Users\luciano\prj\telemob\repo>pip install -r simple-requirements.txt
  Downloading/unpacking Django==1.6.2 (from -r simple-requirements.txt (line 1))
  ...
  ... muitas e muitas linhas omitidas ...
  ...
  Successfully installed Django South django-localflavor django-localflavor-br Unipath distr
  ibute dj-database-url dj-static python-decouple django-recaptcha static pystache
  Cleaning up...

  (.venv) C:\Users\luciano\prj\telemob\repo>

3. Copie o arquivo ``.env-for-local-testing`` para ``.env``:

.. code-block::

  (.env) C:\Users\luciano\prj\telemob\repo>copy .env-for-local-testing .env

4. Rode o script ``manage.py`` com o comando ``syncdb`` e a opção ``--migrate``. Você terá que criar um usuário administrador para o Django:

.. code-block::

  (.venv) C:\Users\luciano\prj\telemob\repo>python manage.py syncdb --migrate
  Syncing...
  Creating tables ...
  Creating table django_admin_log
  Creating table auth_permission
  Creating table auth_group_permissions
  Creating table auth_group
  Creating table auth_user_groups
  Creating table auth_user_user_permissions
  Creating table auth_user
  Creating table django_content_type
  Creating table django_session
  Creating table south_migrationhistory

  You just installed Django's auth system, which means you don't have any superusers defined
  .
  Would you like to create one now? (yes/no): yes
  Username (leave blank to use 'luciano'):
  Email address:
  Password:
  Password (again):
  Superuser created successfully.
  Installing custom SQL ...
  Installing indexes ...
  Installed 0 object(s) from 0 fixture(s)
  Migrating...
  Running migrations for main:
   - Migrating forwards to 0005_auto__chg_field_contact_result.
   > main:0001_initial
   > main:0002_auto__add_helptext__add_field_contact_result__add_field_politician_cat
   > main:0003_auto__chg_field_contact_politician__del_unique_contact_politician__chg
   > main:0004_auto__add_field_politician_parliamentary_name
   > main:0005_auto__chg_field_contact_result
   - Loading initial data for main.
  Installed 513 object(s) from 1 fixture(s)

  Synced:
   > django.contrib.admin
   > django.contrib.auth
   > django.contrib.contenttypes
   > django.contrib.sessions
   > django.contrib.messages
   > django.contrib.staticfiles
   > south
   > captcha

  Migrated:
   - telemob.main

  (.venv) C:\Users\luciano\prj\telemob\repo>

Executar e testar o Telemob localmente
========================================

1. Rode o script ``manage.py`` com o comando ``runserver``:

.. code-block::

  (.env) C:\Users\luciano\prj\telemob\repo>python manage.py runserver
  Validating models...

  0 errors found
  March 18, 2014 - 18:44:49
  Django version 1.6.2, using settings 'telemob.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.

2. Acesse a URL ``http://127.0.0.1:8000/`` com seu navegador preferido!

