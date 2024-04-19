import streamlit as st

col1, col2= st.columns(2)
col1, col2 = st.columns([3,3])

with col1:
    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: #0B6623; /* Green background */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 15px;
            transition-duration: 0.4s;
            cursor: pointer;
        }

        div.stButton > button:hover {
            background-color: #008631; /* Darker green on hover */
        }
        </style>
        """
        , unsafe_allow_html=True
    )
    st.image('https://i.ibb.co/XjtdCtD/Whats-App-Image-2024-03-07-at-17-50-22.png')
    if st.button('Voltar'):
        st.switch_page('pages/homepage.py')
    st.text_input('Nome')
    st.text_area('Interesses')
    st.text_area('Biografia')
    #with st.expander('Alterar perfil'):
    #    st.text_input('Nome de usuário')
    #    st.write('')
    #    # st.form_submit_button('Alterar seu nome de usuário')
    #    st.text_input('Interesses')
    #    st.write('')
    #    # st.form_submit_button('Alterar seus interesses')
    #    st.text_input('Biografia')
    #    st.write('')
    #    # st.form_submit_button('Alterar sua biografia')
    #    st.button('Salvar')
with col2:
    for i in range(11):
        st.text("")
    with st.form(key='my_form2'):
       st.file_uploader('Foto de perfil')
       st.form_submit_button('Alterar senha')
       st.form_submit_button('Deslogar')
    with st.form(key='my_form3'):
       st.text_input('Grupos que participo')
       st.form_submit_button('Mostrar todos')
