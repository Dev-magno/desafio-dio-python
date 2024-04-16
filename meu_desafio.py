# Criando um sistema bancário com as operações: sacar, depositar e visualizar
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
   
    if opcao == '1':
        valor = float(input("Informe o valor do deposito: "))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito efetuado. Volte sempre!")
        else:
            print("O valor inválido, tente novamente!")

    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
       
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente para realizar essa operação!")
           
        elif excedeu_limite:
            print("Falha na operação. O valor do saque excede o limite!.")

        elif excedeu_saques:
            print("Operação sem sucesso! Número máximo de saques excedido!")
           
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {saldo:.2f}\n"
            numero_saques += 1
            print("Saque efetuado. Volte sempre!")
        
        else:
            print("Operação falhou! O valor é inválido.")
           
    elif opcao == '3':
            print("\n============ EXTRATO ============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=================================")
       
    elif opcao == '4':
        break

    else:
        print("Operação inválida, por favor selecione a opração correta.")


print('Obridado por usar nosso sistema, volte sempre!')