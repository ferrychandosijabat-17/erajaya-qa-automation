# Automation Script Mobile - Eraspace Apps (Erajaya Pre-Test QA)

Repository otomatisasi pengujian mobile Android untuk aplikasi **Eraspace** menggunakan **Appium (UiAutomator2)**, **Python**, dan **Pytest** dengan implementasi **Page Object Model (POM)**.

Proyek ini dirancang untuk menjawab **Soal 3 – Automation Script Mobile** dan dioptimalkan agar dapat dijalankan pada **Virtual Device** (Android Virtual Device / AVD Emulator, Genymotion, BlueStacks) maupun Real Device.

---

## 📋 Test Scenarios & Traceability Matrix

### Scenario 1: Login

| TC ID | Test Case Description | Test Steps | Expected Result | Automation Test Method |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | Login with invalid data | 1. Input invalid username<br>2. Input invalid password<br>3. Klik Login | 1. Data berhasil terinput<br>2. Data berhasil terinput<br>3. 1. Login gagal, 2. Tampil pesan error | `test_tc_1_1_login_with_invalid_data` |
| **1.2** | Login with valid data | 1. Input valid username<br>2. Input valid password<br>3. Klik Login | 1. Data berhasil terinput<br>2. Data berhasil terinput<br>3. 1. Login success, 2. Redirect ke homepage, 3. Menampilkan list menu, 4. Menampilkan nama akun, 5. Menampilkan list point | `test_tc_1_2_login_with_valid_data` |

---

## 🏛️ Project Architecture (Page Object Model)

```
Automation Mobile Android/
├── config/
│   ├── __init__.py
│   ├── config.py             # Pengaturan konfigurasi, env, dan timeout
│   └── capabilities.py       # Pengaturan UiAutomator2 capabilities untuk Virtual Device
├── data/
│   └── test_data.json        # Data uji (kredensial valid & invalid, expected values)
├── drivers/
│   ├── __init__.py
│   └── driver_factory.py     # Inisialisasi dan lifecycle Appium driver
├── pages/
│   ├── __init__.py
│   ├── base_page.py          # Wrapper explicit wait, tap, typing, screenshot, scroll
│   ├── login_page.py         # Locators & aksi pada halaman Login Eraspace
│   └── home_page.py          # Locators & verifikasi homepage, menu list, akun, & poin
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Pytest fixtures, driver setup/teardown, report hook
│   └── test_login.py         # Test script untuk TC 1.1 dan TC 1.2
├── utils/
│   ├── __init__.py
│   └── logger.py             # Formatter logging console dan file
├── reports/                  # Direktori output HTML test report
│   └── .gitkeep
├── screenshots/              # Direktori output otomatis screenshot jika test gagal
│   └── .gitkeep
├── .env.example              # Template variabel lingkungan
├── .gitignore                # File filter git
├── pytest.ini                # Konfigurasi Pytest & HTML reporting
├── requirements.txt          # Dependensi Python
└── README.md                 # Dokumentasi proyek
```

---

## 📱 Panduan Setup Virtual Device (Android Emulator)

Framework ini mendukung berbagai virtual device Android:

### Opsi A: Android Studio Emulator (AVD - Disarankan)
1. Buka **Android Studio** -> Masuk ke **Device Manager / Virtual Device Manager**.
2. Klik **Create Device** (contoh: Pixel 6 / Pixel 7 dengan Android 12.0 atau 13.0, Google Play Image).
3. Jalankan virtual device (Device id default: `emulator-5554`).
4. Verifikasi device terdeteksi di terminal:
   ```bash
   adb devices
   ```
   *Output contoh:*
   ```
   List of devices attached
   emulator-5554    device
   ```

### Opsi B: Genymotion / BlueStacks
1. Buka Genymotion atau BlueStacks (aktifkan Android Debug Bridge / ADB pada menu Settings).
2. Hubungkan ADB jika menggunakan BlueStacks:
   ```bash
   adb connect 127.0.0.1:5555
   adb devices
   ```

### Install Aplikasi Eraspace ke Virtual Device
- Unduh APK Eraspace resmi dari Google Play Store pada virtual device atau transfer file `.apk`:
  ```bash
  adb install eraspace.apk
  ```

---

## ⚙️ Persiapan & Instalasi

### 1. Prasyarat Sistem
- **Python 3.10+** terinstall.
- **Node.js** (LTS) terinstall.
- **Java JDK 11 atau 17** terinstall (untuk Appium UiAutomator2 driver).
- **Android SDK & platform-tools (`adb`)** terdaftar di PATH.

### 2. Install Appium Server & UiAutomator2 Driver
Buka terminal / PowerShell dan jalankan:
```bash
npm install -g appium
appium driver install uiautomator2
```
Cek instalasi driver:
```bash
appium driver list --installed
```

### 3. Setup Virtual Environment Python & Dependencies
Di dalam folder proyek `Automation Mobile Android`:
```powershell
# Buat virtual environment
python -m venv .venv

# Aktifkan virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Install seluruh dependencies
pip install -r requirements.txt
```

### 4. Konfigurasi Environment (`.env`)
Salin file `.env.example` menjadi `.env`:
```powershell
copy .env.example .env
```
Sesuaikan nilai di dalam `.env` jika diperlukan:
```env
APPIUM_SERVER_URL=http://127.0.0.1:4723
PLATFORM_NAME=Android
PLATFORM_VERSION=13.0
DEVICE_NAME=Android Emulator
UDID=emulator-5554
AUTOMATION_NAME=UiAutomator2
APP_PACKAGE=com.eraspace.app
APP_ACTIVITY=com.eraspace.app.presentation.SplashScreenActivity
NO_RESET=true
```

---

## 🚀 Menjalankan Pengujian

### 1. Jalankan Appium Server
Buka terminal baru dan jalankan:
```bash
appium
```
*Appium server akan berjalan pada port default `http://127.0.0.1:4723`.*

### 2. Jalankan Virtual Device
Pastikan Virtual Device (AVD / Emulator) sudah aktif dan status `device` muncul saat menjalankan `adb devices`.

### 3. Jalankan Test Automation Script
Buka terminal proyek (dengan `.venv` aktif):

- **Menjalankan Seluruh Skenario:**
  ```powershell
  pytest
  ```

- **Menjalankan TC 1.1 (Login with invalid data):**
  ```powershell
  pytest -k test_tc_1_1_login_with_invalid_data
  ```

- **Menjalankan TC 1.2 (Login with valid data):**
  ```powershell
  pytest -k test_tc_1_2_login_with_valid_data
  ```

- **Menjalankan dengan Custom HTML Report:**
  ```powershell
  pytest --html=reports/report.html --self-contained-html
  ```

Laporan HTML dapat dibuka di browser pada file [reports/report.html](reports/report.html).

---

## 📤 Langkah Push ke GitHub Repository

Sesuai instruksi soal: *"Tuliskan GitHub-nya"*, ikuti langkah berikut untuk mengunggah proyek ke GitHub:

1. Buat repository baru di GitHub (misal: `erajaya-mobile-automation-eraspace`).
2. Jalankan perintah git pada root direktori proyek:
   ```powershell
   git init
   git add .
   git commit -m "feat: complete mobile automation framework for Eraspace login scenario using Appium & Pytest"
   git branch -M main
   git remote add origin https://github.com/<USERNAME-ANDA>/<NAMA-REPO-ANDA>.git
   git push -u origin main
   ```
3. Salin URL GitHub tersebut ke lembar jawaban pre-test Anda.
