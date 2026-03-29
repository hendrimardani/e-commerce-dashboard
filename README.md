## Deskripsi

Dataset ini berisi informasi nyata (yang telah dianomimkan) dari sekitar 100.000 pesanan (orders) yang terjadi pada periode 2016 hingga 2018 di beberapa lokapasar (marketplace) di Brasil melalui platform Olist.

Sumber Tautan : https://www.kaggle.com/datasets/sulistiawan/e-commerce-public-dataset

## Informasi Dataset
### 1. `customers_dataset.csv` (Data Pelanggan)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `customer_id` | `object/string` | ID kunci yang terhubung dengan tabel orders. Tiap pesanan mendapat ID baru. |
| `customer_unique_id` | `object/string` | ID unik pelanggan untuk melacak pembelian berulang. |
| `customer_zip_code_prefix` | `int64` | 5 digit pertama kode pos pelanggan. |
| `customer_city` | `object/string` | Nama kota pelanggan. |
| `customer_state` | `object/string` | Nama negara bagian pelanggan (contoh: SP untuk Sao Paulo). |

<br>

### 2. `geolocation_dataset.csv` (Data Geografis)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `geolocation_zip_code_prefix` | `int64` | 5 digit pertama kode pos. |
| `geolocation_lat` | `float64` | Titik koordinat Latitude (Garis Lintang). |
| `geolocation_lng` | `float64` | Titik koordinat Longitude (Garis Bujur). |
| `geolocation_city` | `object/string` | Nama kota. |
| `geolocation_state` | `object/string` | Nama negara bagian. |

<br>

### 3. `orders_dataset.csv` (Data Induk Pesanan)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `order_id` | `object/string` | ID unik untuk setiap pesanan. |
| `customer_id` | `object/string` | ID pelanggan yang melakukan pesanan (terhubung ke tabel *customers*). |
| `order_status` | `object/string` | Status pesanan (misal: *delivered*, *shipped*, *canceled*). |
| `order_purchase_timestamp` | `datetime` | Waktu saat pesanan dibuat pelanggan. |
| `order_approved_at` | `datetime` | Waktu saat pembayaran pesanan disetujui. |
| `order_delivered_carrier_date` | `datetime` | Waktu pesanan diserahkan ke pihak logistik/kurir. |
| `order_delivered_customer_date` | `datetime` | Waktu pesanan benar-benar sampai di tangan pelanggan. |
| `order_estimated_delivery_date` | `datetime` | Estimasi tanggal pengiriman yang diinformasikan ke pelanggan. |

<br>

### 4. `order_items_dataset.csv` (Data Detail Item Pesanan)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `order_id` | `object/string` | ID pesanan. |
| `order_item_id` | `int64` | Nomor urut item di dalam satu pesanan (jika beli 3 barang, urutannya 1, 2, 3). |
| `product_id` | `object/string` | ID unik produk. |
| `seller_id` | `object/string` | ID unik penjual (*seller*). |
| `shipping_limit_date` | `datetime` | Batas waktu maksimal penjual harus menyerahkan barang ke kurir. |
| `price` | `float64` | Harga asli dari produk (item). |
| `freight_value` | `float64` | Biaya pengiriman / ongkir untuk item tersebut. |

<br>

### 5. `order_payments_dataset.csv` (Data Pembayaran)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `order_id` | `object/string` | ID pesanan. |
| `payment_sequential` | `int64` | Urutan metode bayar (jika pelanggan menggunakan lebih dari 1 metode). |
| `payment_type` | `object/string` | Metode pembayaran yang digunakan (kredit, debit, tiket, voucher). |
| `payment_installments` | `int64` | Jumlah cicilan yang dipilih. |
| `payment_value` | `float64` | Total nilai transaksi yang dibayarkan. |

<br>

### 6. `order_reviews_dataset.csv` (Data Ulasan/Review)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `review_id` | `object/string` | ID unik ulasan. |
| `order_id` | `object/string` | ID pesanan yang diberi ulasan. |
| `review_score` | `int64` | Skor ulasan berskala 1 sampai 5. |
| `review_comment_title` | `object/string` | Judul komentar ulasan (jika ada). |
| `review_comment_message` | `object/string` | Isi teks dari komentar ulasan. |
| `review_creation_date` | `datetime` | Tanggal email survei kepuasan dikirimkan ke pelanggan. |
| `review_answer_timestamp` | `datetime` | Tanggal dan waktu pelanggan mengisi ulasan tersebut. |

<br>

### 7. `products_dataset.csv` (Data Produk)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `product_id` | `object/string` | ID unik produk. |
| `product_category_name` | `object/string` | Nama kategori produk (dalam bahasa Portugis). |
| `product_name_lenght` | `float64` | Jumlah karakter dari nama produk. |
| `product_description_lenght`| `float64` | Jumlah karakter dari deskripsi produk. |
| `product_photos_qty` | `float64` | Jumlah foto produk yang dipajang. |
| `product_weight_g` | `float64` | Berat produk dalam satuan gram. |
| `product_length_cm` | `float64` | Panjang produk dalam sentimeter. |
| `product_height_cm` | `float64` | Tinggi produk dalam sentimeter. |
| `product_width_cm` | `float64` | Lebar produk dalam sentimeter. |

