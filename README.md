# 🚀 Erajaya QA Automation Technical Assessment

Repository containing the complete Test Automation solution for **Erajaya QA Assessment**, covering manual test case design, Web UI automation, and Android Mobile automation.

---

## 📌 Assessment Overview

| Assessment Component | Target Application / Scope | Tech Stack & Framework | Location |
| :--- | :--- | :--- | :--- |
| **Soal 1: Test Case Design** | COD Payment Method Feature (C2C E-Commerce) | Manual Test Scenarios (Positive & Negative) | [`Soal 1 – Test Case (Positive & Negative).md`](./Soal%201%20–%20Test%20Case%20(Positive%20&%20Negative).md) |
| **Soal 2: Web Automation** | CURA Healthcare Service (`katalon-demo-cura.herokuapp.com`) | Python 3.12, Playwright, Pytest, Page Object Model (POM) | [`web-automation/`](./web-automation/) |
| **Soal 3: Mobile Automation** | Eraspace Android Application (`com.eraspace.app`) | Python 3.12, Appium (UiAutomator2), Pytest, Page Object Model (POM) | [`mobile-automation/`](./mobile-automation/) |

---

## 📂 Repository Architecture

```text
erajaya-qa-automation/
├── mobile-automation/                           # Android Mobile App Automation (Appium)
│   ├── config/                                  # Capabilities & Environment settings
│   ├── data/                                    # Test datasets (credentials & expected results)
│   ├── drivers/                                 # Appium driver factory & lifecycle
│   ├── pages/                                   # Page Object Model (POM) classes
│   ├── tests/                                   # Pytest automation test scripts
│   ├── reports/                                 # HTML Test execution reports
│   ├── screenshots/                             # Automated failure screenshots
│   ├── utils/                                   # Helper functions & custom waiters
│   ├── pytest.ini                               # Pytest configuration & markers
│   ├── requirements.txt                         # Mobile automation dependencies
│   ├── .env.example                             # Environment variables template
│   └── README.md                                # Detailed mobile documentation & setup guide
│
├── web-automation/                              # Web UI Test Automation (Playwright)
│   ├── config/                                  # Base URL, timeouts, and env settings
│   ├── data/                                    # Test datasets (test_data.json)
│   ├── pages/                                   # Page Object Model (BasePage, LoginPage, etc.)
│   ├── tests/                                   # Pytest automation scripts (Login & Appointment)
│   ├── reports/                                 # Auto-generated HTML execution reports
│   ├── pytest.ini                               # Pytest options, markers, and default configs
│   ├── requirements.txt                         # Web automation dependencies
│   ├── .env.example                             # Environment variables template
│   └── README.md                                # Detailed web documentation & setup guide
│
├── Soal 1 – Test Case (Positive & Negative).md  # Comprehensive test cases for COD feature
├── .gitignore                                   # Global repository ignore rules
└── README.md                                    # Root repository documentation (this file)
```

---

## 🌐 1. Web Automation (Playwright + Python)

Automated end-to-end test suite for **CURA Healthcare Service** built using **Playwright** and **Page Object Model (POM)**.

### Covered Scenarios
- **Scenario 1: Login**
  - **TC 1.1**: Login with invalid data *(verifies input values and error alert notification)*
  - **TC 1.2**: Login with valid data *(verifies successful login and redirection to Appointment page)*
- **Scenario 2: Make Appointment**
  - **TC 2.1**: Make Appointment without mandatory field *(verifies HTML5 mandatory field validation blocks submission)*
  - **TC 2.2**: Make Appointment success *(selects date from picker, fills all fields, books appointment, and validates confirmation summary details)*

### Quick Start (Web)
```bash
# Navigate to web directory
cd web-automation

# Create & activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # On Windows
# source .venv/bin/activate  # On macOS/Linux

# Install dependencies & browsers
pip install -r requirements.txt
playwright install chromium

# Run all web tests
pytest

# View generated interactive HTML report
start reports/report.html
```
👉 *For complete details, see [web-automation/README.md](./web-automation/README.md).*

---

## 📱 2. Mobile Automation (Appium + Android)

Automated mobile test suite for the **Eraspace** Android application utilizing **Appium** (UiAutomator2 driver) and **Page Object Model (POM)**.

### Quick Start (Mobile)
```bash
# Navigate to mobile directory
cd mobile-automation

# Create & activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # On Windows
# source .venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run all mobile tests
pytest
```
👉 *For complete details, see [mobile-automation/README.md](./mobile-automation/README.md).*

---

## 📝 3. Test Case Design (Fitur COD)

Documented manual test cases covering Positive and Negative scenarios for the Cash On Delivery (COD) payment method feature on a C2C e-commerce platform based on specified business requirements and acceptance criteria.

👉 *Read the full test specifications in [Soal 1 – Test Case (Positive & Negative).md](./Soal%201%20–%20Test%20Case%20(Positive%20&%20Negative).md).*

---

## ⚙️ Tech Stack & Design Patterns

- **Language**: Python 3.12
- **Testing Framework**: Pytest
- **Web Engine**: Playwright Python
- **Mobile Engine**: Appium Python Client (UiAutomator2)
- **Architecture**: Page Object Model (POM)
- **Reporting**: Pytest-HTML (with failure screenshots)
- **Data Handling**: Data-driven JSON configuration
