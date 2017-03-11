"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dashboard import views as dashboard_view
from twitter_board import views as twitter_view
from fb import views as fb_view
from quora import views as quora_view
from topic import views as topic_view
from darkweb import views as darkweb_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dashboard_view.home),
    url(r'^twitter/', twitter_view.home),
    url(r'^fb/', fb_view.home),
    url(r'^quora/', quora_view.home),
    url(r'^topic/', topic_view.home),
    url(r'^darkweb/', darkweb_view.home),
    url(r'^profile/', dashboard_view.profile),
    url(r'^contributors/', dashboard_view.contrib),
]
