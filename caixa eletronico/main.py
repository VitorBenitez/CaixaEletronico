import tkinter as tk
from tkinter import ttk, messagebox


class ContaBancaria:
    def __init__(self, numero_conta, nome, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome = nome
        self._saldo = saldo_inicial  

    def verificar_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return f"Depósito de {valor} realizado com sucesso!"
        else:
            return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor <= 0:
            return "Valor inválido para saque."
        elif valor > self._saldo:
            return "Saldo insuficiente."
        else:
            self._saldo -= valor
            return f"Saque de {valor} realizado com sucesso!"


contas = {"1234": ContaBancaria("1234", "Vitor", 50000)}


def verificar_saldo():
    numero_conta = entrada_conta.get()
    if numero_conta in contas:
        saldo = contas[numero_conta].verificar_saldo()
        messagebox.showinfo("Saldo", f"Saldo da conta {numero_conta}: {saldo}")
    else:
        messagebox.showerror("Erro", "Conta não encontrada.")

def depositar():
    try:
        numero_conta = entrada_conta.get()
        valor = float(entrada_valor.get())
        if numero_conta in contas:
            resultado = contas[numero_conta].depositar(valor)
            messagebox.showinfo("Depósito", resultado)
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido para depósito.")

def sacar():
    try:
        numero_conta = entrada_conta.get()
        valor = float(entrada_valor_saque.get())  
        if numero_conta in contas:
            resultado = contas[numero_conta].sacar(valor)
            messagebox.showinfo("Saque", resultado)
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido para saque.")

def criar_conta():
    numero_conta = entrada_conta.get()
    if numero_conta not in contas:
        nome = entrada_nome.get()  
        try:
            saldo_inicial = float(entrada_valor.get())  
        except ValueError:
            saldo_inicial = 0  
        contas[numero_conta] = ContaBancaria(numero_conta, nome, saldo_inicial)
        messagebox.showinfo("Conta Criada", f"Conta {numero_conta} criada com sucesso!")
    else:
        messagebox.showerror("Erro", "Conta já existente.")



root = tk.Tk()
root.title("Caixa Eletrônico")
root.geometry("700x500")


ttk.Label(root, text="Número da Conta").grid(row=0, column=0)
entrada_conta = tk.Entry(root)
entrada_conta.grid(row=0, column=1)

ttk.Label(root, text="Nome").grid(row=1, column=0)
entrada_nome = tk.Entry(root)
entrada_nome.grid(row=1, column=1)

ttk.Label(root, text="Valor para Depósito").grid(row=2, column=0)
entrada_valor = tk.Entry(root)
entrada_valor.grid(row=2, column=1)

ttk.Label(root, text="Valor para Saque").grid(row=3, column=0)
entrada_valor_saque = tk.Entry(root)  
entrada_valor_saque.grid(row=3, column=1)


ttk.Button(root, text="Criar Conta", command=criar_conta).grid(row=4, column=0)
ttk.Button(root, text="Verificar Saldo", command=verificar_saldo).grid(row=4, column=1)
ttk.Button(root, text="Depositar", command=depositar).grid(row=5, column=0)
ttk.Button(root, text="Sacar", command=sacar).grid(row=5, column=1)

root.mainloop()
