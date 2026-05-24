# 🚀 Proje Kurulum ve PostgreSQL Yapılandırma Kılavuzu 

Bu proje, veritabanı altyapısı olarak **PostgreSQL** kullanmaktadır. Projeyi yerel bilgisayarınızda test etmek ve hazır verileri yüklemek için lütfen aşağıdaki adımları sırasıyla uygulayın:

### Adım 1: Veritabanını Oluşturma
Yerel PostgreSQL sunucunuzda (pgAdmin veya terminal üzerinden) **`blog_db`** adında boş bir veritabanı oluşturun.

### Adım 2: Veritabanı Bağlantı Ayarları
`hyperspace/settings.py` dosyasındaki `DATABASES` ayarlarından kullanıcı adı (`USER`) ve şifre (`PASSWORD`) alanlarını kendi yerel PostgreSQL sunucu bilgilerinize göre güncelleyin:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',        # PostgreSQL kullanıcı adınız
        'PASSWORD': 'YOUR_PASSWORD', # PostgreSQL şifreniz
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Adım 3: Bağımlılıkların Kurulması
Projenin çalışması için gerekli kütüphaneleri yükleyin:
pip install -r requirements.txt


Adım 4: Tabloların ve Hazır Verilerin Yüklenmesi
Aşağıdaki komutları sırasıyla çalıştırarak veritabanı tablolarını oluşturun ve hazır veri yedeğini (kullanıcılar, blog yazıları ve loglar dahil) sisteme aktarın:
python manage.py migrate
python manage.py loaddata data.json


Adım 5: Sunucuyu Başlatma
python manage.py runserver

🔐 Hazır Yönetici (Admin) Bilgileri
Proje verilerini panel üzerinden incelemek için loaddata ile yüklenen hazır admin hesabını kullanabilirsiniz:

URL: http://127.0.0.1:8000/admin

Kullanıcı Adı: beyto