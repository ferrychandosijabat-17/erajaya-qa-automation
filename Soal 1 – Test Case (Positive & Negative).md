# Soal 1 - Test Case (Positive & Negative) Fitur COD

**User Story:**

Sebuah perusahaan mempunyai aplikasi ecommerce (C2C) yang terdiri dari beberapa tipe member yaitu silver, gold, platinum. Akan ditambahkan sebuah fitur baru yaitu COD (Cash on Delivery) di Payment Method.

**Acceptance Criteria:**
- Hanya transaksi di atas 2 juta yang dapat menggunakan fitur ini
- Fitur COD hanya dapat digunakan 1x per hari
- Hanya member platinum yang mempunyai akses untuk menggunakan COD

---

**TC-01 (Positive)**

**Description:**

Memastikan COD berhasil digunakan oleh member Platinum dengan nominal belanja di atas 2 juta untuk pertama kali pada hari ini.

**Steps:**

1. Login menggunakan akun member Platinum
2. Tambahkan produk ke dalam keranjang hingga total belanja lebih dari 2 juta
3. Navigasi ke halaman checkout
4. Pilih opsi COD
5. Klik tombol "Buat Pesanan"

**Expected Result:**

Opsi pembayaran COD tersedia, dapat dipilih, dan pesanan berhasil terbuat.

---

**TC-02 (Negative)**

**Description:**

Memastikan COD tidak dapat digunakan oleh member Platinum jika nominal belanja sama dengan atau kurang dari 2 juta.

**Steps:**

1. Login menggunakan akun member Platinum
2. Tambahkan produk ke dalam keranjang hingga sama dengan atau kurang dari 2 juta
3. Navigasi ke halaman checkout
4. Perhatikan opsi pembayaran yang tersedia

**Expected Result:**

Opsi pembayaran COD disabled atau tidak ditampilkan dan sistem menampilkan informasi jika belanja masih belum melebihi 2 juta

---

**TC-03 (Negative)**

**Description:**

Memastikan COD tidak dapat digunakan kembali oleh member Platinum yang sudah melakukan pemesanan menggunakan COD sebelumnya di hari yang sama.

**Steps:**

1. Login menggunakan akun member Platinum yang sudah sukses melakukan transaksi menggunakan COD
2. Tambahkan produk ke dalam keranjang hingga total belanja lebih dari 2 juta
3. Navigasi ke halaman checkout
4. Perhatikan opsi pembayaran yang tersedia

**Expected Result:**

Opsi pembayaran COD disabled atau tidak ditampilkan dan sistem menampilkan informasi jika sudah mencapai batas maksimal penggunaan COD harian.

---

**TC-04 (Negative)**

**Description:**

Memastikan COD tidak dapat digunakan oleh akun member Gold meskipun syarat minimum telah terpenuhi.

**Steps:**

1. Login menggunakan akun member Gold
2. Tambahkan produk ke dalam keranjang hingga total belanja lebih dari 2 juta
3. Navigasi ke halaman checkout
4. Perhatikan opsi pembayaran yang tersedia

**Expected Result:**

Opsi pembayaran COD disabled atau tidak ditampilkan.

---

**TC-05 (Negative)**

**Description:**

Memastikan COD tidak dapat digunakan oleh akun member Silver meskipun syarat minimum telah terpenuhi.

**Steps:**

1. Login menggunakan akun member Silver
2. Tambahkan produk ke dalam keranjang hingga total belanja lebih dari 2 juta
3. Navigasi ke halaman checkout
4. Perhatikan opsi pembayaran yang tersedia

**Expected Result:**

Opsi pembayaran COD disabled atau tidak ditampilkan.
