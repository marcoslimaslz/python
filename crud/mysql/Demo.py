import mysql.connector
from funcoes import *
import time

#Estou conectando no mysql 
conexao = fct_AbreConexao(0)

#Estou criando o banco de dados com nome de 'python'
fct_CriarBancoDados(conexao, 'python');

#Estou conectando no banco de dados 'python'
conexao = fct_AbreConexao()

#Estou criando a tabela de log
fct_CriarTabelaLog(conexao)

#Estou gravando os dados na tabela de log
fct_GravarLog(conexao, "Sistema iniciado.")

#Espera 10 segundos
time.sleep(10)

#Estou gravando os dados na tabela de log
fct_GravarLog(conexao, "Sistema fechado.")

#Fechando a conexao com o banco dedados
fct_FechaConexao(conexao)

#Fim
print('####################################################')
print('Fim do programa.')
print('####################################################')