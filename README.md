# Teleplay

Teleplay adalah sebuah <b>E-Commerce</b> yang memberikan layanan entertainment atau informasi berupa video untuk dinikmati khayalak umum. Proyek Teleplay ini ditujukan untuk Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Fransisca Ellya Bunaren dengan NPM 2306152286. Proyek ini dibuat dengan sistem operasi microsoft. <br>
<b>Tautan menuju aplikasi PWS yang sudah di-deploy</b> : <br> [Link Repo PWS](http://fransisca-ellya-teleplay.pbp.cs.ui.ac.id/) <br><br>
<b>Tugas</b> :
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)


## Tugas 2
### 1.Proses Pembuatan Proyek Django
1. Membuat sebuah repository lokal bernama `teleplay` dan membuat sebuah repository github bernama 'teleplay'

2. Buat <i>branch</i> utama baru di terminal atau command prompt, jalankan 
```
git branch -M master
```

3. Hubungkan dengan repositori Github. <br>
Menghubungkan direktori lokal dengan github dengan `git remote`

4. Di direktori lokal, buat virtual environment Python baru dengan command :
```
python -m venv env
```

5. Mengaktifkan <i>virtual environment</i> dengan perintah berikut.  
```
env\Scripts\activate
```


6. Di dalam direktori sama, buat berkas `requirements.txt`dan tambahkan beberapa dependencies. 
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

7. Melakukan instalasi <i>depedencies</i> dengan perintah berikut.
```
pip install -r requirements.txt
```

8. Buat proyek Django bernama `teleplay` dengan cara
```
django-admin startproject teleplay .
```

9. Menambahkan kedua string pada `ALLOWED_HOST` di `settings.py` untuk keperluan deployment:
```
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
```

10. Untuk membuat aplikasi baru dengan nama <b>main</b> 
```
python manage.py startapp main
```

11. Tambahkan `'main'` ke dalam `INSTALLED_APPS` sebagai elemen terakhir yang terdapat di `settings.py` di dalam direktori proyek `teleplay`. 

```
INSTALLED_APPS = [
    ...,
    'main'
]
```

12. Buat berkas `models.py` pada direktori aplikasi `main`. Isi berkas `models.py` adalah sebagai berikut. 
```
from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def is_movie_good(self):
        return self.rating > 7
```

13. Melakukan migrasi model. Jalankan perintah berikut untuk membuat migrasi model.
```
python manage.py makemigrations
```

14. Menjalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal.
```
python manage.py migrate
```

15. Membuat direktori baru bernama `templates` di dalam direktori aplikasi `main`. Di dalam direktori tersebut, buat berkas bernama `main.html`. Berkas tersebut berisi nama E-Commerce, nama, dan kelas. 

```
<h1>{{ app_name }}</h1>
<p>Sebuah <b>E-Commerce</b> yang memberikan layanan entertainment atau informasi berupa video untuk dinikmati khayalak umum</p>

<h5>Name: </h5>
<p>{{ name }}</p>
<h5>Class: </h5>
<p>{{ class }}</p>
```
16. Untuk mengintegrasikan komponen MVT, buka berkas `views.py` yang terletak di dalam berkas aplikasi `main`. Tambahkan fungsi `show_main` yang akan mereturn fungsi render beserta argumennya. Fungsi ini untuk render tampilan HTML dengan menggunakan data yang diberikan. Berkas `views.py` akan berisi sebagai berikut.

```
from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Teleplay',
        'name' : 'Fransisca Ellya Bunaren',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)
```

17. Mengonfigurasi <i>Routing</i> pada aplikasi `main` pada file `urls.py` di direktori `main`. 
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
``` 

18. Mengonfigurasi <i>Routing</i> pada aplikasi `main` pada file `urls.py` di subdirektori `teleplay`.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls'))
]
```

19. Menguji aplikasi pada localhost dengan perintah. Kemudian,  membuka di `http://localhost:8000/` di peramban web. 
```
python manage.py runserver
```


20. Melakukan deployment ke PWS terhadap aplikasi dengan cara. Pertama, tekan `Create New Project`, isi `Project Name` dengan `teleplay`, dan tekan `Create New Project`. Akan muncul, <i>Project Credentials</i> dan <i>Project Commands</i> simpan kedua hal tersebut. Pada `settings.py` di subdirektori `teleplay`, tambahkan URL deployment PWS pada ALLOWED_HOSTS. 
```
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "fransisca-ellya-teleplay.pbp.cs.ui.ac.id"]
...
```
Melakukan `git add`, `commit`, dan `push` di github.

