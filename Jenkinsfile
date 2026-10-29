
pipeline {
    agent any

    environment {
        DOCKERHUB_REPO = 'amalan4321/shopping-app'
    }

    stages {
        stage('Build v1') {
            steps {
                sh 'docker build -t ${DOCKERHUB_REPO}:v1 ./v1'
            }
        }

        stage('Build v2') {
            steps {
                sh 'docker build -t ${DOCKERHUB_REPO}:v2 ./v2'
            }
        }

        stage('Build v3') {
            steps {
                sh 'docker build -t ${DOCKERHUB_REPO}:v3 ./v3'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login \
                            --username "$DOCKER_USER" \
                            --password-stdin
                    '''
                }
            }
        }

        stage('Push Images') {
            steps {
                sh '''
                    docker push ${DOCKERHUB_REPO}:v1
                    docker push ${DOCKERHUB_REPO}:v2
                    docker push ${DOCKERHUB_REPO}:v3
                '''
            }
        }
    }

    post {
        success {
            echo 'All Shopping App images built and pushed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
