# Entrada do usuário
email = input().strip()

# Verifica se o e-mail atende a todas as regras
if (
    not email or
    " " in email or
    "@" not in email or
    email.startswith("@") or
    email.endswith("@") or
    not (email.endswith("@gmail.com") or email.endswith("@outlook.com"))
):
    print("E-mail inválido")
else:
    print("E-mail válido")
