# DIO Backend Python Santander
# Estruturas condicionais aninhada

#conta_normal = True
#conta_universitaria = False
#conta_especial = False

# Sistema bancário desenvolvido com diferentes tipos de contas, tudo aplicado aqui foi seguindo o que foi estudado e revisado em aulas, praticando desde a estruturas até operadores.
# Desenvolvedor dos códigos --> Renan Mestre

saldo = 2000
cheque_especial = 450
especial = 1500
especial_extra = 4500
opcao = "-1"

print("Bem-vindo ao sistema bancário!")
print("\nInforme se você deseja sacar ou se quer sair:")

while True:
    opcao = int(input("[1] Sacar\n[0] Sair\n"))

    if(opcao == 1):
        print("Opção Saque selecionada!")
        saque = int(input("Informe o valor do saque: "))
        conta = str(input("Informe a sua conta (Normal, Universitário ou Especial): "))

        # Conta normal 
        if conta == "Normal" or conta == "normal":
            if saldo >= saque:
                print("Saque realizado com sucesso!")
            elif saque <= (saldo + cheque_especial):
                print("Saque realizado com o uso de cheque especial!")
            else:
                print("Não foi possível realizar o saque!")
        # Conta de cliente universitário(a)
        elif conta == "Universitária" or conta == "Universitário" or conta == "universitária" or conta == "universitário":
            if saldo >= saque:
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque!")
        # Conta de cliente especial
        elif conta == "Especial" or conta == "especial":
            if saldo >= saque:   
                resposta = str(input("Deseja utilizar o cliente especial?\nSe aceitar terá alguns benefícios como:\nAumento de saldo: de 1500 até 4500 a mais do que você já tem no seu banco digital.\n(Aceito!/Hoje não): "))
                if resposta == "Aceito" or resposta == "aceito":
                    beneficio = int(input("Informe o aumento de 1500 ou 4500(1500/4500): "))
                    if(beneficio == 1500):
                        saldo_especial = saldo + especial
                        print("Seu saldo aumentou para", saldo_especial)
                        print("Saque realizado com sucesso!")
                    elif(beneficio == 4500):
                        saldo_especial = saldo + especial_extra
                        print("Seu saldo aumentou para", saldo_especial)
                        print("Saque realizado com sucesso!")
                    else:
                        print("Benefício inválido, por favor informe 1500 ou 4500!")
                elif resposta == "Hoje não" or resposta == "hoje não":
                    print("Saque realizado com o uso do cliente especial!")
                else:
                    print("Resposta inválida, por favor responda com Sim ou Não!")
            else:
                print("Saldo insuficiente para saque!")
        else:
            print("Sistema não reconhece a conta informada, entre em contato com o gerente!")
    else:
        print("Saindo do sistema bancário...")
        print("Obrigado por utilizar nosso sistema bancário! Até logo!")
        break
# Fim do código