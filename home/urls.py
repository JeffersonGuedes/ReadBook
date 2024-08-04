from django.urls import path
from home.views import *

urlpatterns = [
          path("", redirect_to_login),
          path("home/", index, name="index"),
          path('register/', register, name='register'),
          path('login/', login_view, name='login'),
          path('livro/create/', livro_create, name='livro_create'),
          path('livros/', livro_list, name='livro_list'),
          path('base/', base, name="base"),

          path("add/", salvar_livro, name="salvar"),
          path("editar<int:id>/", editar_livro, name="editar"),
          path("update<int:id>/", update_livro, name="update"),
          path("delete<int:id>/", delete_livro, name="delete"),
]