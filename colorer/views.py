from django.shortcuts import render, redirect
from django.template import loader
from . import compl
import jsonpickle
import random

color_history = [{'bg': '#563d7c', 'txt': 'rgba(255, 255, 255, 0.5)', 'txth': 'rgba(255, 255, 255, 0.7)',
                  'texb': '#FFFFFF'}]
article1 = '''Возникало ли у Вас желание изменить цветовую гамму страницы? Данный проект создан в образовательных целях.
 Здесь можно легко изменить цветовую гамму страницы, нажав на кнопку "Изменить". Вернуться на исходный вариант можно по 
 ссылке в меню "Домой"'''
article2 = '''url ссылка "Изменить" перенаправляет нас на страницу /change. Через маршрутизацию urls.py мы выходим на 
метод views.py, где производится случайная генерация цвета. Сформированный параметр сериализуется в json для дальнейшей 
его передачи в jquery с целью избежать расхождения в типах переменных. Как локальный параметр этот json передается в 
шаблон страницы, где принимается переменной javascript и применяется через jquery в css стиле. Для удобства изменения, 
в css созданы переменные в разделе :root.
Несколько труднее с выбором контрастного цвету фона шрифта. Я остановился на двух цветах, либо черный, либо белый. 
Вопрос только - когда его менять?
Для этого используется "магическая" математика - конвертация в различных цветовых пространствах и выбор некоего 
критерия, на основании которого и принимается это решение.'''

context = {
    'title': 'Калейдоскоп',
    'value': [article1, article2],
    'colors': color_history,
    'json_colors': jsonpickle.encode(color_history),
}
# Create your views here.
def home_page(request):
    color_history = [{'bg': '#563d7c', 'txt': 'rgba(255, 255, 255, 0.5)', 'txth': 'rgba(255, 255, 255, 0.7)',
                      'texb': '#FFFFFF'}]
    context['colors'] = color_history
    context['json_colors'] = jsonpickle.encode(color_history)
    return redirect(make_up)

def make_up(request):
    return render(request, template_name='colorer/base.html', context=context)


def random_color(prefix, maxlen):
    symbols = '0123456789ABCDF'
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def detect_text_color(color):
    return compl.contrast(color)

def change_color(request):
    new_color = random_color('#',6)
    text_color = detect_text_color(new_color)
    if text_color in ['#FFFFFF', '#ffffff']:
        btn_color = '#000000'
    else:
        btn_color = '#FFFFFF'
    context['colors'].append({'bg': new_color, 'txt': text_color})
    context['json_colors'] = jsonpickle.encode({'bg': new_color, 'txt': compl.hex_to_rgba(text_color, 0.5),
                                                'txth': compl.hex_to_rgba(text_color, 0.7), 'txtb': btn_color})
    return redirect(make_up)