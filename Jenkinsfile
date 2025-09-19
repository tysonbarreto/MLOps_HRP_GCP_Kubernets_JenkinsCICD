pipeline{
    agent any
    environment{
        GCP_PROJECT = "mlopshrp"
        PATH="/var/jenkins_home/google-cloud-sdk/bin:$PATH"
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
                    sh "whoami"
                    sh "python -m pip install --break-system-packages -U uv"
                    sh "python -m uv venv --python 3.11"
                    sh "python -m uv sync"
                }
            }
        }
        stage('Building and Pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker image to GCR...'
                        sh'''
                        cd ~/..
                        docker --version
                        chmod +x /var/jenkins_home/google-cloud-sdk/bin
                        ./var/jenkins_home/google-cloud-sdk/install.sh
                        gcloud --version
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker
                        cd /var/jenkins_home/workspace/MLOps-HRP/
                        cat ${GOOGLE_APPLICATION_CREDENTIALS} > mlops.json
                        docker build --build-arg=${GOOGLE_APPLICATION_CREDENTIALS} -t gcr.io/${GCP_PROJECT}/mlopshrp:latest .
                        docker push gcr.io/${GCP_PROJECT}/mlopshrp:latest
                        '''
                    }

                }
            }
        }
        stage('Building and Pushing Docker image to Google Cloud Run'){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker image to Google Cloud Run...'
                        sh'''
                        cd ~/..

                        chmod +x /var/jenkins_home/google-cloud-sdk/bin
                        ./var/jenkins_home/google-cloud-sdk/install.sh
                        gcloud --version
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}

                        gcloud run deploy ...\
                            --image=gcr.io/${GCP_PROJECT}/mlopshrp:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated
                        '''
                    }

                }
            }
        }
        }
}