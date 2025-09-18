pipeline{
    agent any
    environment{
        GCP_PROJECT = "mlopshrp"
        GCLOUD_PATH = "var/jenkins_home/google_cloud_sdk/bin" 
    }
    stages{
        stage('Clonning GitHub Repo to Jenkins'){
            steps{
                script{
                    echo 'Clonning GitHub Repo to Jenkins...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/tysonbarreto/MLOps_HRP_GCP_Kubernets_JenkinsCICD.git']])
                }
            }
        }
        stage('Setting up Virtual Environment and Installing Dependencies'){
            steps{
                script{
                    echo 'Setting up Virtual Environment and Installing Dependencies...'
                    sh '''
                    $PWD
                    python -m venv venv
                    
                    venv/bin/python -m pip install --upgrade pip
                    venv/bin/python -m pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Building and Pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    scripts{
                        echo 'Building and Pushing Docker image to GCR...'
                        sh '''
                        cd /var/jenkins_home/workspace/MLOps-HRP
                        $PWD
                        echo 'List of files in this directory...'&&ls -l .

                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker

                        docker build -t gcr.io/${GCP_PROJECT}/mlopshrp:latest .

                        docker push gcr.io/${GCP_PROJECT}/mlopshrp:latest

                        '''
                    }

                }
            }
        }
        }
}
