from django.shortcuts import render, HttpResponse
import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR/'.env')


GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY') # Sua chave de API do GoogleGemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-8b-001')


def joke(request):
    print(f'Metodo:{request.method}')
    
    excuse_pt='Desculpe, não há uma desculpa para hoje.'
    
    if request.method == 'POST':
        try:
            objective = request.POST.get('target_exc')
            if not objective:
                raise ValueError("Nenhum alvo de desculpa foi fornecido.")
            
            print(objective)
            print('Conexão bem sucedida.')
           
            prompt = f"""
                Crie uma desculpa esfarrapada e completamente inacreditavel para faltar ou negar algo a:{objective}.
                Apenas me de a desculpa sem criar explicações.
                Não use desculpas genericas tipo : Meu unicornio magico comeu meu bilhete.
                Deixe claro na desculpa o ambiente ou com quem você está falando dentro da propria desculpa de uma forma que fosse uma conversa, não é permitido aspas ou parenteses.
                A desculpa tem que fazer sentido no final.
            """


        
            resposta = model.generate_content(prompt)

            excuse_pt = resposta.text.strip()

        except Exception as e:
            print(f'Erro:{e}')

    context = {
        'excuse':excuse_pt,
    }
    return render(request,'joke/joke.html',context)