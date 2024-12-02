from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomRegistrationForm, ProductForm
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta

from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from PIL import Image
import io
from django.db.models import Q
from .utils import upload_image_to_imgbb  # Assuming the above function is in utils.py

from collections import defaultdict
from django.core.cache import cache

from django.core.cache import cache
from django.db.models import QuerySet

from asgiref.sync import sync_to_async



def ping(request):
    return HttpResponse("Pong")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')






def home(request):
    products = Product.objects.filter(product_category='home').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'home.html', context)

def headgear(request):
    products = Product.objects.filter(product_category='headgear').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'headgear.html', context)


def footwear(request):
    products = Product.objects.filter(product_category='footwear').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'footwear.html', context)




def bags(request):
    products = Product.objects.filter(product_category='bags').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'bags.html', context)




def apparel(request):
    products = Product.objects.filter(product_category='apparel').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'apparel.html', context)





def beauty(request):
    products = Product.objects.filter(product_category='health_beauty').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'beauty.html', context)


def computers(request):
    products = Product.objects.filter(product_category='gadgets_computers').order_by('-created_at')

    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares

    return render(request, 'computers.html', context)


def faqs(request):
    return render(request, 'faqs.html')

def food(request):
    products = Product.objects.filter(product_category='food').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'food.html',context)

def jewelry(request):
    products = Product.objects.filter(product_category='jewelry_accessories').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'jewelry.html', context)


def error(request):
    return render(request, 'error.html')



def vendor(request):
    return render(request, 'vendor.html')


def register(request):
    # If the user is already authenticated
    if request.user.is_authenticated:
        # Retrieve products uploaded by the logged-in user
        user_products = Product.objects.filter(user=request.user)

        # Handle the 'Mark as Sold' action
        if request.method == 'POST' and 'mark_sold' in request.POST:
            product_id = request.POST.get('product_id')
            try:
                product = Product.objects.get(id=product_id, user=request.user)
                product.is_sold = True
                product.save()
                messages.success(request, 'Product marked as sold.')
            except Product.DoesNotExist:
                messages.error(request, 'Product not found or you are not the owner.')

        # Return the user's products to the template
        return render(request, 'register.html', {'user_products': user_products})

    # Handle the registration form submission if the user is not authenticated
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            messages.success(request, "Registration successful! You can now log in.")
            return redirect('Eapp:login')  # Redirect to login after successful registration
        else:
            # Loop through the form errors and add them as Django messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomRegistrationForm()

    # Render the registration form if the user is not authenticated
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)  # Use Django's built-in login function
            return redirect('Eapp:sell')  # Redirect to home page after successful login
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'login.html')


# Async function to handle the database fetching
@sync_to_async
def get_products_from_db():
    # Fetch products from database and process them
    products = Product.objects.filter(product_category__in=[
        'electronics', 'home', 'health_beauty', 'jewelry_accessories',
        'apparel', 'bags', 'footwear', 'headgear', 'gadgets_computers', 'food'
    ]).order_by('product_category', '-created_at')

    # Group products by category and limit to 4 per category
    grouped_products = defaultdict(list)
    for product in products:
        if len(grouped_products[product.product_category]) < 4:
            grouped_products[product.product_category].append(product)

    return grouped_products

async def index(request):
    # Try to fetch from cache
    cache_key = 'homepage_products'
    data = cache.get(cache_key)

    if not data:
        # Fetch products in the background (async)
        data = await get_products_from_db()

        # Save the grouped data to cache
        cache.set(cache_key, data, timeout=60 * 5)  # Cache for 5 minutes

    # Render the template with the data (data will either be cached or freshly fetched)
    return render(request, 'index.html', {
        'electronics': data.get('electronics', []),
        'home': data.get('home', []),
        'health_beauty': data.get('health_beauty', []),
        'jewelry_accessories': data.get('jewelry_accessories', []),
        'apparel': data.get('apparel', []),
        'bags': data.get('bags', []),
        'footwear': data.get('footwear', []),
        'headgear': data.get('headgear', []),
        'gadgets_computers': data.get('gadgets_computers', []),
        'food': data.get('food', []),
    })

    
    
    
    
    
    
    
    
CATEGORY_URL_MAPPING = {
    'electronics': 'electronics',
    'home': 'home',
    'health_beauty': 'beauty',
    'jewelry_accessories': 'jewelry',
    'apparel': 'apparel',
    'bags': 'bags',
    'footwear': 'footwear',
    'headgear': 'headgear',
    'food': 'food',
    'gadgets_computers': 'computers',
}
@login_required(login_url='Eapp:login')
def sell(request):
    if request.method == 'POST':
        # Set up today's date range
        today_start = now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)

        # Check the user's daily upload limit
        user_products_today = Product.objects.filter(
            user=request.user, created_at__range=(today_start, today_end)
        ).count()
        if user_products_today >= 3:
            messages.error(request, "You can only upload a maximum of 3 products per day.")
            return redirect('Eapp:index')

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user

            product_image = request.FILES.get('product_image')

            if product_image:
                # Validate file type to ignore non-image uploads
                if product_image.content_type not in ['image/jpeg', 'image/png', 'image/gif', 'image/pjpeg']:
                    messages.error(request, 'Only image files are allowed (JPEG, PNG, GIF).')
                    return render(request, 'sell.html', {'form': form})

                try:
                    # Upload to ImgBB
                    image_url = upload_image_to_imgbb(product_image)
                    if image_url:
                        product.product_image_url = image_url
                    else:
                        messages.error(request, 'Failed to upload the image. Please try again.')
                        return render(request, 'sell.html', {'form': form})

                except Exception as e:
                    messages.error(request, f'Error processing image: {str(e)}')
                    return render(request, 'sell.html', {'form': form})

            product.save()
            category_slug = CATEGORY_URL_MAPPING.get(product.product_category, 'Eapp:shop')

            messages.success(request, 'Product uploaded successfully! Redirecting in 3 seconds.')
            request.session['show_share_modal'] = True

            return redirect(f'/{category_slug}')
        else:
            messages.error(request, 'Invalid submission. Please check your details and try again.')
    else:
        form = ProductForm()

    return render(request, 'sell.html', {'form': form})

def electronics(request):
    products = Product.objects.filter(product_category='electronics').order_by('-created_at')
    # Check if the modal should be shown based on session and last shared time
    show_share_modal = request.session.get('show_share_modal', False)
    last_shared_time = request.session.get('last_shared_time')

    # If the last shared time is within 24 hours, don't show the modal
    if last_shared_time and (timezone.now() - last_shared_time) < timedelta(hours=24):
        show_share_modal = False

    context = {
        'products': products,
        'show_share_modal': show_share_modal
    }

    # Remove the session flag after rendering, but only if the user shared on WhatsApp (handled by JS)
    if show_share_modal:
        request.session['show_share_modal'] = True  # Persist modal until user shares
    return render(request, 'electronics.html', context)

def shop(request):
    # Get all products
    products = Product.objects.all().order_by('-created_at')  # Fetch all products from the database
    return render(request, 'shop.html', {'products': products})

@login_required
def update_share_status(request):
    if request.method == 'POST':
        shared = request.POST.get('shared') == 'true'
        if shared:
            request.session['last_shared_time'] = timezone.now()
            request.session['show_share_modal'] = False
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
