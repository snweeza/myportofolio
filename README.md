Nama: Nafeeza Arwatabina
NPM: 2506604573
Kelas: PBP A

# Deskripsi Website
Website portofolio pribadi yang digunakan untuk menampilkan profil, pengalaman, dan skills saya. Website ini dibuat dengan Django dan menerapkan konsep MVT untuk mengelola serta menampilkan data secara dinamis. Proyek ini menjadi media untuk mempraktikkan penggunaan Django Model, View, Template, ModelForm, database, serta fitur CRUD dan pencarian data untuk memenuhi tugas individu pada matkul Pemrograman Berbasis Aplikasi.

# Set up
1. Clone Repository -> menduplikasi seluruh konten dari repositori yang ada di GitHub ke komputer lokal
command : git clone <https://github.com/snweeza/myportofolio.git>
2. Ganti directory
command: cd myportofolio
3. cek commit terbaru
command: Git checkout <commit-terbaru>
4. Buat Virtual Environment
command: python -m venv env
5. Aktifkan
command: env\Scripts\activate
6. Install Dependencies
command: pip install -r requirements.txt
7. Migrasi data -> menerapkan format model ke database
command: python manage.py migrate
8. Jalankan server
command: python manage.py runserver
9. Development server akan dijalankan di http://127.0.0.1:8000/

### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
= Saya hanya menggunakan section dan aside, dimana section saya gunakan untuk membuat section-2 yang berisi tampilan seluruh experience dan aside saya gunakan untuk tampilan photo menjadi di samping deskripsi pada isi summary karena saya hanya menggunakan flexbox. Untuk article saat ini saya belum benar-benar memahami sebaiknya digunakan dimana, karena untuk membungkus elemen kebanyakan saya masih menggunakan div.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
= Saya mengalami banyak tantangan dan harus belajar banyak mengenai perbedaan flexbox dan grid, ukuran pixel, padding, dan margin sehingga dalam mengatur CSS untuk tetap responsive, saya masih merasa banyak kurang karena banyak fitur yang ukurannya diatur secara tetap. Dan untuk tampilan mobile, saya mengevaluasi prioritas dan komposisi yang enak dipandang dan biasanya melihat elemen yang dapat menyebabkan overflow lalu memindahkan-nya di bagian bawah. 

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
= Desain awal yang ingin saya bikin pada section 2 itu berupa sidebar dan slide yang apabila button di click maka akan pindah ke slide yang sesuai dengan idnya, disini saya menyadari kesulitan untuk membuat tampilan slider nya. Untuk selanjutnya, saya ingin menyiapkan fungsionalitas seperti itu dan menambahkan animasi/pergerakan tampilan yang saat ini belum saya tambahkan.

Deklarasi AI:
Saya mengerjakan tugas hampir sepenuhnya secara mandiri dengan belajar banyak dari berbagai macam website, trial and error, serta menemukan solusi dari beberapa permasalahan di website yang memberikan potongan kode. Saya merasa adanya keharusan untuk membangun dan mendesain sendiri agar familiar dengan seluruh elemen yang digunakan. Permasalahan yang saya hadapi kebanyakan karena saya belum paham betul struktur sehingga beberapa perubahan tidak muncul. Oleh karena itu, saya membutuhkan sangat banyak waktu saat trial dan error. Dan saat mengerjakan bagian terakhir yaitu membuat tampilan menjadi responsive, saya merasa bahwa trial dan error yang saya hadapi sebelumnya benar-benar meningkatkan pemahaman saya. Walau saat ini, saya merasa bahwa masih ada fitur yang kurang responsif pada tampilan mobile tertentu.

Saya pun tetap memanfaatkan AI Search di google untuk contoh potongan kode, penjelasan rinci mengenai perbedaan beberapa elemen html & css, dan saya menggunakan chatGPT untuk permasalahan commit di branch yang salah.

