"""
run_tests.py

Cross-platform script to run API tests with pytest and generate Allure reports.

Features:
- Deletes old Allure results before running tests
- Creates a new results folder
- Runs pytest and outputs results to 'allure-results'
- Serves interactive Allure report if Allure CLI is installed and in PATH

Usage:
1. Activate your virtual environment.

2. Run the script:
   python run_tests.py

Requirements:
- Python
- pytest installed in the virtual environment
- Optional: Allure CLI in PATH for serving reports
"""
import os
import shutil
import subprocess
import sys

results_dir = "allure-results"

if os.path.exists(results_dir):
    print(f"🗑️ Removing old results: {results_dir}")
    shutil.rmtree(results_dir)

os.makedirs(results_dir, exist_ok=True)

print("▶️ Running pytest...")
subprocess.run(
    [
        sys.executable,
        "-m",
        "pytest",
        f"--alluredir={results_dir}"
    ],
    check=True
)

try:
    print("🌐 Serving Allure report...")
    subprocess.Popen(["allure", "serve", results_dir])
except FileNotFoundError:
    print("⚠️ Allure CLI not found in PATH. Skipping report serve.")
    print("Install Allure and add it to PATH to view the report.")
