from django.shortcuts import render, redirect
from .models import ContactMessage


def index(request):
    return render(request, 'mains/index.html')

def about(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return redirect("contact")
    return render(request, 'mains/about.html')

def services(request):
    return render(request, 'mains/services.html')

def projects(request):
    return render(request, 'mains/garage.html')

from django.core.paginator import Paginator

def blog(request):
    news_list = [
        {
            'number': '01',
            'category': 'MONZA / RACE',
            'date': '06 SEP 2026',
            'title': 'Антонелли совершает невероятный камбэк и выигрывает в Монце',
            'text': 'Кими Антонелли стартовал с 19-й позиции после штрафа за замену силовой установки, но сумел прорваться к победе в домашней гонке Mercedes.',
            'image': 'assets/img/gallery/antonelli.png',
        },
        {
            'number': '02',
            'category': 'MONZA / QUALIFYING',
            'date': '05 SEP 2026',
            'title': 'Гасли сенсационно завоёвывает первый поул в карьере',
            'text': 'Пилот Alpine неожиданно оказался быстрее всех в квалификации.',
            'image': 'assets/img/gallery/gasli.png',
        },
        {
            'number': '03',
            'category': 'FERRARI / PADDOCK',
            'date': '10 SEP 2026',
            'title': 'Хэмилтон и Леклер обсудили инцидент в Монце',
            'text': 'После напряжённого старта Гран-при Италии пилоты Ferrari поговорили о произошедшем и договорились оставить конфликт позади.',
            'image': 'assets/img/gallery/ferincident.png',
        },
        {
            'number': '04',
            'category': 'MADRID / PREVIEW',
            'date': '11 SEP 2026',
            'title': 'Формула-1 впервые выходит на трассу Madring',
            'text': 'Новый городской автодром принимает свой первый этап Формулы-1. Для команд и пилотов это новый вызов без опыта предыдущих гонок.',
            'image': 'assets/img/gallery/madrid.png',
        },
        {
            'number': '05',
            'category': 'CHAMPIONSHIP / 2026',
            'date': '10 SEP 2026',
            'title': 'Антонелли укрепляет лидерство в чемпионате',
            'text': 'Победа в Монце позволила пилоту Mercedes увеличить отрыв от Джорджа Расселла и укрепить позицию лидера сезона 2026.',
            'image': 'assets/img/gallery/madrid.png',
        },
        {
            'number': '06',
            'category': 'MERCEDES / RACE',
            'date': '06 SEP 2026',
            'title': 'Расселл финиширует вторым после долгой борьбы с Антонелли',
            'text': 'Джордж Расселл большую часть гонки контролировал ситуацию, но в конце уступил напарнику Кими Антонелли и занял второе место.',
            'image': 'assets/img/gallery/second.png',
        },
        {
            'number': '07',
            'category': 'RED BULL / RACE',
            'date': '06 SEP 2026',
            'title': 'Ферстаппен приносит Red Bull третье место в Монце',
            'text': 'Макс Ферстаппен воспользовался борьбой Mercedes и завершил Гран-при Италии на третьей позиции.',
            'image': 'assets/img/gallery/third.png',
        },
        {
            'number': '08',
            'category': 'FERRARI / INCIDENT',
            'date': '06 SEP 2026',
            'title': 'Леклер попадает в аварию и завершает гонку досрочно',
            'text': 'Шарль Леклер потерял контроль над Ferrari в начале гонки. После инцидента на трассе появился красный флаг.',
            'image': 'assets/img/gallery/dtp.png',
        },
        {
            'number': '09',
            'category': 'FERRARI / RACE',
            'date': '06 SEP 2026',
            'title': 'Хэмилтон финиширует шестым после сложного старта',
            'text': 'После инцидента с Леклером Льюис Хэмилтон потерял позиции, но сумел восстановиться и завершить гонку шестым.',
            'image': 'assets/img/gallery/hamilton.png',
        },
        {
            'number': '10',
            'category': 'MONZA / DRIVER',
            'date': '06 SEP 2026',
            'title': 'Антонелли получает награду Driver of the Day',
            'text': 'Болельщики выбрали Кими Антонелли лучшим пилотом Гран-при Италии после его камбэка с 19-го места.',
            'image': 'assets/img/gallery/news10.png',
        },
        {
            'number': '11',
            'category': 'MERCEDES / CHAMPIONSHIP',
            'date': '06 SEP 2026',
            'title': 'Mercedes укрепляет позиции в борьбе за чемпионство',
            'text': 'Двойной подиум в Монце помог Mercedes увеличить преимущество в борьбе за оба чемпионских титула.',
            'image': 'assets/img/gallery/news11.png',
        },
        {
            'number': '12',
            'category': 'MONZA / STRATEGY',
            'date': '06 SEP 2026',
            'title': 'Стратегия Mercedes становится ключом к победе Антонелли',
            'text': 'Пит-стоп Антонелли во время Virtual Safety Car позволил ему получить более свежие шины для решающей атаки.',
            'image': 'assets/img/gallery/news12.png',
        },
        {
            'number': '13',
            'category': 'MONZA / PRACTICE',
            'date': '04 SEP 2026',
            'title': 'Расселл быстрее всех во второй тренировке в Монце',
            'text': 'Джордж Расселл показал лучшее время FP2, опередив Шарля Леклера и своего напарника Кими Антонелли.',
            'image': 'assets/img/gallery/news13.png',
        },
        {
            'number': '14',
            'category': 'MERCEDES / QUALIFYING',
            'date': '03 SEP 2026',
            'title': 'Mercedes планирует работать командой в квалификации',
            'text': 'Расселл и Антонелли обсуждали командную работу в квалификации перед стартом с Гран-при Италии.',
            'image': 'assets/img/gallery/news14.png',
        },
        {
            'number': '15',
            'category': 'MONZA / GRID',
            'date': '06 SEP 2026',
            'title': 'Сразу несколько пилотов получают штрафы перед стартом',
            'text': 'Антонелли, Пиастри, Лоусон, Албон и Алонсо получили штрафы, изменившие стартовую расстановку в Монце.',
            'image': 'assets/img/gallery/news15.png',
        },
        {
            'number': '16',
            'category': 'MADRID / PREVIEW',
            'date': '10 SEP 2026',
            'title': 'Madring готовится к дебютному Гран-при Испании',
            'text': 'Новая трасса в Мадриде принимает свой первый этап Формулы-1 и становится главной темой паддока.',
            'image': 'assets/img/gallery/news16.png',
        },
        {
            'number': '17',
            'category': 'MADRID / PRACTICE',
            'date': '11 SEP 2026',
            'title': 'Расселл возглавляет первую тренировку на Madring',
            'text': 'Джордж Расселл показал лучшее время первой тренировки в Мадриде, а Кими Антонелли замкнул Mercedes-дубль.',
            'image': 'assets/img/gallery/news17.png',
        },
        {
            'number': '18',
            'category': 'MADRID / CIRCUIT',
            'date': '10 SEP 2026',
            'title': 'La Monumental — самый необычный поворот новой трассы',
            'text': 'Банковский поворот 12 становится одной из главных особенностей нового Madring и требует точной работы пилотов.',
            'image': 'assets/img/gallery/news18.png',
        },
        {
            'number': '19',
            'category': 'CHAMPIONSHIP / PREVIEW',
            'date': '10 SEP 2026',
            'title': 'Антонелли не думает о чемпионстве перед Гран-при Испании',
            'text': 'Лидер чемпионата предпочитает сосредоточиться на каждой сессии и не хочет позволять давлению влиять на выступление.',
            'image': 'assets/img/gallery/news19.png',
        },
        {
            'number': '20',
            'category': 'MADRID / FREE PRACTICE',
            'date': '11 SEP 2026',
            'title': 'Ferrari начинает уикенд в Мадриде с двух лучших времён',
            'text': 'Шарль Леклер и Льюис Хэмилтон завершили первую тренировку на третьем и четвёртом местах, сразу за пилотами Mercedes.',
            'image': 'assets/img/gallery/news20.png',
        },

        # сюда добавишь остальные новости
    ]

    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mains/blog.html', {
        'page_obj': page_obj
    })

def blog_details(request):
    return render(request, 'mains/blog_details.html')

def elements(request):
    return render(request, 'mains/elements.html')

def contacts(request):
    return render(request, 'mains/contact.html')
