from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib import messages
from core.models import Produto
from core.forms import ProdutoModelForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import Post, Category, Author
from django.db.models import Q
from django.views.generic import ListView
from .forms import NewUserForm, PerfilEditForm



from django.contrib.auth.forms import AuthenticationForm
# editar perfil
def view_perfilEdit(request, pk):
    data = dict()
    data['db'] = User.objects.get(pk=pk)
    data['form'] = PerfilEditForm(instance=data['db'])
    
    return render(request, 'perfilEdit.html', data)

# ver perfil
def view_perfil(request, pk):
    data = dict()
    data['db'] = User.objects.get(pk=pk)
    print(f'data: {data}')
    return render(request, 'perfil.html', data)

# update dados do perfil
def update_perfil(request, pk):
    data = dict()
    data['db'] = User.objects.get(pk=pk)
    form = PerfilEditForm(request.POST or None, instance=data['db'])
    
    print('=-=================================')
    print('request:', request)
    print('request post:', request.POST)
    print('id:', data['db'])
    
    if form.is_valid():
        form.save()
    
        return render(request, 'perfil.html', data)
        # return HttpResponseRedirect('/')
        # return HttpResponsePermanentRedirect('/')
        

    
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# pagina do contato
def contato_request(request):
    return render(request, 'contato.html')

# pagina register/cadastro
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

@login_required(login_url='/login/')

def information(request):
    return redirect(request, 'info')

def logout_user(request):
    logout(request)
    messages.info(request, "logout feito com sucesso")
    return redirect('/')
    
def index(request):
   produtos =Produto.objects.all().order_by('-tempo_post')
   context = {
    'produtos' : produtos
   }
   return render(request, 'index.html', context)
#    substitui produto por post
def post(request):
    if request.method == 'POST':
      
        form = ProdutoModelForm(request.POST, request.FILES)
       
        if form.is_valid():
          
            form.save()
            messages.success(request, 'produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar o produto')
            # return render (request, 'produto.html')
    else:
        form = ProdutoModelForm()
       
    context = {'form' : form }
    return render(request, 'post.html', context)

def produto_submit(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST.get("text"), request.FILES)
        ProdutoModelForm['user'].widget.attrs['readonly'] = True 
        if form.is_valid():
            form.save()
            messages.success(request, 'produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar o produto')
            return render (request, 'produto.html')
    else:
        return redirect('index')
# def post_submit(request):
#     if request.method == 'POST':
#         form = ProdutoModelForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'produto salvo com sucesso')
#             form = ProdutoModelForm()
#         else:
#             messages.error(request, 'Erro ao salvar o produto')
#             return render (request, 'post.html')
#     else:
#         return redirect('index')
def perfil_request(request):
    return render (request, 'perfil.html')
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {
        'user_value' : ""
    }    
    return render(request, 'login.html', context)
def login_submit(request):
    if request.method == 'POST':
        if request.POST:
            usuario = request.POST.get('usuario')
            senha = request.POST.get('senha')
            user = authenticate(username=usuario, password=senha)
            if user:
                messages.success(request, 'Login com sucesso')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Error: Usuario ou senha invalido")
                
                context = {
                    'user_value' : usuario
                }
            return render(request, 'login.html', context)
    messages.error(request, 'Erro ao logar, nao envio de dados')
    context ={
        'user_value' : ""
    }
    return render(request, 'login.html', context)
    
def registre(request):    
    return render(request, 'registre.html')

def create_usuario(request):
    if request.POST:
        if not request.POST.get('password1'):
            return render(request, 'registre.html')
        if not request.POST.get('password2'):
            return render(request, 'registre.html')
        if request.POST.get('password1') == request.POST.get('password2'):       
            user = User.objects.create(
                username = request.POST.get('username'),
                email = request.POST.get('email'),
                first_name = request.POST.get('first_name')
                )
            user.set_password(request.POST.get('password1'))
            user.save()
            
            messages.success(request, 'Cadastro com sucesso')
            return redirect('/')
        else:
            messages.error(request, "senhas não batem")
            return render(request, 'registre.html')

# def post(request):    
#     return render(request, 'post.html')
def create_post(request):
    if request.POST:
        if not request.POST.get('password1'):
            return render(request, 'registre.html')
        if not request.POST.get('password2'):
            return render(request, 'registre.html')
        if request.POST.get('password1') == request.POST.get('password2'):       
            user = User.objects.create(
                username = request.POST.get('username'),
                email = request.POST.get('email'),
                first_name = request.POST.get('first_name')
                )
            user.set_password(request.POST.get('password1'))
            user.save()
            
            messages.success(request, 'Cadastro com sucesso')
            return redirect('/')
        else:
            messages.error(request, "senhas não batem")
            return render(request, 'registre.html')
# ----------------------------

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_bar.html', context)

