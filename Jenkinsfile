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
                    git branch: 'main', credentialsId: 'github-jenkins', url: 'https://github.com/tysonbarreto/MLOps_HRP_GCP_Kubernets_JenkinsCICD.git'
                }
            }
        }
        stage('Setting up Virtual Environment and Installing Dependencies'){
            steps{
                script{
                    echo 'Setting up Virtual Environment and Installing Dependencies...'
                    sh '''
                    $PWD
                    whoami
                    ls -l .
                    chmod +x .
                    curl -LsSf https://astral.sh/uv/0.8.18/install.sh | sh
                    uv venv --python 3.11
                    uv add pdm
                    pdm install
                    '''
                }
            }
        }
        // stage('Building and Pushing Docker image to GCR'){
        //     steps{
        //         withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
        //             scripts{
        //                 echo 'Building and Pushing Docker image to GCR...'
        //                 sh '''
        //                 cd /var/jenkins_home/workspace/MLOps-HRP
        //                 $PWD
        //                 echo 'List of files in this directory...'&&ls -l .

        //                 export PATH=$PATH:${GCLOUD_PATH}

        //                 gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

        //                 gcloud config set project ${GCP_PROJECT}

        //                 gcloud auth configure-docker

        //                 docker build -t gcr.io/${GCP_PROJECT}/mlopshrp:latest .

        //                 docker push gcr.io/${GCP_PROJECT}/mlopshrp:latest

        //                 '''
        //             }

        //         }
        //     }
        // }
        }
}
