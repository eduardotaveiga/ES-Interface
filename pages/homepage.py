
import streamlit as st
from UFABConnect_API import fazer_post, carregar_publicacao, carregar_grupos

# Logica para manter o botão de fazer postagem como True de forma 'permanente"
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button(i, titulo, conteudo):
    if i == 0:
        st.session_state.button = not st.session_state.button
    else:
        pass
        #resp = fazer_post(titulo, conteudo)
        #st.session_state.button = not st.session_state.button

if 'button_visao_grupo' not in st.session_state:
    st.session_state.button_visao_grupo = False

def visao_grupo_button():
    st.session_state.button_visao_grupo = not st.session_state.button_visao_grupo

# Layout de colunas para organizar os componentes

coluna_paginas = st.sidebar
coluna_postagens = st

# Barra Lateral

imagem_url = 'https://i.ibb.co/XjtdCtD/Whats-App-Image-2024-03-07-at-17-50-22.png'
st.sidebar.image(imagem_url, width=200, caption='')
pagina_home = coluna_paginas.button('Home', on_click=visao_grupo_button)

# Ações do usuário (execução das ações fica lá em baixo)

fazer_postagem = st.sidebar.button('Novo post', on_click=click_button, args=[0, '', ''])
st.sidebar.write('')
st.sidebar.write('')

# Outras páginas

pagina_perfil = coluna_paginas.button('Perfil')
pagina_criar_gp = coluna_paginas.button('Criar Grupo')

if pagina_perfil:
    st.switch_page('pages/tela_perfil.py')

if pagina_criar_gp:
    st.switch_page('pages/tela_criar_grupo.py')

st.sidebar.write('')
st.sidebar.write('')

# Grupos já existentes

st.sidebar.write("Grupos")
grupos = carregar_grupos()
for gp in grupos:
    grupo = coluna_paginas.button(gp, on_click=visao_grupo_button)

# Feed
if st.session_state.button:
    titulo = st.text_input('Título')
    conteudo = st.text_area('Descrição')
    st.file_uploader('Arquivos')
    voltar = st.button('Voltar', on_click=click_button, args=[0, '', ''])
    if st.button('Publicar'):
        resp = fazer_post(titulo, conteudo)
        if resp == 1:
            st.write('Publição feita!')
elif st.session_state.button_visao_grupo:
    # Prototipo para envio das mensagens

    msg_outro_usuario, msg_usuario_atual = st.columns([1, 1])
    # Seção de exibição das mensagens
    with msg_outro_usuario:
        st.markdown(
            "<div style='background-color: #486a84; padding: 3px; border-radius: 1px; font-size: small;'>Usuário 1</div>",
            unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color: #486a84; padding: 8px; border-radius: 1px;'>Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto</div>",
            unsafe_allow_html=True)
        for i in range(8):
            st.text('')
        st.markdown(
            "<div style='background-color: #486a84; padding: 3px; border-radius: 1px; font-size: small;'>Usuário 1</div>",
            unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color: #486a84; padding: 8px; border-radius: 1px;'>Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto</div>",
            unsafe_allow_html=True)

    with msg_usuario_atual:
        for i in range(7):
            st.text('')
        st.markdown(
            "<div style='background-color: #000080; padding: 3px; border-radius: 1px; font-size: small;'>Você</div>",
            unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color: #000080; padding: 8px; border-radius: 1px;'>Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto</div>",
            unsafe_allow_html=True)

    for i in range(4):
        st.text('')
    input_placeholder = st.empty()
    message = input_placeholder.text_input("Digite sua mensagem...", "")

    if st.button("Enviar") and message:
        with msg_usuario_atual:
            for i in range(8):
                st.text('')
            st.markdown(
                "<div style='background-color: #000080; padding: 3px; border-radius: 1px; font-size: small;'>Você</div>",
                unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #000080; padding: 8px; border-radius: 1px;'>{message}</div>",
                        unsafe_allow_html=True)
else:
    st.text_input('Procurar grupos')
    st.header('Feed')

    # Ações do usuário

    # Função para formatar e exibir um post
    def exibir_post(titulo, postagem, nome_usuario, email, url_foto_perfil):
        with st.form(key=chave_formatacao):
            st.image(url_foto_perfil, width=75, caption='')
            st.write(f"""{nome_usuario} ({email})""")
            st.header(f'{titulo}')
            st.write(postagem)
            like = st.form_submit_button("Curti")

    # Incluir lógica para carregar grupos
    def exibir_grupo(nome_grupo, url_foto_grupo, cod_acesso):
        with st.form():
            st.image(url_foto_grupo, width=75, caption='')
            st.write(f"""{nome_grupo}""")
            entrar = st.button("Entrar")


    # Exibir todos os posts, formatados
    url_foto_perfil_exemplo = imagem_url

    chave_formatacao = "my_form_" + str(0)
    for i in range(17, 24):  # Carregar alguns exemplos, logica para carregar mais recentes depois
        dp = carregar_publicacao(i)
        if dp is not None:
            exibir_post(dp[0], dp[1], dp[2], dp[3], url_foto_perfil_exemplo)
            chave_formatacao = "my_form_" + str(i)
