import streamlit as st
from UFABConnect_API import criar_grupo

def main():
    col1, col2, col3 = st.columns(3, gap='large')
    col1, col2, col3 = st.columns([7,1,2])
    with col1:
        st.image('https://i.ibb.co/XjtdCtD/Whats-App-Image-2024-03-07-at-17-50-22.png', width = 300)
        nome = st.text_input('Nome do grupo')
        #st.write("Teste: nome do grupo: ", nome)
        tema = st.text_input('Tema')
        tags = st.text_input('Insira tags relacionadas - separe por vírgulas')
        usuários = st.text_input('Adicione participantes (@nomedeusuário)')
        st.text("\n")
        if st.button('Voltar'):
            st.switch_page('pages/homepage.py')
    with col3:
        for i in range(13):
            st.text("")
        st.image('https://cdn.icon-icons.com/icons2/495/PNG/512/add-circle-1_icon-icons.com_48714.png')
        st.write('Adicione uma foto')
        for i in range(6):
            st.text("")
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
        if st.button('Criar'):
            resposta = criar_grupo(nome, tema)
            if resposta == 1:
                st.write('Grupo criado com sucesso!')
            else:
                st.write('Falha ao criar o grupo :(')
            #st.switch_page('pages/homepage.py')


if __name__ == "__main__":
    main()