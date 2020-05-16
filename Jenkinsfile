pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('test') {
            steps {
                sh 'python3 test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}
