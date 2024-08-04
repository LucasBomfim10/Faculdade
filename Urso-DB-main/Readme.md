# Projeto Urso.db

## Descrição

Este é um projeto da disciplina de Banco de Dados da faculdade, desenvolvido em colaboração com a minha amiga Emanuelly. Ele usa Python para a lógica do programa e MySQL para o banco de dados. A interface gráfica é construída usando Tkinter.

## Instalação

1. Certifique-se de ter Python e MySQL instalados em seu sistema.
2. Clone este repositório para o seu sistema.
3. Instale os requisitos com 'pip install -r requirements.txt'
4. Atualize as credenciais do MySQL no arquivo `urso.py` para corresponder às suas configurações locais.

## Uso

Execute o arquivo `urso.py` para iniciar a aplicação. A interface gráfica possui botões para as seguintes operações:

- **Selecionar**: Exibe todas as entradas no banco de dados.
- **Inserir**: Insere uma nova entrada no banco de dados. Atualmente, esta função está configurada para inserir um urso chamado 'Urso Pardo'.
- **Deletar**: Deleta uma entrada do banco de dados. Atualmente, esta função está configurada para deletar o urso chamado 'Urso Pardo'.

## Funções

O arquivo `urso.py` contém as seguintes funções:

- `conectar_bd()`: Conecta-se ao banco de dados MySQL.
- `fechar_conexao()`: Fecha a conexão com o banco de dados.
- `executar_instrucao(sql)`: Executa uma instrução SQL no banco de dados.
- `executar_consulta(sql)`: Executa uma consulta SQL e retorna os resultados.
- `selecionar()`: Seleciona todas as entradas no banco de dados e as exibe na interface gráfica.
- `inserir()`: Insere uma nova entrada no banco de dados.
- `deletar()`: Deleta uma entrada do banco de dados.


