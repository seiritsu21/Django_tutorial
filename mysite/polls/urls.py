from django.urls import path

from . import views

# app_nameがあると同じ名前のnameが複数のアプリケーションにある時も区別できる
app_name = 'polls'

urlpatterns = [
    # ここでnameをつけておくことでhtmlで{%url%}をつかってnameで指定してあげられるのでurlパスへの依存をなくせる
    # 例えば/polls/5/ を/polls/specifics/5/ にしたい時、ここの(url.py)のpathを変えればよくなる
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
