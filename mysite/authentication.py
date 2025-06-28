from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    template_name = "login.html"
    pesan = ""
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            pesan = "Username dan Password Wajib Diisi!"
        else:
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                pesan = "Berhasil Login"
                return redirect('/dashboard')
            else:
                pesan = "Username atau Password Salah!"
        
    context = {
        "pesan": pesan
    }
    return render(request, template_name, context)


def registrasi(request):
    template_name = "registrasi.html"
    pesan = ""
    
    if request.method == "POST":
        username = request.POST.get('username')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        password = request.POST.get('password')
        konf_password = request.POST.get('konf_password')
        
        if not username or not nama_depan or not nama_belakang or not password or not konf_password:
            pesan = "Semua wajib diisi!"
        else:
            if password != konf_password:
                pesan = "Password tidak cocok"
            else:
                user = User.objects.filter(username=username)
                if user.exists():  # Memperbaiki pemanggilan exists()
                    pesan = "Username sudah digunakan!"
                else:
                    user = User.objects.create(
                        username=username,
                        first_name=nama_depan,
                        last_name=nama_belakang
                    )
                    user.set_password(password)
                    user.save()
                    return redirect("/")
        
    context = {
        'pesan': pesan
    }
    return render(request, template_name, context)

def logout(request):
    auth_logout(request)
    return redirect('/')