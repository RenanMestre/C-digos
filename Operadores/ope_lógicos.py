# DIO Backend Python Satander
# Operadores de Identidade

# AND = para ser True tudo tem que ser True
# OR = para ser True só precisa de um True
print(True and True)
print(True and False)
print(False and True)
print(True or True)
print(True or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Forma básica de escrever porém duvidosa para outros programadores
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

# Forma mais bonita de escrever
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# Forma mais legível e mais fácil de entender
saldo_suficiente_conta_normal = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque
print(saldo_suficiente_conta_normal or conta_especial_com_saldo_suficiente)