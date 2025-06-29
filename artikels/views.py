from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from artikels.forms import *
from django.contrib import  messages

def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user > 0:
        return False
    else:
        return True

######################### user #########################
def home(request):
    artikels = ArtikelBlog.objects.all()
    return render(request, 'artikels/index.html', {'artikels': artikels})

def artikel_detail(request, id):
    artikels = get_object_or_404(ArtikelBlog, id=id)
    return render(request, 'artikels/artikel_detail.html', {'artikels': artikels})

@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = ArtikelBlog.objects.filter(created_by=request.user)
    context = {
        "artikel": artikel
    }
    
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    forms = ArtikelForms()
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil menambah artikel')
            return redirect(admin_artikel_list)
        else:
            print(forms.errors)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user)
    except:
        messages.warning(request, "Halaman tidak ditemukan")
        return redirect("/dashboard")
    
    forms = ArtikelForms(instance=artikel)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil mengupdate artikel')
            return redirect(artikel_list)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel, created_by=request.user).delete()
        messages.success(request, 'Berhasil menghapus artikel')
        
    except:
        messages.error(request, 'Gagal menghapus artikel')
        
    return redirect(artikel_list)


######################### admin #########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori": kategori
    }
    
    return render(request, template_name, context)

@login_required(login_url='auth_login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    forms = KategoriForms()
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil menambah kategori')
            return redirect(admin_kategori_list)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = Kategori.objects.get(id=id_kategori)
    forms = KategoriForms(instance=kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil mengupdate kategori')
            return redirect(admin_kategori_list)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
    try:
        kategori = Kategori.objects.get(id=id_kategori).delete()
        messages.success(request, 'Berhasil menghapus kategori')
        
    except Kategori.DoesNotExist:
        messages.error(request, 'Gagal menghapus kategori')

    return redirect('admin_kategori_list')

######################### artikel blog #########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = ArtikelBlog.objects.all()
    context = {
        "artikel": artikel
    }
    
    return render(request, template_name, context)

@login_required(login_url='auth_login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    forms = ArtikelForms()
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil menambah artikel')
            return redirect(admin_artikel_list)
        else:
            print(forms.errors)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = ArtikelBlog.objects.get(id=id_artikel)
    forms = ArtikelForms(instance=artikel)
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil mengupdate artikel')
            return redirect(admin_artikel_list)

    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
    try:
        artikel = ArtikelBlog.objects.get(id=id_artikel).delete()
        messages.success(request, 'Berhasil menghapus artikel')
        
    except:
        messages.error(request, 'Gagal menghapus artikel')
        
    return redirect('admin_artikel_list')

######################### Manajemen user oleh operator #########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user": daftar_user
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = "dashboard/admin/user_edit.html"
    users = get_object_or_404(User, pk=user_id)
    all_groups = Group.objects.all()
    group_user = []
    for group in users.groups.all():
        group_user.append(group.name)

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff = request.POST.get("is_staff")
        groups_checked = request.POST.getlist('groups')
        
        if is_staff == None:
            is_staff = False
        else:
            is_staff = True
            
        users.first_name = first_name
        users.last_name = last_name
        users.is_staff = is_staff
        users.groups.set(Group.objects.filter(id__in=groups_checked))
        users.save()
        
        messages.success(request, f"Berhasil update user {users.username}")
        return redirect(admin_management_user_list)
    
    else:
        forms = UserEditForm(instance=users)
            
    context = {
        "users": users,
        "all_groups": all_groups,
        "group_user": group_user
    }
    return render(request, template_name, context)
