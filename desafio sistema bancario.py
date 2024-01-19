
menu ='''        
#######  Bem vindo ao Silascool #######!
Por favor selecione a operação desejada:

[1] Sacar
[2] Depositar
[3] Consultar extrato
[4] Sair

 '''

opcao = 'Início'
qtd_limite_saque = 3
VALOR_LIMITE_SAQUE = 500.0
saldo = 1500.0
valor_saque = valor_deposito = 0
historico_depositos = []
historico_saques = []
historico_saldos = [saldo]

# menu
while True:
    print('-'*41)
    opcao = str(input(menu)).upper()
    print('-'*41)
    
    if opcao == '1':
        # saque
        valor_saque = int(input('Digite o valor a ser sacado: R$ '))
        print()
        
        if qtd_limite_saque > 0:
            if valor_saque <= VALOR_LIMITE_SAQUE:
                if valor_saque <= saldo:
                    qtd_limite_saque -= 1
                    saldo -= valor_saque
                    print(f'       Saque de R$ {valor_saque:.2f} realizado com sucesso')
                    
                    # extrato
                    historico_saques.append(valor_saque)
                       
                else:
                    print('      Não foi possivel realizar a transação, saldo insuficiente :(')
            else:
                print('       Não foi possivel realizar a transação, valor do saque exede o limite por operação')
        else:
            print('        Não foi possivel realizar a transação, limite diario de saques atingido')
        
        print('\nRetornando ao menu...')
        

    elif opcao == '2':
        # depósito
        valor_deposito = int(input('Insira o valor a ser depositado: R$ '))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'      Depósito de R$ {valor_deposito:.2f} realizado com sucesso')
        else:
            print('\nValor de depósito inválido')
            
        print('\nRetornando ao menu...')
        
        # extrato
        historico_depositos.append(valor_deposito)
    
    elif opcao == '3':
        print('-' * 41)
        print('\n            Extrato :\n')
        if len(historico_depositos) == 0 and len(historico_saques) == 0:
            print('       Nenhuma operação realizada')
            print('-' * 41)
        else:
            print(f'Saldo inicial: R$ {historico_saldos[0]:.2f}\n')
        if len(historico_depositos) > 0:
            print('depósitos'.upper())
            for deposito in historico_depositos:
                print(f'R$ {deposito:.2f}')
            print('-' * 41)
        if len(historico_saques) > 0:
            print('saques'.upper())
            for saque in historico_saques:
                print(f'R$ {saque:.2f}')
            print('-' * 41)
        print(f'Saldo da conta: R$ {saldo:.2f}')
        print(f'Saques diários restantes: {qtd_limite_saque}\n')
    
    elif opcao == '4':
        print(' O Silascool agradece a prefência !!! ')
        print()
        break
    
    else:
        print('   Operação inválida. Por favor digite uma das opções abaixo:')
        print()