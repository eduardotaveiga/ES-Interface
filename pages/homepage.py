
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Layout de colunas para organizar os componentes

coluna_paginas = st.sidebar
coluna_postagens = st

# Barra Lateral

imagem_url = 'https://i.ibb.co/XjtdCtD/Whats-App-Image-2024-03-07-at-17-50-22.png'
st.sidebar.image(imagem_url, width=200, caption='')

pagina_home = coluna_paginas.button('Home')

# Ações do usuário (execução das ações fica lá em baixo)

fazer_postagem = st.sidebar.button('Novo post')
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
grupos = ["Grupo 1", "Grupo 2", "Grupo 3"]
for i in range(0, len(grupos)):
    grupo = coluna_paginas.button(str(grupos[i]))

# Feed

st.text_input('Procurar grupos')
st.header('Feed')

# Ações do usuário

todos_grupos = ["Grupo 1", "Grupo 2", "Grupo 3", "Grupo 4", "Grupo 5", "Grupo 6"]

#if fazer_postagem:
#    nova_postagem = st.text_area('Faça uma nova postagem:')
#    enviar_postagem = st.button('Enviar')
#
#    if enviar_postagem:
#        st.write('Postagem enviada:', nova_postagem)
#        st.write(nova_postagem)
#        feed_postagens.append(nova_postagem)


# Função para formatar e exibir um post

def exibir_post(postagem, nome_usuario, url_foto_perfil):
    with st.form(key=chave_formatacao):
        st.image(url_foto_perfil, width=75, caption='')
        st.write(f"""{nome_usuario}""")
        st.write(postagem)
        like = st.form_submit_button("Curti")


def exibir_grupo(nome_grupo, url_foto_grupo, cod_acesso):
    with st.form():
        st.image(url_foto_grupo, width=75, caption='')
        st.write(f"""{nome_grupo}""")
        entrar = st.button("Entrar")


# Exibir todos os posts, formatados

postagem_exemplo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
nome_usuario_exemplo = "Usuário Exemplo"
url_foto_perfil_exemplo = imagem_url

dados_posts = [[postagem_exemplo, nome_usuario_exemplo, url_foto_perfil_exemplo],
               [postagem_exemplo, nome_usuario_exemplo, url_foto_perfil_exemplo],
               [postagem_exemplo, nome_usuario_exemplo, url_foto_perfil_exemplo]
               ]

iteracao = 0
chave_formatacao = "my_form_" + str(iteracao)

for i in dados_posts:
    exibir_post(i[0], i[1], i[2])
    iteracao = iteracao + 1
    chave_formatacao = "my_form_" + str(iteracao)
