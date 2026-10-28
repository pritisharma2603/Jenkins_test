
pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('house_price_jenkins_reference_style') {
                    bat '..\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Train Model') {
            steps {
                dir('house_price_jenkins_reference_style') {
                    bat '..\\.venv\\Scripts\\python.exe src\\train.py'
                }
            }
        }
    }
}
