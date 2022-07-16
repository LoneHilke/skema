from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name= "index"),
  path('add/', views.add, name= "add"),
  path('add/addrecord/', views.addrecord, name= "addrecord"),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('tlf', views.tlf_index, name= "tlf_index"),
  path('tlf_add/', views.tlf_add, name= "tlf_add"),
  path('tlf_add/tlf_addrecord/', views.tlf_addrecord, name= "tlf_addrecord"),
  path('tlf_delete/<int:id>', views.tlf_delete, name='tlf_delete'),
  path('tlf_update/<int:id>', views.tlf_update, name='tlf_update'),
  path('tlf_update/tlf_updaterecord/<int:id>', views.tlf_updaterecord, name='tlf_updaterecord'),
]