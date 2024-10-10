
from django.shortcuts import render,redirect
from App.models import *
from decimal import Decimal
from django.http import HttpResponse
# Create your views here.


def index(request):
    mainCat = MainCategory.objects.get(name = 'Arts & Crafts')
    print(mainCat)
    SubCat_data = [ 'Painting, Drawing & Art Supplies'
'Beading & Jewelry Making','Crafting','Fabric','Fabric Decorating','Knitting & Crochet','Needlework','Organization, Storage & Transport','Printmaking','Scrapbooking & Stamping','Sewing','Party Decorations & Supplies','Gift Wrapping Supplies' ]
    print(SubCat_data)
    
    # if(mainCat):
    #     for name in SubCat_data:
    #         SubCategory.objects.create(
    #             name = name,
    #             main_category = mainCat
    #         )
    # else:
    #     return HttpResponse("Data already sotred!")
        
    return render(request, 'home.html')



def Addproduct(request):
    main_category_selected = None
    sub_categories = SubCategory.objects.none()
    if request.method == "POST":
        # Get form data
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_price = request.POST.get('product_price')
        product_stock = request.POST.get('product_stock')
        main_category_id = request.POST.get('category')
        sub_category_id = request.POST.get('subcategory')
        image = request.FILES.get('images')    
        
        if(main_category_id):
            main_category_selected = MainCategory.objects.get(id = main_category_id)
            sub_categories = SubCategory.objects.filter(main_category = main_category_selected)
            
            
        if(sub_category_id and product_name and product_description and product_stock and product_price ):
            main_category = MainCategory.objects.get(id = main_category_id)
            sub_category = SubCategory.objects.get(id = sub_category_id)
            
            
            queryset = Product.objects.create(
                name = product_name,
                description = product_description,
                price = product_price,
                stock = product_stock,
                main_category = main_category,
                sub_category = sub_category,
                image = image,
            )
            
            queryset.save()
            print(main_category)
            print(sub_category)
            print(product_name)
            print(product_description)
            print(product_stock)
            print(product_price)
            print(image)
            
            
            
            return redirect('/form')
        
        
        
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
        
    main_categories = MainCategory.objects.all()
    
    context = {
        'main_categories': main_categories,
        'main_category_selected': main_category_selected,
        'sub_categories': sub_categories,
    }
    
    
    return render(request, 'Addproduct.html', context)


