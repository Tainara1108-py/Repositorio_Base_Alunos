def senha():
    senha=input('digite sua senha para validar o acesso.')
    print('digite sua senha')
    
    senhacorreta='variavel'
    print(senha==senhacorreta)
    if senha==senhacorreta:
      print('acesso concedido, parabens')
    else:
     print('acesso negado, tente novamente..')
senha() 