### Tugas 2
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
= Saat pengguna membuka halaman portofolio baru, browser akan mengirimkan request HTTP ke server. Request tersebut diterima oleh urls.py proyek lalu dicocokkan dengan path aplikasi yang sesuai kemudian diteruskan ke urls.py aplikasi. Selanjutnya, urls.py aplikasi akan routing path ke page melalui view. View akan menerima request lalu mengambil data yang dibutuhkan dari model. Setelah itu, view akan memanggil template dan mengirimkan context berisi data tadi.

Model sendiri merupakan representasi tabel di database yang menyimpan data aplikasi sehingga view bisa mengambil seluruh data dan dikirimkan ke template. Template bertugas merender tampilan HTML menggunakan data dari context. Di dalam-nya, Django Template Language (DTL) dipakai untuk menampilkan data yang kemudian dikirim balik ke browser sebagai HTTP response dan ditampilkan ke pengguna.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
= Agar adanya pemisahan logika antara kode pemrograman dan tampilan visual. Dengan model, data bisa ditambah, diubah, atau dihapus tanpa menyentuh kode template sama sekali. Hal ini membuat update data menjadi lebih cepat karena struktur HTML tidak ada yang perlu di edit dan data dapat divalidasi sehingga mengurangi risiko error dibandingkan dengan hardcode. Selain itu, penggunaan model juga memungkinkan data digunakan ulang di berbagai page dan aplikasi lebih mudah diskalakan karena data disimpan secara terstruktur di database.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
= makemigrations menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Lalu migrate mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan perintah sebelumnya. Pada kasus saya, penambahan field photo di experience dan pembuatan model baru yaitu tech stack membutuhkan kedua perintah tersebut.

Deklarasi AI:
Saya menggunakan DeepSeek untuk membantu saya menambahkan field photo di model experience. Awalnya saya berpikir bahwa dengan menggunakan urlfield sudah cukup tetapi photo untuk page experience merupakan photo yang berasal dari file pribadi. Oleh karena itu, saya meminta bantuan Gen AI untuk dapat menambahkan field photo. DeepSeek kemudian memberikan saya dua respon yaitu menggunakan form dan via admin. Saya pun melakukan pengecekan cakupan tugas tiga tahun lalu untuk menjadikan acuan mana yang masih cakupan tugas dua. Setelah saya telusuri, saya akhirnya memutuskan untuk meminta langkah2 yang menggunakan django admin. Deepseek merespon secara detail, mulai dari penggunaan imagefield, install pillow, hingga pembuatan superuser.

### Tugas 3
1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!
= karena modelform merupakan fitur yang telah disediakan oleh django untuk memudahkan dalam menerjemahkan kode yang telah didefinisikan di model menjadi bentuk form. Modelform ini dapat melakukan validasi secara otomatis berdasarkan aturan model dan menampilkan pesan error bawaan jika field required tidak diisi atau salah tipe data. {% csrf_token %} diwajibkan untuk ditambahkan oleh Django dalam pembuatan Form untuk memberikan perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). CSRF token memastikan bahwa request POST yang mengubah data berasal dari form yang dibuat Django, sehingga request palsu dari situs lain dapat ditolak oleh Django.

2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
= JSON lebih banyak digunakan dalam pengembangan aplikasi web modern karena ukurannya yang lebih ringkas, parser yang sangat cepat, dan integrasi yang sangat natural dengan JavaScript di sisi frontend.

3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
= fungsi view yang mengembalikan data portofolio didefinisikan dengan mengambil title query dari parameter request dan memfilter object model yang cocok dengan title query, lalu proses serialization untuk mengubah object model menjadi format JSON. Proses ini diperlukan karena object Django tidak dapat langsung dikirim sebagai response JSON. Dengan serialization, data dari object model dapat diubah menjadi struktur data yang dapat dikirim dan dibaca dalam format JSON.

Deklarasi AI:
Saya menggunakan chatGPT untuk membantu saya dalam memperbaiki CSS terutama penggunaan font yang responsive dengan clamp(), styling tombol, layout di bagian skill, dan penyesuaian tampilan untuk perangkat mobile. Output dari chatGPT tidak langsung digunakan tanpa diperiksa terlebih dahulu karena tidak semua solusi yang diberikan sesuai dengan design yang diinginkan. Selain itu, saya juga mengirimkan error message, hasil jawaban pertanyaan refleksi yang diketik sendiri untuk diperiksa dan diperbaiki kalimatnya, lalu menyusun set up project di environment lain, dan penyusunan AI log hehe.

