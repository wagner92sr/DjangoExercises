from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')
   # return HttpResponse('Olá Mundo')

def lerDoBanco(nome):
    lista_consoles = [
        {'nome': 'xbox', 'empresa': 'Microsoft'},
        {'nome': 'dreamcast', 'empresa': 'Sega'},
        {'nome': 'playstation', 'empresa': 'Sony'},
        {'nome': 'nes', 'empresa': 'Nintendo'}
    ]

    for console in lista_consoles:
        if console['nome'] == nome:
            return console
    else:
        return{'nome': ' ', 'empresa': ' '}

def console(request, nome):
    result = lerDoBanco(nome)
    print(result)
    if result['nome'] != '':
       return HttpResponse('O console ' + result['nome'] + ' foi fabricado pela empresa ' + result['empresa'])
    else:
        return HttpResponse('O console não foi encontrado.')

def console2(request, nome):
    empresa = lerDoBanco(nome)['empresa']
    return render(request, 'console.html', {'v_empresa': empresa})