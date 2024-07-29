pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project.'
                sh 'pwd'
                sh 'ls -al'
                sh 'docker ps'
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
            echo 'Post Always AZERTY xx: Will always run, irrespective of success or failure'
        }
    }
}
