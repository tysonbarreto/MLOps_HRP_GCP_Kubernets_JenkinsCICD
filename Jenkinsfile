pipeline{
    agent any
    environment{
        VENV_DIR = 'venv',
        GCP_PROJECT = "mlopshrp",
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
                    python -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install pdm
                    pdm use -f ${VENV_DIR}
                    pdm install
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
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/mlopshrp:latest .

                        docker push gcr.io/${GCP_PROJECT}/mlopshrp:latest

                        '''
                    }

                }
            }
        }
        }
}
