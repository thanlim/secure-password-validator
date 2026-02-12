# Secure Password Validator

A small Python project demonstrating secure coding practices, automated testing with **pytest**, and continuous integration with **GitHub Actions**.  
The project validates password strength using secure validation rules and integrates automated security scanning using **Bandit** as part of the CI pipeline.

---

## Features

- Validates password strength based on secure criteria:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- Automated unit tests using **pytest**
- CI pipeline using **GitHub Actions**
- Security scanning using **Bandit**

---

## Requirements

- Python 3.9+
- `pip`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/secure-password-validator.git
cd secure-password-validator

2. Create and activate a virtual environment:

python -m venv venv


Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt

Usage

To validate a password manually:

from app.validator import validate_password

print(validate_password("Secure123!"))  # True
print(validate_password("weak"))        # False

Running Tests
pytest

Security Scan

This project includes Bandit for static security analysis:

bandit -r app/

CI Pipeline (GitHub Actions)

This repository includes a GitHub Actions workflow (.github/workflows/ci.yml) that automatically:

Installs dependencies

Runs pytest tests

Runs Bandit security scan

The pipeline runs on every push and pull request to the main branch.

Contributing

Contributions are welcome.
Please open a pull request or create an issue for enhancements or bug fixes.

License

This project is open-source and available for reuse.
