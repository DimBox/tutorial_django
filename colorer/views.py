from django.shortcuts import render, redirect
from django.template import loader
import jsonpickle
import random

color_history = ['#563d7c']
article1 = 'Возникало ли у Вас желание изменить цветовую гамму страницы? Данный проект создан в образовательных целях. Здесь можно легко изменить цветовую гамму страницы, нажав на кнопку "Изменить". Вернуться на исходный вариант можно по ссылке в меню "Домой"'
article2 = 'url ссылка "Изменить" перенаправляет нас на страницу /change. Через маршрутизацию urls.py мы выходим на метод views.py, где производится случайная генерация цвета. Сформированный параметр сериализуется в json для дальнейшей его передачи в jquery с целью избежать расхождения в типах переменных. Как локальный параметр этот json передается в шаблон страницы, где принимается переменной javascript и применяется через jquery в css стиле. Для удобства изменения, в css созданы переменные в разделе :root.'

context = {
    'title': 'Калейдоскоп',
    'value': [article1, article2],
    'colors': color_history,
    'json_colors': jsonpickle.encode(color_history),
}
# Create your views here.
def home_page(request):
    color_history = ['#563d7c']
    context['colors'] = color_history
    context['json_colors'] = jsonpickle.encode(color_history)
    return redirect(make_up)

def make_up(request):
    return render(request, template_name='colorer/base.html', context=context)


def random_color(prefix, maxlen):
    symbols = '0123456789ABCDF'
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

def change_color(request):
    new_color = random_color('#',6)
    context['colors'].append(new_color)
    context['json_colors'] = jsonpickle.encode(new_color)
    return redirect(make_up)