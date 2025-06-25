import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')  # opcional

# Criação da janela
app = ctk.CTk()
app.title('Tabuada Interativa')# 
app.geometry('300x450')

# Função para calcular e exibir a tabuada
def mostrar_tabuada():
    try:
        n = int(entry_numero.get())
        operacao = operacao_menu.get()
        resultado_textbox.configure(state="normal")  # Ativa edição temporária
        resultado_textbox.delete("1.0", "end")  # Limpa antes de exibir

        resultado_textbox.insert("end", f"Tabuada do {n} com '{operacao}':\n\n")
        
        for i in range(1, 11):
            if operacao == '+':
                resultado = n + i
                linha = f"{n} + {i} = {resultado}\n"
            elif operacao == '-':
                resultado = n - i
                linha = f"{n} - {i} = {resultado}\n"
            elif operacao == '*':
                resultado = n * i
                linha = f"{n} * {i} = {resultado}\n"
            elif operacao == '/':
                if i != 0:
                    resultado = n / i
                    linha = f"{n} / {i} = {resultado:.2f}\n"
                else:
                    linha = "Divisão por zero não é permitida.\n"
            else:
                linha = "Operação inválida.\n"
            
            resultado_textbox.insert("end", linha)
        
        resultado_textbox.configure(state="disabled")  # Impede edição

    except ValueError:
        resultado_textbox.configure(state="normal")
        resultado_textbox.delete("1.0", "end")
        resultado_textbox.insert("end", "Digite um número válido!")
        resultado_textbox.configure(state="disabled")

# Widgets
entry_numero = ctk.CTkEntry(app, placeholder_text="Digite um número inteiro")
entry_numero.pack(pady=10)

operacao_menu = ctk.CTkOptionMenu(app, values=["+", "-", "*", "/"])
operacao_menu.pack(pady=10)

btn_calcular = ctk.CTkButton(app, text="Mostrar Tabuada", command=mostrar_tabuada)
btn_calcular.pack(pady=20)

resultado_textbox = ctk.CTkTextbox(app, height=200, width=250, text_color= "green")
resultado_textbox.pack(pady=10)
resultado_textbox.configure(state="disabled")  # Começa bloqueado para edição

# Loop da aplicação
app.mainloop()
