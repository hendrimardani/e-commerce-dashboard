Proyek ini menggunakan dataset publik e-commerce di kaggle dan sudah deploy menggunakan streamlit sebagai dashboard yang interaktif.

## Cara Menjalankan Proyek Dashboard Streamlit

```
streamlit run dashboard.py
```

## Conclusion

### Pertanyaan 1: Produk apa yang paling banyak dan sedikit terjual ?

**Insight:**

- Kategori produk terlaris ada di kategori produk tempat tidur, sedangkan kategori produk keamanan dan layanan berada di produk terendah, ini berarti segmentasi pelanggan kita dominan belanja kategori peralatan tempat tidur dibandingkan mementingkan peralatan keamanan. Karena itu produk kategori peralatan keamanan kita bisa lakukan promosi besar-besaran agar produk ini banyak terjual, misalnya dengan menambahkan inovasi pada produk keamanan ini berbasis teknologi yang canggih ataupun melakukan diskon.

### Pertanyaan 2: Wilayah mana yang paling menguntungkan perusahaan dan paling sering melakukan transaksi ?

**Insight:**

- Pelanggan didominasi oleh wilayah SP yang melonjak tinggi dibandingkan wilayah lainnya, hampir 4 kali lipat dari wilayah RJ. Selain mendominasi Wilayah SP juga menunjukan pendapatan yang paling menguntungkan bagi perusahaan
- Pendapatan terendah didominasi oleh wilayah RR. Ini berarti wilayah RR mungkin pelosok dan jauh dari kota ataupun UMR yang sangat minim sehingga lebih mementingkan kebutuhan pokok dibandingkan belanja

### Pertanyaan 3: Kapan terakhir pelanggan melakukan transaksi ? (Recency)

**Insight:**

- Pelanggan 4a7d paling sering melakukan transaksi (langganan), sedangkan pelanggan 08c5 justru jarang melakukan transaksi ini berarti pelanggan 08c5 akan mengalami pemberhentian langganan (churn) solusi dari perspektif perusahaan bisa melakukan promosi besar-besaran pada pelanggan tersebut tujuannya untuk menghindari berhentinya langganan dan kembali menjadi aktif transaksi.

### Pertanyaan 4 : Seberapa sering seorang pelanggan melakukan transaksi ? (Frequency)

**Insight:**

- Pada Hasil visualisasi diatas, seditdaknya pelanggan memilki transaksi 1 kali baik pelanggan langganan baik pelanggan yang sering transaksi ataupun yang jarang transaksi

### Pertanyaan 5: Berapa banyak uang yang dihabiskan pelanggan dalam beberapa bulan terakhir ? (Monetary)

**Insight:**

- Pelanggan 1617 termasuk pelanggan yang paling menguntungkan bagi perusahaan, sedangkan pelanggan 9f9d dan 161d pelanggan yang pendapatannya paling rendah bagi perusahaan, ini mungkin disebabkan karena pelanggan 9f9d dan pelanggan 161d memiliki pendapatan UMR atau bahkan dibawah UMR yang hanya cukup unuk memenuhi kebutuhan pokok saja dibandingkan membeli barang baru.
