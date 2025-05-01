import sqlite3  


def excluir_dados(dell):
 try:  
    conexao = sqlite3.connect("MicroSigma.db")  
    cursor = conexao.cursor()  
    
    
    sql = """DELETE FROM MicroSigma WHERE Pedidos = ?"""
    cursor.execute(sql, (dell,))  
   
    conexao.commit()

    cursor.execute("SELECT * FROM MicroSigma")
    registros = cursor.fetchall()

   
    for registro in registros:
        print(registro)

 except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")



def atualizar_dado(valor_antigo, valor_novo, campo):
    try:
        conexao = sqlite3.connect("MicroSigma.db") 
        cursor = conexao.cursor()
        
        #! Atualiza o valor no campo especificado
        cursor.execute(f"UPDATE MicroSigma SET {campo} = ? WHERE {campo} = ?", (valor_novo, valor_antigo)) 
        #* Setando o CAMPO que será alterado, 
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"{cursor.rowcount} registro(s) atualizado(s) com sucesso.")
            
        else:
            print("Nenhum registro encontrado com esse valor.")
    
    except sqlite3.Error as e:
        print("Erro ao atualizar dado:", e)
    
    finally:
        cursor.close()
        conexao.close()
        

class banco:
  def __init__(self, acao):
      self.acao = acao
      
      if self.acao == "A":
        print("Para atualizar dados, digite um valor antigo, um novo valor e a coluna")
        old_dt = input("Valor antigo: ")
        nw_dt = input("Novo valor: ")
        cl_dt = input("Coluna: ")
        atualizar_dado(old_dt, nw_dt, cl_dt)
        
      if self.acao == "E":
        print("Para excluir dados, digite um valor existente da coluna Pedido")
        delete = input("Valor que será excluido: ")
                 
        excluir_dados(delete)
    
    
print(" A p/ Atualizar")
print(" E p/ Excluir")


banco(acao = input("Qual ação gostaria de tomar? "))

