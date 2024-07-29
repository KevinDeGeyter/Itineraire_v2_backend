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
                sh 'ssh -o StrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY} jenkins@${DEPLOYMENT_SERVER_HOST} "docker login -u ${USER_REGISTRY} -p ${USER_PASSWORD_REGISTRY} && docker pull ${IMAGE_NAME}:latest && docker run  ${IMAGE_NAME}:latest -d"'
            }
        }
    }
post {
        always {
            echo 'Post Always AZERTY bbbb: Will always run, irrespective of success or failure'
        }
    }
}
