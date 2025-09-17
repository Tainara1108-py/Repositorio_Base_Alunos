import streamlit as st

st.sidebar.title( 'o site mais legal do mundo com a propython mais legal do mundo')
st.sidebar.image ('evom.jpg')
st.sidebar.image('calma.jpg')
st.sidebar.title('duas imagens fortes...')
conls=st.columns(2)
conls [0].write('🤖coluna 1')
conls [1].write('👾coluna 2')
if st.button('botão meu'):
    st.write ('clica no meu botao e ta achando que a vida é mamão com açucar🤣🤦‍♀️')
