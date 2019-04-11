from django.shortcuts import render, redirect
from django.template import loader
from colorer import compl
import jsonpickle
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
    'json_colors': jsonpickle.encode(color_default),
}
# Create your views here.
def home_page(request):
    color_history = [{'bg': '#563d7c', 'txt': 'rgba(255, 255, 255, 0.5)', 'txth': 'rgba(255, 255, 255, 0.7)',
                      'texb': '#FFFFFF'}]
    context['colors'] = color_history
    context['json_colors'] = jsonpickle.encode(color_history)
    return render(request, template_name='ajax_colorer/base.html', context=context)


def random_color(prefix, maxlen):
    symbols = '0123456789ABCDF'
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def detect_text_color(color):
    return compl.contrast(color)

def change_color(request):
    pass