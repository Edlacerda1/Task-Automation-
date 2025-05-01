# ------------- Automação de cadastro e consulta no MicroSigma via TOTVS -------------

# // Bibliotecas
from tkinter import ttk
import tkinter as tk
import pyautogui as py
import time
import subprocess
import psutil
import keyboard
import ctypes
from PIL import Image, ImageTk
import pytesseract
from PIL import ImageGrab 
import datetime as dt
import sqlite3
from  ttkthemes import ThemedStyle
import pandas as pd
from Security import front_authentic


pytesseract.pytesseract.tesseract_cmd = r'C:/Users/elacerda/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

py.PAUSE = 0.3
py.FAILSAFE = False

if front_authentic():
   pass
else:
   print("Insira credenciais válidas.")
   exit()


def fechar_smartclient():
    app = "smartclient.exe"
    for procura in psutil.process_iter(['name']): 
        if procura.info['name'] == app: 
            procura.terminate() 
            procura.wait()  
    print("Iniciando processo...") 



def error():

     screenshot = ImageGrab.grab(bbox= (753, 398, 856, 422))
   
     texto = pytesseract.image_to_string(screenshot).strip()
     
     if texto == "Problema:":
         py.alert("Erro no cadastro")
         print("Erro de processo")
         exit()

 

def minusculo():  
    
    if ctypes.windll.user32.GetKeyState(0x14) == 1:
        keyboard.press_and_release('caps lock') 


def usuermax():
     
     screenshot = ImageGrab.grab(bbox= (761, 447, 853, 469))
     
     texto = pytesseract.image_to_string(screenshot).strip()
     
     if texto == "Problema":
         py.alert("Número de usuários excedentes")
         fechar_smartclient()
         print("Excedents users")
         exit()
 
 
def moves(item):
   
    time.sleep(1)
                    
                                                                       
    if item == "01":                                    
       py.moveTo(183, 272, duration=1)               
       print("Moveu para posição 1")  
       py.click()  
       keyboard.press("enter")
       py.moveTo(80, 194, duration=1)    
       py.click()  
                     
                   
    elif item == "02":
       py.moveTo(183, 314, duration=1)  
       print("Moveu para posição 2")   
       py.click()  
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()  
                   
                     
    elif item == "03":
       py.moveTo(183, 353, duration=1)  
       print("Moveu para posição 3")   
       py.click()  
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()  
       
                     
    elif item == "04":
       py.moveTo(183, 385, duration=1)  
       print("Moveu para posição 4")   
       py.click() 
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()   
                       
                  
    elif item == "05":
       py.moveTo(183, 425, duration=1)  
       print("Moveu para posição 5")    
       py.click() 
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()   
                   
                     
    elif item == "06":
       py.moveTo(183, 460, duration=1)  
       print("Moveu para posição 6")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()          
                     
                     
    elif item == "07":
       py.moveTo(183, 500, duration=1)  
       print("Moveu para posição 7")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()  
                     
                                       
    elif item == "08":
       py.moveTo(183, 533, duration=1)  
       print("Moveu para posição 8")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()  
                     
                     
    elif item == "09":
       py.moveTo(183, 575, duration=1)  
       print("Moveu para posição 9")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()     
                     
                     
    elif item == "10":
       py.moveTo(183, 610, duration=1)  
       print("Moveu para posição 10")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()   
       
       
    elif item == "11":
       py.moveTo(183, 645, duration=1)  
       print("Moveu para posição 11")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()
       
       
    elif item == "12":
       py.moveTo(183, 685, duration=1)  
       print("Moveu para posição 12")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()   
       
       
    elif item == "13":
       py.moveTo(183, 725, duration=1)  
       print("Moveu para posição 13")   
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()   
       
       
    elif item == "14":
       py.moveTo(183, 760, duration=1)  
       print("Moveu para posição 14")      
       py.click()   
       keyboard.press("enter") 
       py.moveTo(80, 194, duration=1)   
       py.click()       
 
             
