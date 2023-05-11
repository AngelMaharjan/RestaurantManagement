from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm

from .models import Menu, SubCategory,Customer, OrderItem, Order
# Create your views here

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
            messages.success(request, 'Signup Successfull')
            # Redirect to the login page
            return redirect('loginPage')
        else:
            messages.error(request, 'Signup Failed..!!')

    
    # If the request method is not POST, display an empty form
    else:
        form = CustomUserCreationForm()
    
    # Render the joinnow.html template with the form
    return render(request, 'ForkAndKnife/joinnow.html', {'form': form}) 


@login_required
def logoutview(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully..!!')
    return redirect('loginPage')


@login_required
def home(request):
    menus = Menu.objects.all()
    return render(request, 'ForkAndKnife/home.html',{'menuss': menus})


def menu(request):
    return render(request, "ForkAndKnife/menu.html",)

def about(request):
    return render(request, 'ForkAndKnife/about.html')


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

@login_required
def orderItem(request, id):
    order = get_object_or_404(Menu, id = id)

    if request.method == "POST":
        quantity = request.POST.get('quantity')
        user = request.user
        #order, created = Order.objects.get_or_create(user=request.user)
        order_item = OrderItem( quantity=quantity, item_id=order.id, user=user)
        order_item.save()
       # print(order_item.get_total)
       # order.items.add(order_item)
        #order.total += order_item.price
        #order.save()


        #order_item = OrderItem(prod= 'prod',quantity='quantity', id = 'idd',)
      #  order.save()
        #return HttpResponse(user)
        messages.success(request, 'Item added into cart..!!')

        return redirect('homePage')


    return render(request, "ForkAndKnife/orderMenu.html", { 'order': order})  





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


@login_required
def place_order(request):
    if request.method== 'POST':
        address = request.POST.get('address')
        #number = request.POST.get('number')
        cart_items = OrderItem.objects.filter(user=request.user)
        total_quantity = 0
        for i in cart_items:
            total_quantity += i.quantity
        total = total_quantity
        total_cost = sum(item.get_total for item in cart_items) + 100
        order = Order.objects.create(user=request.user,delivery_address=address, quantity=total,
                                     total_price = total_cost )
#        order = Order(delivery_address=address, quantity=total,
 #                      total_price = total_cost )
       # order.items.set(cart_items)
        order.save()
        cart_items.delete()
        messages.success(request, 'Order placed successfully.')
        return redirect('homePage')
    else:
        messages.error(request, 'Unable to place order..!!')


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    context = {
        'orders': orders,
       # 'item' : OrderItem
    }
    return render(request, 'ForkAndKnife/orderhistory.html', context) 

# 

@login_required
def cart(request):
    items = OrderItem.objects.filter(user=request.user)
    
   # total_price = sum(item.get_total() for item in items)
    #name = items.item_id.name
    #context = {'items': items}
   # return HttpResponse(items)
    total_price = 0
    for i in items:
        total_price += i.get_total
    total = total_price

    delivery = total + 100

    return render(request, 'ForkAndKnife/newCart.html', {'context': items, 'total' : total , 'delivery' : delivery})
    
## code for updating items in Cart
@login_required
def update_cart(request, id):
    # get the item id and new quantity from the POST data
    id = str(id)
    quantity = int(request.POST['quantity'])
   # update the item quantity in the cart
    cart_item = OrderItem.objects.filter(id=id).first()
    print(f"quantiy is : {cart_item}")
    try:
        cart_item = OrderItem.objects.get(id=id)
    except OrderItem.DoesNotExist:
        print(f"No OrderItem found with item_id={id}")

    if cart_item is not None:
        #cart_item.quantity = quantity
        #cart_item.save()
        cart_item.quantity = quantity
        print(f"Quantity updated to {quantity}")
        cart_item.save()
        print("Item saved to database")


    return redirect('cartPage')


@login_required
def delete_cart(request, id):
    # Get the item id
    item_id = int(id)
    
    # Get the order item to be deleted
    order_item = OrderItem.objects.get(id=item_id)
    
    # Delete the order item from the cart
    order_item.delete()
    
    # Redirect to the cart page
    return redirect('cartPage')


'''


def generate_bill(request, order_id):
    # retrieve the order from the database
    order = Order.objects.get(id=order_id)

    # render the bill template with the relevant data
    bill_template = 'ForkAndKnife/bill.html'
    context = {'order': order}
    html = render(request, bill_template, context)

    # return the rendered template as an HTTP response
    response = HttpResponse(html, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename=Bill-{order_id}.html'
    return response
'''

from django.template.loader import get_template
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas

@login_required
def generate_bill(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.items.all()
   # item = OrderItem.objects.filter(user=request.user)

   # quantity = order.quantity

    # get the template
    template = get_template('ForkAndKnife/bill.html')
    context = {'order': order, 'items': items,}

    # create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    # http://www.reportlab.com/docs/reportlab-userguide.pdf
    p.drawString(100, 750, "Order Invoice")
    p.drawString(100, 700, "Order ID: {}".format(order.id))
    p.drawString(100, 650, "User: {}".format(order.user.username))
    p.drawString(100, 600, "Delivery Address: {}".format(order.delivery_address))
    p.drawString(100, 550, "Payment Method: {}".format(order.payment_method))

    # loop through the items and draw them on the PDF
    y = 500
    for item in items:
        p.drawString(100, y, item.name)
       # p.drawString(200, y, str(item.quantity))
        p.drawString(300, y, str(item.price))
      #  p.drawString(400, y, str(item.get_total()))
        y -= 50

    p.drawString(300, y-30, "Total Quantity: {}".format(order.quantity))

    p.drawString(300, y-50, "Total: {}".format(order.total_price))

    # close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    response.write(pdf)
    return response




from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash, authenticate, login

User = get_user_model()

@login_required
def deleteAccount(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user.delete()
        return redirect('homePage')
    else:
        return render(request, 'ForkAndKnife/deleteaccount.html')



@login_required
def reset_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = authenticate(username=request.user.username, password=old_password)
        if user is not None:
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('homePage')
            else:
                messages.error(request, 'The new passwords did not match.')
        else:
            messages.error(request, 'Your old password was incorrect.')
    return render(request, 'ForkAndKnife/reset.html')
