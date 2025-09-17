import streamlit as st
conls= st.columns(4)
conls [0].write('🤖COLUNA 1 (+++++)')
conls [1].write('👾COLUNA 2 (-----)')
conls [2].write('🍡COLUNA 3 (*****)')
conls [3].write('🖥️COLUNA 4 (/////)')

with conls[0]:
 numero1= st.text_input('digite um numero')
 numero2= st.text_input('digite um numero2')

 if st.button('clique para saber a soma dos numeros um e dois'):
    resultado=int(numero1)+int(numero2)
    int(resultado)
    st.write(resultado)

with conls [1]:
     numero1=st.text_input('digite o primeiro numero')
     numero2= st.text_input('o segundo agora..')

     if st.button('solta o numero que eu solto a resposta da subtração '):
       resultado=int(numero1)-int(numero2)
       int(resultado)
       st.write(resultado)


with conls [2]:
    numero1=st.text_input('digite um numero para fazer o calculo')
    numero2= st.text_input('digite só mais um para o resultaado')

    if st.button('se um mais um é dois. Quanto é o numero1 * numero2?'):
     resultado=int(numero1)*int(numero2)
     int(resultado)
     st.write(resultado)

   
with conls [3]:
    numero1=st.text_input('digite um numero que seja menor que o infinito')
    numero2= st.text_input('digite um numero novo vai')

    if st.button('nao posso te ajudar no ENEM, mas aqui nóis faz uma divisão de jenio'):
        resultado=int(numero1)/int(numero2)
        int(resultado)
        st.write(resultado)
        st.write('oq é a vida?')

    if st.button ('só progesso rapaziada'):
     st.write('progressão pythozera')
     st.image('coluna.jpg')

resposta=st.text_input('digite sim para gostei e nao para precisa melhorar ')

if st.button('enviar avaliação'):
   st.success('avaliação enviada!')