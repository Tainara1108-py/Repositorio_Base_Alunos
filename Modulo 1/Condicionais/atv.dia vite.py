lista=[5, -2, 0, 8, -1, 0,]
positivo=0
negativo=0
zero=0
       
for i in lista:
    if i >0:
        print(i,'positivo')
        positivo=positivo+1
    elif i<0:
        print(i,'negativo')
        negativo=negativo-1
    else:
        
        print(i,'igual a zero')
               
   
print(positivo)
print(negativo)




       
# for i in lista:
#     print('numero', i)