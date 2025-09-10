lista=[]
while True:
 opcao=input('digite a opção')
 if opcao in '1':
  user=input('digite seu nome')
  lista.append(user)
  print(lista)
 if opcao == '2':
  print(lista)
 if opcao =='3':
   user=input('digite o nome que voce deseja remover')
   lista.remove(user)
   print(lista)
 if opcao =='4':
  user=input('obrigado por usar nossos serviços, tenha um bom dia.')
  
  lista.clear()

 print(lista)
 break

  
 

