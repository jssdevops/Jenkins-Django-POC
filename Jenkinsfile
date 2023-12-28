pipeline {
    agent any

    stages {
        stage('install dependencies') {
            steps {
                
                // Install required packages
                sh 'pip install -r /var/lib/jenkins/workspace/my_app/requirements.txt'
            }
        }

        stage('Run Django Tests') {
            steps {

                // Run Django tests
                sh 'python3 /var/lib/jenkins/workspace/my_app/myproject/manage.py test'
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

