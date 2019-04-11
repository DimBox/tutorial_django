from django.shortcuts import render, redirect
from django.http import JsonResponse
from colorer import compl

import random

color_default = [{'bg': '#563d7c', 'txt': 'rgba(255, 255, 255, 0.5)', 'txth': 'rgba(255, 255, 255, 0.7)',
                  'texb': '#FFFFFF'}]
article = '''В данной версии мы будем изменять цветовую схему без перегрузки страницы, нажав на кнопку "Изменить".
 В этом нам поможет технология AJAX. Как и прежде, вернуться на исходный вариант можно по ссылке в меню "Домой"
 Теперь url ссылка "Изменить" по методу click будет вызывать генерацию запроса ajax к нашему web серверу'''

context = {
    'title': 'Калейдоскоп-AJAX',
    'value': [article],
    'colors': color_default,
    'json_colors': color_default,
}
# Create your views here.
def home_page(request):
    color_default = [{'bg': '#563d7c', 'txt': 'rgba(255, 255, 255, 0.5)', 'txth': 'rgba(255, 255, 255, 0.7)',
                      'texb': '#FFFFFF'}]
    context['colors'] = color_default
    context['json_colors'] = color_default
    return render(request, template_name='ajax_colorer/base.html', context=context)


def random_color(prefix, maxlen):
    symbols = '0123456789ABCDF'
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def detect_text_color(color):
    return compl.contrast(color)


def change_color(request):
    new_color = random_color('#', 6)
    text_color = detect_text_color(new_color)
    if text_color in ['#FFFFFF', '#ffffff']:
        btn_color = '#000000'
    else:
        btn_color = '#FFFFFF'
    context['colors'].append({'bg': new_color, 'txt': text_color})
    context['json_colors'] = {'bg': new_color, 'txt': compl.hex_to_rgba(text_color, 0.5),
            'txth': compl.hex_to_rgba(text_color, 0.7), 'txtb': btn_color}
    return JsonResponse(context['json_colors'])
