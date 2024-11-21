pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
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
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('paycare-image:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image('paycare-image:latest').inside {
                        sh 'pytest tests/tests.py --junitxml=results.xml'
                    }
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