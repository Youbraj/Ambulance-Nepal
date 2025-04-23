from django.urls import path, include
from meroapp import views

app_name = 'meroapp'

urlpatterns = [
    #path('test/<int:id>',views.index,name='index'),
    path('ambulances/',views.ambulances_search,name='ambulances-search'),
    # path('ambulances/',views.create2,name='ambulances2'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('admin-login/',views.admin,name='login'),
    path('admin-home/',views.admin_home,name='admin_home'),
    path('view-ambulances', views.view_ambulances, name='view-ambulances'),
    path('insert-ambulance', views.insert_ambulance, name='insert-ambulance'),
    path('update-ambulance/<str:id>', views.update_ambulance, name='update-ambulance'),
    path('delete-ambulance/<str:id>', views.delete_ambulance, name='delete-ambulance'),
    path('view-queries/', views.view_queries, name='view-queries'),
    # path('add-query/',views.send_query,name='add-query')
]