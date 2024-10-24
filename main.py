import tkinter as tk
from tkinter import ttk

# Cria formulário principal
formulario = tk.Tk()
formulario.title("Conversor de Unidades")
formulario.geometry("400x400")

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

# Função para efetuar a conversão
def efetuar_conversao():
    try:
        valor = float(entry_valor.get())
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
    entry_valor.delete(0, tk.END)  # Limpa o valor digitado
    label_resultado.config(text="Resultado: ")  # Limpa o resultado exibido

# Labels
tk.Label(formulario, text="Tipo de Conversão:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(formulario, text="Unidade de Conversão:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(formulario, text="Valor:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Primeiro Combobox (Tipo de Conversão) - Distância, Volume, Massa e Velocidade
combo_tipo = ttk.Combobox(formulario, values=["Distância", "Volume", "Massa", "Velocidade"], width=25)
combo_tipo.grid(row=0, column=1, padx=10, pady=10)
combo_tipo.current(0)
combo_tipo.bind("<<ComboboxSelected>>", atualizar_opcoes)

# Segundo Combobox (Unidades de Conversão)
combo_valores = ttk.Combobox(formulario, width=25)
combo_valores.grid(row=1, column=1, padx=10, pady=10)
combo_valores["values"] = list(fatores_distancia.keys())  # Inicializando com as unidades de distância
combo_valores.current(0)

# Caixa de entrada para o valor numérico
entry_valor = tk.Entry(formulario, width=10)
entry_valor.grid(row=2, column=1, padx=10, pady=10)

# Botão para realizar a conversão
botao_converter = tk.Button(formulario, text="Converter", command=efetuar_conversao)
botao_converter.grid(row=3, column=1, padx=10, pady=10)

# Botão para zerar todos os campos
botao_zerar = tk.Button(formulario, text="Zerar", command=reiniciar_tudo)
botao_zerar.grid(row=3, column=0, padx=10, pady=10)

# Label para exibir o resultado da conversão
label_resultado = tk.Label(formulario, text="Resultado: ")
label_resultado.grid(row=4, column=1, padx=10, pady=10)

# Roda o loop principal do Tkinter
formulario.mainloop()
