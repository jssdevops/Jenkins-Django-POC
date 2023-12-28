// pipeline {
//     agent any

//     stages {
//         stage('install dependencies') {
//             steps {
                
//                 // Install required packages
//                 sh 'pip install -r /var/lib/jenkins/workspace/my_app/requirements.txt'
//             }
//         }

//         stage('Run Django Tests') {
//             steps {

//                 // Run Django tests
//                 sh 'python3 /var/lib/jenkins/workspace/my_app/myproject/manage.py test'
//             }
//         }
//     }

//     post {
//         always {
//             // Deactivate the virtual environment
//             sh 'deactivate || true'
//         }
//     }
// }

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
        failure {
            // If the pipeline fails, deactivate the virtual environment
            sh 'deactivate || true'
        }

        success {
            // Adding a manual approval step after successful execution
            input {
                message "Proceed with deployment?"
                ok "Deploy"
            }
        }

        // Adding a deploy stage based on manual approval
        stage('Deploy') {
            when {
                expression {
                    currentBuild.currentResult == 'SUCCESS'
                }
            }
            steps {
                // Your deployment steps here
                sh 'python3 /var/lib/jenkins/workspace/my_app/myproject/deploy.py'
            }
        }
    }
}
