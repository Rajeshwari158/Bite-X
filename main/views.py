from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Food
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Order

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'User already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    search = request.GET.get('search')
    category = request.GET.get('category')

    foods = Food.objects.all()

    if search:
        foods = foods.filter(name__icontains=search)

    if category:
        foods = foods.filter(category=category)

    return render(request, 'home.html', {'foods': foods})
def splash(request):
    return render(request, 'splash.html')
def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    cart.append(id)
    request.session['cart'] = cart
    return redirect('home')
def cart(request):
    cart = request.session.get('cart', [])
    foods = Food.objects.filter(id__in=cart)

    total = sum(food.price for food in foods)

    return render(request, 'cart.html', {
        'foods': foods,
        'total': total
    })
def remove_from_cart(request, id):
    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)

    request.session['cart'] = cart

    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', [])
    foods = Food.objects.filter(id__in=cart)

    total = sum(food.price for food in foods)

    if request.method == "POST":
        Order.objects.create(user=request.user, total=total)
        request.session['cart'] = []
        return render(request, 'success.html')

    return render(request, 'checkout.html', {'foods': foods, 'total': total})
def orders(request):
    user_orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': user_orders})