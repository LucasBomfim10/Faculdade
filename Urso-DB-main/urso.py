import mysql.connector
from tkinter import *


# Função para se conectar ao banco de dados
def conectar_bd():
    global conexao
    conexao = mysql.connector.connect(
        host="127.0.0.1",  # Endereço do servidor MySQL
        user="root",  # Nome de usuário do MySQL
        passwd="admin",  # Senha do MySQL
        port='3306',
        database="ursos",  # Nome do banco de dados
        autocommit=True
    )
    if conexao.is_connected():
        print("conexao correta")


# Função para fechar a conexão com o banco de dados
def fechar_conexao():
    conexao.close()


# Função para executar uma consulta SQL e retornar os resultados
# Retorna
def executar_consulta(sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados


# Função para executar uma instrução SQL que pode assumir insert, update, delete
def executar_instrucao(sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    cursor.close()


# Funções para as operações do CRUD
def selecionar_todos_ursos():
    #resultado.delete(1.0, END)
    sql = "SELECT * FROM urso"
    resultados = executar_consulta(sql)
    
    return resultados

def inserir_urso():
    sql = ("INSERT INTO urso (nome_cientifico, nome_comum, status_conservacao, foto, id_habitat, "
           "id_risco_extincao)VALUES ('exemplo', 'exemplo', 'ex', 'ex', 1, 1)")
    executar_instrucao(sql)

def deletar_urso():
    sql = "DELETE FROM urso WHERE nome_comum LIKE 'exemplo%'"
    executar_instrucao(sql)

def update_urso():
    sql = "UPDATE urso SET nome_comum = 'exemplo_novo', foto = 'exemplo' WHERE nome_comum = 'exemplo'"
    executar_instrucao(sql)

# Criar a interface gráfica
def criar_menu_inicial():
    def selecionar():
        resultado.delete(1.0, END)
        resultado.insert(END, "Selecionando todos os ursos...\n")
        lista_ursos = selecionar_todos_ursos()
        for urso in lista_ursos:
            resultado.insert(END, f"{urso}\n")

    def inserir():
        resultado.delete(1.0, END)
        resultado.insert(END, "Inserindo um urso...\n")
        inserir_urso()
        resultado.insert(END, "Urso inserido com sucesso.\n")

    def deletar():
        resultado.delete(1.0, END)
        resultado.insert(END, "Deletando um urso...\n")
        deletar_urso()
        resultado.insert(END, "Urso deletado com sucesso.\n")

    def atualizar():
        resultado.delete(1.0, END)
        resultado.insert(END, "Atualizando um urso...\n")
        update_urso()
        resultado.insert(END, "Urso atualizado com sucesso.\n")

    root = Tk()
    root.title("Menu Inicial")

    frame = Frame(root)
    frame.pack(padx=20, pady=20)

    botao_select = Button(frame, text="Selecionar", command=selecionar)
    botao_select.pack(pady=5)

    botao_inserir = Button(frame, text="Inserir", command=inserir)
    botao_inserir.pack(pady=5)

    botao_atualizar = Button(frame, text="Atualizar", command=atualizar)
    botao_atualizar.pack(pady=5)

    botao_deletar = Button(frame, text="Deletar", command=deletar)
    botao_deletar.pack(pady=5)

    resultado = Text(root)
    resultado.pack()

    root.mainloop()

conectar_bd()
criar_menu_inicial()
fechar_conexao()