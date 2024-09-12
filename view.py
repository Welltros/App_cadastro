# Importando banco de dados
import sqlite3 as lite
#Criando conexão  com o banco
con = lite.connect('dados.db')

dados = ['vaso','sala de estar', 'vaso que comprei ao lado','Marca chinesa','27/08/2024','100','seriexxccsx','c:imagens']
#Inserir dado no banco
with con:
  cur = con.cursor()
  query = "INSERT INTO inventario(nome,local, descricao, marca, data_da_compra,valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
  cur.execute(query,dados)    #Executa a query que salva os valores no banco de dados na tabela iventario

ver_dados =[]
#Ver dados no banco
with con:
  cur = con.cursor()
  query = "SELECT * FROM inventario" #Seleciona tudo da tabela inventario
  cur.execute(query)

  rows = cur.fetchall()
  for row in rows:
    ver_dados.append(row)
print(ver_dados)



'''parei no curso 2 aos 20minutos link https://www.youtube.com/watch?v=dV0B6xWsbJE'''