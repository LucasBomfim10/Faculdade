import mysql.connector
from tkinter import *


# Função para se conectar ao banco de dados
def conectar_bd():
   global conexao
   conexao = mysql.connector.connect(
       host="172.17.0.2",  # Endereço do servidor MySQL
       user="root",  # Nome de usuário do MySQL
       passwd="admin",  # Senha do MySQL
       port='3306',
       database="ursos",  # Nome do banco de dados
       autocommit=True
   )
   if conexao.is_connected():
       print("Conexão correta")


# Função para fechar a conexão com o banco de dados
def fechar_conexao():
   conexao.close()


# Função para executar uma consulta SQL e retornar os resultados
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
   sql = "SELECT * FROM urso"
   resultados = executar_consulta(sql)
   return resultados


def inserir_urso():
   sql = "CALL insert_urso('exemplo', 'exemplo', 'ex', 'ex', 1, 1)"
   executar_instrucao(sql)


def deletar_urso():
   sql = "DELETE FROM urso WHERE nome_comum LIKE 'exemplo%'"
   executar_instrucao(sql)


def update_urso():
   sql = "UPDATE urso SET nome_comum = 'exemplo_novo', foto = 'exemplo' WHERE nome_comum = 'exemplo'"
   executar_instrucao(sql)


def selecionar_view_ursos():
   sql = "SELECT * FROM view_ursos"
   resultados = executar_consulta(sql)
   return resultados


# Função para executar uma transação no banco de dados
def executar_transacao():
   try:
       cursor = conexao.cursor()


       # Iniciar transação
       cursor.execute("START TRANSACTION;")


       # Inserir novo urso
       cursor.execute("""
       INSERT INTO urso (nome_cientifico, nome_comum, status_conservacao, foto, id_habitat, id_risco_extincao)
       VALUES ('Ursus malayanus', 'Urso-malayo', 'Vulnerável', 'https://example.com/urso-malayo.jpg', 1, 2);
       """)


       # Obter ID do último urso inserido
       cursor.execute("SET @id_urso = LAST_INSERT_ID();")


       # Inserir detalhes da espécie
       cursor.execute("""
       INSERT INTO Detalhes_Especie (id_urso, alimentacao, distribuicao_geografica, populacao_estimada)
       VALUES (@id_urso, 'Omnívoro (frutas, insetos, pequenos animais)', 'Florestas do Sudeste Asiático', 1500);
       """)


       # Inserir estatísticas de população
       cursor.execute("""
       INSERT INTO Estatisticas_Populacao (id_urso, ano_estatisticas, tamanho_populacao, tendencia_populacao)
       VALUES (@id_urso, 2024, 1500, 'Estável');
       """)


       # Confirmar transação
       conexao.commit()
       resultado = "Transação concluída com sucesso!"


   except mysql.connector.Error as err:
       print(f"Erro: {err}")
       # Reverter transação em caso de erro
       conexao.rollback()
       resultado = "Transação revertida."


   finally:
       cursor.close()
       return resultado


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


   def selecionar_view():
       resultado.delete(1.0, END)
       resultado.insert(END, "Selecionando ursos da view...\n")
       lista_ursos = selecionar_view_ursos()
       for urso in lista_ursos:
           resultado.insert(END, f"{urso}\n")


   def executar_transacao_com_mensagem():
       resultado.delete(1.0, END)
       resultado.insert(END, "Executando transação...\n")
       mensagem = executar_transacao()
       resultado.insert(END, mensagem + "\n")


   root = Tk()
   root.title("Mapeamento de Ursos")
   root.configure(bg="#874b0f")


   frame = Frame(root, bg="#9a5e22")
   frame.pack(padx=20, pady=20)


   botao_select = Button(frame, text="Selecionar", command=selecionar, bg="#fffafa")
   botao_select.pack(pady=5)


   botao_inserir = Button(frame, text="Inserir", command=inserir, bg="#fffafa")
   botao_inserir.pack(pady=5)


   botao_atualizar = Button(frame, text="Atualizar", command=atualizar, gb="#fffafa")
   botao_atualizar.pack(pady=5)


   botao_deletar = Button(frame, text="Deletar", command=deletar, gb="#fffafa")
   botao_deletar.pack(pady=5)


   botao_view = Button(frame, text="Selecionar View", command=selecionar_view, bg="#fffafa")
   botao_view.pack(pady=5)


   botao_transacao = Button(frame, text="Executar Transação", command=executar_transacao_com_mensagem, bg="#fffafa")
   botao_transacao.pack(pady=5)


   resultado = Text(root, height=15, width=80. bg="e0e0e0", fg ="#000000")
   resultado.pack()


   root.mainloop()


conectar_bd()
criar_menu_inicial()
fechar_conexao()
