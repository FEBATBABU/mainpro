from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q
# Create your views here.
def home(request,c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    cat=Category.objects.all()
    # paginator = Paginator(products, 6)
    # try:
    #     page=int(request.GET.get('page',1))
    # except:
    #      page=1
    # try:
    #      pro=paginator.page(page)
    # except (EmptyPage,InvalidPage):
    #      pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':products,'ct':cat})

def ProdCatDetail(request,c_slug,product_slug):
    try:
        prod=get_object_or_404(Product,category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})

def SearchResult(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request,"search.html",{'qr':query,'pr':prod})
