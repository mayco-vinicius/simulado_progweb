#!\bin\python

from os import getenv
from bottle import debug, run, get, post, template, request, redirect
from dotenv import load_dotenv

# Carregando o arquivo .env para as variáveis de 
# ambiente da sessão.
load_dotenv()

# Obtendo a variável LISTA_PORT da variável de
# ambiente que foi carregado no .env 
PORT = getenv("LISTA_PORT", 8080)

# Obtendo a variável LISTA_AMBIENTE da variável de
# ambiente que foi carregado no .env 
AMBIENTE = getenv("LISTA_AMBIENTE", "PROD")

# Verificando se o ambiente é DEV ou PROD
# DEV = desenvolvimento
# PROD = produção
dev_mode = AMBIENTE == "DEV"

# Ativar modo debug
debug(dev_mode)

# Familiares
familiares = [
        "Pai",
        "Mãe",
        "Filho"
    ]

# Lista de compras existente
lista_de_compras = [
    {
        "descricao": "Arroz Cristal 5kg",
        "quantidade": 2,
        "solicitante": familiares[0],
    },
    {
        "descricao": "Feijão Barão 2kg",
        "quantidade": 4,
        "solicitante": familiares[1],
    },
    {
        "descricao": "Coca-cola 2Lt",
        "quantidade": 2,
        "solicitante": familiares[2],
    },
]

# Metodo GET no caminho / (raiz)
# Retornará o template com a lista 
@get("/")
def mostra_login():
    # Retorna o template para ser mostrado no navegador
    # enviando os dados:
    # * lista_de_compras
    # * familiares
    return template("lista", lista_de_compras=lista_de_compras, familiares=familiares)

# Metodo POST no caminho /adicionar
# Receberá o form de login para validação
@post("/adicionar")
def adicionar_item():
    # Recebe o formulário e cria um dicionário
    # para ser adicionado a lista
    item = {
        "descricao": request.forms.get("descricao"), # input name=descricao
        "quantidade": request.forms.get("quantidade"), # input name=quantidade
        "solicitante": request.forms.get("solicitante"), # select name=solicitante
    }
    # Adiciona novo dicionário com o item na lista
    lista_de_compras.append(item)
    # Redireciona para o link raiz
    redirect("/")

# Metodo GET no caminho /limpar
# Limpará a lista e redirecionará para a raiz 
@get("/limpar")
def limpar_lista():
    # Remove todos os itens da lista
    lista_de_compras.clear()
    # Redireciona para o link raiz
    redirect("/")

# Execução do servidor
# Parâmetros:
# - port: porta de escuta
# - reloader: atualizar o servidor ao editar o arquivo
run(port=PORT, reloader=dev_mode)