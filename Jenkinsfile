pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/guyanf/study_03.git', branch: 'main'
            }
        }
        stage('Setup Virtualenv and Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    ./venv/bin/pytest tests/ --junitxml=report.xml
                '''
            }
        }
        stage('Publish Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
