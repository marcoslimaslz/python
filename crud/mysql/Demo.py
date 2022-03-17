import mysql.connector
from funcoes import *
import time

#Estou conectando no mysql 
conexao = AbreConexao(0)

#Estou criando o banco de dados com nome de 'python'
CriarBancoDados(conexao, 'python');

#Estou conectando no banco de dados 'python'
conexao = AbreConexao()

#Estou criando a tabela de log
CriarTabelaLog(conexao)

#Estou gravando os dados na tabela de log
GravarLog(conexao, "Sistema iniciado.")

#Espera 10 segundos
time.sleep(10)

#Estou gravando os dados na tabela de log
GravarLog(conexao, "Sistema fechado.")

#Fechando a conexao com o banco dedados
FechaConexao(conexao)

#Fim
print('Fim do programa.')