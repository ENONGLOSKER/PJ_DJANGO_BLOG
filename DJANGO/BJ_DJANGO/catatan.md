01 MEMBUAT DAN MENJALANKAN  ENV
python -m venv env
env\Scripts\activate

02 INSTALL DJANGO
pip install django

03 MEMBUAT PROJECT 
django-admin startproject mysite

STRUKTUR FOLDER
Direktori mysite/ adalah root direktori yang berisi seluruh file dari project. Nama direktori ini bisa diganti dengan apa saja, karena tidak akan jadi masalah bagai Django.
File manage.py adalah program untuk mengelola project Django. saat ingin melakukan sesuatu terhadap project, misalnya: menjalankan server, melakukan migrasi, menciptakan sesuatu, dll.
File mysite/__init__.py adalah sebuah file kosong yang menyatakan direktori ini adalah sebuah paket (python package).
File mysite/settings.py adalah tempat kita mengkonfigurasi project.
File mysite/urls.py adalah tempat kita mendeklarasikan URL.
File mysite/wsgi.py adalah entri point untuk WSGI-compatible

-CARA KERJA DJANGO : HTTP REQUEST -> URL -> VIEWS -> (MODEL*jika butuh data) -> TEMPLATES -> HTTP RESPONSE

04 MENJALANKAN DAN MIGRASI SERVER 
python manage.py runserver
python manage.py migrate

05 MEMBUAT SUPER USER
python manage.py createsuperuser

06 LOGIN ADMIN
http://127.0.0.1:8000/admin

07 MEMBUAT APPS
python manage.py startapp blog