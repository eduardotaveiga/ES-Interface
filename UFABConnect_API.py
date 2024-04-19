import requests


def fazer_login(username, password):
#    Para teste->  username:daeskk password:123456
    re = requests.post('http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/iam/login',
                   json={'username': username, 'password': password})
    if re.status_code == 201:
        token = re.json()['accessToken']
        with open('token.txt', 'w') as file:
            file.write(token)
        return 1
    else:
        return 0


def criar_grupo(nome, descricao):
    with open('token.txt', 'r') as file:
        bearer_token = file.read()
        headers = {"Authorization": f"Bearer {bearer_token}"}

    re = requests.post('http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/groups',
                       json={'name': nome, 'description': descricao},
                       headers=headers)
    if re.status_code == 201:
        return 1
    else:
        return 0


def fazer_post(titulo, conteudo):
    with open('token.txt', 'r') as file:
        bearer_token = file.read()
        headers = {"Authorization": f"Bearer {bearer_token}"}
    re = requests.post('http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/posts',
                       json={'groupId': 1, 'title': titulo,
                             'content': conteudo},
                       headers=headers)
    if re.status_code == 201:
        return 1
    else:
        return 0


def carregar_publicacao(id):
    with open('token.txt', 'r') as file:
        bearer_token = file.read()
        headers = {"Authorization": f"Bearer {bearer_token}"}

    re = requests.get(
        f'http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/posts/by-id/{id}',
        headers=headers)

    try:
        dados = re.json()
    except:
        pass
    else:
        return [dados['title'], dados['content'], dados['author']['username'], dados['author']['email']]


def carregar_grupos():
    with open('token.txt', 'r') as file:
        bearer_token = file.read()
        headers = {"Authorization": f"Bearer {bearer_token}"}

    re = requests.get('http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/groups',
                      headers=headers)
    saida = []
    for c in re.json():
        saida.append(c['name'])

    return saida



if '__name__' == '__main__':
    pass