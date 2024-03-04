
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.TaskListview.as_view(),name='cbvhome'),

]