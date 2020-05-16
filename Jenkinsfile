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
                //sh 'python test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}
