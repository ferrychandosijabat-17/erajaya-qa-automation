# Erajaya QA Automation Test Repository (Eraspace)

This repository contains the end-to-end Test Automation Framework for **Eraspace** applications (Mobile & Web), built with Python, Pytest, and Page Object Model (POM).

---

## 📂 Repository Structure

```
├── mobile-automation/       # Android Mobile App Automation (Appium + UiAutomator2)
│   ├── config/              # Capabilities & Environment settings
│   ├── data/                # Test datasets (credentials & expected results)
│   ├── drivers/             # Appium driver factory & lifecycle
│   ├── pages/               # Page Object Model (POM) classes
│   ├── tests/               # Pytest automation scripts (TC 1.1 & TC 1.2)
│   ├── reports/             # HTML Test execution reports
│   ├── screenshots/         # Automated failure screenshots
│   ├── .env.example          # Environment variables template
│   ├── pytest.ini           # Pytest configuration
│   ├── requirements.txt     # Python dependencies
│   └── README.md            # Detailed Mobile Automation documentation
│
└── web-automation/          # Web UI Automation (Selenium / Playwright)
    └── README.md            # Web Automation documentation
```

---

## 📱 Mobile Test Automation

For complete instructions on running the **Mobile Automation Test Suite (Android Appium UiAutomator2)**, please see:
👉 **[Mobile Automation Documentation](mobile-automation/README.md)**

### Quick Start (Mobile Automation)
```powershell
cd mobile-automation

# Setup virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Start Appium in a separate terminal:
appium

# Run mobile test scenarios:
pytest --html=reports/report.html --self-contained-html
```

---

## 🌐 Web Test Automation

For instructions on running the **Web Automation Test Suite**, please see:
👉 **[Web Automation Documentation](web-automation/README.md)**

---

## 📄 Test Execution Reports
Generated HTML test reports are located inside `mobile-automation/reports/report.html`.
