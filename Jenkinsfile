pipeline{
    agent any
    stages{
        stage('init'){
            steps{
                sh 'export PATH=$PATH:/usr/bin'
            }
        }
        stage('SCM'){
            steps{
                //pulling this line
                git branch: 'main', url: 'https://github.com/MaheshDevops0107/python_project_jenkins.git'
            }
        }
        stage('build docker image'){
            steps{
              sh 'docker build -t maheshveer152122/python-server .'  
            }

        }
        stage('Docker login'){
            steps{
                  echo 'Login to docker'
                  //sh 'echo $DOCKER_HUB_TOKEN | docker login -u maheshveer152122 --password-stdin'
                  withCredentials([string(credentialsId: 'DOCKER_HUB_TOKEN', variable: 'DOCKER_HUB_TOKEN')]) {
                    sh 'echo $DOCKER_HUB_TOKEN | docker login -u maheshveer152122 --password-stdin'
                  }
            }
          
        }
        stage('push docker image'){
            steps{
                //remove existing docker service
                sh 'docker service rm python-service'

            }
        }
        stage('push docker'){
            steps{
                sh 'docker service create --name python-service --replicas 2 -p 5000:5000 maheshveer152122/python-server'
            }
        }
    }
}
