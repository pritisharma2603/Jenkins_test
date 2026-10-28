# House Price Prediction — Jenkins MLOps Practical

Beginner-friendly project inspired by the folder layout and staged Jenkins workflow in the reference repository.

## Structure
```text
house_price_jenkins/
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── tests/test_model.py
├── models/
├── deployed_models/
├── Jenkinsfile
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally on Windows
```powershell
python -m venv .venv
.venv\\Scripts\\python.exe -m pip install -r requirements.txt
.venv\\Scripts\\python.exe -m pytest tests -v
.venv\\Scripts\\python.exe src\\train.py
.venv\\Scripts\\python.exe src\\evaluate.py
.venv\\Scripts\\python.exe src\\predict.py
```

## Jenkins setup
1. Ensure the Jenkins agent has Python 3 installed and `python` available on PATH.
2. Push this project to a Git repository.
3. In Jenkins, choose **New Item** → **Pipeline**.
4. Choose **Pipeline script from SCM**, select **Git**, and enter the repository URL.
5. Set Script Path to `Jenkinsfile`, save, then click **Build Now**.
6. Check **Console Output** for each stage and the final result.

## Pipeline stages
1. Check Python
2. Create Virtual Environment
3. Install Dependencies
4. Run Tests
5. Train Model
6. Evaluate Model
7. Test Prediction
8. Deploy Model Artifact

This Jenkinsfile uses Windows `bat` commands. For Linux, replace `bat` with `sh` and adjust virtual-environment paths.

The dataset is synthetic and prices are illustrative, not suitable for real property valuation.
