# Scripted & Declarative Pipelines Demo

`Learning Resources for DevOps, SRE, Cloud & Engineering Management`

[![BINPIPE](https://img.shields.io/badge/BINPIPE-YouTube-red)](https://www.youtube.com/channel/UCPTgt4Wo0MAnuzNEEZlk90A)
[![Learn DevOps!](https://img.shields.io/badge/BINPIPE-Learn--DevOps-orange)](https://github.com/BINPIPE/resources/blob/master/devops-lesson-plans.md)
[![BINPIPE](https://img.shields.io/badge/Live--Classroom-blue)](https://forms.gle/tDJxDyj2nJyfsgsk7)
---


## Prerequisites
Run the below prerequisites on Jenkins (one-time task) to be able to handle the Python commands:

```
sudo apt update
sudo apt install python3-pip
pip3 install xmlrunner

- Apart from the above, install the Blue-Ocean plugin in Jenkins to be able to view the Junit Test Reports. We assume that Docker is already installed in the Jenkins server.
```

**A demonstration of Scripted Pipeline with Stages to run a Python script**

```
node('master') {
 stage('Source') {
  git 'https://github.com/BINPIPE/scripted-and-declarative-pipeline-demo.git'
 }
 stage('Build') {
  sh 'docker build -t flask-app:latest .'
 }

 stage('Test') {
  sh 'python3 test.py'
 }

}

```

Choose the Pipeline option while creating the Jenkins job and add the below code in the script window. Alternatively, use the Jenkinsfile-Scripted in the repository to avail the pipelinescript. Follow the video for other details of execution:

<hr>

**A demonstration of Declarative Pipeline with Stages to run a Python script**

Choose the Pipeline option while creating the Jenkins job and add the below code in the script window. Alternatively, use the Jenkinsfile-Declarative in the repository to avail the pipelinescript. Follow the video for other details of execution:

```
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
                sh 'docker rm -f flask-app || true'
                sh 'docker run -d -p 5000:5000 --name flask-app flask-app:latest'
                sh 'echo "Check App at http://ip-address:5000/"'

              }
        }    
        
    }     
}

```

<pre>
<a href="https://www.binpipe.org">BINPIPE</a> aims to simplify learning for those who are looking to make a foothold in the industry.
Write to me at <b>nixgurus@gmail.com</b> if you are looking for tailor-made training sessions.
For self-study resources look around in this repository, <a href="https://www.binpipe.org/">the Binpipe Blog</a> and <a href="https://www.youtube.com/channel/UCPTgt4Wo0MAnuzNEEZlk90A">Youtube Channel</a>.
</pre>

___
:ledger: Maintainer: **[Prasanjit Singh](https://www.linkedin.com/in/prasanjit-singh)** | **www.binpipe.org**
___

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
