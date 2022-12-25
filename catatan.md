# CARA MEMBUAT FILE GITIGNORE
Buat Repository di github anda
Clone Repositori anda ke PC anda
buat file .gitignore pada repository yang baru anda clone
buka file .gitignore anda pada text editor
kemudian definisikan file-file atau folder yang akan anda abaikan ketika anda mau push project anda ke repository
contoh mendefinisikan file dan folder pada .gitignore :

/* mendefinisikan folder test dengan semua file didalamnya */

test/*

/* mendefinisikan file index.php */

index.php

/* mendefinisikan semua file yang berextensi .txt */

*.txt

# CARA MEMBUAT VIRTUAL ENV

python -m pip install virtualenv
python -m venv env