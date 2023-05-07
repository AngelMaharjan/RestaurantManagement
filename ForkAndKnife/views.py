from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Customer


from .models import Menu, SubCategory, Order, OrderItem
# Create your views here.

# def index(request:
    # menus = Menu.objects.all)
    # return render(request, "ForkAndKnife/index.html", {'menuss': menus)

# Define a view function to display the home page
def index(request):
    # Get all the Menu objects from the database
    menus = Menu.objects.all()
    
    # Render the index.html template with the menus as context
    return render(request, "ForkAndKnife/index.html", {'menuss': menus})

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('homePage')
        else:
            messages.error(request, 'Login failed. Please try again.')
            #error_message = 'Invalid username or password.'
            #return render(request, "ForkAndKnife/signin.html", {'error_message': error_message})
    #else:
     #   return render(request, 'ForkAndKnife/signin.html')
    return render(request, "ForkAndKnife/signin.html")

# def signup(request):
    # if request.method == 'POST':
        # form = CustomUserCreationForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('loginPage')
    # else:
        # form = CustomUserCreationForm()
    # return render(request, 'ForkAndKnife/joinnow.html', {'form': form})
# 
    #return render(request, "ForkAndKnife/joinnow.html")

# Define a view function to handle user registration
def signup(request):
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a new instance of the CustomUserCreationForm using the form data
        form = CustomUserCreationForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the user to the database
            form.save()
            
            # Redirect to the login page
            return redirect('loginPage')
    
    # If the request method is not POST, display an empty form
    else:
        form = CustomUserCreationForm()
    
    # Render the joinnow.html template with the form
    return render(request, 'ForkAndKnife/joinnow.html', {'form': form}) 

#from .models import CustomUser

#def signup(request):

    
 #   return render(request, 'ForkAndKnife/joinnow.html',)


def logoutview(request):
    logout(request)
    return redirect('indexPage')

'''
#@login_required
def home(request):
    if request.user.is_authenticated:
        menus = Menu.objects.all()
        return render(request, 'ForkAndKnife/home.html',{'menuss': menus})
    else:
        return redirect('loginPage') '''

def home(request):
    menus = Menu.objects.all()
    return render(request, 'ForkAndKnife/home.html',{'menuss': menus})


def menu(request):
    return render(request, "ForkAndKnife/menu.html",)

def about(request):
    return render(request, 'ForkAndKnife/about.html')

# def profile(request,username):
    # user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(User, user=user)
    # context = {'user': user, 'profile': profile}
    # return render(request, "ForkAndKnife/profile.html",context)
@login_required
def profile(request):
    user = request.user
    customer = Customer.objects.get(id=user.id)
    context = {
        'user': user,
        'customer': customer,
        'phone_number': customer.phone_number,
        'address': customer.address,        

    }

    return render(request, 'ForkAndKnife/profile.html',context)


def menuFoodList(request):
    obj = SubCategory.objects.all()
    menus = Menu.objects.all()

    return render(request, "ForkAndKnife/menuFood.html", {'objj': obj , 'menuss': menus})

def orderItem(request, id):
    #menus = Menu.objects.all()
    order = get_object_or_404(Menu, id = id)
    #order = Menu.objects.get(id=id)
    return render(request, "ForkAndKnife/orderMenu.html", { 'order': order})

# def orderItem(request):
    # return render(request, "ForkAndKnife/orderMenu.html")
# 
def menuList(request):
    return HttpResponse("hello")

def menuDrinkList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuDrink.html", {'objj': obj , 'menuss': menus})


def menuBakeryList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuBakery.html", {'objj': obj , 'menuss': menus})


def menuDesertList(request):
     obj = SubCategory.objects.all()
     menus = Menu.objects.all()
    
     return render(request, "ForkAndKnife/menuDeserts.html", {'objj': obj , 'menuss': menus})

#@ogin_required
def cart(request):
    cart_items = OrderItem.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
        'total_cost': sum(item.total_cost for item in cart_items)
    }
    #return render(request, 'cart.html', context)
    return HttpResponse("This is cart....!!!")


#@login_required
def add_to_cart(request, product_id):
    food = Menu.objects.get(id=product_id)
    cart_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        foods=food,
        defaults={'quantity': 1, 'total_cost': food.price}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.total_cost += food.price
        cart_item.save()
    messages.success(request, 'Item added to cart.')
    return redirect('cart')



#@login_required
def place_order(request):
    cart_items = OrderItem.objects.filter(user=request.user)
    total_cost = sum(item.total_cost for item in cart_items)
    order = Order.objects.create(user=request.user, total_cost=total_cost)
    order.items.set(cart_items)
    order.save()
    cart_items.delete()
    messages.success(request, 'Order placed successfully.')
    return redirect('order_history')


#@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_created')
    context = {
        'orders': orders
    }
    return render(request, 'order_history.html', context)


@login_required
def deleteAccount(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('loginPage')
    else:
        return redirect('indexPage')




'''def deleteAccount(request, username):

    if request.method == 'DELETE':
        try:
            user = User.objects.get(username = username)
            user.delete()
            context['msg'] = 'Bye Bye'
        except Exception as e: 
            context['msg'] = 'Something went wrong!'

    else:
        context['msg'] = 'Request method should be "DELETE"!'

    return render(request, 'deleteaccount.html', context=context) '''





