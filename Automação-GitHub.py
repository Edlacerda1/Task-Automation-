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
import os
import pandas as pd
from Security import front_authentic



#TODO: Melhorias futuras futuros
#! Erro
#? Dúvidas
#* Explicações de Bibliotecas
#// Testes || comentarios pessoais
#Explicação de lógicas 


# TODO: Incrementar e polir a função de cadastro com OCR'S melhorada
# TODO: Terminar funcao de cadastro 
# TODO: Organizar e gerar arquivo em .exe
# TODO: Função para cada produto

# // Caminho do pytesseract no windowns
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/elacerda/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

py.PAUSE = 0.3

if front_authentic():
   pass
else:
   print("Insira credenciais válidas.")
   exit()

def fechar_smartclient():
    app = "smartclient.exe"
    for procura in psutil.process_iter(['name']): #* Verifica todos os software em run
        if procura.info['name'] == app: #* name é um comando interno para o nome do software
            procura.terminate()  #* Fecha o processo
            procura.wait()  #* Aguarda o término do processo
    print("Iniciando processo...") 



def minusculo():  
    
    if ctypes.windll.user32.GetKeyState(0x14) == 1:
        keyboard.press_and_release('caps lock') 



def error():
     #* Captura uma área da tela 
     screenshot = ImageGrab.grab(bbox= (761, 447, 853, 469))
        #* Usa o pytesseract para fazer OCR
     texto = pytesseract.image_to_string(screenshot).strip()
     
     if texto == "Problema":
         py.alert("Número de usuários excedentes")
         fechar_smartclient()
         print("Excedents users")
         exit()
 
 
def moves(item):
                    
                                                                       
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
             
