pipeline {
    agent { docker { image 'servergurus/python-3.7' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install --user flask'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
    }
}
