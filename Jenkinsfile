pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project.'
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
            echo 'Will always run, irrespective of success or failure'
        }
    }
}
