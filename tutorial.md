# Guia de desenvolvimento da plataforma

## Criando estrutura inicial do projeto
- Entrando no diretório Documents/
	`$ cd Documents/`
- Criando diretório raiz para o projeto
	`$ mkdir book_catalog`
- Entrando no diretório raiz do projeto
	`$ cd book_catalog/`
- Criando ambiente virtual com Python3
	`$ virtualenv -p python3.6 venv`
- Ativando o ambiente virtual
	`$ source venv/bin/activate`
- Salvando lista de pacotes pip para posterior instalação rápida
	`$ pip freeze > requirements-dev.txt`
- Salvando estrutura de diretórios e arquivos do projeto em forma de árvore
	`$ tree > project.tree`
- Inicializando um diretório para monitoramento de versões com git
	`$ git init`
- Adicionando a identificação do usuário
  `$ git config --global user.email "clebiano@alumni.usp.br"`
  `$ git config --global user.name "Clebiano da Costa Sá"`
- Ver status do monitoramento
  `$ git status`
- Criando arquivo .gitignore, necessário para ignorar arquivos e/ou diretórios durante o commit do projeto
	`$ touch .gitignore`
- Adicionando arquivos e diretórios ao arquivo .gitignore
	`$ echo 'venv/' >> .gitignore`
- Ver status do monitoramento
  `$ git status`
- Adicionando todas as alterações na lista de espera
  `$ git add .`
- Ver status do monitoramento
  `$ git status`
- Confirmando mudanças no projeto
  `$ git commit -m "First project commit."`
- Verificando o log dos commits
  `$ git log`
  `$ git log -p` #mostra o diff de cada commit
  `$ git log --pretty=oneline`
- Instalando o Django mais recente no ambiente virtual venv
	`$ source venv/bin/activate`
	`$ pip install --upgrade django`
- Criando o projeto inicial django no ambiente virtual venv
	`$ django-admin.py startproject book_catalog . ` # o "." permite que o arquivo "manage.py" seja criado na raiz do projeto
- Verificando se existem alterações para o banco de dados
	`$ python manage.py makemigrations`
- Migrando alterações do django para o banco de dados
	`$ python manage.py migrate`
- Testando o projeto
	`$ python manage.py runserver`
	Entre na página inicial da plataforma colocando o link http://127.0.0.1:8000/ no Browser (ex.: Chrome, Firefox ...)
- Criando uma conta administrativa
	`$ python manage.py createsuperuser`
	Username (leave blank to use 'clebiano'): 03939033383
	Email address: clebiano@alumni.usp.br
	Password: \*\*\*\*\*\*\*
- Instalação do django-rest-framework
	- `$ pip install djangorestframework`
	- `$ pip install markdown       # Markdown support for the browsable API.`
	- `$ pip install django-filter  # Filtering support`
- Adicionar `'rest_framework',` ao apps instalados em settings.py
- Entrar no ambiente Admin do Django
	http://127.0.0.1:8000/admin/
- Instalação do postman para gerenciamento de api
	- `$sudo snap install postman`
- Estrutura inicial pronta!

## Instalação em uma nova máquina
- Deletar venv
- Criar uma nova venv
 - `$ sudo apt install virtualenv`
 - `$ virtualenv -p python3.6 venv`
- `$ pip install -r requirements-dev.txt`

## APP core (principal APP)
- Criando APP core
	`$ python manage.py startapp core`

##
