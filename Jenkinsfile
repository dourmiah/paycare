pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }
    environment {
        DOCKER_IMAGE = "paycare-image:latest"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/dourmiah/paycare.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m  pip install --upgrade pip --user 
                python3 -m pip install --user -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest tests/tests.py --junitxml=results.xml'
                }
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
        // stage('Build Docker Image') {
        //     steps {
        //         script {
        //             docker.build("paycare-image:latest")
        //         }
        //     }
        // }
         stage('Build Docker Image') {
            steps {
                script{
                    sh 'docker build . -t ${DOCKER_IMAGE}'
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    sh 'docker run --rm -v "$(pwd):/home/app" ${DOCKER_IMAGE}'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully !'
            // Send email notification
        }
        failure {
            echo 'Pipeline failed.'
            // Send email notification
        }
    }
}