pipeline {
    agent any

    stages {
        stage('Run Django Test') {
            steps {
                // Run Django tests cases python
                sh '''
                        source /path/to/your/venv/bin/activate  # Activate virtual environment (if applicable)
                        export PYTHONPATH=/path/to/your/django/project:$PYTHONPATH  # Set PYTHONPATH (if needed)
                        python3 /var/lib/jenkins/workspace/my_app/myproject/manage.py test
                    '''            
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