def reworking():
   
   py.PAUSE = 0.5
   
   py.write("00")
   time.sleep(0.5)
   py.press('right')  
   time.sleep(0.1)
   py.press('right')
   time.sleep(0.1)
   py.press('right')
   time.sleep(0.1)
   py.press('right')
   time.sleep(0.1)
   py.press('right')
   time.sleep(0.1)
   
   py.write("RETRABALHO")      
   time.sleep(0.5)  
   py.press('tab')
   py.press('space')
   time.sleep(0.1)  
   py.press('space')
   time.sleep(0.1) 
   py.write("RETRABALHO")
   time.sleep(1)  
   py.press('tab')
   time.sleep(0.1)  
   py.press('space')   
   time.sleep(0.1)  
   
   py.press('right')
   time.sleep(0.1)  
   py.press('right')
   time.sleep(0.1)  
   py.press('right')
   time.sleep(0.1)  
   py.press('right')
   time.sleep(0.1)  
   py.press('right')
   time.sleep(0.1)  
   py.press('right')
   time.sleep(0.1)    
   py.press('right')
   time.sleep(1)
    
   py.write("0,01")
   time.sleep(2)
           
   py.press('down')
   time.sleep(2)
               

class Microsigma: 
   
   def __init__(self, acao, pvi, item, prod, servico, cod): 
        self.acao = acao
        self.item = item
        self.pvi = pvi
        self.prod = prod
        self.servico = servico 
        self.cod = cod

       
        if self.prod == "" or self.servico == "":
          py.alert("Insira o produto.")
          print("Reinicie o processo. ")
          exit()
          
         
        if self.acao == "cadastro": 
            self.cadastro()
            self.banco()
            
        elif self.acao == "consulta":
            self.consulta()
  
  

   def consulta(self):
        
     time.sleep(0.5)
     fechar_smartclient()
     time.sleep(1)
        
        #* Abrir o microsigma
     subprocess.Popen(["C:\\smartclient\\smartclient.exe"])
     time.sleep(5)
     minusculo()

      
     py.moveTo(997, 700, duration=0.1)
     py.PAUSE = 5 
     py.click(x=997, y=700)
     py.click(x=997, y=700)

     time.sleep(1)
        
   
     py.moveTo(815, 473, duration=0.1)
     py.click(x=815, y=473)
     

     py.write('XXXXXXXX', interval=0.1)
        
     time.sleep(0.5)   
        

     py.moveTo(715, 588, duration=0.1)
     py.click(x=715, y=588)
        
     time.sleep(0.5)
        
     py.write('XXXXXXXX', interval=0.1)
     py.PAUSE = 0.1
        

     py.moveTo(925, 647, duration=0.1)
     time.sleep(1.5)
     py.click(x=925, y=647)
        
     time.sleep(2)
     py.PAUSE = 0.1


     py.moveTo(998, 930, duration=0.1)
     time.sleep(1.5)
     py.click(x=998, y=930)
        
     time.sleep(2)
     py.PAUSE = 0.5

    
     py.moveTo(49, 502, duration=0.1)
     time.sleep(1.5)
     py.click(x=49, y=502)
        
     time.sleep(3)
        
        
     py.moveTo(68, 553, duration=0.1)
     time.sleep(1.5)
     py.click(x=68, y=553)
        
     time.sleep(5)
     usuermax() 
     usuermax()
        
       
     py.moveTo(477, 193, duration=0.1)
     time.sleep(3)
     py.click(x=477, y=193)
        
     time.sleep(2)
        
      
     py.moveTo(468, 253, duration=0.1)
     time.sleep(2.5)
     py.click(x=468, y=253)
     time.sleep(1)

      
     py.moveTo(1111, 471, duration=0.1)
     time.sleep(2)
     py.scroll(-900)
     py.scroll(-900)
        
     time.sleep(1.5)

       
     py.moveTo(951, 409, duration=0.1)
     time.sleep(1.5)
     py.click(x=951, y=409)
     time.sleep(3)

     py.write(self.pvi, interval=0.1) 
       
     time.sleep(2)
     py.PAUSE = 0.1

     py.write(self.pvi, interval=0.1) 
     time.sleep(1.5) 
     py.PAUSE = 0.1

     py.moveTo(1199, 794, duration=0.1)
     time.sleep(1.5)                               
     py.click(x=1199, y=794)


   def cadastro(self):
        
        
        self.consulta()
        
        time.sleep(5)
        
           
        
        produtos = ImageGrab.grab(bbox=(209,200, 440, 954))
       
        time.sleep(2) 
                 
        
        produtos = produtos.convert('L')
   
        time.sleep(2) 
        
          
        codigo = pytesseract.image_to_string(produtos)
        
        
        lista_informacoes = codigo.split()
         
         
        print(lista_informacoes)

          
        servico = [] 
        
        
        print(servico)
        
        time.sleep(1)
        
        tipo_produto = ImageGrab.grab(bbox=(970, 203, 1024, 620))
        
        time.sleep(2)
         
        tipo_produto = tipo_produto.convert('L')
        
        unidade = pytesseract.image_to_string(tipo_produto)
        
        lista_uni = unidade.split() 
        
        print(lista_uni)  
         
        print(type(lista_informacoes))
        print(type(lista_uni))
        
        
        print(f"{self.item}")
        print(type(self.item))
   
    
        time.sleep(0.5)
  
        
        moves(self.item)
        
        print(f"Código CR {lista_informacoes[int(self.item)]} na posição {self.item}")
        
        self.cod = lista_informacoes[int(self.item)]
        print(f"{self.cod}")
        
        
        time.sleep(1.5)

        py.moveTo(1900, 152, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=1900, y=152)
        
        
  
        time.sleep(1.5)

        py.moveTo(1900, 152, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=1900, y=152)
        
     
        time.sleep(1)

        py.moveTo(85, 581, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=85, y=581)
        
        
    
        time.sleep(7)

        py.moveTo(47, 191, duration=0.1)
        time.sleep(0.5)                               
        py.click(x=47, y=191)
   
        py.PAUSE = 0.1
        py.write('99', interval=0.3)
        
        indice = int(self.item)
         
        print(f"{lista_informacoes[indice]}")
        
        time.sleep(0.3)
        
        py.write(lista_informacoes[indice], interval=0.1)
        
        
        time.sleep(1.5)
        
        
        reworking()
        
      
        arquivo = f"{self.pvi} - {self.item}"

        origem = f"//srv-friese1/E/Arquivos/Engenharia/Engenharia CR/Engenharia_CR/Corrugado/Fichas/01 - Fichas Geral - 2025/{arquivo}.xlsm"

        try:  
          df = pd.read_excel(origem, sheet_name="Automação", header=2, usecols="C:F",engine="openpyxl")
          print("Leitura bem-sucedida!")
     
          df = df.dropna(how='all')
    
 
          sequencia = df['Seq.'].astype(str)
          centro_custo = df['C.C.'].astype(str)
          operacao = df['Trabalho'].astype(str)
          horas = df['Horas'].astype(str)
                
          
          py.PAUSE = 0.3
          
          for s, c, o, h in zip(sequencia, centro_custo, operacao, horas):
           print(f"Sequencia {s}, Centro de custo {c}, Operacao {o}, horas {h}")
           
           
                      
           if pd.isna(s) or pd.isna(c) or pd.isna(o) or pd.isna(h):
             print("No more data, carry on")
             py.press('up')
             continue
          
          
           if int(s) < 10:
                          
            py.press('enter')    
            time.sleep(1)
            py.write(f"0{s}")
            error()
            time.sleep(1)


            py.write(f"00{c}")
            error()
            time.sleep(0.5)
            py.press('right')   
            time.sleep(0.1)
            py.press('right')
            time.sleep(0.1)
            py.press('right')
            time.sleep(0.1)
            py.press('right')
            time.sleep(1)  
       
            py.write(str(o))
            error()
            time.sleep(1)  
            py.press('enter')
            py.press('space')
            time.sleep(0.1)  
            py.press('space')
            time.sleep(0.1) 
            py.write(str(o))
            error()
            time.sleep(1.5)  
            py.press('tab')
            error()
            time.sleep(0.1)  
            py.press('space')   
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)        
            py.press('right')
            time.sleep(0.1)    
            py.press('right')
            time.sleep(1)
    
            py.write(str(h))
            error()
            time.sleep(1)
            py.press('tab')    
            error()
            time.sleep(0.5)
        
            py.press('down')
            time.sleep(0.5)
            
           else:
                              
            time.sleep(1)
            py.write(str(s))
            error()
            time.sleep(0.5)
            py.press('enter')
            py.write(f"00{c}")
            error()
            time.sleep(0.5)
            py.press('right')   
            time.sleep(0.1)
            py.press('right')
            time.sleep(0.1)
            py.press('right')
            time.sleep(0.1)
            py.press('right')
            time.sleep(1)  
       
            py.write(str(o))
            error()
            time.sleep(1)  
            py.press('enter')
            py.press('space')
            time.sleep(0.1)  
            py.press('space')
            time.sleep(0.1) 
            py.write(str(o))
            error()
            time.sleep(1.5)  
            py.press('tab')
            error()
            time.sleep(0.1)  
            py.press('space')   
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)  
            py.press('right')
            time.sleep(0.1)        
            py.press('right')
            time.sleep(0.1)    
            py.press('right')
            time.sleep(1)
    
            py.write(str(h))
            error()
            time.sleep(1)
            py.press('tab')
            error()
            time.sleep(0.5)
        
            py.press('down')
            time.sleep(0.5)
       

        except Exception as e:
             print(f"Um erro ocorreu: {e}")
             
        
        py.press("up")
             
        time.sleep(1.3)
     #// IN DEV   
        # Salvar formulário
      #?  py.moveTo(x=1849, y=155)
      #?  py.click(x=1849, y=155)
        
      #?  time.sleep(1.3)
        
        # Confirmar formulário
      #?  py.moveTo(x=1208, y=639)
      #?  py.click(x=1208, y=639)
             
      #?  time.sleep(1.3)
        
        # Fechar 
      #?  py.moveTo(x=1899, y=139)
      #?  py.click(x=1899, y=139)
      #?  time.sleep(3)
        
        # Abrir ORDENS DE PRODUÇÃO 
      #?  py.moveTo(68, 553, duration=0.1)
      #?  time.sleep(1.5)
      #?  py.click(x=68, y=553)
      #?  time.sleep(5)
        
        # Configurações de filtro
     #?   py.moveTo(1511, 191, duration=0.1)
     #?   time.sleep(1.5)
     #?   py.click(x=1511, y=191)
        
        # Filtro de pedido 
     #?   py.moveTo(1772, 286, duration=0.1)
     #?   time.sleep(1.5)
     #?   py.click(x=1772, y=286)
             
        # Numero do pedido
     #?   py.moveTo(1531, 427, duration=0.1)
     #?   time.sleep(1.5)
     #?   py.click(x=1531, y=427)
     #?   time.sleep(1)
               
        # Caixa de pedido
     #?   py.moveTo(1629, 193, duration=0.1)
     #?   time.sleep(1.5)
     #?   py.click(x=1629, y=193)
     #?   py.click(x=1629, y=193)
     #?   py.write({self.pvi}, interval= 0.1)
             
        # Buscar    
     #?   py.moveTo(1813, 190, duration=0.1)
     #?   time.sleep(1.5)
     #?   py.click(x=1813, y=190)


   def banco(self):
       
    try:  
       
     conexao = sqlite3.connect("MicroSigma.db") 
     cursor = conexao.cursor() 
     
    except sqlite3.error as e:
       print(e)
       
   
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MicroSigma (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Pedidos INTEGER,
            Produto TEXT,
            Item TEXT,
            Serviço TEXT,
            Código TEXT,
            Data TEXT
        )
    ''')

    # Dados de cadastro
    cadastros = [(self.pvi, self.item ,self.prod, self.servico, self.cod, dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))] 
    
    #* Execução de insert em db
    cursor.executemany("INSERT INTO MicroSigma (Pedidos, Item, Produto, Serviço, Código, Data) VALUES (?, ?, ?, ?, ?, ?)", cadastros)

    #* Salvar as alterações no banco
    conexao.commit()

    #* Consulta de dados, retornando todos valores 
    cursor.execute("SELECT * FROM MicroSigma")
    registros = cursor.fetchall()

    #* Fechar o cursor e a conexão
    cursor.close()
    conexao.close()
   
   
    print("Processo finalizado e cadastrado no banco de dados")



def front_end():
 
    def validar_numeros(char):  
        return char.isdigit()
    
   
    def atualizar():
        data_atual = dt.datetime.now().strftime("%d-%m || %H:%M:%S")
        label_data.config(text=f"{data_atual}")  
        root.after(1000, atualizar)             


    root = tk.Tk()
    root.title("Automação MicroSigma")
    root.config(bg="gray17")
    
    
    style =ThemedStyle(root) 
    style.set_theme('equilux') 
    
    
    screen_largura = root.winfo_screenwidth()
    screen_altura = root.winfo_screenheight()
    largura_janela = 500
    altura_janela = 550
 

    x = (screen_largura // 2) - (largura_janela // 2)
    y = (screen_altura // 2) - (altura_janela // 2)   
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

   
    botao_cadastro = tk.Button(root, text="Cadastro", font="bold", bg="gray17", fg="white",  command=lambda: [Microsigma("cadastro", entrada.get(), item.get(), prod.get(), serv.get(), None)])
    botao_consulta = tk.Button(root, text="Consulta", font="bold", bg="gray17", fg="white", command=lambda: [Microsigma("consulta", entrada.get(), item.get(), prod.get(), serv.get(), None )])
    

   
    verif = (root.register(validar_numeros), '%S')

  
    label = tk.Label(root, text="Insira o PV e item:", fg="white",bg="gray17", font="bold")
    label.place(x=50, y=50)
    

    entrada = tk.Entry(root, validate='key', validatecommand=verif, font="bold", bg="gray27", fg="white")
    entrada.place(x=250, y=50, width=120)

    item = tk.Entry(root, validate='key', validatecommand=verif, font="bold", bg="gray27", fg="white")
    item.place(x=380, y=50, relwidth=0.1)
    
    label = tk.Label(root, text="Produto:", bg="gray17", font="bold", fg="white") 
    label.place(x=50, y=100)
    
    
    opcoes = ["Rolos", "Prensa", "Diversos", "Testes" ,""]
    
    
    prod = ttk.Combobox(root, font="bold", values=opcoes, state="readonly")
    prod.place(x=250, y=95, width=181)
    

    label = tk.Label(root, text="Serviço:", bg="gray17", font="bold", fg="white") 
    label.place(x=50, y=150)
    
    
    Servicos = ["Novo", "Retifica", "Regeneração", "Transformação" ,""]
    
    
    serv = ttk.Combobox(root, font="bold", values=Servicos, state="readonly")
    serv.place(x=250, y=145, width=181)
    
    # Adicionando os botões na root
    botao_cadastro.place(x=50, y=230, width=120, height=40)
    botao_consulta.place(x=200, y=230, width=120, height=40)

    # Adicionando a imagem
    imagem = Image.open("logo-friese.jpg")
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = tk.Label(root, image=imagem_tk, bg="gray17")
    label_imagem.place(y= 350,anchor="nw")


    label_data = tk.Label(root, text="", font=("Times", 14,), bg="gray17", fg="white")
    label_data.place(relx=1.0, rely=1.0, anchor="se")  

   
    atualizar()

   
    root.mainloop()

front_end()

