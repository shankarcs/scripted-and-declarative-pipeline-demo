pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        
        
        stage('Test') {
            steps {
                sh 'python3 test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
        
        stage('Approve Deployment') {
            input{
                 message "Do you want to proceed for deployment?"
                    }
            steps {
                sh 'echo "Deploying into Server"'
                sh 'docker run -d -p 5000:5000 flask-app:latest'
                sh 'echo "Check App at http://ip-address:5000/"'

              }
        }     
}
