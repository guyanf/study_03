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
        stage('Upload Report to GitHub') {
            steps {
                sh 'git add report.xml'
                sh 'git commit -m "Add pytest report"'
                sh 'git push origin main'
            }
        }
    }
}