Tautan menuju aplikasi PWS yang sudah di-deploy : [http://fransisca-ellya-teleplay.pbp.cs.ui.ac.id/](http://fransisca-ellya-teleplay.pbp.cs.ui.ac.id/)

21. Menjalankan perintah yang terdapat pada PWS, yaitu `git remote`, `branch`, dan `push`.

22. Pada side bar situs PWS, klik proyek untuk melihat status deployemnt. Apabila `Running`, dapat mengakses URL deployment dengan menekan `View Project`. Lakukan,
```
git push pws master: master
```

### 2. Bagan Request Client ke Web Aplikasi Berbasis Django Beserta Responnya
![bagan](https://github.com/user-attachments/assets/dc15b2ed-f80d-4c7e-8691-a9a10a687c39)
Seorang user melakukan request yang akan diproses terlebih dahulu melalui urls.py. Kemudian, urls.py meneruskan ke view yang sesuai di views.py. Lalu, view akan membaca/menulis data di model dan menggunakan template untuk menentukan tampilan antarmuka pengguna. Setelah itu, views.py akan mengembalikan response ke user. 

### 3. Fungsi `git` dalam Pengembangan Perangkat Lunak
Git adalah sistem kontrol versi yang memiliki tujuan untuk melacak perubahan pada kode sumber proyek sehingga dapat memantau semua revisi yang telah dilakukan pada proyek seiring waktu. Git memainkan peran penting dalam pengembangan perangkat lunak modern dan kolaborasi tim dengan melacak perubahan kode, menyimpan versi, dan bekerja bersama dlam proyek secara efisien. 

### 4. Alasan Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak
Django adalah kerangka (framework) yang populer untuk pengrmbangan aplikasi web dengan bahasa pemrograman Python. Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak dengan alasan sebagai berikut.
* <b>Struktur yang terorganisir dan mudah dipahami</b> <br>
Django memiliki arsitektur MVT (Model-View-Template) yang memisahkan logika aplikasi, interaksi database, dan antarmuka pengguna.
* <b>Fitur lengkap</b> <br>
Django memiliki banyak fitur bawaan, seperti ORM(Object-Relational Mapping) dan masih banyak lagi. 
* <b>Pendekatan yang Berfokus pada Keamanan</b> <br>
Django memiliki berbagai fitur keamanan bawaan sehingga ini mengajarkan untuk membangun aplikasi yang aman sejak awal.
* <b>Dokumentasi Detail dan Komunitas yang Besar</b> <br>
Django memiliki dokumentasi yang sangat baik dan banyak tutorial.
* <b>Mendorong Praktik Pengembangan yang Baik</b> <br>
Django mengajarkan untuk melakukan praktik DRY (Don't Repeat Yourself), penggunaan pola desain, dan struktur proyek yang modular.
* <b>Scability dan Real-World Use</b> <br>
Django juga digunakan oleh perusahaan besar sehingga ini membuktikan bahwa keterampilan yang dipelajari relevan juga untuk dunia nyata.
* <b>Mudah dipelajari untuk Latar Belakang yang Ragam</b> <br>
Django menggunakan python yang mudah dipelajari. Ini membuat Django lebih mudah diakses oleh orang dari berbagai macam latar. 

### 5. Alasan Model Django Disebut Sebagai ORM
Model Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara kode Python dan dtabase relasional. Berikut adalah alasan mengapa Model Django dianggap sebagai ORM.
* <b>Menghubungkan Objek Python dengan Tabel Database</b> <br>
Dengan ORM, bisa memungkinkan untuk bekerja dengan database menggunakan objek Python. 
* <b>Abstaraksi Database</b> <br>
Django menyembunyikan kompleksitas SQL dari pengembang sehingga memungkinkan mereka untuk fokus pada logika aplikasi
* <b>Mapping Otomastis antara Kode dan Database</b> <br>
Django secara otomatis memetakan atribut kelas model ke kolom database dan instance model ke baris dengan tabel. 
* <b>Dukungan untuk Berbagai Jenis Database</b> <br>
Django ORM mendukung berbagai database, seperti Oracle.
* <b>Otomatisasi Query SQL dari Kode Python</b> <br>
ORM memungkinkan untuk menulis query kompleks menggunakan metode chaining yang mudah dibaca, seperti .filter()
* <b>Validasi Data dan Manajemen Skema yang Mudah</b> <br>
Django memungkinkan pengembang mengelola versi skema database dengan menyediakan migrasi otomatis dan mempervarui aplikasi secara aman. 
* <b>Keamanan</b> <br>
Django ORM menyediakan lapisan keamanan yang mencegah serangan SQL injection dengan otomatis.
* <b>Pengembangan yang Lebih Cepat</b> <br>
Menggunakan ORM dapat mempercepat proses pengembangan karena pengambang tidak perlu menuliskan kode SQL secara eksplisit. Selain itu, ORM memudahkan proses debugging dan perubahan skema.

Dengan alasan-alasan tersebut, model Django disebut sebagai ORM karena menyediakan cara yang lebih mudah, aman, dan efisien untuk berinteraksi dengan database relasional menggunakan kode Python. 

## Tugas 3
### 1. Proses Pembuatan form input, views, dan routing url
* <b>Membuat Form Input Data dan Menampilkan di Berkas HTML</b> <br>
1. Membuat `forms.py` di main untuk membuat struktur form yang dapat menerima data Mood Entry baru.

```
from django.forms import ModelForm
from django import forms
from main.models import Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ["name", "price", "description", "duration", "rating"]
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : "Enter video's name"}),
            'duration' : forms.TimeInput(format='%H:%M:%S', attrs={'placeholder' : "HH:MM:SS"}),
        }
```
2. Membuka berkas `views.py` yang ada di direktori `main` dan tambahkan fungsi `create_video_entry` yang menerima parameter `request`. Fungsi ini untuk  untuk menambahkan entri database. Selain itu, mengubah fungsi `show_main` yang sudah ada pada berkas views.py menjadi seperti berikut.
```
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import VideoForm
from main.models import Video

def show_main(request):
    video_entries = Video.objects.all()

    context = {
        'app_name' : 'Teleplay',
        'name' : 'Fransisca Ellya Bunaren',
        'class' : 'PBP F',
        'video_entries': video_entries
    }

    return render(request, "main.html", context)

def create_video_entry(request):
    form = VideoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_video_entry.html", context)

```
3. Untuk mengakses fungsi `show_main` dan `create_video_entry`, import dan tambahkan pada urlpatterns di `urls.py`.
```
from django.urls import path
from main.views import show_main, create_video_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-video-entry', create_video_entry, name='create_video_entry'),
    ...
    ]
```
4. Buat berkas `main.html`, mengubah kodenya menjadi sebagai berikut. `main.html` untuk menampilkan data entri. 
```{% extends 'base.html' %}
{% load static %}
{% block content %}

<h1 style="text-align: center; background-color: blanchedalmond; padding: 20px;">{{ app_name }}</h1>
<p style="text-align: center;">Sebuah <b>E-Commerce</b> yang memberikan layanan entertainment atau informasi berupa video untuk dinikmati khayalak umum</p>

<h3 style="text-align: center;">Name: </h3>
<p style="text-align: center;">{{ name }}</p>
<h3 style="text-align: center;">Class: </h3>
<p style="text-align: center;">{{ class }}</p>

{% if not video_entries %}
<p>Belum ada data video pada teleplay.</p>
{% else %}
<table id="table-main">
  <tr class="table-row">
    <th class="data-table">Nama Video</th>
    <th class="data-table">Price</th>
    <th class="data-table">Description</th>
    <th class="data-table">Duration</th>
    <th class="data-table">Rating</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
  {% endcomment %} 
  {% for video_entry in video_entries %}
  <tr class="table-row">
    <td class="data-table">{{video_entry.name}}</td>
    <td class="data-table">{{video_entry.price}}</td>
    <td class="data-table">{{video_entry.description}}</td>
    <td class="data-table">{{video_entry.duration}}</td>
    <td class="data-table">{{video_entry.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_video_entry' %}">
  <button style="text-align: right;">Add New Video Entry</button>
</a>
{% endblock content %}
```
5. Buat berkas `create_video_entry.html`, mengubah kodenya menjadi sebagai berikut. `main.html` untuk menampilkan data entri.
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Video Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td style="text-align: right;">
        <input type="submit" value="Add Video Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
``` 
* <b>Fungsi-Fungsi untuk Menambahkan Objek Model dengan Format XML, JSON, XML by ID, dan JSON by ID</b> <br>
1. Buka `views.py`, import `HttpResponse` dan `Serializer`. Tambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. 
```
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import VideoForm
from main.models import Video
...
def show_xml(request):
    data = Video.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Video.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
``` 
* <b>Membuat routing URL untuk masing-masing views</b> <br>
1.. Buka `urls.py`, import fungsi yang telah dibuat. Tambahkan <i>path url</i> ke dalam urlpatterns.
```
...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
...
```
2. Jalankan proyek Django-mu dengan `perintah python manage.py runserver`.
Untuk melihat hasil menggunakan `show_json` : [http://localhost:8000/json/](http://localhost:8000/json/)
Untuk melihat hasil menggunakan `show_xml` : [http://localhost:8000/xml/](http://localhost:8000/json/)
Untuk melihat hasil menggunakan `show_xml_by_id` : [http://localhost:8000/xml/[id]/](http://localhost:8000/xml/[id]/) dengan id yang didapatkan ketika mengakses endpoint /json/ atau /xml/.
Untuk melihat hasil menggunakan `show_json_by_id` : [ http://localhost:8000/json/[id]/](http://localhost:8000/json/[id]/) dengan id yang didapatkan ketika mengakses endpoint /json/ atau /xml/.

### 2. Jawaban dari Pertanyaan
<b>Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</b><br>

Data delivery sangat penting karena merupakan proses pengiriman data dari satu titik ke titik lainnya secara efisiensi, kecepatan, dan keandalan yang optimal. Alasan utama data delivery dibutuhkan adalah :
1. <b>Akses Data yang Cepat dan Real-Time</b> sehingga pengguna bisa mendapatkan informasi terbaru.
2. <b>Skalabilitas</b> sehingga dapat mengelola permintaan data dari banyak pengguna secara bersamaan tanpa adanya penurunan performa.
3. <b>User Experience (Pengalaman Pengguna)</b> karena pengalaman pengguna sangat dipengaruhi oleh seberapa cepat platform tersebut dapat menyajikan data.
4. <b>Keamanan Data</b> <br>
Data delivery yang baik dapat mengintegrasikan mekanisme enkripsi dan protokol keamanan yang kuat untuk melindungi data-data sensitif.
5. <b>Penyebaran Konten yang Luas</b> <br>
Platform yang memiliki jangkauan global/luas membutuhkan mekanisme data delivery yang dapat menjangkau pengguna di berbagai lokasi grafis.
6. <b>Pengambilan Keputusan dan Analisis</b> <br>
Platform sering mengandalkan data untuk analisi dan pengambilan keputusan.
Jadi, data delivery digunakan untuk memastikan platform dapat berjalan dengan lancar, aman, dan responsif terhadap kebutuhan pengguna serta perkembangan data yang dinamis.

 <b>Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?</b> <br>

Menurut saya, JSON lebih baik daripada XML karena keringkasan dan sederhana. Selain itu, integrasi dengan javascript. JSON adalah bagian dari JavaScript sehingga mudah diproses oleh browser atau aplikasi yang menggunakan JavaScript. Lalu, JSON lebih ringan dan kurang kompleks sehingga proses parsing dan transfer data JSON lebih cepat dibandingkan XML. Kemudian, JSON mendukung tipe data yang lebih banyak, seperti array, objek, string, integer, boolean, dan null sehingga memudahkan representasi struktur data yang kompleks dibandingkan dengan XML tidak mendukung array atau tipe data primitif lainnya. Dalam pengembangan API berbasis REST, JSON menjadi standar de facto karena kesederhanaan dan kemampuan untuk memproses data yang cepat. Terakhir, JSON sangat fleksibilitas untuk pertukaran data yantar aplikasi modern.

JSON lebih populer karena sederhana dan ringkas, cepat dan mudah diolah, mendukung REST API, dan memiliki ekosistem yang modern. Secara unum, JSON lebih baik dalam hal keringkasan, kinerja, dan integrasi dengan web yang modern. 

<b>Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?</b> <br>

Fungsi dari method `is_valid()` adalah memvalidasi data input, membersihkan data, dan mendeteksi error. 

Fungsi ini dibutuhkan untuk keamanan dan validitas data,menjadga integritas data, dapat melakukan error handling yang mudah, dan membuat alur kerja yang standar dan konsisten. Tanpa validasi yang baik, data yang diterima dapat tidak sesuai atau berbahaya, yang bisa menyebabkan masalah di dalam aplikasi.

<b>Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?</b> <br>

CSRF token (Cross-Site Request Forgery token) adalah token yang berfungsi untuk mencegah serangan CSRF dan token ini digenerate oleh django. Seangan CSRF adalah jenis serangan di mana penyerang mencoba melakukan permintaan yang sah (seperti mengirim form) dari browser. Oleh karena itu, kita membutuhkan CSRF token untuk keamanan form django. 

Jika kita tidak menambahkan CSRF token, situs akan rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan sesi pengguna yang aktif di browser, seperti mengirim form tanpa sepengetahuan pengguna. Penyerang dapat membuat halaman berbahaya yang secara diam-diam mengirim POST ke aplikasi. Jika pengguna login ke aplikasi kemudian mengunjungi halaman penyerang, maka form dari halaman jahat tersebut dapat dikirim menggunakan kredensial atau sesi pengguna, seolah-olah pengguna yang melakukan tindakan itu sendiri. 

Penyerang dapat memanfaatkan hal ini dengan:
- Mengeksploitasii sesi aktif
Ketika pengguna login ke situs kemudian mengunjungi situs lain berbahaya, situs berbahaya tersebut dapat mengirimkan permintaan ke server kita menggunakan sesi aktif pengguna tanpa sepengetahuan pengguna. 
- Menjalankan aksi tanpa izin
Penyerang dapat memanipulasi aplikasi untuk melakukan tindakan, seperti mengirimkan pesan, mengubah data profil, dan tindakan lainnya yang membutuhkan otorisasi pengguna.

### 3. Screenshot dari hasil akses URL pada Postman
* <b>Hasil akses json</b> <br>
![Screenshot 2024-09-17 052236](https://github.com/user-attachments/assets/b4ed4ae5-c676-4eb0-ab8c-fa3ae204a140)
* <b>Hasil akses xml</b> <br>
![Screenshot 2024-09-17 052152](https://github.com/user-attachments/assets/6d62a2f7-b391-487c-afc6-5bf3a3f60942)
* <b>Hasil akses json/</b> <br>
![Screenshot 2024-09-17 052308](https://github.com/user-attachments/assets/53f4bcb9-d915-42d0-9011-9910259819a4)
* <b>Hasil akses xml/[id]</b> <br>
![Screenshot 2024-09-17 052326](https://github.com/user-attachments/assets/19287553-919d-4f75-b71c-d1fe991f8c42)

## Tugas 4
### 1. Checklist
1. * Untuk mengimplementasi fungsi registrasi, menambahkan fungsi `registrasi` di views.py dan library yang dibutuhkan `redirect` dari django.shortcuts, `UserCreationForm` dari django.contrib.auth.forms, dan `messages` dari django.contrib. Untuk fungsi login, tambahkan fungsi `login_user` dan library yang dibutuhkan adalah `login` dari django.contrib.auth dan `AuthenticationForm` dari django.contrib.auth.forms. Terakhir, untuk implementasi fungsi logout, tambahkan fungsi `logout` dan import `logout` dari django.contrib.auth. Pada fungsi, login_user ditambahkan decoratir agar user harus login terlebih dahulu sebelum mengakses halaman lain. 
```
@login_required(login_url='/login')
def login_user(request):
   if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Kemudian, menambahkan ke `urls.py` untuk routing. Pertama, import terlebih dahulu fungsi-fungsi tersebut dari `main.views`. 
```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

Membuat halaman html untuk register.
```
{% extends 'base.html' %}
{% block content %}

<h1 style="text-align: center; background-color: blanchedalmond; padding: 20px; margin-top: auto;">{{ app_name }}</h1>
<p style="text-align: center;">Sebuah <b>E-Commerce</b> yang memberikan layanan entertainment atau informasi berupa video untuk dinikmati khayalak umum</p>

<h3>Name: </h3>
<p>{{ name }}</p>
<h3>Class: </h3>
<p>{{ class }}</p>

<br>
{% if not video_entries %}
<p>Belum ada data video pada teleplay.</p>
{% else %}
<table id="table-main">
  <tr class="table-row-header">
    <th class="data-table">Nama Video</th>
    <th class="data-table">Price</th>
    <th class="data-table">Description</th>
    <th class="data-table">Duration</th>
    <th class="data-table">Rating</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data video di bawah baris ini 
  {% endcomment %} 
  {% for video_entry in video_entries %}
  <tr class="table-row">
    <td class="data-table">{{video_entry.name}}</td>
    <td class="data-table">{{video_entry.price}}</td>
    <td class="data-table">{{video_entry.description}}</td>
    <td class="data-table">{{video_entry.duration}}</td>
    <td class="data-table">{{video_entry.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />
<h5>Sesi terakhir login: {{ last_login }}</h5>


<div>
  <a href="{% url 'main:create_video_entry' %}">
    <button>Add New Video Entry</button>
  </a>
  <br><br>
  <a href="{% url 'main:logout' %}">
    <button>Logout</button>
  </a>
</div>

{% endblock content %}
```
Membuat halaman html untuk login.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
* Menghubungkan model `Product` dengan `user`
Untuk mengubungkan model `Product` dengan `user`, menambahkan ForeignKey untuk hubungan user dengan product dan mengimpor `User` dari `django.contrib.auth.models` di `models.py`. 
```
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Kemudian, di `views.py` yang ada di `main`, membuat kode sebagai berikut. 
```
def create_video_entry(request):
    form = VideoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        video_entry = form.save(commit=False)
        video_entry.user = request.user
        video_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_video_entry.html", context)
```

Pada fungsi `show_main`, menambahkan `video_entries = Video.objects.filter(user=request.user)` dan pada context, `'name': request.user.username,` Lalu, lakukan makemigrations dan migrate.

* Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model 
    - Dummy 1
      ![Screenshot 2024-09-25 045457](https://github.com/user-attachments/assets/2b025124-5304-41cb-a449-6181dabed051)

    - Dummy 2
      ![Screenshot 2024-09-25 045517](https://github.com/user-attachments/assets/ad3284ff-e73c-4112-9994-578062fd4f32)


* Detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. <br>
Di `views.py`, melakukan import datetime, HttpResponseRedirect dari django.http, dan import reverse dari django.urls . Untuk menambahkan fungsionalitas cookie, menambahkan last_login untuk melihat terakhir kali pengguna login.
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
Pada fungsi show_main, menambahkan `last_login': request.COOKIES['last_login']` ke dalam variabel context.  Pada fungsi `logout_user` menambahkan `response.delete_cookie('last_login')` untuk menghapus cookie last login dan `response = HttpResponseRedirect(reverse('main:login'))` untuk kembali ke halaman login. Untuk menampilkan sesi terakhir login di main.html, `<h5>Sesi terakhir login: {{ last_login }}</h5>`

### 2. Jawaban dari Pertanyaan
1. Perbedaan antara HttpResponseRedirect() dan redirect():
    * HTTPResponseRedirect() 
    HTTPResponseRedirect() untuk melakukan redirect secara eksplisit ke URL tertentu dan argumen yang dapat diterima hanya URL. 
    * redirect()
    Fungsi ini adalah lefih fleksibel dan dapat menerima argumen berupa model, view, atau url. 

2. Cara kerja penghubungan model Product dengan User: 
    Untuk menghubungkan model `Product` dengan `User` di Django, menggunakan ForeignKey dengan fungsi untuk hubungan satu-ke-banyak. 
    ```
    class Video(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    Potongan kode ini untuk menghubungkan satu video dengan satu user melalui sebuah <i>relationship</i> di mana sebuah Video pasti memiliki satu user, sedangkan user dapat memiliki banyak video/product.

3. Authentication adalah sebuah proses yang memverifikasi identitas, sedangkan authentication adalah proses penentuan hak akses atau izin pengguna. Saat pengguna login, langkah yang diambil adalah 
    <br> (i) Authentication: <br>
    Pengguna memasukkan nama pengguna dan kata sandi. Sistem memverifikasi kredensial terhadap data yang tersimpan dalam database. Jika kredensial benar, pengguna telah terautentikasi.
    <br> (ii) Authorization: <br>
    Setelah autentikasi, sistem memeriksa izin pengguna untuk menentukan halaman atau fitur yang dapat diakses. <br>
    <b>Implementasi di Django</b><br>
    1. Authentication<br>
    Menambahkan import AuthenticationForm dan login, kemudian menambahkan fungsi `login_user` di `views.py` untuk mengautentikasi pengguna.
        * Model user : Django menyediakan model User yang menyimpan informasi.
        * Form Authentication : Django memiliki form untuk menangangi login (AuthenticationForm) dan regiatrasi pengguna.
        * Middleware : Django menggunakan middleware untuk menangani sesi pengguna dan autentikasi. <br>
    
    2. Authorization<br>
    Setelah login, Django menangani otorisasi.
        * Pemissions: Django menyediakan sistem izin yang memungkinkan untuk menetapkan izin khusu pada model.
        * Groups: Pengelompokkan pengguna dan memberikan izin kepada group tersebut.
        * Decorators: Django menyediakan decorators seperti `@login_required` yang menyebabkan hanya dapat mengakses view tertentu bersasarkan autentikasi dan otorisasi pengguna. 
    
    4. Django mengingat pengguna yang login adalah holding state dengan menggunakan Cookies dan Session. Data cookie disimpan pada sisi klien, sedangkan data session biasanya disimpan pada sisi server. <br>
    Ketika pengguna login, Django membuat objek sesi pengguna dan menyimpan ID sesi di server. Untuk Cookie sesi, Django mengirimkan cookie sesi ke browser pengguna. Setiap kali pengguna membuat request baru, 
    browser mengirimkan cookie sesi kembali ke server. Untuk validasi sesi, Django menggunakan ID sesi dalam cookie untuk mencari informasi sesi di server dan menghubungkannya dengan pengguna yang login. <br>
    Kegunaan lain dari cookies adalah:
        * Menyimpan preferensi pengguna untuk menyimpan pengaturan pengguna.
        * Pelacakan aktivitas pengguna untuk melacak aktivitas pengguna. 
        * Manajemen keranjang belanja memungkinkan unruk melacak barang-barang dalam keranjang belanja pengguna.
        * Analitik dan iklan untuk melacak perilaku pengguna dan menampilan iklan yang dipersonalisasi. <br>
    <b>Tidak semua cookies aman digunakan. Ada risiko penggunaan cookies, yaitu </b>
        * Cookies bisa dibaca oleh pihak ketiga
        * Cookies bisa dicuru dalam transmisi (Man-in-the-Middle Attack) <br>
        Jika cookies dikirim dalam koneksi yang tidak aman, seorang penyerang dapat mencegatnya dalam perjalanan antara browser dan server.
        * Cookies bisa dimanipulasi oleh pengguna oleh penyerang.
        * CSRF (Cross-Site Request Forgery) dapat memanfaatkan cookies sesi untuk mengeksekusi perintah tanpa izin pengguna.

## Tugas 5
### 1. Checklist
* Untuk mengimplemantasikan fungsi menghapus dan mengedit product, dibuat fungsi `edit_fungsi` dan `delete_video` di views.py yang berisi sebagai berikut. Fungsi-fungsi ini kemudian akan dipanggil di `urls.py` kemudian dikirim ke `halaman yang membutuhkan fungsi ini`

```
def edit_video(request, id):
    video = Video.objects.get(pk = id)

    form = VideoForm(request.POST or None, request.FILES or None, instance=video)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_video.html", context)

def delete_video(request, id):
    mood = Video.objects.get(pk = id)
    mood.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

* Kustomisasi halaman daftar product.
- Jika tidak ada, form entry produk akan mengirimkan pesan dan gambar. Saya mengimplentasikannya dengan cara berikut.

```
{% if not video_entries %}
    <div class="flex flex-col items-center justify-center min-h-[12rem] p-4">
        <img src="{% static 'image/No Video.png' %}" alt="No Video" class="w-24 h-24 mb-2"/>
        <p class="text-center text-gray-600 mt-4">Belum ada data video pada {{ app_name }}.</p>
    </div>
...
```

- Kemudian, jika sudah ada product akan menampilkan card product.
```
  {% else %}
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for video_entry in video_entries %}
          {% include 'card_video.html' with video_entry=video_entry %}
      {% endfor %}
  </div>
  {% endif %}
```
Card yang saya buat dengan menggunakan Tailwind CSS CDN seperti ini. 
```
{% load static %}

<div class="relative break-inside-avoid">
    <div class="relative shadow-md rounded-2xl break-inside-avoid flex flex-col group hover:shadow-lg hover:border-transparent motion-safe:hover:scale-105">
        <div class="block rounded-lg bg-white shadow-secondary-1 group">
            {% if video_entry.video_thumbnail %}
                <img src="{{ video_entry.video_thumbnail.url }}" alt="Thumbnail" class="rounded-t-lg"/>
                <div class="opacity-0 group-hover:opacity-100 duration-300 absolute inset-x-0 justify-center items-end text-xl bg-gradient-to-t from-purple-300 to-indigo-300 text-black font-semibold">
                    <h5 class="p-6 text-surface text-black">Deskripsi</p>
                    <p class="text-gray-600 text-left break-words overflow-x scroll_bar">{{video_entry.description}}</p>
                </div>
                {% else %}
                <div class="relative text-center overflow-hidden">
                    <img src="{% static 'image/default.png' %}"  alt="default video thumbnail" class="rounded-t-lg"/>
                    <div class="absolute inset-0 flex items-center justify-center">
                        <h2 class="text-4xl font-bold text-white break-words text-center bg-black bg-opacity-50 p-2 rounded">
                            {{ video_entry.name }}
                        </h2>
                    </div>
                </div>
                <div class="opacity-0 group-hover:opacity-100 duration-300 absolute inset-x-0 justify-center items-end text-xl bg-gradient-to-t from-purple-300 to-indigo-300 text-black font-semibold">
                    <h5 class="p-6 text-surface text-black">Deskripsi</p>
                    <p class="text-gray-600 text-left break-words overflow-x scroll_bar">{{video_entry.description}}</p>
                </div>
            {% endif %}
        </div>
        <div class="p-6 text-surface text-black">
            <div class="flex justify-between items-center mb-2"> 
                <h5 class="font-bold text-xl break-words">{{ video_entry.name }}</h5>
                <p class="text-gray-600 text-right">
                    {{ video_entry.release_date }}
                </p>
            </div>
            <p class="font-semibold text-lg mb-2">Price</p> 
            <p class="text-gray-700 mb-2">
                <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{video_entry.price}}</span>
            </p>
            <p class="font-semibold text-lg mb-2">Duration</p> 
            <p class="text-gray-700 mb-2">
                <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{video_entry.duration}}</span>
            </p>
        </div>
    </div>
    <div class="absolute top-0 -right-4 flex space-x-1">
        <a href="{% url 'main:edit_video' video_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
        </a>
        <a href="{% url 'main:delete_video' video_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </a>
    </div>
</div>
```

* Dari fungsi edit dan hapus, dapat dilakukan pembuatan button. Berikut implementasinya.
```
  <a href="{% url 'main:edit_video' video_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
      </svg>
  </a>
  <a href="{% url 'main:delete_video' video_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
```

* Implementasi yang saya lakukan agar navbar responsive sebagai berikut. Selain itu, saya menggunakan flex agar setiap elemen dapat responsive saya menggunakan flex.

```
{% load static %}

<nav class="bg-gradient-to-t from-[#6a11cb] to-[#00008b] shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <a
            class="text-4xl font-bold text-center text-white"
            href="{% url 'main:show_main' %}">
                <img
                src="{% static 'image/Logo.png' %}"
                style="height: 40px"
                alt="Logo Teleplay"
                loading="lazy" />
          </a>
        </div>
        <div class="hidden md:flex items-center space-x-4">
          {% if user.is_authenticated %}
          <a
          class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
          href="{% url 'main:show_main' %}">
              {{ app_name }}
          </a>
            <a href="{% url 'main:create_video_entry' %}" 
            class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                Create Video
            </a>
            <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
      <div class="pt-2 pb-3 space-y-1 mx-auto">
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
          <ul>
            <li>
              <a href="{% url 'main:show_main' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                Home
              </a>
            </li>
            <li>
              <a href="{% url 'main:create_video_entry' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                Create Video
              </a>
            </li>
            <li>
              <a href="{% url 'main:logout' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
                Logout
              </a>
            </li>
          </ul>
        {% else %}
          <a href="{% url 'main:login' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```

### 2. Jawab Pertanyaan

1. CSS Selectors memiliki urutan untuk digunakan. Pertama,
(i) Inline styles adalah style yang berada di dalam sebuah style tag.
(ii) ID selectors adalah style yang dipakai berdasarkan ID yang dipilih.
(iii) Classes selector adalah style yang dipakai berdasarkan class yang sudah didefinisikan dan dipilih.
(iv) Element selector adalah jenis selector dalam CSS yang digunakan untuk memilih elemen HTML berdasarkan nama tag-nya. Contoh :
```
p{
  font-size: 16px;
}
```

2. Responsive design adalah membuat sebuah website yang baik untuk semua tampilan di segala device. Responsive design sangat penting karena untuk memastikan tampilan dan pengalaman pengguna optimal di berbagai perangkat. Alasan-alasan lainnya adalah sebagai berikut.
(i) Pengalaman pengguna yang konsisten
(ii) SEO Friendly: Google memprioritaskan situs responsif dalam pencarian.
(iii) Efisiensi Pengembangan: Dengan responsive design, pengambang bisa fokus untuk membuat satu situs web yang dapat sesuai dengan beebagai perangkat.
(iv) Efeksibilitas yang lebih baik: Responsivitas meningkatkan aksesbilitas bagi pengguna dengan berbagai kebutuhan.

Contoh aplikasi yang sudah menerapkan responsive design adalah youtube.
Baik di dekstop maupun perangkat mobile, Youtube dapat menyesuaikan tampilan elemen-elemen.

Contoh aplikasi yang belum menerapkan responsive design adalah Brainly. Antar pengguna dapat memberikan jawaban yang bervariasi bisa menggunakan foto atau lain-lainnya sehingga ketika diakses di mobile phone. Terdapat jawaban yang tidak dapat dilihat karena kepotong dengan size di mobile phone. 

3. Perbedaan antara margin, border, dan padding serta cara penggunaannya. 
* Margin adalah bagian tepi di luar border eleemen. Margin digunakan untuk memberi jarak antara elemen HTML tanpa mempengaruhi ukutan elemen itu sendiri.
* Border adalah garis yang membungkus elemen di antara padding dan margin. Border digunakan untuk menambahkan garis pembatas di sekitar elemen dengan berbagai gaya seperti solid, dashed, dotted, dll.
* Padding adalah ruang kosong di dalam border elemen yang memberikan jarak antara konten elemen dengan border elemen tersebut. Kegunaannya adalah untuk membuat ruang di dalam elemen sehingga tidak bersentuhan langsung dengan border. 

4. Flexbox dan Grid Layout adalah dua modul layout CSS yang digunakan untuk mengatur dan menyusun elemen-elemen dalam halaman web secara efisien. 
(i) Flexbox / Flexible Box Layout 
Untuk menyusun elemen-elemen dalam satu dimensi, konsep felexbok dalam flex container adalah elemen induk yang menggunakan `display; flex;` semua elemen di dalamnya akan menjadi flex items.
(ii) Flex items 
Elemen-elemen anak yang diatur tata letaknya oleh flexbox. 
Properti dalam flexbox: `flex-direction` menentukan arah susunan elemen, `justify-content` menyusun flex items secara horizintal/vertikal, `align-items` menyusun flex items secara vertikal/horizintal, dan `flex-wrap` menentukan apakah elemen cukup untuk di-wrap dalam satu baris atau tidak. 

Grid Layout memungkinkan pengaturan elemen dalam dua dimensi (baris/kolom). Grid sangat cocok untuk tata letak kompleks di mana elemen perlu ditempatkan pada posisi spesifik. 
(i) Grid Container adalah elemen induk yang menggunakan `display: grid;`. Elemen di dalamnya adalah grid items.
(ii) Grid Items adalah elemen-elemen yang diatur dalam grid. 

Perbedaan utama Flexbox dan Grid Layout adalah
(i) Flexbox adalah lebih cocok untuk tata letak yang lebih sederhan atau ketika hanya membutuhkan pengaturan elemen dalam satu arah.
(ii) Grid Layout lebih cocok untuk membuat tata letak web yang fleksibel dan responsif.