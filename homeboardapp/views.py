from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from articleapp.models import NewArticle


has_ownership=[
            login_required,
            account_ownership_required
]

# Create your views here.


def start_work(request):
    return render(request, 'homeboardapp/start_work.html')

def family_sns(request):
    return render(request, 'homeboardapp/family_sns.html')



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homeboard(request):
    article_list = NewArticle.objects.all().order_by('-created_at')   # 모든 아티클을 가져옴
    paginator = Paginator(article_list, 5)  # 페이지당 5개 아티클

    page = request.GET.get('page', '1')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # 페이지가 정수가 아닌 경우, 첫 번째 페이지를 반환
        articles = paginator.page(1)
    except EmptyPage:
        # 페이지가 비어있는 경우, 마지막 페이지를 반환
        articles = paginator.page(paginator.num_pages)

    return render(request, 'homeboardapp/homeboard.html', {'articles': articles})
