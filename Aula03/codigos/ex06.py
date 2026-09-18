"""
Exercício 6 — Validação de Usuário e Senha
 
Peça um usuário e uma senha.
 
Se o usuário "unisa" e a senha "1234" estiverem corretos:
    - Pergunte se o usuário deseja acessar como administrador.
    - Se responder "sim", mostre "Acesso total!".
    - Caso contrário, mostre "Acesso restrito".
 
Se o usuário "usuario" e a senha "5678" estiverem corretos:
    - Mostre "Acesso externo".
 
Caso o usuário ou a senha estejam incorretos:
    - Mostre "Usuário ou senha inválidos".
 
Usuários cadastrados:
    - unisa / 1234   -> Administrador
    - usuario / 5678 -> Usuário comum
"""
 
def main():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
 
    if usuario == "unisa" and senha == "1234":
        admin = input("Você deseja acessar como administrador? (sim/não): ")
        if admin == "sim":
            print("Acesso total!")
        else:
            print("Acesso restrito")
    else:
        if usuario == "usuario" and senha == "5678":
            print("Acesso externo")
        else:
            print("Usuário ou senha inválidos")
 
if __name == "main__":
    main()
