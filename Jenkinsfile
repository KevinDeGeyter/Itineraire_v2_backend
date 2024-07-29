pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project.'
                sh 'whoami'
                sh 'pwd'
                sh 'ls -al'
                sh 'docker ps'
                sh 'docker login -u ${USER_REGISTRY} -p ${USER_PASSWORD_REGISTRY}'
                }
            }
        stage('Test') {
            steps {
                echo 'Running tests.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application.'
            }
        }
    }
post {
        always {
            echo 'Post Always AZERTY xx yy aa bb cc: Will always run, irrespective of success or failure'
        }
    }
}
