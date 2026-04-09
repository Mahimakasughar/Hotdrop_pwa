from django.shortcuts import render, redirect
from .models import Vendor, Order
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password



# ===============================
# HOME & STATIC PAGES
# ===============================
def home(request):
    return render(request, 'hotdrop/home.html')

def about(request):
    return render(request, 'hotdrop/about.html')

def categories(request):
    return render(request, 'hotdrop/categories.html')

def register(request):
    return render(request, 'hotdrop/register.html')

def login(request):
    return render(request, 'hotdrop/login.html')

def contact(request):
    return render(request, 'hotdrop/contact.html')

def success(request):
  latest_order = Order.objects.last()
  return render(request, 'hotdrop/success.html', {"order": latest_order})


# ===============================
# PRODUCTS
# ===============================
def products(request):
    return render(request, 'hotdrop/products.html')


# ===============================
# PRODUCT DETAILS PAGE
# ===============================
def product_detail(request, id):
    # Static product data
    products = {
        1: {"id": 1, "name": "Oreo Shake", "type": "Beverages", "price": 150, "image": "hotdrop/img/oreo-shake.jpg","vendor_id":1},
        2: {"id": 2, "name": "Aalu Methi", "type": "North Indian", "price": 250, "image": "hotdrop/img/aalu-methi.jpg","vendor_id":2},
        3: {"id": 3, "name": "Chicken Rice", "type": "Mughlai", "price": 300, "image": "hotdrop/img/chicken-rice.jpg","vendor_id":3},
        4: {"id": 4, "name": "Dal Makhani", "type": "Mughlai", "price": 500, "image": "hotdrop/img/dal-makhani.jpg","vendor_id":4},
        5: {"id": 5, "name": "Dosa", "type": "South Indian", "price": 200, "image": "hotdrop/img/dosa.jpg","vendor_id":5},
        6: {"id": 6, "name": "Macaroni", "type": "Snacks", "price": 500, "image": "hotdrop/img/macaroni.jpg","vendor_id":6},
        7: {"id": 7, "name": "Cheese Burst Pizza", "type": "Italian", "price": 400, "image": "hotdrop/img/cheese burst pizza.jpg","vendor_id":7},
        8: {"id": 8, "name": "Cold Drink", "type": "Beverages", "price": 100, "image": "hotdrop/img/cold drink.jpg","vendor_id":8},
        9: {"id": 9, "name": "Spring Roll", "type": "Chinese", "price": 150, "image": "hotdrop/img/spring roll.jpg","vendor_id":9},
        10: {"id": 10, "name": "Dim Sim", "type": "Chinese", "price": 600, "image": "hotdrop/img/dim sim.jpg","vendor_id":10},
        11: {"id": 11, "name": "Palak Paneer", "type": "North Indian", "price": 400, "image": "hotdrop/img/palak panner.jpg","vendor_id":12},
        12: {"id": 12, "name": "Rajma Chaval", "type": "North Indian", "price": 400, "image": "hotdrop/img/rajma chaval.jpg","vendor_id":13},
        13: {"id": 13, "name": "Lemon Rice", "type": "South Indian", "price": 300, "image": "hotdrop/img/lemon rice.jpg","vendor_id":14},
        14: {"id": 14, "name": "Mughlai Kabab", "type": "Mughlai", "price": 450, "image": "hotdrop/img/Mughlai kabab.jpg","vendor_id":15},
        15: {"id": 15, "name": "French Toast", "type": "Breakfast", "price": 700, "image": "hotdrop/img/french toast.jpg","vendor_id":16},
        16: {"id": 16, "name": "Pancake", "type": "Breakfast", "price": 500, "image": "hotdrop/img/pancake.jpg","vendor_id":17},
        17: {"id": 17, "name": "Fruit Salad", "type": "Fruits", "price": 400, "image": "hotdrop/img/fruit salad.jpg","vendor_id":18},
        18: {"id": 18, "name": "Fruit Juice", "type": "Beverages", "price": 400, "image": "hotdrop/img/fruit juice.jpg","vendor_id":19},
        19: {"id": 19, "name": "Granola", "type": "Breakfast", "price": 400, "image": "hotdrop/img/granola.jpg","vendor_id":20},
        20: {"id": 20, "name": "Karanji", "type": "Snacks", "price": 400, "image": "hotdrop/img/karanji.jpg","vendor_id":21},
    }

    product = products.get(id)
    if not product:
        return render(request, 'hotdrop/404.html', status=404)
    return render(request, 'hotdrop/product_detail.html', {'product': product})



