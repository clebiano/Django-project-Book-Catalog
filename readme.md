# Capítulo 2: Guia de desenvolvimento da plataforma

## 1 Introdução  

O desenvolvimento desta plataforma já se inicia com um ambiente previamente preparado a partir da instalação de programas importantes. Para a preparação deste ambiente siga o "Guia de instalação e manutenção" do projeto e o tutorial "readme_web_dev_django" (https://docs.google.com/document/d/1idKW5nrvjKQuSFTgQGQbz5swY3EUdDXkokJXfvPqdtY/edit?usp=sharing).

## 2 Criando estrutura inicial do projeto  
- Entrando no diretório Documents/  
	`$ cd Documents/`
- Criando diretório raiz para o projeto  
	`$ mkdir vpsdb`
- Entrando no diretório raiz do projeto  
	`$ cd vpsdb/`
- Criando ambiente virtual com Python3  
	`$ virtualenv -p python3.6 venv`
- Ativando o ambiente virtual  
	`$ source venv/bin/activate`
- Salvando lista de pacotes pip para posterior instalação rápida  
	`$ pip freeze > requirements.txt`
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
	`$ django-admin.py startproject proj . ` # o "." permite que o arquivo "manage.py" seja criado na raiz do projeto  
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
- Entrar no ambiente Admin do Django  
	http://127.0.0.1:8000/admin/  
- Estrutura inicial pronta!
