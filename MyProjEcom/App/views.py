from django.shortcuts import render
from App.models import *
# Create your views here.


def index(request):
    return render(request, 'home.html')




def Addproduct(request):
    if request.method == "POST":
        # Get form data
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_stock = request.POST.get('product_stock')
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')

        # Debugging prints
        print(f"Product Name: {product_name}")
        print(f"Product Description: {product_description}")
        print(f"Product Price: {product_price}")
        print(f"Product Stock: {product_stock}")
        print(f"Category ID: {category_id}")
        print(f"SubCategory ID: {subcategory_id}")
        
        
    categories = MainCategory.objects.all()
    subcategories = SubCategory.objects.all()

    return render(request, 'Addproduct.html', {'categories': categories, 'subcategories': subcategories})


