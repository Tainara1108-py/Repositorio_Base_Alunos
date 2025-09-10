senha=input('insira sua senha para acessar:')
senhacorreta='123456'
saldo=1000
if senha==senhacorreta:
    print('acesso liberado')
    while True:
    
        menu=input('digite a opçao que voce quer bootzinho')

        if menu=='1':
             print('vamos sacar')
    
             saque=int(input('escolha o valor que deseja sacar...'))
    
             print(saldo-saque)
    
        print('saque efetuado com sucesso!!!')

        if menu=='2':
         print(' Depositar:')
         depósito=int(input('insira o valor a ser depositado'))   
         print(saldo+depósito) 
     
         print('depósito efetuado') 
        if menu=='3':
         print(saldo)
        if menu=='4':
         print('sair')
         print('obrigador por usar nossos serviços')
         break
else:
    print('acesso negado')
    print('tente novamente!')




