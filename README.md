# 🏢 Enterprise E-Commerce Microservices Target Repository

This directory contains a **production-quality multi-module Enterprise Microservices Backend Application** engineered to test and demonstrate **ALL 10 MCP SERVER TOOLS** in DevOps AI Agent.

---

## 🏗️ Repository Project Structure

```text
demo_repo_setup/
├── setup.py                    # Editable setuptools configuration (pip install -e .)
├── pyproject.toml              # Pytest configuration (pythonpath = ".")
├── conftest.py                 # Pytest sys.path root path configuration
├── sample_requirements.txt     # Production dependencies (PyYAML 5.1, Requests 2.31.0, FastAPI 0.110)
├── sample_workflow.yml         # GitHub Actions CI workflow
├── app/                        # Main Application Package
│   ├── __init__.py
│   ├── models/                 # Domain Data Models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── order.py
│   │   └── payment.py
│   └── services/               # Microservices Business Logic
│       ├── __init__.py
│       ├── auth_service.py     # Authentication & JWT validation
│       ├── payment_service.py  # Payment Gateway & Promo Code calculations
│       └── order_service.py    # Order Fulfillment & Shipping Label Generator
└── tests/
    ├── __init__.py
    └── test_services.py        # Automated Pytest suite
```

---

## 🎯 How This Repository Tests ALL 10 MCP Tools

| # | MCP Tool | How This Target Repo Tests & Exercises Tool |
|---|:---|:---|
| 1 | **`get_build_status`** | Fetches live GitHub Actions run status (`completed`, `failure`, `run_id`). |
| 2 | **`get_build_logs`** | Extracts exact failure traceback snippet from workflow log archive. |
| 3 | **`get_recent_commits`** | Fetches git commits, author names, and timestamps for correlation. |
| 4 | **`check_dependency_vulnerabilities`** | Scans `requirements.txt` containing `pyyaml==5.1` against Google OSV.dev for **`CVE-2020-14343`** (Critical RCE). |
| 5 | **`get_package_info`** | Queries PyPI registry for latest safe release (`pyyaml==6.0.3`). |
| 6 | **`check_service_status`** | Checks operational health of GitHub Actions & Cloud APIs. |
| 7 | **`search_error_kb`** | Queries ChromaDB RAG Vector Store ($0 API cost) for matched error signatures (`AttributeError: 'NoneType'`). |
| 8 | **`get_past_incidents`** | Queries SQLite database for historical outages in `order-service`. |
| 9 | **`log_new_incident`** | Prompts operator for human **`y/n`** approval before logging new incident. |
| 10 | **`get_weather_by_ip`** | Retrieves live IP location & weather telemetry via Open-Meteo REST API. |

---

## 🚀 Setup Instructions (Fresh Target Repository)

```bash
git init
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/demo-target-repo.git

# Copy all files from demo_repo_setup/
cp /path/to/demo_repo_setup/setup.py ./setup.py
cp /path/to/demo_repo_setup/pyproject.toml ./pyproject.toml
cp /path/to/demo_repo_setup/conftest.py ./conftest.py
cp /path/to/demo_repo_setup/sample_requirements.txt ./requirements.txt
cp -r /path/to/demo_repo_setup/app ./app
cp -r /path/to/demo_repo_setup/tests ./tests

# Copy GitHub Actions CI Workflow
mkdir -p .github/workflows
cp /path/to/demo_repo_setup/sample_workflow.yml .github/workflows/ci.yml

# Push to main branch
git add .
git commit -m "Initial commit of Enterprise E-Commerce Microservices backend"
git branch -M main
git push -u origin main
```
