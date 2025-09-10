unidades=50

while True:
    estoque=input('escolha uma dessas opções:''(1)adicionar unidades ao estoque,(2)remover unidades do estoque(3),verificar estoque atual,(4)para sair.')
   
    if estoque=='1':
        
        print('adicionar unidades ao estoque')
      
        produtos=int(input('digite um valor para adicionar unidades ao estoque!'))
        estoqueFinal=   unidades+produtos
        print(estoqueFinal)
        print('unidades adicionadas com maestria')

    if estoque=='2':
        print('remover unidades do estoque')
        
        produtos=int(input('escreva o valor de unidades que deseja remover'))
        estoquefinal=    unidades-produtos
        print(estoquefinal)
        print('unidades removidas...')
    if estoque =='3':
        print(unidades)
    if estoque=='4':
            print('sair')
            print('obrigado(a) por usar nossos serviços!')
            break
        
        