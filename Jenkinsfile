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
            post {
                success {
                    // Adding a manual approval step after successful Django tests
                    input {
                        message "Proceed with post-test actions?"
                        ok "Continue"
                    }
                }
            }
        }
    }

    post {
        always {
            // Deactivate the virtual environmentss
            sh 'deactivate || true'
        }
    }
}
