# DIO Backend Python Satander
# Interpolação de variáveis - String

nome = "Renan"
idade = 18
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Renan", "idade": 18}

# Mostrando variáveis
print("Nome: %s idade: %d" % (nome, idade))

# Mostrando variáveis sem definir String e Inteiro
print("Nome: {} idade: {}".format(nome, idade))

# Mostrando variáveis por meio de casas - números
print("Nome: {1} idade: {0}".format(idade, nome))
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))

# Mostrando variáveis por meio de casas e formatações chamando as variáveis
print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} idade: {age} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} idade: {idade}".format(**dados))

# Colocando valores em decimais de 2 casas e espaços a mais
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")