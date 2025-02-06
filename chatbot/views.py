import openai
import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

openai.api_key = settings.OPENAI_API_KEY

# Home View
def home(request):
    return render(request, 'chatbot/home.html', context={'title': 'Home'})

# Chat View
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('user_message', '')
        response_text = query_openai(user_message)
        return JsonResponse({'response': response_text})
    return render(request, 'chatbot/chat.html', context={'title': 'Chat'})

# OpenAI-API Query Function
def query_openai(query):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Or any specific model
            prompt=query,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error querying OpenAI: {e}")
        return "Sorry, there was an error processing your request."