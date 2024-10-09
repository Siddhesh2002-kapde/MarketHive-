from unicodedata import category
from django.shortcuts import render
from App.models import *
from decimal import Decimal

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
        image = request.FILES.get('images')
        
        
        # product_price=Decimal(product_price)
        # product_stock=Decimal(product_stock)
        # Debugging prints
        print(f"Product Name: {product_name}")
        print(f"Product Description: {product_description}")
        print(f"Product Price: {product_price}")
        print(f"Category ID: {category_id}")
        print(f"SubCategory ID: {subcategory_id}")
        print(f"Images is :{image}")
        
       
        product_price = Product.objects.values_list('price', flat = True)
        product_stock = Product.objects.values_list('stock', flat = True)
        print(product_stock)
        
        # queryset = Product.objects.create(
        #     name=product_name,
        #     description=product_description,
        #     price=product_price,
        #     stock=product_stock,
        #     main_category=main_category,
        #     sub_category=sub_category,
        #     image=image
        # )
        # queryset.save() 
        
        categories = MainCategory.objects.all()  # Retrieve all categories
        subcategories = []
        if category_id:
            subcategories = SubCategory.objects.filter(main_category__id = category_id)
    
        
        
    return render(request, 'Addproduct.html', {'categories': categories, 'subcategories': subcategories})


