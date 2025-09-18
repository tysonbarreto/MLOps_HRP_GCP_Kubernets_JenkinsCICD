pipeline{
    agent any
    environment{
        GCP_PROJECT = "mlopshrp"
    }
    stages{
        stage('Clonning GitHub Repo to Jenkins'){
            steps{
                script{
                    echo 'Clonning GitHub Repo to Jenkins...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-jenkins', url: 'https://github.com/tysonbarreto/MLOps_HRP_GCP_Kubernets_JenkinsCICD.git']])
                }
            }
        }
        stage('Setting up Virtual Environment and Installing Dependencies'){
            steps{
                script{
                    echo 'Setting up Virtual Environment and Installing Dependencies...'
                    sh "gcloud --version"
                    sh "python -m pip install --break-system-packages -U uv"
                    sh "python -m uv venv --python 3.11"
                    sh "python -m uv sync"
                }
            }
        }
        stage('Building and Pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    scripts{
                        echo 'Building and Pushing Docker image to GCR...'
                        sh """
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker
                        docker build -t gcr.io/${GCP_PROJECT}/mlopshrp:latest .
                        docker push gcr.io/${GCP_PROJECT}/mlopshrp:latest
                        """
                    }

                }
            }
        }
        }
}
