pipeline {
    agent any
    stages {
        stage('Check Python') {
            steps {
                bat 'where python'
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version'
                bat 'python -m pip --version'
            }
        }
        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv .virtual_env'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest tests -v'
            }
        }
        stage('Train Model') {
            steps {
                bat '.venv\\Scripts\\python.exe src\\train.py'
            }
        }
        stage('Evaluate Model') {
            steps {
                bat '.venv\\Scripts\\python.exe src\\evaluate.py'
            }
        }
        stage('Test Prediction') {
            steps {
                bat '.venv\\Scripts\\python.exe src\\predict.py'
            }
        }
        stage('Deploy Model Artifact') {
            steps {
                bat "if not exist deployed_models mkdir deployed_models\r\ncopy /Y models\\model.pkl deployed_models\\model_%BUILD_NUMBER%.pkl"
            }
        }
    }
    post {
        success {
            echo 'House-price MLOps pipeline completed successfully!'
            archiveArtifacts artifacts: 'models/*.pkl,deployed_models/*.pkl', fingerprint: true
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
