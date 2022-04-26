from django.shortcuts import render
from .models import Articles
# from .forms import ArticlesForm
from django.views.generic import DetailView


def index(request):
    polls = Articles.objects.order_by('-date')  # order_by сортировка обектов по времени
    comps = []
    s = comps
    for el in polls:
        # if el.id < 4:
        comps.append(el.id)
        comps.append(el.title)
        comps.append(el.price)
        comps.append(el.date)
    # pag = ['1', '2', '3']

    return render(request, 'polls/index.html', {'id1': s[0], 'title1': s[1], 'price1': s[2], 'date1': s[3],
                                                'id2': s[4], 'title2': s[5],
                                                'price2': s[6], 'date2': s[7], 'id3': s[8],
                                                'title3': s[9],
                                                'price3': s[10],
                                                'date3': s[11]})


def sign(request):
    return render(request, 'polls/about.html')


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'polls/detail_view.html'
    context_object_name = 'article'


def table():
    return
