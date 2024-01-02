pipeline {
    agent any

    stages {


        stage('Build Docker Image') {
            steps {
                // Build your Docker image
                script {
                    docker.build 'my-django-app'
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                // Run Django tests inside the Docker container
                script {
                    docker.image('my-django-app').inside('-v /var/lib/jenkins/workspace/my_app:/app') {
                        sh 'python3 /app/myproject/manage.py test'
                    }
                }
            }
        }
    }

    post {
        always {
            // Deactivate the virtual environment
            sh 'deactivate || true'
        }
    }
}
