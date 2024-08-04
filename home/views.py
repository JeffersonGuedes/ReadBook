from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def redirect_to_login(request):
    return redirect('/auth/login/')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com essse username')

        user = User.objects.create_user(username=username,password=senha)
        user.save()
        return redirect(login_view)

        
def login_view(request):
    if request.method == "GET":   
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)
        if user:
            login(request, user)

            return redirect (index)
        else:
            return HttpResponse('Usuário ou senha inválida')
        
@login_required(login_url="/auth/login/")
def index(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/")
def base(request):
    return render(request, 'base.html')
    
@login_required(login_url="/auth/login/")
def livro_list(request):
    user = request.user
    user_id = user.id
    livro = Livro.objects.raw(
        """SELECT l.id, l.titulo, l.descricao, l.autor, l.formato, l.preco, l.user_id FROM public.home_livro l left join public.auth_user u on l.user_id = u.id where user_id = %s;""",
        [user_id]
    )
    return render(
        request,
        "livro_list.html",
        {"livros": livro},
    )

@login_required(login_url="/auth/login/")
def livro_create(request):
    return render(request, 'livro_form.html')

@login_required(login_url="/auth/login/")
def salvar_livro(request):
    if request.method == "POST":
        user = request.user
        titulo = request.POST.get("nome")
        if titulo == "":
            return render(request, "page_404.html")
        nome_autor = request.POST.get("nome_autor")
        data_publicacao = request.POST.get("data_publicacao")
        if data_publicacao == "":
            data_publicacao = None
        editora = request.POST.get("editora")
        if editora == "":
            editora = None
        num_pag = request.POST.get("num_pag")
        if num_pag == "":
            num_pag = None
        genero = request.POST.get("genero")
        if genero == "":
            genero = None
        idioma = request.POST.get("idioma")
        if idioma == "":
            idioma = None
        formato = request.POST.get("formato")
        if formato == "":
            formato = None
        preco = request.POST.get("preco")
        if preco == "":
            preco = None
        capa = request.POST.get("capa")
        if capa == "":
            capa = None
        descricao = request.POST.get("descricao")
        if descricao == "":
            descricao = None

        Livro.objects.create(
            user=user,
            titulo=titulo,
            autor=nome_autor,
            data_publicacao=data_publicacao,
            editora=editora,
            numero_paginas=num_pag,
            genero=genero,
            idioma=idioma,
            descricao=descricao,
            capa=capa,
            formato=formato,
            preco=preco,    
        )
        return redirect(livro_list)
    return redirect(salvar_livro)
    
@login_required(login_url="/auth/login/")
def editar_livro(request, id):
    livros = Livro.objects.get(id=id)
    return render(request, "editar_livro.html", {"livros": livros})

@login_required(login_url="/auth/login/")
def update_livro(request, id):
    if request.method == "POST":
        livro = Livro.objects.get(id=id)
        titulo = request.POST.get("nome")
        if titulo == "":
            return render(request, "page_404.html")
        nome_autor = request.POST.get("nome_autor")
        if nome_autor == "":
            nome_autor = livro.autor
        data_publicacao = request.POST.get("data_publicacao")
        if data_publicacao == "":
            data_publicacao = livro.data_publicacao
        editora = request.POST.get("editora")
        if editora == "":
            editora = livro.editora
        num_pag = request.POST.get("num_pag")
        if num_pag == "":
            num_pag = livro.numero_paginas
        genero = request.POST.get("genero")
        if genero == "":
            genero = livro.genero
        idioma = request.POST.get("idioma")
        if idioma == "":
            idioma = livro.idioma
        formato = request.POST.get("formato")
        if formato == "":
            formato = livro.formato
        preco = request.POST.get("preco")
        if preco == "":
            preco = livro.preco
        capa = request.POST.get("capa")
        if capa == "":
            capa = livro.capa
        descricao = request.POST.get("descricao")
        if descricao == "":
            descricao = livro.descricao
        
        livro.titulo = titulo
        livro.save()
        livro.autor = nome_autor
        livro.save()
        livro.data_publicacao = data_publicacao
        livro.save()
        livro.editora = editora
        livro.save()
        livro.numero_paginas = num_pag
        livro.save()
        livro.genero = genero
        livro.save()
        livro.idioma = idioma
        livro.save()
        livro.descricao = descricao
        livro.save()
        livro.capa = capa
        livro.save()
        livro.formato = formato
        livro.save()
        livro.preco = preco
        livro.save()
        return redirect(livro_list)

@login_required(login_url="/auth/login/")
def delete_livro(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect(livro_list)

    