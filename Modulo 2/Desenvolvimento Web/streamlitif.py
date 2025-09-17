import streamlit as st


nome=st.text_input   ('digite   seu nome')
numero=st.text_input('digite seu numero de telefone com DDD')
email=st.text_input ('digite  seu email')


st.write (nome)
st.write(numero)

if st.button('enviar'):
    if email==('pythonzeraprogramers@gmail.com'):
        st.success ('email enviado com sucesso')
    else:st.error('email invalido')