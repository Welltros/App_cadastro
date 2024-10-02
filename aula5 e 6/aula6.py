def criar_tabelas():
try:
 #abertura da conexão
conexao = conector.connect('registro_notas.db')
 #aquisição de um cursor
cursor = conexao.cursor()
 #execução de comandos SQL
sql1 = '''CREATE TABLE if not exists tbaluno (
matricula INTEGER NOT NULL,
nome TEXT NOT NULL,
curso TEXT NOT NULL,
 PRIMARY KEY (matricula) 
  );'''
sql2 = '''CREATE TABLE if not exists tbnota (
item INTEGER PRIMARY KEY AUTOINCREMENT,
valor FLOAT NOT NULL,
matricula INTEGER NOT NULL,
 FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
 );'''
cursor.execute(sql1)
cursor.execute(sql2)
 #efetivação do comando
conexao.commit()
print('Banco de dados ok')
except conector.DatabaseError as err:
print('Erro de banco de dados',err)
finally:
 #fechamento das conexões
if(conexao):
cursor.close()
conexao.close()
#fim da função
criar_tabelas()