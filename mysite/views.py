from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from artikels.models import ArtikelBlog, Kategori
from django.contrib.auth.models import User, Group

def home(request):
    template_name = "landingpage/index.html"
    artikels = ArtikelBlog.objects.all()
    kategori = Kategori.objects.all()
    context = {
        "artikels": artikels,
        "kategori": kategori
    }
    
    return render(request, template_name, context)

def artikel_detail(request, id):
    template_name = "landingpage/artikel_detail.html"
    artikels = get_object_or_404(ArtikelBlog, id=id)  # Ambil artikel berdasarkan ID
    kategori = artikels.kategori  # Ambil kategori terkait artikel

    artikel_lainnya = ArtikelBlog.objects.all().exclude(id=id)
    context = {
        "artikels": artikels,
        "kategori": kategori,
        "artikel_lainnya": artikel_lainnya
    }

    return render(request, template_name, context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    template_name = "dashboard/index.html"
    artikel = ArtikelBlog.objects.count()
    kategori = Kategori.objects.count()
    users = User.objects.count()
    
    context = {
        "artikel": artikel,
        "kategori": kategori,
        "users": users
    }
    
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    
    context = {
        "title": "Selamat datang"
    }
    
    return render(request, template_name, context)
