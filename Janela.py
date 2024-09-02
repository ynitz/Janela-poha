import tkinter as Fr
window = Fr.Tk()
window.title("Messi")
window.geometry("500x500")
window.configure(background='#90ee90')

nome=Fr.Label(window, text="Aiiiiii gostoso🙉🙈👌😎😘")
nome.pack()

txtEntrada =Fr.Entry(window)
txtEntrada.pack()

def machado_de_assis():
    inspiracao= txtEntrada.get()
    t=Fr.Label(window, text=inspiracao)
    t.pack()

btn=Fr.Button(window, text="mostrar", command=machado_de_assis)
btn.pack()
btm=Fr.Button(text="Calculadora")

import tkinter as Fr

def nova_janela():
    nova_window = Fr.Toplevel(window)
    nova_window.title("Calculadora")
    nova_window.geometry("300x200")

    label_nova = Fr.Label(nova_window, text="Nova janela aberta!")
    label_nova.pack()

    
    num1_label = Fr.Label(nova_window, text="Número 1:")
    num1_label.pack()
    num1_entry = Fr.Entry(nova_window)
    num1_entry.pack()

    num2_label = Fr.Label(nova_window, text="Número 2:")
    num2_label.pack()
    num2_entry = Fr.Entry(nova_window)
    num2_entry.pack()

    
    def soma():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado = num1 + num2
        resultado_label.config(text=f"Resultado: {resultado}")

    def subtracao():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado = num1 - num2
        resultado_label.config(text=f"Resultado: {resultado}")

    def multiplicacao():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        resultado = num1 * num2
        resultado_label.config(text=f"Resultado: {resultado}")

    def divisao():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 != 0:
            resultado = num1 / num2
            resultado_label.config(text=f"Resultado: {resultado}")
        else:
            resultado_label.config(text="Erro: Divisão por zero!")

    soma_button = Fr.Button(nova_window, text="+", command=soma)
    soma_button.pack()

    subtracao_button = Fr.Button(nova_window, text="-", command=subtracao)
    subtracao_button.pack()

    multiplicacao_button = Fr.Button(nova_window, text="*", command=multiplicacao)
    multiplicacao_button.pack()

    divisao_button = Fr.Button(nova_window, text="/", command=divisao)
    divisao_button.pack()

    resultado_label = Fr.Label(nova_window, text="Resultado:")
    resultado_label.pack()

btm = Fr.Button(window, text="nova janela", command=nova_janela)
btm.pack()


















window.mainloop()