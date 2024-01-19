from datetime import datetime
from unicodedata import category
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Product, ProductChat , ProductImages , Category
from accounts.models import *
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout


# from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ProductChat, ChatMessages
# Create your views here.

@login_required(login_url='/products/admin_login/')
def admin_index_olx(request):
    return render(request, "admin_dashboard_olx.html", locals())

@login_required(login_url='/products/admin_login/')
def user_detail_olx(request):
    data = UserProfile.objects.all()
    d = {'data': data}
    return render(request, "user_detail_olx.html", d)

@login_required(login_url='/products/admin_login/')
def delete_user_olx(request, pid):
    reg = UserProfile.objects.get(id=pid)
    user = User.objects.get(id=reg.user.id)
    user.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/products/user_detail_olx/')

@login_required(login_url='/products/admin_login/')
def add_product_olx(request, pid=None):
    product = None
    if pid:
        product = Product.objects.get(id=pid)
    if request.method == "POST":
        productform = ProductForm(request.POST, request.FILES, instance=product)
        if productform.is_valid():
            new_product = productform.save()
            new_product.save()
        messages.success(request, "Submited Successful")
        return redirect('/products/view_product_olx/')
    owner = UserProfile.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    return render(request, 'add_product_olx.html', locals())

@login_required(login_url='/products/admin_login/')
def view_product_olx(request):
    data = Product.objects.all()
    d = {'data': data}
    return render(request, "view_product_olx.html", d)

@login_required(login_url='/products/admin_login/')
def delete_product_olx(request, pid):
    data = Product.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/products/view_product_olx/')

@login_required(login_url='/products/admin_login/')
def add_category_olx(request, pid=None):
    category = None
    if pid:
        category = Category.objects.get(id=pid)
    if request.method == "POST":
        categoryform = CategoryForm(request.POST, request.FILES, instance=category)
        if categoryform.is_valid():
            new_category = categoryform.save()
            new_category.save()
        messages.success(request, "Submited Successful")
        return redirect('/products/view_category_olx/')
    return render(request, 'add_category_olx.html', locals())

@login_required(login_url='/products/admin_login/')
def view_category_olx(request):
    data = Category.objects.all()
    d = {'data': data}
    return render(request, "view_category_olx.html", d)

@login_required(login_url='/products/admin_login/')
def delete_category_olx(request, pid):
    data = Category.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/products/view_category_olx/')

@login_required(login_url='/products/admin_login/')
def add_brand_olx(request, pid=None):
    brand = None
    if pid:
        brand = Brand.objects.get(id=pid)
    if request.method == "POST":
        brandform = BrandForm(request.POST, request.FILES, instance=brand)
        if brandform.is_valid():
            new_brand = brandform.save()
            new_brand.save()
        messages.success(request, "Submited Successful")
        return redirect('/products/view_brand_olx/')
    return render(request, 'add_brand_olx.html', locals())

@login_required(login_url='/products/admin_login/')
def view_brand_olx(request):
    data = Brand.objects.all()
    d = {'data': data}
    return render(request, "view_brand_olx.html", d)

