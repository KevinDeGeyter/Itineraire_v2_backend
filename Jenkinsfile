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
                sh 'sshpass -p od1235jenkins scp ./docker-compose.yml jenkins@${DEPLOYMENT_SERVER_HOST}:/home/jenkins \
                && sshpass -p od1235jenkins ssh jenkins@${DEPLOYMENT_SERVER_HOST} \
                "docker login -u ${USER_REGISTRY} -p ${USER_PASSWORD_REGISTRY} \
                && docker pull ${IMAGE_NAME}:${IMAGE_TAG} \
                && export DC_IMAGE_NAME=${IMAGE_NAME} && export DC_IMAGE_TAG=${IMAGE_TAG} && export DC_APP_PORT=8501 \
                && docker compose down && docker compose up -d"'
            }
        }
    }
}
