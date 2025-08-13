# DIO Backend Python Satander
# Métodos úteis - String

nome = "ReNaN"

# Filtros para o nome com letras maiúsculas
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!  "

# Filtros para textos com espaços
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

menu = "Python"

# Filtros com caractéres especiais
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")

# Print com um - no final
for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))