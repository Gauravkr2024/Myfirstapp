pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.build('your-docker-image-name')
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('your-docker-image-name').push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    kubernetesDeploy(
                        kubeconfigId: 'your-kubeconfig-credentials',
                        configs: 'path/to/kubeconfig/file',
                        enableConfigSubstitution: true
                    )
                }
            }
        }
    }
}
