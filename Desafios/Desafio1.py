# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO10":

    desconto = preco * 0.10
    valortotal = preco - desconto

    print(f"{valortotal:.2f}")

if cupom == "DESCONTO20":

    desconto = preco * 0.20
    valortotal = preco - desconto

    print(f"{valortotal:.2f}")

if cupom == "SEM_DESCONTO":

    print(f"{preco:.2f}")