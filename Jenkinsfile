pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Ensure credentials are set in Jenkins
        DOCKER_HUB_REPO = 'zarmeenta/MLOps_Activity01'
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Pull code from GitHub
                git branch: 'main', url: 'https://github.com/zarmeenta/MLOps_Activity01.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    def image = docker.build("${DOCKER_HUB_REPO}:latest", "-f Dockerfile .")
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_HUB_CREDENTIALS) {
                        // Push the Docker image to Docker Hub
                        image.push('latest')
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Docker image successfully built and pushed to Docker Hub.'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
