from email import message
from email.mime import audio
from math import prod
from pyexpat.errors import messages
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *
from datetime import date
from django.contrib import messages

# Create your views here.
def Home(request):
    cat = ""
    pro = ""
    cat = ""
    num = 0
    num1 = 0
    cat = Category.objects.all()
    pro = Product.objects.all()
    num = []
    num1 = 0
    try:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        cart = Cart.objects.filter(profile=profile)
        for i in cart:
            num1 += 1

    except:
        pass
    a = 1
    li = []

    for j in pro:
        b = 1
        for i in cat:
            if i.name == j.category.name:
                if not j.category.name in li:
                    li.append(j.category.name)
                    if b == 1:
                        num.append(a)
                        b = 2
        a += 1


    d = {'pro': pro, 'cat': cat,'num':num,'num1':num1}
    return render(request, 'home.html',d)
	

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')	
	
	
def Signup(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        f = request.POST['fname']
        l = request.POST['lname']
        p = request.POST['pwd']
        d = request.POST['date']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        i = request.FILES['img']
        con = request.POST['contact']
        user = User.objects.create_user(username=u, email=e, password=p, first_name=f,last_name=l)
        Profile.objects.create(user=user, dob=d, city=c, address=ad, contact=con,image=i)
        error = True
    d = {'error':error}
    return render(request, 'signup.html',d)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if not user.is_staff and user:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error = "not"
    d = {'error': error}
    return render(request,'login.html',d)

def Admin_Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "yes"
            else:
                error = "not"
        except:
            error="not"
    d = {'error': error}
    return render(request,'administration/loginadmin.html',d)


def Logout(request):
    logout(request)
    return redirect('home')


def View_user(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    users = [i.id for i in User.objects.filter(is_staff=0)]
    pro = Profile.objects.filter(user__in = users)
    d = {'user':pro}
    return render(request,'administration/view_user.html',d)


def Add_Product(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    cat = Category.objects.all()
    error=False
    if request.method=="POST":
        c = request.POST['cat']
        p = request.POST['pname']
        pr = request.POST['price']
        i = request.FILES['img']
        d = request.POST['desc']
        l = request.POST['language']
        f = request.POST['format']
        pub = request.POST['publisher']
        ed = request.POST['edition']
        cd = request.POST['condition']
        pa = request.POST['page']
        au = request.POST['author']
        ct = Category.objects.get(name=c)
        Product.objects.create(user=request.user, condition=cd, category=ct, name=p, price=pr, image=i, desc=d, language=l, author=au, pages=pa, edition=ed, publisher=pub, format=f,)
        error=True
    d = {'cat': cat,'error':error}
    if request.user.is_staff:
        return render(request, 'administration/admin_add_product.html', d)
    else:
        return render(request, 'add_product.html', d)

def edit_product(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    cat = Category.objects.all()
    data = Product.objects.get(id=pid)
    error=False
    if request.method=="POST":
        c = request.POST['cat']
        p = request.POST['pname']
        pr = request.POST['price']
        try:
            i = request.FILES['img']
            data.image = i
            data.save()
        except:
            pass
        d = request.POST['desc']
        l = request.POST['language']
        f = request.POST['format']
        pub = request.POST['publisher']
        ed = request.POST['edition']
        pa = request.POST['page']
        au = request.POST['author']
        cd = request.POST['condition']
        ct = Category.objects.get(name=c)
        Product.objects.filter(id=pid).update(user=request.user, condition=cd, category=ct, name=p, price=pr, desc=d, language=l, author=au, pages=pa, edition=ed, publisher=pub, format=f,)
        error=True
    d = {'cat': cat,'error':error, 'data':data}
    return render(request, 'edit_product.html', d)

def my_product(request):
    pro = Product.objects.filter(user=request.user)
    d = {'pro1': pro}
    return render(request, 'my_product.html', d)

def All_product(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    cart = Cart.objects.filter(profile=profile)
    num1=0
    for i in cart:
        num1 += 1
    cat = Category.objects.all()
    pro = Product.objects.all()
    d ={'pro':pro,'cat':cat,'num1':num1}
    return render(request,'all_product.html',d)


def Admin_View_Booking(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    book = Booking.objects.all()
    d = {'book': book}
    return render(request, 'administration/admin_viewBokking.html', d)


def View_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Send_Feedback.objects.all()
    d = {'feed': feed}
    return render(request, 'administration/view_feedback.html', d)


def View_prodcut(request, pid):
    cat = ""
    cat1 = ""
    pro1 = ""
    num1 = 0
    user=""
    profile=""
    cart=""
    pro=""
    num=""
    if not request.user.is_staff and request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        cart = Cart.objects.filter(profile=profile)
        for i in cart:
            num1 += 1
    if request.user.is_authenticated:
        if pid == 0:
            cat = "All Product"
            pro1 = Product.objects.filter(status="Available").exclude(user=request.user)
        else:
            cat1 = Category.objects.get(id=pid)
            pro1 = Product.objects.filter(category=cat1,status="Available").all().exclude(user=request.user)
        cat = Category.objects.all()
        pro = Product.objects.filter(status="Available").exclude(user=request.user)
        num = []
        b = 1
        for j in cat:
            a = 1
            for i in pro:
                if j.name == i.category.name:
                    if a == 1:
                        num.append(i.id)
                        a = 2
    else:
        pro1 = Product.objects.filter()
    category = Category.objects.all()
    getcategory = request.GET.get('category',0)
    if getcategory:
        getcategory = getcategory.split(',')
        pro1 = pro1.filter(category__name__in=getcategory)
    d = {'pro': pro, 'cat': cat,'cat1': cat1,'num':num,'pro1':pro1,'num1':num1, 'category':category}
    return render(request, 'view_product.html', d)


def Add_Categary(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    error=False
    if request.method=="POST":
        n = request.POST['cat']
        Category.objects.create(name=n)
        error=True
    d = {'error':error}
    return render(request, 'administration/add_category.html', d)


def View_Categary(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    pro = Category.objects.all()
    d = {'pro': pro}
    return render(request,'administration/view_category.html', d)



def View_Booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    cart = Cart.objects.filter(profile=profile)
    book = Booking.objects.filter(profile=profile)
    num1=0
    for i in cart:
        num1 += 1
    d = {'book': book,'num1':num1}
    return render(request, 'view_booking.html', d)


def Feedback(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    user1 = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user1)
    cart = Cart.objects.filter(profile=profile)
    num1 =0
    for i in cart:
        num1 += 1
    date1 = date.today()
    user = User.objects.get(id=pid)
    pro = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        d = request.POST['date']
        u = request.POST['uname']
        e = request.POST['email']
        con = request.POST['contact']
        m = request.POST['desc']
        user = User.objects.filter(username=u, email=e).first()
        pro = Profile.objects.filter(user=user, contact=con).first()
        Send_Feedback.objects.create(profile=pro, date=d, message1=m)
        error = True
    d = {'pro': pro, 'date1': date1,'num1':num1,'error':error}
    return render(request, 'feedback.html', d)

def Change_Password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    num1=0
    user = User.objects.get(id=request.user.id)
    
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error,'num1':num1}
    if request.user.is_staff:
        return render(request, 'administration/change_password.html', d)
    else:
        return render(request,'change_password.html',d)
    

def Add_Cart(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=user)
        product = Product.objects.get(id=pid)
        total = int(1) * int(product.price)
        Cart.objects.create(profile=profile, product=product, total=total, quantity=1)
        return redirect('cart')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    getpid = request.GET.get('pid', 0)
    getmid = request.GET.get('mid', 0)
    # getcart = request.GET.get('cart', 0)
    if getpid:
        mydata = Cart.objects.get(id=getpid)
        if int(mydata.quantity) < 5:
            mydata.quantity = int(mydata.quantity) + 1
            mydata.total = (int(mydata.quantity))*int(mydata.product.price)
            mydata.save()
    if getmid:
        mydata = Cart.objects.get(id=getmid)
        if int(mydata.quantity) > 1:
            mydata.quantity = int(mydata.quantity) - 1
            mydata.total = (int(mydata.quantity))*int(mydata.product.price)
            mydata.save()
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    cart =  Cart.objects.filter(profile=profile).all()
    total=0
    num1=0
    book_id=request.user.username
    message1="Here ! No Any Product"
    for i in cart:
        total+=int(i.total)
        num1+=1
        book_id = book_id+"."+str(i.product.id)
    d = {'profile':profile,'cart':cart,'total':total,'num1':num1,'book':book_id,'message':message1}
    return render(request,'cart.html',d)


def remove_cart(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    cart = Cart.objects.get(id=pid)
    cart.delete()
    return redirect('cart')

def Booking_order(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data1 = User.objects.get(id=request.user.id)
    data = Profile.objects.filter(user=data1).first()
    cart = Cart.objects.filter(profile=data).all()
    total = 0
    num1 = None
    for i in cart:
        total+=i.total
        if num1:
            num1 = num1+","+i.quantity
        else:
            num1 = i.quantity
    user1 = data1.username
    li = pid.split('.')
    li2 = []
    for j in li:
        if user1 != j:
            li2.append(int(j))

    date1 = date.today()
    if request.method == "POST":
        d = request.POST['date1']
        c = request.POST['name']
        c1 = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        b = request.POST['book_id']
        t = request.POST['total']
        user = User.objects.get(username=c)
        profile = Profile.objects.get(user=user)
        status = Status.objects.get(name="pending")
        book1 = Booking.objects.create(profile=profile, book_date=d,booking_id=b,total=t,quantity=num1,status=status)
        cart2 = Cart.objects.filter(profile=profile).all()
        cart2.delete()
        return redirect('payment',book1.total)
    d = {'data': data, 'data1': data1, 'book_id': pid, 'date1': date1,'total':total,'num1':num1}
    return render(request, 'booking.html', d)


def payment(request,total):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    user = User.objects.get(id=request.user.id)
    profile= Profile.objects.get(user=user)
    cart = Cart.objects.filter(profile = profile).all()
    if request.method=="POST":
        error=True
    d ={'total':total,'error':error}
    return render(request,'payment2.html',d)


def delete_admin_booking(request, pid,bid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    book = Booking.objects.get(booking_id=pid,id=bid)
    book.delete()
    return redirect('admin_viewBooking')

def delete_booking(request, pid,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.get(booking_id=pid,id=bid)
    book.delete()
    return redirect('view_booking')

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_user')

def delete_feedback(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Send_Feedback.objects.get(id=pid)
    feed.delete()
    return redirect('view_feedback')


def booking_detail(request,pid,bid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=user)
    cart =  Cart.objects.filter(profile=profile).all()
    product = Product.objects.all()
    book = Booking.objects.get(booking_id=pid, id=bid)
    total=0
    num1=0
    user1 = user.username
    li = book.booking_id.split('.')
    li2=[]
    for j in li:
        if user1!= j :
            li2.append(int(j))
    for i in cart:
        total+=i.product.price
        num1+=1
    d = {'profile':profile,'cart':cart,'total':total,'num1':num1,'book':li2,'product':product,'total':book, 'bookingid':book.id}
    return render(request,'booking_detail.html',d)


def admin_booking_detail(request,pid,bid,uid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=uid)
    profile = Profile.objects.get(user=user)
    cart =  Cart.objects.filter(profile=profile).all()
    product = Product.objects.all()
    book = Booking.objects.get(booking_id=pid, id=bid)
    total=0
    num1=0
    user1 = user.username
    li = book.booking_id.split('.')
    li2=[]
    for j in li:
        if user1!= j :
            li2.append(int(j))
    for i in cart:
        total+=i.product.price
        num1+=1
    d = {'profile':profile,'cart':cart,'total':total,'num1':num1,'book':li2,'product':product,'total':book, 'booking_id':pid}
    return render(request,'administration/admin_view_booking_detail.html',d)

def Edit_status(request,pid,bid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    book = Booking.objects.get(booking_id=pid,id=bid)
    stat = Status.objects.all()
    if request.method == "POST":
        n = request.POST['book']
        s = request.POST['status']
        book.booking_id = n
        sta = Status.objects.filter(name=s).first()
        book.status = sta
        book.save()
        return redirect('admin_viewBooking')
    d = {'book': book, 'stat': stat}
    return render(request, 'administration/status.html', d)


def Admin_View_product(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    pro = Product.objects.all()
    d = {'pro':pro}
    return render(request,'administration/admin_view_product.html',d)

def delete_product(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    pro = Product.objects.get(id=pid)
    pro.delete()
    return redirect('admin_view_product')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    cart=""
    num1 = 0
    total = 0
    try:
        cart = Cart.objects.get(profile=pro)
        for i in cart:
            total += i.product.price
            num1 += 1
    except:
        pass

    user = User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    d={'pro':pro,'user':user,'num1':num1,'total':total}
    return render(request,'profile.html',d)


def Edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    user=User.objects.get(id=request.user.id)
    pro = Profile.objects.get(user=user)
    cart = ""
    num1 = 0
    total = 0
    try:
        cart = Cart.objects.get(profile=pro)
        for i in cart:
            total += i.product.price
            num1 += 1
    except:
        pass
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        d = request.POST['date']

        try:
            i = request.FILES['img']
            pro.image = i
            pro.save()

        except:
            pass


        if d:
            try:
                pro.dob = d
                pro.save()
            except:
                pass
        else:
            pass

        pro.user.username=u
        pro.user.first_name=f
        pro.user.last_name=l
        pro.user.email=e
        pro.contact=con
        pro.city=c
        pro.address=ad
        pro.save()
        error = True
    d = {'error':error,'pro':pro,'num1':num1,'total':total}
    return render(request, 'edit_profile.html',d)

def Admin_Home(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    book = Booking.objects.all()
    customer = Profile.objects.all()
    pro = Product.objects.all()
    feedback = Send_Feedback.objects.all()
    total_book = 0
    total_customer = 0
    total_pro = 0
    for i in book:
        total_book+=1
    for i in customer:
        total_customer+=1
    for i in pro:
        total_pro+=1
    d = {'total_pro':total_pro,'total_customer':total_customer,'total_book':total_book, 'total_feedback':feedback.count}
    return render(request,'administration/admin_home.html',d)

def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    cat = Category.objects.get(id=pid)
    cat.delete()
    return redirect('view_categary')

def product_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Product.objects.get(id=pid)
    latest = Product.objects.filter(category=data.category).exclude(user=request.user).order_by('-id')[:4]
    return render(request, 'product_detail.html', {'data': data, 'latest': latest})

def sold_product(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        userid = request.POST['sold_to']
        user = User.objects.get(id=userid)
        status = request.POST['status']
        product.status = status
        product.sold_to = user
        product.save()
    pro = Profile.objects.filter().exclude(user__id = product.user.id)
    return render(request, 'status.html', {'pro':pro})

def sold_product_admin(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    product = Product.objects.get(id=pid)
    if product.status == "Sold":
        product.status = "Available"
    else:
        product.status = "Sold"
    product.save()
    return redirect('admin_view_product')