import mysql.connector

def fct_Comitar(conexao):
    try:
        conexao.commit()
    except:
        print('# Erro ao realizar [COMMIT]. Executando [ROLLBACK].')
        try:
            conexao.rollback()
        except:
            print('# Erro ao realizar [ROLLBACK].')
        else:
            print('# [ROLLBACK] realizado com sucesso!')        
    else:
        print('# Commit realizado com sucesso!')

def fct_Executar(cursor, comando):
    print('####################################################')
    print('Executando comando SQL:')    
    print(comando)
    print('####################################################')    
    try:
        cursor.execute(comando)
    except:
        print('# Erro ao executar o comando SQL.')
    else:
        print('# Comando SQL realizado com sucesso.')

def fct_CriarBancoDados(conexao, nomebanco):   
    cursor = conexao.cursor()               
    cmdSQL = f'CREATE DATABASE IF NOT EXISTS {nomebanco}'
    cmdSQL = cmdSQL + '\n CHARACTER SET utf8mb4'
    cmdSQL = cmdSQL + '\n COLLATE utf8mb4_0900_ai_ci '
    
    fct_Executar(cursor, cmdSQL)
    fct_Comitar(conexao)    

    cursor.close()   
    fct_FechaConexao(conexao)

def fct_AbreConexao(opcao = 1):
    try:
        if opcao == 0:
            return mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
            )
        else:
            return mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='python',
            )            
    except:
        print('>> Erro ao conectar no banco de dados!')
    else:
        print('>> Conexão no banco de dados realizada com sucesso!')    
     
def fct_FechaConexao(conexao):
    conexao.close()

def fct_GravarLog(conexao, descricao):
    cursor = conexao.cursor()
    cmdSQL = f'INSERT INTO log (descricao) VALUES("{descricao}")'    
    
    fct_Executar(cursor, cmdSQL)
    fct_Comitar(conexao)    

    cursor.close()

def fct_CriarTabelaLog(conexao):
    cursor = conexao.cursor()
    cmdSQL = 'DROP TABLE IF EXISTS log;'

    fct_Executar(cursor, cmdSQL)
    fct_Comitar(conexao)    
    
    cmdSQL = '';
    cmdSQL = cmdSQL + 'CREATE TABLE IF NOT EXISTS log('
    cmdSQL = cmdSQL + '\n   id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, '
    cmdSQL = cmdSQL + '\n   data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, '
    cmdSQL = cmdSQL + '\n   descricao VARCHAR(100) NOT NULL '
    cmdSQL = cmdSQL + '\n ); '
    
    fct_Executar(cursor, cmdSQL)
    fct_Comitar(conexao)    

    cursor.close()