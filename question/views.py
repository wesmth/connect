from django.shortcuts import render, redirect
import requests

def make_question(request):
    if request.method == 'POST':
        question = request.POST.get('make_question')
        request.session['question'] = question
        return redirect('make_question')

    question = request.session.get('question')

    answer = None
    answer_image = None

    url = 'https://yesno.wtf/api'

    if question:
        try:
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()

            answer = data.get('answer')
            if answer == 'yes':
                answer = 'Sim'
            elif answer == 'no':
                answer = 'Não'
            else:
                answer = 'Talvez'

            answer_image = data.get('image')

            if 'question' in request.session:
                del request.session['question']

        except requests.RequestException as error:
            print('Falha na conexão:', error)
            answer = 'Erro na API'
            answer_image = None
            

    context = {
        'answer': answer,
        'answer_image': answer_image,
        'question': question
    }

    return render(request, 'question/question_page.html', context)