@login_required(login_url='/products/admin_login/')
def delete_brand_olx(request, pid):
    data = Brand.objects.get(id=pid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect('/products/view_brand_olx/')

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('/products/admin_index_olx/')
            else:
                messages.success(request, "Invalid User")
                return redirect('admin_login')
        except:
            messages.success(request, "Invalid User")
            return redirect('admin_login')
    return render(request, "admin-login.html")

@login_required(login_url='/products/admin_login/')
def logout_user(request):
    logout(request)
    messages.success(request, "logout Successful")
    return redirect('/')

@login_required(login_url='/products/admin_login/')
def change_password(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(c)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password')

    return render(request, 'change_password.html')

@login_required
def ad_post(request, pid=None):
    ad_post_pro = None
    all_image = None
    if pid:
        ad_post_pro = Product.objects.get(id=pid)
        all_image = ProductImages.objects.filter(product=ad_post_pro)
    if request.method == "POST":
        form = AdProductForm(request.POST, request.FILES, instance=ad_post_pro)
        if form.is_valid():
            new_ads = form.save()
            new_ads.owner = request.user
            new_ads.save()
            multiple_file = request.FILES.getlist('fileselect[]')
            print(multiple_file)
            for i in multiple_file:
                ProductImages.objects.create(image=i, product=new_ads)
            messages.success(request, "Ads Posted Successfully.")
            return redirect('/')
        else:
            print(form.errors)
    category = Category.objects.all()
    brand = Brand.objects.all()
    condition_type = Product.CONDITION_TYPE
    return render(request, 'Product/post-ads.html', locals())

def productlist(request , category_slug=None):
    category = None
    productlist = Product.objects.filter().exclude(owner=request.user)
    categorylist = Category.objects.annotate(total_products=Count('product'))

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        productlist = productlist.filter(category=category).exclude(owner=request.user)

    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query) 
        ).exclude(owner=request.user)

    paginator = Paginator(productlist, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    template = 'Product/product_list.html'

    context = {'product_list' : productlist , 'category_list' : categorylist ,'category' : category }
    return render(request , template , context)

def my_productlist(request , category_slug=None):
    category = None
    product_list = Product.objects.filter(owner=request.user)
    category_list = Category.objects.annotate(total_products=Count('product'))
    cat_list = Category.objects.all()

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        product_list = product_list.filter(category=category)

    search_query = request.GET.get('q')
    if search_query :
        product_list = product_list.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query)
        )

    paginator = Paginator(product_list, 5) # Show 25 contacts per page
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    template = 'Product/my-product_list.html'

    return render(request , template , locals())

@login_required
def load_new_messages(request, chat_id):
    product_chat = ProductChat.objects.get(id=chat_id)
    chat_messages = ChatMessages.objects.filter(chat=product_chat)
    return render(request, 'Product/created-chat.html', locals())

@login_required
def check_for_new_objects(request, chat_pid):
    my_chat = ProductChat.objects.get(id=chat_pid)
    chat_messages = ChatMessages.objects.filter(chat=my_chat).count()
    if int(request.session['chat-count']) != chat_messages:
        request.session['chat-count'] = chat_messages
        chat_messages = ChatMessages.objects.filter(chat=my_chat, created__gt=datetime.fromisoformat(request.session['created']))
        request.session['created'] = datetime.now().isoformat()
        return render(request, 'Product/all_created_chat.html', locals())
    else:
        request.session['created'] = datetime.now().isoformat()
        return JsonResponse({'new_objects': 0})

@login_required
def chat(request, slug, chat_id=None):
    product = get_object_or_404(Product, id=slug)
    created_messages = None
    product_chat = None
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            if product.owner.id != request.user.id:
                product_chat, created = ProductChat.objects.get_or_create(product=product, product_user=product.owner, other_user=request.user)
                print("created chat", created)
            else:
                product_chat = ProductChat.objects.get(id=chat_id)
            if product.owner.id == request.user.id:
                created_messages = ChatMessages.objects.create(chat=product_chat, other_user=product.owner, message=message)
            else:
                created_messages = ChatMessages.objects.create(chat=product_chat, message_user=request.user, message=message)
            return render(request, 'Product/created-chat.html', locals())
    if request.GET.get('action') == 'start-chat':
        if product.owner.id != request.user.id:
            product_chat, created = ProductChat.objects.get_or_create(product=product, product_user=product.owner, other_user=request.user)
            return redirect('/products/my-chat/')
        else:
            return redirect('/products/my-chat/')

@login_required
def my_chat(request):
    product_ids = Product.objects.filter(owner=request.user).values_list('id', flat=True)
    own = User.objects.get(pk=request.user.pk)
    my_chat = ProductChat.objects.filter(product__in=product_ids)
    buyer_chat = ProductChat.objects.filter(other_user=own)
    # my_chat = ProductChat.objects.filter(Q(other_user=request.user) | Q(product_user=request.user))
    return render(request, 'Product/your_chat.html', locals())

@login_required
def main_chat_user(request, pid):
    my_chat = ProductChat.objects.get(id=pid)
    chat_messages = ChatMessages.objects.filter(chat=my_chat)
    request.session['chat-count'] = chat_messages.count()
    request.session['created'] = datetime.now().isoformat()
    return render(request, 'Product/main-chat-user.html', locals())

def productdetail(request , product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_detail' : productdetail , 'product_images' : productimages}
    return render(request , template , context)