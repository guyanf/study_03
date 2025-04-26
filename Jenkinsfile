pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/guyanf/study_03.git', branch: 'main'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=report.xml'
            }
        }
        stage('Publish Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