# ADD TO CART & CART PAGE

def add_to_cart(request, id):
    # Product dictionary for lookup
    products = {
         1: {"id": 1, "name": "Oreo Shake", "type": "Beverages", "price": 150, "image": "hotdrop/img/oreo-shake.jpg","vendor_id":1},
        2: {"id": 2, "name": "Aalu Methi", "type": "North Indian", "price": 250, "image": "hotdrop/img/aalu-methi.jpg","vendor_id":2},
        3: {"id": 3, "name": "Chicken Rice", "type": "Mughlai", "price": 300, "image": "hotdrop/img/chicken-rice.jpg","vendor_id":3},
        4: {"id": 4, "name": "Dal Makhani", "type": "Mughlai", "price": 500, "image": "hotdrop/img/dal-makhani.jpg","vendor_id":4},
        5: {"id": 5, "name": "Dosa", "type": "South Indian", "price": 200, "image": "hotdrop/img/dosa.jpg","vendor_id":5},
        6: {"id": 6, "name": "Macaroni", "type": "Snacks", "price": 500, "image": "hotdrop/img/macaroni.jpg","vendor_id":6},
        7: {"id": 7, "name": "Cheese Burst Pizza", "type": "Italian", "price": 400, "image": "hotdrop/img/cheese burst pizza.jpg","vendor_id":7},
        8: {"id": 8, "name": "Cold Drink", "type": "Beverages", "price": 100, "image": "hotdrop/img/cold drink.jpg","vendor_id":8},
        9: {"id": 9, "name": "Spring Roll", "type": "Chinese", "price": 150, "image": "hotdrop/img/spring roll.jpg","vendor_id":9},
        10: {"id": 10, "name": "Dim Sim", "type": "Chinese", "price": 600, "image": "hotdrop/img/dim sim.jpg","vendor_id":10},
        11: {"id": 11, "name": "Palak Paneer", "type": "North Indian", "price": 400, "image": "hotdrop/img/palak panner.jpg","vendor_id":12},
        12: {"id": 12, "name": "Rajma Chaval", "type": "North Indian", "price": 400, "image": "hotdrop/img/rajma chaval.jpg","vendor_id":13},
        13: {"id": 13, "name": "Lemon Rice", "type": "South Indian", "price": 300, "image": "hotdrop/img/lemon rice.jpg","vendor_id":14},
        14: {"id": 14, "name": "Mughlai Kabab", "type": "Mughlai", "price": 450, "image": "hotdrop/img/Mughlai kabab.jpg","vendor_id":15},
        15: {"id": 15, "name": "French Toast", "type": "Breakfast", "price": 700, "image": "hotdrop/img/french toast.jpg","vendor_id":16},
        16: {"id": 16, "name": "Pancake", "type": "Breakfast", "price": 500, "image": "hotdrop/img/pancake.jpg","vendor_id":17},
        17: {"id": 17, "name": "Fruit Salad", "type": "Fruits", "price": 400, "image": "hotdrop/img/fruit salad.jpg","vendor_id":18},
        18: {"id": 18, "name": "Fruit Juice", "type": "Beverages", "price": 400, "image": "hotdrop/img/fruit juice.jpg","vendor_id":19},
        19: {"id": 19, "name": "Granola", "type": "Breakfast", "price": 400, "image": "hotdrop/img/granola.jpg","vendor_id":20},
        20: {"id": 20, "name": "Karanji", "type": "Snacks", "price": 400, "image": "hotdrop/img/karanji.jpg","vendor_id":21},
    }

    product = products.get(id)
    cart = request.session.get('cart', {})

    if product:
        if str(id) in cart:
            cart[str(id)]['quantity'] += 1
        else:
           cart[str(id)] = {
    "name": product["name"],
    "price": product["price"],
    "quantity": 1,
    "image": product["image"],
    "vendor_id": product["vendor_id"]
}
        request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        item["subtotal"] = item["price"] * item["quantity"]
        total += item["subtotal"]

    return render(request, 'hotdrop/cart.html', {"cart": cart, "total": total})

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    cart = request.session.get('cart', {})
    total = sum(item["price"] * item["quantity"] for item in cart.values())

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        address = f"{address1} {address2}".strip()
        city = request.POST.get("city")
        payment_method = request.POST.get("payment_method")

        # ✅ Get vendor of first cart item
        first_item = list(cart.values())[0]
        vendor = Vendor.objects.get(id=first_item["vendor_id"])

        # ✅ Save Order with vendor
        Order.objects.create(
            full_name = full_name,
            email = email,
            phone = phone,
            address = address,
            city = city,
            payment_method = payment_method,
            total_amount = total,
            vendor = vendor
        )

        # ✅ Clear cart
        request.session['cart'] = {}

        # ✅ Redirect to success page
        return redirect('success')

    return render(request, 'hotdrop/checkout.html', {"cart": cart, "total": total})

