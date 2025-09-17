pipeline{
    agent any
    stages{
        stage('Clonning GitHub Repo to Jenkins'){
            steps{
                script(
                    echo 'Clonning GitHub Repo to Jenkins...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/tysonbarreto/MLOps_HRP_GCP_Kubernets_JenkinsCICD.git']])
                )
            }
        }
        }
}