<br>

### 8. `sellers_dataset.csv` (Data Penjual/Mitra)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `seller_id` | `object/string` | ID unik penjual. |
| `seller_zip_code_prefix` | `int64` | 5 digit pertama kode pos lokasi penjual. |
| `seller_city` | `object/string` | Kota tempat penjual berada. |
| `seller_state` | `object/string` | Negara bagian tempat penjual berada. |

<br>

### 9. `product_category_name_translation.csv` (Kamus Translasi Kategori)

| Nama Kolom | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| `product_category_name` | `object/string` | Nama kategori dalam bahasa Portugis. |
| `product_category_name_english` | `object/string` | Nama kategori yang sudah diterjemahkan ke dalam bahasa Inggris. |

## Setup Environment - Anaconda
```python
conda create --name e-commerce python=3.13
conda activate e-commerce
pip install -r requirements.txt
```

## Menjalankan Streamlit

```python
cd dashboard
streamlit run main.py

```

## URL Streamlit
https://bxeukn9nkn3yrpp66ukzhh.streamlit.app/

## Kesimpulan

### Pertanyaan 1: Produk apa yang paling banyak dan sedikit terjual ?
<img width="1158" height="382" alt="image" src="https://github.com/user-attachments/assets/6416b9a8-4dbf-4629-8e5e-4d9f86937c16" />
<img width="1154" height="358" alt="image" src="https://github.com/user-attachments/assets/53a8d0e4-733a-4263-80d4-95eea5df601b" />

**Insight:**
- Kategori produk terlaris ada di kategori produk tempat tidur, sedangkan kategori produk keamanan dan layanan berada di produk terendah, ini berarti segmentasi pelanggan kita dominan belanja kategori peralatan tempat tidur dibandingkan mementingkan peralatan keamanan. Karena itu produk kategori peralatan keamanan kita bisa lakukan promosi besar-besaran agar produk ini banyak terjual, misalnya dengan menambahkan inovasi pada produk keamanan ini berbasis teknologi yang canggih ataupun melakukan diskon.

### Pertanyaan 2: Wilayah mana yang paling menguntungkan perusahaan dan paling sering melakukan transaksi ?
<img width="1155" height="433" alt="image" src="https://github.com/user-attachments/assets/f261ee6c-8821-45eb-a51f-99ea90ad27f0" />

**Insight:**
- Pelanggan didominasi oleh wilayah SP yang melonjak tinggi dibandingkan wilayah lainnya, hampir 4 kali lipat dari wilayah RJ. Selain mendominasi Wilayah SP juga menunjukan pendapatan yang paling menguntungkan bagi perusahaan
- Pendapatan terendah didominasi oleh wilayah RR. Ini berarti wilayah RR mungkin pelosok dan jauh dari kota ataupun UMR yang sangat minim sehingga lebih mementingkan kebutuhan pokok dibandingkan belanja

### Pertanyaan 3: Kapan terakhir pelanggan melakukan transaksi ? (Recency)
<img width="1156" height="348" alt="image" src="https://github.com/user-attachments/assets/f9d9c1cf-9a9b-4477-bf8c-04f7cb8ec003" />
<img width="1154" height="350" alt="image" src="https://github.com/user-attachments/assets/18bbe559-01ec-4dac-b678-58430b831915" />

**Insight:**
- Pelanggan 4a7d paling sering melakukan transaksi (langganan), sedangkan pelanggan 08c5 justru jarang melakukan transaksi ini berarti pelanggan 08c5 akan mengalami pemberhentian langganan (churn) solusi dari perspektif perusahaan bisa melakukan promosi besar-besaran pada pelanggan tersebut tujuannya untuk menghindari berhentinya langganan dan kembali menjadi aktif transaksi.

### Pertanyaan 4 : Seberapa sering seorang pelanggan melakukan transaksi ? (Frequency)
<img width="1157" height="348" alt="image" src="https://github.com/user-attachments/assets/912b69eb-f1c9-44a9-9f4a-c4c58395ec8d" />

**Insight:**
- Pada Hasil visualisasi diatas, seditdaknya pelanggan memilki transaksi 1 kali baik pelanggan langganan baik pelanggan yang sering transaksi ataupun yang jarang transaksi

### Pertanyaan 5: Berapa banyak uang yang dihabiskan pelanggan dalam beberapa bulan terakhir ? (Monetary)
<img width="1153" height="344" alt="image" src="https://github.com/user-attachments/assets/cb0f31c2-ad7e-4cd7-b09e-4b5cdbfbe92a" />
<img width="1159" height="351" alt="image" src="https://github.com/user-attachments/assets/c176b470-ee3e-473e-b087-92d2c8f659ec" />

**Insight:**

- Pelanggan 1617 termasuk pelanggan yang paling menguntungkan bagi perusahaan, sedangkan pelanggan 9f9d dan 161d pelanggan yang pendapatannya paling rendah bagi perusahaan, ini mungkin disebabkan karena pelanggan 9f9d dan pelanggan 161d memiliki pendapatan UMR atau bahkan dibawah UMR yang hanya cukup unuk memenuhi kebutuhan pokok saja dibandingkan membeli barang baru.
