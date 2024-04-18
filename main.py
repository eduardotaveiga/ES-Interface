
import streamlit as st
from UFABConnect_API import fazer_login

st.image('https://i.ibb.co/XjtdCtD/Whats-App-Image-2024-03-07-at-17-50-22.png')

with st.form(key='my_form'):
    username = st.text_input('Nome de usuário')
    password = st.text_input('Senha')
    st.form_submit_button('Esqueci a senha')
    st.checkbox('Mantenha-me conectado')
    if st.form_submit_button('Login'):
        resposta = fazer_login(username, password)
        if resposta == 1:
            st.switch_page('pages/homepage.py')
        else:
            st.write('Usuário ou senha inválidos')