def admin_dashboard(request):
    total_orders = Order.objects.count()
    delivered_orders = Order.objects.filter(status="Delivered").count()
    pending_orders = Order.objects.filter(status="Pending").count()
    cancelled_orders = Order.objects.filter(status="Cancelled").count()

    context = {
        'total_orders': total_orders,
        'delivered_orders': delivered_orders,
        'pending_orders': pending_orders,
        'cancelled_orders': cancelled_orders,
    }
    return render(request, 'hotdrop/admin_dashboard.html', context)
def manage_users(request):
    return render(request, 'hotdrop/manage_users.html')

def manage_orders(request):
    return render(request, 'hotdrop/manage_orders.html')

def admin_orders(request):
    orders = Order.objects.all().order_by('-date_ordered')
    return render(request, 'hotdrop/admin_orders.html', {'orders': orders})

def logout_view(request):
    logout(request)
    return redirect('login')


def vendor_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            vendor = Vendor.objects.get(email=email)

            if not vendor.is_approved:
                return render(request, "hotdrop/vendor_login.html", {"error": "Your account is awaiting approval"})

            if vendor.password == password:
                request.session['vendor_id'] = vendor.id
                return redirect("vendor_dashboard")
            else:
                return render(request, "hotdrop/vendor_login.html", {"error": "Invalid password"})
        except Vendor.DoesNotExist:
            return render(request, "hotdrop/vendor_login.html", {"error": "Vendor not found"})

    return render(request, "hotdrop/vendor_login.html")

def vendor_logout(request):
    request.session.flush()
    return redirect('vendor_login')

def vendor_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Check email exists
        if Vendor.objects.filter(email=email).exists():
            messages.error(request, "Email already registered! Please login.")
            return render(request, 'hotdrop/vendor_register.html', {     # ✅ change redirect → render
                'name': name,
                'email': email,
                'phone': phone
            })

        Vendor.objects.create(
            name=name, email=email, phone=phone,
            password=password, is_approved=False
        )
        messages.success(request, "Registration Successful. Wait for admin approval.")
        return redirect('vendor_login')

    return render(request, 'hotdrop/vendor_register.html')

def vendor_dashboard(request):
    vendor_id = request.session.get('vendor_id')

    if not vendor_id:
        return redirect("vendor_login")

    vendor = Vendor.objects.get(id=vendor_id)
    orders = Order.objects.filter(vendor=vendor)

    return render(request, "hotdrop/vendor_dashboard.html", {
        "vendor": vendor,
        "orders": orders
    })