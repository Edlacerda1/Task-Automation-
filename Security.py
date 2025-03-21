import tkinter as tk
from ttkthemes import ThemedStyle

usuarios = {
    "user": ["Ed", 
             "Edmundo", 
             "ed", 
             "ED", 
             "eD"]
    
}
chave = "123"

def authentic(users, password, root, auth_status):
   
    if users in usuarios["user"] and password == chave:
        print("Acesso liberado!")
        auth_status["status"] = True  
        root.destroy()  
    
    else:
        print("Credenciais inválidas. Tente novamente.")


def front_authentic():
    
    root = tk.Tk()
    root.title("Autenticação")
    
    style = ThemedStyle(root)
    style.set_theme('equilux')

    screen_largura = root.winfo_screenwidth()
    screen_altura = root.winfo_screenheight()

    largura_janela = 250
    altura_janela = 150  
    
    # Centralizar janela na tela
    x = (screen_largura // 2) - (largura_janela // 2)
    y = (screen_altura // 2) - (altura_janela // 2)   
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    
    root.configure(bg="gray17")

    user_label = tk.Label(root, text="Usuário:", bg="gray17", fg="white", font=("Times", 13))
    user_label.place(x=20, y=20)

    inp_user = tk.Entry(root, bg="gray27", fg="white", font= ("times", 12, "bold")) 
    inp_user.place(x=100, y=22, width=120, height=20)

    password_label = tk.Label(root, text="Senha:", bg="gray17", fg="white", font=("Times", 13)) 
    password_label.place(x=20, y=60)

    inp_password = tk.Entry(root, show="*", bg="gray27", fg="white", font= ("times", 12, "bold"))  #* Esconde a senha
    inp_password.place(x=100, y=62, width=120, height=20)

    auth_status = {"status": False}  

    def validar_login():
        authentic(inp_user.get(), inp_password.get(), root, auth_status)
        if auth_status["status"]:
            root.quit() 
            
    btn_login = tk.Button(root, text="Entrar", command=validar_login, bg="gray17", fg="white", font=("Arial", 13, "bold"))  
    btn_login.place(x=75, y=100, width=120, height=40 )
     

    root.mainloop()
    
    return auth_status["status"]  

if __name__ == "__main__":
    if front_authentic():
        print("Login bem-sucedido!")
    else:
        print("Falha na autenticação.")