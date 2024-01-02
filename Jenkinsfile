pipeline {
    agent any


        stage('Build Image') {
            steps {
                // Build your Docker image
                script {
                    docker.build('my-django-app', '-f Dockerfile .')
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                // Run tests inside the Docker container
                script {
                    docker.image('my-django-app').inside {
                        sh 'python3 /var/lib/jenkins/workspace/my_app/myproject/manage.py test'
                    }
                }
            }
        }
    }
