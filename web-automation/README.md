# 🩺 CURA Healthcare Web Automation Framework

Automated test suite for **CURA Healthcare Service** (`https://katalon-demo-cura.herokuapp.com/`) built with **Playwright**, **pytest**, and the **Page Object Model (POM)** design pattern in Python.

---

## 📋 Test Scenarios Covered

### **Scenario 1: Login**
- **TC 1.1: Login with invalid data**
  - Input invalid username *(verifies input success)*
  - Input invalid password *(verifies input success)*
  - Click Login *(verifies login fails and error message alert is displayed)*
- **TC 1.2: Login with valid data**
  - Input valid username *(verifies input success)*
  - Input valid password *(verifies input success)*
  - Click Login *(verifies login success and redirection to Make Appointment homepage)*

### **Scenario 2: Make Appointment**
- **TC 2.1: Make Appointment – without input mandatory field**
  - Precondition: Login with valid data (TC 1.2)
  - Clear visit date *(verifies date is empty)*
  - Input facility, readmission, program, and comment *(verifies data input success)*
  - Click Make Appointment *(verifies browser validation on mandatory visit date and prevents form submission)*
- **TC 2.2: Make Appointment – Success**
  - Precondition: Login with valid data (TC 1.2)
  - Input all data (facility, readmission, program, visit date from picker, comment) *(verifies all data inputted)*
  - Click Make Appointment *(verifies successful appointment creation and confirms all summary details match input)*

---

## 📁 Project Architecture (Page Object Model)

```
Automation Web/
├── config/
│   ├── __init__.py
│   └── settings.py              # Base URL, timeouts, and env settings
├── data/
│   └── test_data.json           # Test data (credentials and appointment details)
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # Common Playwright actions (click, fill, wait, etc.)
│   ├── login_page.py            # Page Object for CURA Login page
│   ├── appointment_page.py      # Page Object for CURA Make Appointment page
│   └── summary_page.py          # Page Object for Appointment Confirmation page
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures and page initialization
│   ├── test_cura_login.py       # Test suite for Scenario 1 (Login)
│   └── test_cura_appointment.py # Test suite for Scenario 2 (Make Appointment)
├── reports/                     # Auto-generated HTML execution reports
├── pytest.ini                   # Pytest options, markers, and default configurations
├── requirements.txt             # Python project dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Excludes venv, cache, and report artifacts
└── README.md                    # Project documentation
```

---

## 🚀 Setup & Installation

### 1. Clone or Extract the Project
```bash
git clone <your-repository-url>
cd "Automation Web"
```

### 2. Create and Activate Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install chromium
```

---

## 🧪 Running the Tests

### Run all test suites:
```powershell
pytest
```

### Run with browser visible on screen (Headed mode):
```powershell
pytest --headed
```

### Run a specific scenario:
- **Scenario 1 (Login only):**
  ```powershell
  pytest tests/test_cura_login.py --headed
  ```
- **Scenario 2 (Appointment only):**
  ```powershell
  pytest tests/test_cura_appointment.py --headed
  ```

### Run by test markers:
- **Smoke tests:**
  ```powershell
  pytest -m smoke
  ```
- **Regression suite:**
  ```powershell
  pytest -m regression
  ```

---

## 📊 Viewing Test Reports

An interactive HTML report is automatically generated after every test run:
- Open `reports/report.html` in your web browser.
- The report contains execution duration, pass/fail status, and error logs with failure traces.

---

## 📤 Upload Instructions

### Option A: Upload to GitHub
1. Open PowerShell in this folder:
   ```powershell
   git init
   git add .
   git commit -m "feat: complete web automation test suite for CURA Healthcare"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```
*(The `.gitignore` automatically keeps `.venv`, cache, and temporary files from being uploaded).*

### Option B: Upload to Google Drive (ZIP)
To create a clean zip file without the heavy `.venv` directory:
```powershell
Compress-Archive -Path config, data, pages, tests, pytest.ini, requirements.txt, README.md, .gitignore, .env.example -DestinationPath "Automation_Web_Erajaya.zip" -Force
```
Upload the generated `Automation_Web_Erajaya.zip` to Google Drive.
