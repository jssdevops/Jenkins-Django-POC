pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                // Run Django tests
                sh 'cd /var/lib/jenkins/workspace/my_app/myproject'
                sh 'python3 manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                // Wait for manual approval
                input 'Approve deployment to production?'
                // Deploy to production
                // ...
            }
        }
    }
}
