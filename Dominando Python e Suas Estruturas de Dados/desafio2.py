import textwrap

def menu():
    menu ='''\n
    ___________ MENU ___________
    [d]\tDeposito
    [s]\tSacar
    [nc]\tNova Conta
    [lc]\Lista de Contas
    [nu]\tNovo Usuario
    [q]\tSair
    ==>'''
    return input(textwrap.denent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += "Deposito:{:.2f}\n".format(valor)
        print("Deposito realizado com sucesso!")
    else:       
        print("@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato    

def sacar(*, saldo , valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print ("@@@ Operacao falho! Saldo insuficiente. @@@")
    elif valor > limite:
        print("@@@ Operacao falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:
        print ("@@@ Operacao falhou! Numero maximo de saques excedido. @@@")
    elif valor > 0:
        saldo-= valor
        extrato += "Saque: R${:.2f}\n".format(valor)
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("@@@ Operacao falhou ! O valor informado é invalido. @@@ ")
        return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato ):
    print("\n********** EXTRATO **********")
    print("Nao foram realizadas movimentacoes."if not extrato else extrato)
    print("Saldo: R${:.2f}".format(saldo))
    print("******************************")

def cria_usuario(usuarios):
    cpf = input ("Informe o CPF (somente numeros): ")
    usuarios = filtra_usuario(cpf, usuarios)

    if usuarios:
        print("@@@ Ja existe usuario com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: " )
    endereco = input("Informe o endereco ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}) data_nascimento, "endereco": endereco "})
    print("Usuário criado com sucesso!")

def filtra_usuario(cpf, usuarios):
    for usuario in usuario:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cria_conta(agencia, numero_conta, usuarios):
   cpf = input("Infome o CPF do usuario: ")
   usuario = filtra_usuario(cpf, usuarios)
   if usuario:
       print("Conta criada com sucesso!")
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("@@@ Usuario nao encontrado, criacao de conta falhou! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta['agencia']} - Número da Conta: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}"
        print(linha)

def main():

    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500 
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao =="s": 
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo  
                valor=valor
                extrato=extrato
                limite=limite
                numero_saques=numero_saques
                limite_saques=LIMITE_SAQUE
            )

        elif opcao =="e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao =="nu":
            criar_usuario(usuarios)
        
        elif opcao =="nc":
            numero_conta = len(contas) + 1
            contas = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)            
        elif opcao == "q":
            break

if __name__ == "__main__":
    main()
