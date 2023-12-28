pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment') {
            steps {
                // Install virtualenv if not already installed
                sh 'pip install virtualenv'

                // Create a virtual environment
                sh 'virtualenv venv'

                // Activate the virtual environment
                sh 'source venv/bin/activate'
                
                // Install required packages
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Django Tests') {
            steps {
                // Activate the virtual environment
                sh 'source venv/bin/activate'

                // Run Django tests
                sh 'python manage.py test'
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

