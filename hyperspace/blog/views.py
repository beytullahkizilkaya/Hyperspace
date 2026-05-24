from django.shortcuts import render,get_object_or_404
from . models import Blog
from django.core.paginator import Paginator

def post_list(request):
    
    #Tüm blog yazılarını çekiyoruz.
    posts = Blog.objects.all()
    
#Paginasyon işlemi için Paginator sınıfını kullanarak, her sayfada 2 blog yazısı göstermek istediğimizi belirtiyoruz.
    paginator = Paginator(posts,2)
    
    #Kullanıcının hangi sayfayı istediğini URL'den alıyoruz. 
    #Eğer kullanıcı herhangi bir sayfa numarası belirtmezse, varsayılan olarak 1. sayfayı göstermek istiyoruz.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render (request,'blog/post_list.html',{'posts':posts,"page_obj":page_obj})

#post_detail fonksiyonu, belirli bir blog yazısının detay sayfasını göstermek için kullanılır.
def post_detail(request,slug):
   
    #Neden filter değil de get_object_or_404? Çünkü filter sana bir liste döndürür. get ise tek bir nesne döndürür. 
    # Eğer aranan slug bulunamazsa, site "Internal Server Error (500)" vermek yerine kullanıcıya 
    # "Aradığınız sayfa yok (404)" der. Bu, kullanıcı deneyimi için altındır.
    posts = get_object_or_404(Blog,slug=slug)

    return render (request,'blog/post_detail.html',{'post':posts})


