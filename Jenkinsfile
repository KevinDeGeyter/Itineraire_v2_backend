pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the project.'
                sh 'whoami'
                sh 'pwd'
                sh 'docker ps'
                sh 'docker login -u ${USER_REGISTRY} -p ${USER_PASSWORD_REGISTRY}'
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
                sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
                }
            }
        stage('Test') {
            steps {
                echo 'Running tests.'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying the application.'
            }
        }
    }
post {
        always {
            echo 'Post Always AZERTY xx yy aa bb cc dd ff gg: Will always run, irrespective of success or failure'
        }
    }
}
