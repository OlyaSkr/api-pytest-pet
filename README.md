# 🐍 Pytest API Tests

This project contains **API tests** using `pytest` and runs inside a Python virtual environment.
It is designed to verify REST API endpoints, validate responses, and generate Allure reports for easy analysis.
The tests cover the [Petstore Swagger](https://petstore.swagger.io/v2)

---

## 📂 Project Structure

```
├── helpers/               # Helper modules for API requests, utils, etc.
├── tests/                 # Test files
│   └── test_api.py        # Example API test
├── config.py              # Project configuration (URLs, tokens, etc.)
├── conftest.py            # Pytest fixtures and hooks
├── run_tests.py           # Helper script to run tests and generate Allure results
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## ⚙️ Setup

1. **Clone the repository:**

```
git clone https://github.com/OlyaSkr/api-pytest-pet.git
cd <api-pytest-pet>
```

2. **Create virtual environment** (if not already created):

```bash
python -m venv .venv
```

3. **Activate virtual environment:**

- Windows (PowerShell):

```
.\.venv\Scripts\Activate.ps1
```

- Windows (CMD):

```
.venv\Scripts\activate.bat
```

- macOS / Linux:

```
source .venv/bin/activate
```

4. **Install dependencies:**

```
pip install -r requirements.txt
```

## 🧪 Running Tests

### 1️⃣ Run all tests normally:

```
pytest
```

### 2️⃣ Run tests with Allure report (cross-platform):

Helper script run_tests.py includes:

- 🗑️ Removing old Allure results

- 📁 Creating a new results folder

- ▶️ Running all tests

```
python run_tests.py
```

### 3️⃣ Serve Allure report

```
allure serve allure-results
```

## 📝 Notes

- ✅ Make sure Python is installed and added to your PATH.

- 🛠️ Allure CLI must be installed and added to PATH if you want to generate reports.

- 📊 API test results are stored in allure-results.
