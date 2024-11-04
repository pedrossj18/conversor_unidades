import customtkinter as s
import tkinter as tk
from tkinter import ttk

# Janela principal
janela = s.CTk()
janela.title("Conversor de Unidades")
janela.iconbitmap("C:/Users/pedri/OneDrive/Documentos/One Drive/OneDrive/Área de Trabalho/Pedro_IndFlow/conversor_de_unidade/Imagens/conversor-de-unidades-300x300.ico")
janela.geometry("800x400")
janela.maxsize(width=1050, height=550)
janela.resizable(width=False, height=False)

# Definição das listas de conversão
listConversao = {
    "Distância": [
        "km - Quilômetro", 
        "hm - Hectômetro", 
        "dam - Decâmetro", 
        "m - Metro", 
        "dm - Decímetro", 
        "cm - Centímetro", 
        "mm - Milímetro"
    ],
    "Volume": [
        "L - Litro", 
        "mL - Mililitro", 
        "m³ - Metro Cúbico", 
        "cm³ - Centímetro Cúbico"
    ],
    "Massa": [
        "kg - Quilograma", 
        "g - Grama", 
        "mg - Miligrama", 
        "t - Tonelada"
    ],
    "Velocidade": [
        "m/s - Metros por Segundo", 
        "km/h - Quilômetros por Hora", 
        "mph - Milhas por Hora"
    ]
}

# Definição das listas de conversão com fatores de multiplicação para Distância, Volume, Massa e Velocidade
fatores_distancia = {"km": 1000, "hm": 100, "dam": 10, "m": 1, "dm": 0.1, "cm": 0.01, "mm": 0.001}
fatores_volume = {"m³": 1, "cm³": 1000000, "L": 1000, "mL": 1000000}
fatores_massa = {"kg": 1, "g": 1000, "mg": 1000000, "t": 0.001}
fatores_velocidade = {"m/s": 1, "km/h": 3.6, "mph": 2.23694}

# Função para realizar a conversão
def efetuar_conversao():
    try:
        valor = float(entry_valor.get())
        tipo_conversao = combo_tipo.get()
        unidade_selecionada = combo_valores.get().split(" - ")[0]  # Extrair apenas a abreviação da unidade

        if tipo_conversao == "Distância":
            fator_selecionado = fatores_distancia[unidade_selecionada]
            valor_em_metros = valor * fator_selecionado
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_distancia.items():
                valor_convertido = valor_em_metros / fator
                resultado_texto += f"{remove_trailing_zeros(valor_convertido)} {unidade}\n"

        elif tipo_conversao == "Volume":
            fator_selecionado = fatores_volume[unidade_selecionada]
            valor_em_metros_cubicos = valor / fator_selecionado
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_volume.items():
                valor_convertido = valor_em_metros_cubicos * fator
                resultado_texto += f"{remove_trailing_zeros(valor_convertido)} {unidade}\n"

        elif tipo_conversao == "Massa":
            fator_selecionado = fatores_massa[unidade_selecionada]
            valor_em_kg = valor * fator_selecionado
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_massa.items():
                valor_convertido = valor_em_kg / fator
                resultado_texto += f"{remove_trailing_zeros(valor_convertido)} {unidade}\n"

        elif tipo_conversao == "Velocidade":
            fator_selecionado = fatores_velocidade[unidade_selecionada]
            valor_em_metros_por_segundo = valor / fator_selecionado
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_velocidade.items():
                valor_convertido = valor_em_metros_por_segundo * fator
                resultado_texto += f"{remove_trailing_zeros(valor_convertido)} {unidade}\n"

        label_resultado.configure(text=resultado_texto)

    except ValueError:
        label_resultado.configure(text="Por favor, insira um valor numérico válido.")

def remove_trailing_zeros(value):
    return f"{value:.8f}".rstrip('0').rstrip('.')

# Função para atualizar as unidades de acordo com o tipo de conversão selecionado
def atualizar_opcoes(event):
    tipo_conversao = combo_tipo.get()
    combo_valores["values"] = listConversao[tipo_conversao]
    combo_valores.current(0)
    
# Função para zerar todos os campos
def reiniciar_tudo():
    combo_tipo.set('')  # Limpa a seleção do tipo de conversão
    combo_valores.set('')  # Limpa a seleção da unidade de conversão
    entry_valor.delete(0, tk.END)  # Limpa o valor digitado
    label_resultado.configure(text="Resultado: ")  # Limpa o resultado exibido

# Frame com opções de entrada e conversão
def frame1():
    frame1 = s.CTkFrame(master=janela, width=790, height=100, border_width=2, fg_color="lightgrey")
    frame1.place(x=5, y=1)

    # Label e Combobox para Tipo de Conversão
    label_tipo_conversao = s.CTkLabel(frame1, text="Tipo de Conversão:", fg_color="lightgrey")
    label_tipo_conversao.place(x=15, y=10)
    global combo_tipo
    combo_tipo = ttk.Combobox(frame1, width=20, font=('Arial', 11), values=list(listConversao.keys()))
    combo_tipo.place(x=220, y=18)
    combo_tipo.current(0)
    combo_tipo.bind("<<ComboboxSelected>>", atualizar_opcoes)

    # Label e Combobox para Unidade de Conversão
    label_conversao = s.CTkLabel(frame1, text="Valor a ser Convertido em: ")
    label_conversao.place(x=15, y=50)
    global combo_valores
    combo_valores = ttk.Combobox(frame1, width=20, font=('Arial', 11))
    combo_valores.place(x=220, y=70)
    combo_valores["values"] = listConversao[combo_tipo.get()]
    combo_valores.current(0)

    # Caixa de entrada para o valor numérico
    label_valor = s.CTkLabel(frame1, text="Valor:")
    label_valor.place(x=400, y=10)
    global entry_valor
    entry_valor = s.CTkEntry(frame1, height=10)
    entry_valor.place(x=450, y=12)

    # Botões de Conversão e Reinício
    button_converter = s.CTkButton(frame1, text="Converter", height=40, width=50, command=efetuar_conversao)
    button_converter.place(x=710, y=5)
    button_reiniciar = s.CTkButton(frame1, text="Reiniciar", height=40, width=50, command=reiniciar_tudo)
    button_reiniciar.place(x=710, y=50)

frame1()

# Frame para exibir os resultados da conversão
def frame2():
    frame2 = s.CTkFrame(master=janela, width=790, height=280, border_width=2, fg_color="lightgrey")
    frame2.place(x=5, y=105)
    texto = s.CTkLabel(frame2, text="Resultados das conversões:", font=('Arial', 18)).place(x=270, y=5)
    global label_resultado
    label_resultado = s.CTkLabel(frame2, text="Resultado: ", fg_color="lightgrey", wraplength=750)
    label_resultado.place(x=20, y=50)

frame2()

janela.mainloop()
