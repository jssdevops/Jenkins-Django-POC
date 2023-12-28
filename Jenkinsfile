pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                // Run Django tests cases python
                sh 'python3 /var/lib/jenkins/workspace/my_app/myproject/manage.py test'
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
