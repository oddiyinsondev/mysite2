from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Category, CommentPost, Contact
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class Postlist(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'



def category_post(request, slug):
    object_list = Post.objects.filter(category__slug = slug)
    cat = Category.objects.get(slug=slug)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:    
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/categorys_post.html", {'posts':posts, 'page':page, 'cat':cat})





# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post_list.html', {'posts':posts, 'page':page})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)
    if request.method == "POST":
        comment = request.POST.get("text")
        user = request.user
        if len(comment) != 0:
            CommentPost.objects.create(post = post, author = user, body=comment)
    # form = CommentForm(request.POST)
    kamentiyara = CommentPost.objects.filter(post=post).select_related('author')
    return render(request, 'blog/post_detail.html', {'post':post, 'kamentiyara':kamentiyara})



# def registertion(request):
#     form = Registerfrom()
#     if request.method == 'POST':
#         form = Registerfrom(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "O'tish bajarildi!!!")
#             return redirect('home')
#         messages.success(request, "Ma'lumotlar xato toldirilgan")
#     return render(request, 'blog/register.html', {'register_form': form})


def ContactUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            full_name = request.POST.get("fullName")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            Contact.objects.create(full_name=full_name, email=email, phone=phone, message=message)
            messages.info(request, "Sizning Xabaringiz yuborildi")
        return render(request, 'blog/contact_user.html')
    else:
        messages.info(request,"Siz oldin ro'yhatdan o'tishingiz kerak?")
        return redirect('register')
        # return render(request, 'blog/contact_user.html')   

def shohruhbek(request):
    return render(request, 'blog/shohruhbek.html')



def registertion(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.error(request, 'Bu nom foydalingan')
                    return redirect('register')
                elif User.objects.filter(email = email).exists():
                    messages.error(request, 'email foydalingan ')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    login(request, user)
                    messages.success(request, "ajoyib re'yhatdan o'tdingiz!!!")
                    return redirect('post_list')
            else:
                messages.error(request, 'Parollar bir biriga mos emas akan??')
                return redirect('register')
        else:
            return render(request, 'blog/register.html')







def loginUser(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                print("username yoki parol xato")
                return redirect('register')
        
        else:
            return render(request, 'blog/login.html')




def logoutUser(request):
    logout(request)
    messages.info(request, "siz acountizngizdan chiqib ketdiz")
    return redirect('post_list')



def pag_not(request, exception):
    return render(request, 'blog/not_page.html')
    

def about(request):
    return render(request, 'blog/about.html')


