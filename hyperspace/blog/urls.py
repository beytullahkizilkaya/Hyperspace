from django.urls import path
from . import views

#Bu dosya, tarayıcıya yazılan adres ile 
#Python fonksiyonlarını birbirine bağlayan köprüdür.

#Örneğin, tarayıcıya "http://localhost:8000/blog/" yazdığında, bu URL'nin hangi fonksiyona karşılık geldiğini belirleriz.


urlpatterns = [
    #Boş Tırnak (''): Bu, ana sayfa demektir. Yani kullanıcı www.siten.com/blog/ 
    # yazdığında direkt listeye ulaşır.
    #name='post_list': Bu çok değerlidir! HTML içinde link verirken adresi elle 
    # yazmak yerine {% url 'post_list' %} diyebilirsin. Yarın öbür gün adresi değiştirsen 
    # bile (mesela /liste/ yapsan bile) HTML'deki linkler bozulmaz.
    path('',views.post_list,name='post_list'),
    
    #<slug:slug>: İşte sihir burada. Django'ya şunu diyorsun: 
    # "Buraya gelecek olan herhangi bir metni al, slug ismiyle paketle ve views.post_detail 
    # fonksiyonuna kargo olarak gönder."
    #Güvenlik: Başına slug: yazdığın için Django buraya gelen verinin sadece harf, rakam ve 
    # tire içermesini bekler. Saçma sapan karakterler gelirse daha en baştan engeller.
    path('<slug:slug>',views.post_detail,name='post_detail')
]
