Lab Access Control
========================

Lab Access Control é um projeto para controlar acesso a um laboratório. O projeto tem duas partes: API Rest e aplicação em arduino.

A API Restful foi construida com o Django-Rest-Framework. A configuração para o desenvolvimento do projeto é bastante simples.


Instalação de virtualenv
========================

Recomendamos utilizar o virtualenv para separar as dependências deste projeto do ambiente python do seu sistema.
Se você estiver em um sistema Linux ou Mac OS X, você pode utilizar o virtualenvwrapper para ajudar a gerenciar
diversos virtualenvs criados para diferentes projetos.

Virtualenv
----------

Após a instalação do virtualenv, crie um ambiente e ative::

    $ virtualenv lab_access_env
    $ source lab_access_env/bin/activate

Virtualenv com virtualenvwrapper (Opcional)
------------------------------------

No Linux e Mac OSX, você pode instalar o virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
que gerencia seus ambientes virtuais e adiciona o path do projeto ao `site-directory`. É uma opção recomendada se você precisa criar vários ambientes para projetos diferentes.

A instalação é bem simples utilizando o pip::

    $ pip install virtualenvwrapper

Após a instalação adicione as seguintes linhas em seu .bash:

    $ export WORKON_HOME=~/Envs
    $ mkdir -p $WORKON_HOME
    $ source /usr/local/bin/virtualenvwrapper.sh

Com tudo configurado, é simples criar um novo ambiente com o seguinte comando:

    $ mkvirtualenv lab_access_env

Para ativar o ambiente basta fazer::

    $ workon lab_access_env

Usando virtualenvwrapper no Windows (Opcional)
----------------------------------------

Existe uma versão especial do virtualenvwrapper para Windows (https://pypi.python.org/pypi/virtualenvwrapper-win).::

    > mkvirtualenv lab_access_env

Instalando os pacotes necessários para desenvolvimento
======================================================

Dependendo de onde vocês está instalando as dependências, basta ir até o diretório do projeto aonde está o arquivo
requirements.txt e executar o seguinte (certifique-se que o seu ambiente virtual está ativo):

    $ pip install -r requirements.txt


Criando o banco de dados
========================

Para executar a aplicação pela primeira vez é necessário antes criar o banco de dados. O django faz isso automaticamente (seguindo as configurações do projeto) através do seguinte comando:

    $ python manage.py migrate

Estamos utilizando o sqlite3 que já vem instalado por padrão com o Python. Após executar este comando, o sistema irá criar um arquivo "db.sqlite3" na raiz do projeto.

Executando o projeto
====================

Com o ambiente virtual ativo, vá até o diretório do projeto Django (local onde está o manage.py) e execute o seguinte comando::

    $ python manage.py runserver

O Django roda na porta 8000 por padrão, então acesse a seguinte url no seu navegador: http://localhost:8000
