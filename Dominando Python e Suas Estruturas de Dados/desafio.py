### Criando um Sistema Bancário com Python ###
menu = """""

[d]= Deposito
[s]= Saque
[e]= Extrato
[q]= Sair

=> """

saldo = 0
limite = 500 
extrato = ""

numero_saques = 0
LIMITE_SAQUE = 3

while True:
    option=input(menu)

    if option =="d":
        valor_deposito = int(input("Digite o valor do deposito:"))
        saldo += valor_deposito
        print("Valor Depositado RS:{}".format (valor_deposito))

    elif option == "s":
        if numero_saques < LIMITE_SAQUE:
            valor_saque = int(input("Digite o valor a ser sacado:"))
            if saldo >= valor_saque:
                saldo -= valor_saque
                numero_saques+= 1
                extrato += ("Saque: -R${}".format(valor_saque))
                print("Saque de RS:{} realizado com sucesso.".format(valor_saque))
            else:
                print("Saldo insuficiente =(")
        else:
            print("Limite de saques exedido.")
    
    
    elif option == "e":
        print(extrato)
        print("Saldo atual: R${}".format(saldo))
    
    elif option =="q":
        break
    
    else:
      print("Essa opção não é valida")

