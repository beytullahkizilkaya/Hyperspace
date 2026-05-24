from django.contrib import admin
from .models import Blog

# Register your models here

@admin.register(Blog)
class BlogAdmin (admin.ModelAdmin):
    list_display=('title','slug','author')
#admin panelinde hangi sütunların görüneceğini belirler.
#list_display=('title','slug','author') ile title, slug ve author sütunlarının görünmesini sağlıyoruz.     
 
    search_fields=('title','content','author')
#Bu, admin panelinin üstünde bir "Metin Giriş Kutusu" oluşturur.
#Nasıl Çalışır? Sen oraya "Django" yazdığında, sistem gider belirttiğin alanlarda (title, content vb.) bu kelimeyi arar.
#Hangi Durumlarda Kullanılır? Spesifik bir kelimeyi, başlığı veya kullanıcı adını "yazarak" bulmak istediğinde.

    list_filter=('author',)
#Bu, admin panelinin sağ tarafında bir "Hızlı Seçim Menüsü" oluşturur.
#Nasıl Çalışır? Sen oraya tıklamazsın, oradaki seçeneklerden birini (örneğin bir yazarın adını) seçersin. Tıkladığında sadece o yazara ait postlar listelenir.
#Hangi Durumlarda Kullanılır? Kategorize etmek için. "Sadece aktif olanları göster", "Sadece Ahmet'in yazılarını göster" veya "Sadece bugün yazılanları göster" gibi.  
    
    row_id_fields = ['author']
#row_id_fields, admin panelinde ForeignKey alanlarının daha hızlı yüklenmesini sağlar.
#row_id_fields = ['author'] ile author alanının daha hızlı yüklenmesini sağlıyoruz.
