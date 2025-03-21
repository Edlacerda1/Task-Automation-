import sqlite3  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def conectar_banco():
    try:
        conexao = sqlite3.connect("MicroSigma.db", check_same_thread=False) #* check_same_thread permite o uso do banco em diferentes códigos
        return conexao
    except sqlite3.Error as e:
        st.error(f"Erro ao conectar ao banco: {e}")
        return None


def buscar_dados():
    
    conexao = conectar_banco()
    
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT Produto, Serviço FROM MicroSigma")
        registros = cursor.fetchall()

      
        colunas = ["Produto", "Serviço"]
        df = pd.DataFrame(registros, columns=colunas) #* Inserindo dados do Banco em um dataframe
        return df


def banco():
    
    conexao = conectar_banco()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT Produto, Serviço, Código, Data FROM MicroSigma")
        registros = cursor.fetchall()
        conexao.close()  

        colunas = ["Produto", "Serviço", "Código", "Data"]
        dfi = pd.DataFrame(registros, columns=colunas)
        return dfi


st.title("Dashboard de Produtos e Serviços 📊")

df = buscar_dados()
dfi = banco()

if st.sidebar.button("Exibir Gráfico Produto x Serviço"):
    
    if df is not None and not df.empty:
        
        st.subheader("Gráfico de Serviços por Produto")

        df_contagem = df.groupby(["Produto", "Serviço"]).size().unstack(fill_value=0)
        

        fig, ax = plt.subplots(figsize=(10, 5)) 
        df_contagem.plot(kind="bar", stacked=True, colormap="tab20c", ax=ax) 
        
     
        fig.set_facecolor("black") 
        ax.set_facecolor("black")  

        ax.set_xlabel("Produto", color="white") 
        ax.set_ylabel("Quantidade de Serviços", color="white") 
        ax.set_title("Distribuição dos Serviços por Produto", color="white") 
 
        ax.legend(title="Serviço", title_fontsize="13", labelcolor="white", facecolor="black")  

        plt.xticks(rotation=45, ha="right", color="white") 
        plt.yticks(color="white")  
        
        plt.gca().set_facecolor("black") 

        st.pyplot(fig)
    else:
        st.warning("Sem dados para exibir no gráfico.")


if st.sidebar.button("Exibir Banco de dados"):
        st.dataframe(dfi)
    