def reworking():
   
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
    #// construtor
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
          
         
        if self.acao == "cadastro": # chamando cada def com base no filtro
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

        # Confirmar a aberturas
     py.moveTo(997, 700, duration=0.1)
     py.PAUSE = 5 # Pausa maior para garantir que o programa tenha tempo para carregar
     py.click(x=997, y=700)
     py.click(x=997, y=700)

     time.sleep(1)
        
        # Ir para user
     py.moveTo(815, 473, duration=0.1)
     py.click(x=815, y=473)
     
        
        # Digitar usuário
     py.write('xxxxxx', interval=0.1)
        
     time.sleep(2)   
        
        # Ir para senha
     py.moveTo(715, 588, duration=0.1)
     py.click(x=715, y=588)
        
     time.sleep(1.5)
        
        
     py.write('xxxxx', interval=0.1)
     py.PAUSE = 0.1
        
        # Clicar em Entrar após logar
     py.moveTo(925, 647, duration=0.1)
     time.sleep(1.5)
     py.click(x=925, y=647)
        
     time.sleep(3)
     py.PAUSE = 0.1

        # Entrar no broke
     py.moveTo(998, 930, duration=0.1)
     time.sleep(1.5)
     py.click(x=998, y=930)
        
     time.sleep(2)
     py.PAUSE = 0.5

        # Abrir FAVORITOS 
     py.moveTo(49, 502, duration=0.1)
     time.sleep(1.5)
     py.click(x=49, y=502)
        
     time.sleep(3)
        
        # Abrir ORDENS DE PRODUÇÃO 
     py.moveTo(68, 553, duration=0.1)
     time.sleep(1.5)
     py.click(x=68, y=553)
        
     time.sleep(5)
     error() 
     error()
        
        # Abrir OUTRAS AÇÕES
     py.moveTo(477, 193, duration=0.1)
     time.sleep(3)
     py.click(x=477, y=193)
        
     time.sleep(2)
        
        # Abrir VENDAS
     py.moveTo(468, 253, duration=0.1)
     time.sleep(2.5)
     py.click(x=468, y=253)
     time.sleep(1)

        # Clicar no root para rolar janela
     py.moveTo(1111, 471, duration=0.1)
     time.sleep(2)
     py.scroll(-900)
     py.scroll(-900)
        
     time.sleep(1.5)

       # Ir para pedido inicial
     py.moveTo(951, 409, duration=0.1)
     time.sleep(1.5)
     py.click(x=951, y=409)
     time.sleep(3)

     py.write(self.pvi, interval=0.1) # Pedido inicial
       
     time.sleep(2)
     py.PAUSE = 0.1

     py.write(self.pvi, interval=0.1) # Pedido final
     time.sleep(1.5) 
     py.PAUSE = 0.1

     py.moveTo(1199, 794, duration=0.1)
     time.sleep(1.5)                               
     py.click(x=1199, y=794)


   def cadastro(self):
        
        
        self.consulta()
        
        time.sleep(5)
        
           
          #* Captura dos códigos do produto 
        produtos = ImageGrab.grab(bbox=(209,200, 440, 654))
       
        time.sleep(2) 
                 
          #* Converte o texto em uma escala diferente de cores (cinza)
        produtos = produtos.convert('L')
   
        time.sleep(2) 
        
          #* OCR de cada produto completo 
        codigo = pytesseract.image_to_string(produtos)
        
          # Converte em lista 
        lista_informacoes = codigo.split()
         
         
        print(lista_informacoes)

          
        servico = [] 
        uni = []
        

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
        
        # Fechar ORDENS DE PRODUÇAO
        time.sleep(1.5)

        py.moveTo(1900, 152, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=1900, y=152)
        
        
        # Fechar ORDENS DE PRODUÇAO
        time.sleep(1.5)

        py.moveTo(1900, 152, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=1900, y=152)
        
        # Entrar em PROCESSOS PRODUTIVOS
        time.sleep(1)

        py.moveTo(85, 581, duration=0.1)
        time.sleep(1.5)                               
        py.click(x=85, y=581)
        
        
        # Incluir
        time.sleep(7)

        py.moveTo(47, 191, duration=0.1)
        time.sleep(0.5)                               
        py.click(x=47, y=191)
   
        py.PAUSE = 0.1
        py.write('99', interval=0.1)
        
        indice = int(self.item)
         
        print(f"{lista_informacoes[indice]}")
        
        py.PAUSE = 0.1
        py.write(lista_informacoes[indice], interval=0.1)
        
        
        time.sleep(1.5)
        
      
        arquivo = f"{self.pvi} - {self.item}"

        origem = f"//srv-xxxxx/E/Arquivos/xxxxxxx/xxxxxx/xxxxx_xx/xxxxxx/xxxxx/- xxxx xxxx - xxxx/{arquivo}.xlsm"

        try:  
          df = pd.read_excel(origem, sheet_name="Automação", header=2, usecols="C:F",engine="openpyxl")
          print("Leitura bem-sucedida!")
     
          df.dropna
    
 
          sequencia = df['Seq.'].astype(str)
          centro_custo = df['C.C.'].astype(str)
          operacao = df['Trabalho'].astype(str)
          horas = df['Horas'].astype(str)
                
          reworking()
          
          py.PAUSE = 0.3
          
          for s, c, o, h in zip(sequencia, centro_custo, operacao, horas):
           print(f"Sequencia {s}, Centro de custo {c}, Operacao {o}, horas {h}")
             
           if int(s) < 10:
            
            py.press('enter')    
            time.sleep(1)
            py.write(f"0{s}")
            time.sleep(1)

    
            py.write(f"00{c}")
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
            time.sleep(1)  
            py.press('enter')
            py.press('space')
            time.sleep(0.1)  
            py.press('space')
            time.sleep(0.1) 
            py.write(str(o))
            time.sleep(1.5)  
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
    
            py.write(str(h))
            time.sleep(1)
            py.press('tab')
            time.sleep(0.5)
        
            py.press('down')
            time.sleep(0.5)
            
           else:

                                    
            time.sleep(1)
            py.write(str(s))
            time.sleep(0.5)
            py.press('enter')
            py.write(f"00{c}")
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
            time.sleep(1)  
            py.press('enter')
            py.press('space')
            time.sleep(0.1)  
            py.press('space')
            time.sleep(0.1) 
            py.write(str(o))
            time.sleep(1.5)  
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
    
            py.write(str(h))
            time.sleep(1)
            py.press('tab')
            time.sleep(0.5)
        
            py.press('down')
            time.sleep(0.5)
       

        except Exception as e:
             print(f"Um erro ocorreu: {e}")
             
             
        time.sleep(1.3)
        
        # Salvar formulário
        py.moveTo(x=1849, y=155)
        py.click(x=1849, y=155)
        
        time.sleep(1.3)
        
        # Confirmar formulário
        py.moveTo(x=1208, y=639)
        py.click(x=1208, y=639)
             
        time.sleep(1.3)
        
        # Fechar 
        py.moveTo(x=1899, y=139)
        py.click(x=1899, y=139)
        time.sleep(3)
        
        # Abrir ORDENS DE PRODUÇÃO 
        py.moveTo(68, 553, duration=0.1)
        time.sleep(1.5)
        py.click(x=68, y=553)
        time.sleep(5)
        
        # Configurações de filtro
        py.moveTo(1511, 191, duration=0.1)
        time.sleep(1.5)
        py.click(x=1511, y=191)
        
        # Filtro de pedido 
        py.moveTo(1772, 286, duration=0.1)
        time.sleep(1.5)
        py.click(x=1772, y=286)
             
        # Numero do pedido
        py.moveTo(1531, 427, duration=0.1)
        time.sleep(1.5)
        py.click(x=1531, y=427)
        time.sleep(1)
               
        # Caixa de pedido
        py.moveTo(1629, 193, duration=0.1)
        time.sleep(1.5)
        py.click(x=1629, y=193)
        py.click(x=1629, y=193)
        py.write({self.pvi}, interval= 0.1)
             
        # Buscar    
        py.moveTo(1813, 190, duration=0.1)
        time.sleep(1.5)
        py.click(x=1813, y=190)


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
    
    
    cursor.executemany("INSERT INTO MicroSigma (Pedidos, Item, Produto, Serviço, Código, Data) VALUES (?, ?, ?, ?, ?, ?)", cadastros)

    
    conexao.commit()

   
    cursor.execute("SELECT * FROM MicroSigma")
    registros = cursor.fetchall()


    cursor.close()
    conexao.close()
   
   
    print("Processo finalizado e cadastrado no banco de dados")



