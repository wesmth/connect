from django.shortcuts import render, redirect
import requests

# View responsável por exibir e processar o formulário de pergunta
def make_question(request):
    # Verifica se a requisição é do tipo POST (ou seja, o form foi enviado)
    if request.method == 'POST':
        # Pega o valor digitado no campo "make_question"
        question = request.POST.get('make_question')
        # Salva essa pergunta na sessão pra usar depois
        request.session['question'] = question
        # Redireciona pra mesma view (pra evitar reenvio do form ao atualizar a página)
        return redirect('make_question')

    # Tenta recuperar a pergunta salva na sessão
    question = request.session.get('question')

    # Inicializa as variáveis que vão conter a resposta e imagem da API
    answer = None
    answer_image = None

    # URL da API que responde sim/não/talvez
    url = 'https://yesno.wtf/api'

    # Se tiver uma pergunta na sessão, faz a requisição
    if question:
        try:
            # Faz a requisição pra API e já converte em JSON
            response = requests.get(url).json()

            # Pega a resposta e traduz pra português
            answer = response['answer']
            if answer == 'yes':
                answer = 'Sim'
            elif answer == 'no':
                answer = 'Não'
            else:
                answer = 'Talvez'

            # Pega a URL da imagem associada à resposta
            answer_image = response['image']

            print('Conexão bem sucedida.')
            
            # Limpa a pergunta da sessão pra não exibir de novo ao recarregar a página
            del request.session['question']

        # Se der ruim na requisição, exibe erro no terminal
        except (requests.RequestException) as error:
            print('Falha na conexão', error)

    # Cria o dicionário com os dados pra passar pro template
    context = {
        'answer': answer,
        'answer_image': answer_image,
        'question': question
    }

    # Renderiza a página com as informações
    return render(request, 'question/question_page.html', context)