# AI Usage Log
Dokumen ini mencatat penggunaan AI selama proses pengembangan website portfolio Django. AI digunakan sebagai alat bantu untuk memahami konsep, melakukan debugging, mengeksplorasi solusi, dan memperbaiki dokumentasi. Setiap solusi yang diberikan AI tetap diuji dan disesuaikan secara manual dengan kebutuhan project.

| Tanggal    | Prompt / Topik                                           | Bantuan AI                                                                                                                                                                                              | Perubahan yang Saya Lakukan                                                                                                                            |
| ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-09-19 | Styling skill icon dan soft-skill card                   | Membantu menyusun CSS untuk icon skill, informasi skill, soft-skill card, grid, hover effect, dan responsive layout.                                                                                    | Menguji CSS secara langsung dan mengubah ukuran icon, card, gap, serta layout karena beberapa ukuran awal terlalu besar.                               |
| 2026-09-19 | Debugging `FieldError` pada `TechStackForm`              | Membantu membaca error `Unknown field(s) (descriptionicon_url)` dan mengidentifikasi adanya kesalahan penulisan field pada `ModelForm`.                                                                 |
| 2026-09-19 | Debugging `NoReverseMatch` pada update skill             | Membantu menjelaskan bahwa URL `update_skill` membutuhkan `skill_id`, sehingga `{% url 'main:update_skill' %}` tanpa ID menyebabkan error.                                                              | Mengubah pemanggilan URL menjadi `{% url 'main:update_skill' skill.id %}` dan memastikan `skill` tersedia di context template.                         |
| 2026-09-19 | Styling tombol Update dan Batal                          | Membantu menjelaskan perbedaan default antara elemen `<button>` dan `<a>` serta cara membuat styling tombol lebih konsisten.                                                                            | Menyesuaikan CSS `.button` dan mengecek selector yang memengaruhi ukuran tombol tanpa menambahkan styling yang tidak diperlukan.                       |
| 2026-09-19 | Responsive navigation dan font                           | Menjelaskan penggunaan `clamp()` untuk membuat ukuran font responsif terhadap ukuran layar.                                                                                                             | Menggunakan `clamp()` pada beberapa bagian navigation dan menyesuaikan nilai minimum, ukuran relatif, dan maksimum sesuai desain.                      |
| 2026-09-20 | Memahami CSRF token                                      | Menjelaskan fungsi `{% csrf_token %}` dan konsep CSRF sebagai perlindungan terhadap request POST palsu dari situs lain.                                                                                 | Menambahkan `{% csrf_token %}` pada form POST untuk create, update, dan delete serta memperbaiki pemahaman mengenai tujuan CSRF.                       |
| 2026-09-20 | Setup project agar dapat dijalankan di komputer lain     | Menjelaskan hubungan antara repository, `git clone`, virtual environment, `requirements.txt`, migration, dan `runserver`.                                                                               | Menyiapkan pemahaman mengenai langkah setup project dari repository dan mempertimbangkan kebutuhan `requirements.txt`.                                 |
| 2026-09-20 | Memahami `migrate` dan database                          | Menjelaskan bahwa `migrate` menerapkan struktur/perubahan database berdasarkan migration, bukan memindahkan data dari database komputer sebelumnya.                                                     | Membedakan fungsi model, migration, `migrate`, database, dan fixture untuk dokumentasi project.                                                        |
| 2026-09-20 | AI disclosure dan dokumentasi                            | Membantu menyusun AI disclosure yang menjelaskan tools, strategi prompting, bagian yang dibantu AI, serta proses verifikasi manual.                                                                     | Membuat dokumentasi penggunaan AI secara transparan pada README dan membuat log penggunaan AI ini.                                                     |

Dengan demikian, AI digunakan sebagai tutor, brainstorming partner, dan debugging assistant, sedangkan implementasi akhir, pengujian, pemilihan solusi, dan penyesuaian dengan kebutuhan project dilakukan secara manual.