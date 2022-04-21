from django.urls import path

from myToDo.views import Index, Task


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("<int:id>", Task.as_view(), name='task'),
    
]
handler404 = 'myToDo.views.handler404'
