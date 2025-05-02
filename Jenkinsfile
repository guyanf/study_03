pipeline {
    agent any


    environment {
        IMAGE_NAME = 'study_03_app'
        CONTAINER_NAME = 'study_03_container'
    }

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
        // stage('Upload Report to GitHub') {
        //     steps {
        //         sh 'git add report.xml'
        //         sh 'git commit -m "Add pytest report"'
        //         sh 'git push origin main'
        //     }
        // }  

        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/guyanf/study_03.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        // stage('Run Docker Container') {
        //     steps {
        //         script {
        //             docker.image("${IMAGE_NAME}").run('-d --name ${CONTAINER_NAME} -p 5000:5000')
        //         }
        //     }
        // }
    }

    // post {
    //     always {
    //         echo 'Pipeline execution completed.'
    //     }
    // }

    
}
