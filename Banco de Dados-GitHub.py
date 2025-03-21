import sqlite3  

delete = input("Digite o Produto que será excluido do banco de dados: ")

try:  
    conexao = sqlite3.connect("MicroSigma.db")  
    cursor = conexao.cursor()  

    
    sql = """DELETE FROM MicroSigma WHERE Produto = ?"""
    cursor.execute(sql, (delete,))  
   
    conexao.commit()

    cursor.execute("SELECT * FROM MicroSigma")
    registros = cursor.fetchall()

   
    for registro in registros:
        print(registro)

except sqlite3.Error as e:
    print(f"Erro no banco de dados: {e}")

