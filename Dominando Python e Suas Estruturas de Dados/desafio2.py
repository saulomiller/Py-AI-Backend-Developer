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

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += "Deposito:{}".format(valor)
        print("Deposito realizado com sucesso!")
    else:       
        print("@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato    



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
        valor = int(input("informe o valor do deposito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao =="s":
            valor = int(input("Informe o valor do saque: "))

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
            contas = criar_conta(AGEJNCIA, numero_conta, usuarios)
        







main()
