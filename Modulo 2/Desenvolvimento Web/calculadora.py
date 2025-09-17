import streamlit as st

nuemro1 = st.text_input('digi o primeiro numero')
nuemro2 = st.text_input('digi o segundo numero')



if st.button('  + +++  '):
    resultado =int(nuemro1)+int(nuemro2)
    int(resultado)
    st.write(resultado)
if st.button('----'):
      resultado =int(nuemro1)-int(nuemro2)
      st.write(resultado)


