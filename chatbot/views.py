from django.shortcuts import render

# Home View
def home(request):
    return render(request, 'chatbot/home.html', context={'title': 'Home'})

# Chat View
def chat(request):
    return render(request, 'chatbot/chat.html', context={'title': 'Chat'})
