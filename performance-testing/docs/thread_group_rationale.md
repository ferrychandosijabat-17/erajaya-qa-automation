# Justifikasi & Rationale Pemilihan Parameter Thread Group

Dokumen ini menjelaskan alasan pemilihan **Thread Count**, **Ramp-Up**, dan **Loop/Duration** untuk setiap skenario pengujian performa pada aplikasi **DemoQA Book Store**, sesuai dengan kaidah *Performance Engineering*.

---

## 1. Ringkasan Matriks Skenario

| No | Skenario | Thread Count (Users) | Ramp-Up Time | Durasi / Loop | Tujuan Pengujian |
|---|---|---|---|---|---|
| 1 | **Baseline Test** | 1 User | 1 detik | 5 Iterasi | Validasi alur skrip, korelasi, assertion, dan response time dasar (ideal). |
| 2 | **Load Test (Small)** | 10 Users | 20 detik (2s/user) | 300 detik (5 min) | Mengukur stabilitas sistem pada beban awal, throughput, dan error rate. |
| 3 | **Load Test (Medium)** | 50 Users | 50 detik (1s/user) | 600 detik (10 min) | Mengamati stabilitas sistem dan deteksi awal degradasi performa. |
| 4 | **Load Test (Peak)** | 100 Users | 100 detik (1s/user) | 600 detik (10 min) | Menguji kapasitas 100 concurrent users dan menganalisis kegagalan transaksi. |
| 5 | **Ramp-Up / Stress Test** | 100 Users | 60 detik (Agresif) | 300 detik (5 min) | Mendorong sistem dengan cepat ke beban tinggi guna mendeteksi titik jenuh (*breaking point*). |
| 6 | **Soak Test (Endurance)** | 25 Users (25% peak) | 60 detik | 1800 detik (30 min) | Mendeteksi akumulasi kebocoran memori (*memory leak*) dan degradasi bertahap. |

---

## 2. Rationale & Alasan Pemilihan Parameter

### Skenario 1: Baseline (1 User, 5 Iterasi)
- **Thread Count (1 User)**: Mengisolasi pengujian tanpa ada persaingan resource (*resource contention*).
- **Ramp-Up (1 detik)**: Hanya ada 1 thread, sehingga tidak membutuhkan waktu *pacing/staggering*.
- **Loop (5 Iterasi)**: Memberikan sampel pengujian yang cukup untuk menyingkirkan efek *warm-up* iterasi pertama (koneksi SSL handshake pertama kali biasanya lebih lambat), sehingga diperoleh baseline Response Time yang valid dan stabil.

### Skenario 2: Load Test 10 Users
- **Thread Count (10 Users)**: Beban awal (*concurrency level 1*) untuk memastikan multi-user flow berjalan mulus tanpa race condition atau database lock.
- **Ramp-Up (20 detik)**: Mengalokasikan jeda 2 detik per user ($20\text{ detik} / 10\text{ users} = 2\text{ detik/user}$). Ini mencegah fenomena *thundering herd* (semua user menabrak endpoint Login secara bersamaan).
- **Durasi (300 detik / 5 menit)**: Durasi 5 menit memberikan jendela waktu stabil (*steady state*) sekitar 4.5 menit setelah ramp-up selesai, cukup untuk mengukur *Throughput* (TPS) dan rata-rata *Response Time*.

### Skenario 3: Load Test 50 Users
- **Thread Count (50 Users)**: Titik tengah beban (50% dari target puncak). Menguji ketahanan thread pool web server dan koneksi pool database.
- **Ramp-Up (50 detik)**: Mengalokasikan 1 detik per user agar beban naik secara bertahap dan linear.
- **Durasi (600 detik / 10 menit)**: Jendela waktu pengamatan 10 menit penting untuk melihat apakah throughput konstan atau mulai menurun seiring antrean request bertambah.

### Skenario 4: Load Test 100 Users
- **Thread Count (100 Users)**: Sesuai requirement kapasitas target konkurensi maksimum yang diujikan.
- **Ramp-Up (100 detik)**: Menggunakan pola kenaikan 1 user per detik. Pola ini realistis untuk trafik e-commerce normal (kenaikan bertahap, bukan *flash traffic* mendadak).
- **Durasi (600 detik / 10 menit)**: Memberikan waktu ~8.3 menit pada *peak concurrency* penuh (100 users aktif bersamaan) untuk menganalisis error rate (HTTP 5xx / 429), timeout, serta p90/p95/p99 response time.

### Skenario 5: Ramp-Up / Stress Test (100 Users, Ramp-Up 60s)
- **Thread Count (100 Users)**: Target konkurensi agresif.
- **Ramp-Up (60 detik)**: Sesuai requirement soal ("60 detik"). Dibandingkan skenario Load Test (100 detik), ramp-up 60 detik memberikan laju akselerasi beban 1.67 user/detik. Hal ini bertujuan untuk menguji respon autoscale atau resiliensi server terhadap lonjakan trafik yang mendadak.
- **Durasi (300 detik)**: Durasi singkat namun intensif untuk mengidentifikasi apakah server mengalami degradasi tajam atau recovery setelah lonjakan.

### Skenario 6: Soak Test (25 Users, Durasi 30–60 Menit)
- **Thread Count (25 Users)**: Dipilih 25% dari beban puncak (100 users), berada di rentang 20–30% rekomendasi standar industri.
- **Ramp-Up (60 detik)**: Cepat mencapai kondisi steady state karena fokus soak test adalah jangka panjang.
- **Durasi (1800 detik / 30 menit)**: Memungkinkan pengamatan tren pemakaian memori server, pelepasan koneksi database, dan garbage collection over time guna membuktikan tidak adanya *memory leak* atau *resource exhaustion*.

---

## 3. Think Time & Realistis User Behavior

Sesuai requirement wajib:
> *"Timer (think time realistis, bukan tanpa jeda)"*

Pada skrip `BookStore_Master_TestPlan.jmx`, kami menerapkan **Gaussian Random Timer** di setiap langkah transaksi:
- **Login**: Delay 1500ms, Deviation 500ms (1.0 – 2.0 detik)
- **Browse Catalog**: Delay 2000ms, Deviation 500ms (1.5 – 2.5 detik untuk membaca daftar buku)
- **Select Book Detail**: Delay 1500ms, Deviation 500ms (1.0 – 2.0 detik untuk melihat deskripsi buku)
- **Add Book**: Delay 1500ms, Deviation 500ms (1.0 – 2.0 detik untuk memutuskan membeli/menambah)
- **Cleanup**: Delay 1000ms, Deviation 300ms

**Alasan**: Tanpa think time, virtual user akan membombardir server seperti bot DoS, menghasilkan angka throughput yang tidak realistis dan memicu false error akibat rate limiting aplikasi target.
