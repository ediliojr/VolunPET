from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
    nome = models.CharField ('Nome',max_length=100)
    postagem = models.CharField ('Postagem',max_length=1000, blank= True, null = True)
    preco = models.DecimalField ('Preco',decimal_places=2, max_digits=15, blank= True, null = True)
    estoque = models.IntegerField('Qtd no Estoque', blank= True, null = True)
    imagem = models.ImageField ('IMG', blank=False, null=False, upload_to="core")
    tempo_post =  models.DateTimeField(auto_now_add=True)
    tags=models.SlugField()
    usuario = models.ForeignKey (User,
    null=True, 
    blank=True, 
    on_delete=models.SET_NULL,
    related_name="usuarios_produto",)
    

    def __str__(self) -> str:
        return super().__str__()

class User(models.Model):
    nome = models.CharField ('Nome',max_length=100)
    sobrenome = models.CharField ('Sobrenome',max_length=100)
    email = models.EmailField('Email',max_length=150, unique=True)
    data_nascimento = models.DateField ('Data Nascimento', blank=True, null=True)

    def __str__(self):
        return self.nome

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
		
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

# -----------------------------

class Post1(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title