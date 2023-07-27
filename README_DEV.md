# criar ambiente virtual: python3 -m venv venv 
# ativar ambiente virtual: source venv/bin/activate
# baixar biblioteca django: pip install django - para atualizar, caso necessário: pip install --upgrade pip
# criar arquivos base em projetos django: django-admin startproject aula_django . (core da aplicação)
# Utilizar o comando acima como escrito para nao criar subpastas
# Django: MVT (models, views, template), 
# models: onde ficam os arquivos que fazem conexão com o banco de dados, 
# viwes: onde fica a lógica do software - do nosso projeto, 
# template: onde fica a interface do nosso sistema (html, jason, css...)
# criaçao de subdivisao em micro aplicações; 
# criar uma app com o nome de interesse: python3 manage.py startapp autenticacao
# {% %} tag do django
# request com parâmetros GET (através da URL) e POST
# Requisição com GET para renderizar minha página;
# Requisição por POST é para retornar por json; 
# Passo 1: cria a url - chama a view.xxx
# Passo 2: criar a função (xxx) chamada na view no item anterior;
# CRUDE (Create, Read, Update, Delete)
# Tabelas relacionais: De muitos pra um; De um pra um; De muitos pra muitos
