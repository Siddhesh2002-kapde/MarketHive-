# def index(request):
#     sub_cat_name = ['Car Accessories','Bike Accessories','Tools & Equipment']
#     main_cat = MainCategory.objects.get(name = "Automotive")
#     print(main_cat)
#     sub_cat = SubCategory.objects.all()
#     for i in sub_cat_name:
#         sub_cat.create(main_category = main_cat, name = i)
#     return render(request, 'home.html')