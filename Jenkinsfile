pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                echo 'python --version'
            }
        }
         stage('testing') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deployment') {
            steps {
                echo 'Deployment for Python version 10'
            }
        }
    }
}