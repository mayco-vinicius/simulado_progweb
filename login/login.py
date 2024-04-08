#!\bin\python3
from bottle import debug, run, get, post, template, request
from os import getenv
from dotenv import load_dotenv

#Carrefa o arquivo .env
load_dotenv()

#Obtendo a variável LOGIN_PORT
PORT = getenv("LOGIN_PORT", 8080)

#Obtendo a variável LOGIN_AMBIENTE
AMBIENTE = getenv("LOGIN_AMBIENTE", "PROD")

#Verifica se o ambiente é DEV ou PROD
#DEV = desenvolvimento
#PROD = produção
dev_mode = AMBIENTE == "DEV"

#Ativa o modo debug
debug(dev_mode)

#lista de usuários existentes
lista_de_assinantes = [
    {
        "email": "admin@admin.com",
        "senha": "admin123"
    }
]

#Retorna o template com o form de login
@get("/login")
def mostra_login():
    return template("login")

#retorna o form de login para validação
@post("/login")
def login():
    email = request.forms.get("usuario")
    senha = request.forms.get("senha")

    for usuario in lista_de_assinantes:
        if (usuario["email"] == email and usuario["senha"] == senha):
            return "Encontrado"

    return "Inexistente"

#Execução do servidor
#Port = porta de escuta
#Reloader = atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)
