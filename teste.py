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
    "Distancia": ["km → quilômetro", "hm → hectômetro", "dam → decâmetro", "m → metro", "dm → decímetro", "cm → centímetro", "mm → milímetro"],

    "Volume": ["L → litro", "mL → mililitro", "m³ → metro cúbico", "cm³ → centímetro cúbico"],

    "Massa": ["kg → quilograma", "g → grama", "mg → miligrama", "t → tonelada"],

    #"Área": ["km² → quilômetro quadrado", "m² → metro quadrado", "cm² → centímetro quadrado"],

    "Velocidade": ["m/s → metros por segundo", "km/h → quilômetros por hora", "mph → milhas por hora"]
}

# Definição das listas de conversão com fatores de multiplicação para Distância, Volume, Massa e Velocidade
fatores_distancia = {
    "km": 1000,    # 1 quilômetro = 1000 metros
    "hm": 100,     # 1 hectômetro = 100 metros
    "dam": 10,     # 1 decâmetro = 10 metros
    "m": 1,        # 1 metro = 1 metro
    "dm": 0.1,     # 1 decímetro = 0.1 metro
    "cm": 0.01,    # 1 centímetro = 0.01 metro
    "mm": 0.001    # 1 milímetro = 0.001 metro
}

fatores_volume = {
    "m³": 1,          # 1 metro cúbico
    "dm³": 1000,      # 1 metro cúbico = 1000 decímetros cúbicos (litros)
    "cm³": 1000000,   # 1 metro cúbico = 1.000.000 centímetros cúbicos
    "L": 1000,        # 1 metro cúbico = 1000 litros
    "mL": 1000000     # 1 metro cúbico = 1.000.000 mililitros
}

fatores_massa = {
    "kg": 1,          # 1 quilograma
    "g": 1000,        # 1 quilograma = 1000 gramas
    "mg": 1000000,    # 1 quilograma = 1.000.000 miligramas
    "t": 0.001        # 1 quilograma = 0.001 toneladas
}

fatores_velocidade = {
    "m/s": 1,         # 1 metro por segundo
    "km/h": 3.6,      # 1 metro por segundo = 3.6 quilômetros por hora
    "mph": 2.23694    # 1 metro por segundo = 2.23694 milhas por hora
}

def efetuar_conversao():
    try:
        valor = float(enrtry_valor.get())
        tipo_conversao = combo_tipo.get()
        unidade_selecionada = combo_valores.get()

        if tipo_conversao == "Distância":
            fator_selecionado = fatores_distancia[unidade_selecionada]
            valor_em_metros = valor * fator_selecionado

            # Cria um texto com todos os resultados convertidos para distância
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_distancia.items():
                valor_convertido = valor_em_metros / fator
                resultado_texto += f"{valor_convertido:.3f} {unidade}\n"

        elif tipo_conversao == "Volume":
            fator_selecionado = fatores_volume[unidade_selecionada]
            valor_em_metros_cubicos = valor / fator_selecionado

            # Cria um texto com todos os resultados convertidos para volume
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_volume.items():
                valor_convertido = valor_em_metros_cubicos * fator
                resultado_texto += f"{valor_convertido:.3f} {unidade}\n"

        elif tipo_conversao == "Massa":
            fator_selecionado = fatores_massa[unidade_selecionada]
            valor_em_kg = valor * fator_selecionado

            # Cria um texto com todos os resultados convertidos para massa
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_massa.items():
                valor_convertido = valor_em_kg / fator
                resultado_texto += f"{valor_convertido:.3f} {unidade}\n"

        elif tipo_conversao == "Velocidade":
            fator_selecionado = fatores_velocidade[unidade_selecionada]
            valor_em_metros_por_segundo = valor / fator_selecionado

            # Cria um texto com todos os resultados convertidos para velocidade
            resultado_texto = f"Resultado para {valor} {unidade_selecionada}:\n"
            for unidade, fator in fatores_velocidade.items():
                valor_convertido = valor_em_metros_por_segundo * fator
                resultado_texto += f"{valor_convertido:.3f} {unidade}\n"

        # Atualiza o label com o resultado
        label_resultado.config(text=resultado_texto)

    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")


# Função para atualizar as unidades de acordo com o tipo de conversão selecionado
def atualizar_opcoes(event):
    tipo_conversao = combo_tipo.get()
    if tipo_conversao == "Distância":
        combo_valores["values"] = list(fatores_distancia.keys())
    elif tipo_conversao == "Volume":
        combo_valores["values"] = list(fatores_volume.keys())
    elif tipo_conversao == "Massa":
        combo_valores["values"] = list(fatores_massa.keys())
    elif tipo_conversao == "Velocidade":
        combo_valores["values"] = list(fatores_velocidade.keys())
    combo_valores.current(0)

# Função para zerar todos os campos
def reiniciar_tudo():
    combo_tipo.set('')  # Limpa a seleção do tipo de conversão
    combo_valores.set('')  # Limpa a seleção da unidade de conversão
    #entry_valor.delete(0, tk.END)  # Limpa o valor digitado
    label_resultado.config(text="Resultado: ")  # Limpa o resultado exibido


def frame1():
    frame1 = s.CTkFrame(master=janela, width=790, height=100, border_width=2, fg_color="lightgrey")
    frame1.place(x=5, y=1)

    #Label com textos
    label_tipo_conversao = s.CTkLabel(frame1, text="Tipo de Conversão:", fg_color="lightgrey")
    label_tipo_conversao.place(x=15, y=10)

    label_conversao = s.CTkLabel(frame1, text="Valor a ser Convertido em: ")
    label_conversao.place(x=15, y=50)

    # Primeiro Combobox (Tipo de Conversão)
    global combo_tipo
    combo_tipo = ttk.Combobox(frame1, width=20, font=('Arial', 11), values=list(listConversao.keys()))
    combo_tipo.place(x=220, y=18)
    combo_tipo.current(0)  # Define o primeiro valor como selecionado por padrão
    combo_tipo.bind("<<ComboboxSelected>>", atualizar_opcoes)  # Atualiza a segunda combobox ao selecionar

    # Segundo Combobox (Valores de Conversão)
    global combo_valores
    combo_valores = ttk.Combobox(frame1, width=20, font=('Arial', 11))
    combo_valores.place(x=220, y=70)
    combo_valores["values"] = listConversao[combo_tipo.get()]  # Inicializa com os valores do primeiro tipo de conversão
    combo_valores.current(0)

    # Caixa de texto de entrada de valor a ser convertido 
    label_valor = s.CTkLabel(frame1, text="Valor:")
    label_valor.place(x=400, y=10)
    global enrtry_valor
    enrtry_valor = s.CTkEntry(frame1, height=10)
    enrtry_valor.place(x=450, y=12)

    button_converter = s.CTkButton(frame1, text="Converter", height=40, width=50, command=efetuar_conversao)
    button_converter.place(x=710, y=5)
    button_reiniciar = s.CTkButton(frame1, text="Reiniciar", height=40, width=50, command=reiniciar_tudo)
    button_reiniciar.place(x=710, y=50)

frame1()

def frame2():
    frame2 = s.CTkFrame(master=janela, width=790, height=280, border_width=2, fg_color="lightgrey")
    frame2.place(x=5, y=105)

    texto = s.CTkLabel(frame2, text="Resultados das conversões :", font=('Arial', 18)).place(x=270, y=5)
    
    global label_resultado
    label_resultado = tk.Label(frame2, text="Resultado: ")
    label_resultado.place(x=270, y=70)

frame2()

janela.mainloop()