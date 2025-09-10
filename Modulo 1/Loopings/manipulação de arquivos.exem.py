nome=input('digite o nome do arquivo:')
email=input('digite o e-mail:')

arquivo=open('pessoa.txt', 'a')
arquivo.write(nome+ '|' + email + "\n")
arquivo.close()