def front_end():
    # Função para permitir somente números
    def validar_numeros(char):  
        return char.isdigit()
    
    # Função para atualizar a data e hora
    def atualizar():
        data_atual = dt.datetime.now().strftime("%d-%m || %H:%M:%S")
        label_data.config(text=f"{data_atual}") 
        root.after(1000, atualizar)           

    #* Criando a janela principal
    root = tk.Tk()
    root.title("Automação MicroSigma")
    root.config(bg="gray17")
    
    #* Inserindo o tema no root
    style =ThemedStyle(root) 
    style.set_theme('equilux') 

    #* Informações da tela
    screen_largura = root.winfo_screenwidth()
    screen_altura = root.winfo_screenheight()
    largura_janela = 500
    altura_janela = 550
 
    # Centraliza a janela
    x = (screen_largura // 2) - (largura_janela // 2)
    y = (screen_altura // 2) - (altura_janela // 2)   
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

    
    botao_cadastro = tk.Button(root, text="Cadastro", font="bold", bg="gray17", fg="white",  command=lambda: [Microsigma("cadastro", entrada.get(), item.get(), prod.get(), serv.get(), None)])
    botao_consulta = tk.Button(root, text="Consulta", font="bold", bg="gray17", fg="white", command=lambda: [Microsigma("consulta", entrada.get(), item.get(), prod.get(), serv.get(), None )])


    # Registra a validação de números
    verif = (root.register(validar_numeros), '%S')

    # Rótulo e entrada de texto
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

    # Label da data
    label_data = tk.Label(root, text="", font=("Times", 14,), bg="gray17", fg="white")
    label_data.place(relx=1.0, rely=1.0, anchor="se")  # Canto inferior direito

    # Atualização da data
    atualizar()

    # Inicia o loop principal da interface
    root.mainloop()

front_end()

