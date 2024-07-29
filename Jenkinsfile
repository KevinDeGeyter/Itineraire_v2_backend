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
            environment {
                SECRET_FILE = credentials('SSH_PRIVATE_KEY')
            }
            steps {
                echo 'Deploying the application.'
                sh 'sshpass -p od1235jenkins ssh jenkins@${DEPLOYMENT_SERVER_HOST} "docker login -u ${USER_REGISTRY} -p ${USER_PASSWORD_REGISTRY} && docker pull ${IMAGE_NAME}:latest && docker run  ${IMAGE_NAME}:latest -d"'
            }
        }
    }
post {
        always {
            echo 'Post Always AZERTY cccc: Will always run, irrespective of success or failure'
        }
    }
}
