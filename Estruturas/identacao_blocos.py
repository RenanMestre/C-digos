# DIO Backend Python Satander
# Identação e blocos 
def sacar(valor):
    saldo = 500
    
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa")

    print("Obrigado por ser nosso cliente, um ótimo dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)
