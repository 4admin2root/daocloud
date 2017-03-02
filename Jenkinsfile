node ('mytest1') {
    stage('git pull') {
        git changelog: false, poll: false, url: 'https://github.com/4admin2root/daocloud.git'
    }    
    stage('Create Docker Image') {
        dir('dao-2048') {
            docker.build("mytest4:5000/dao-2048:${env.BUILD_NUMBER}")
        }
    }
    stage('push docker imgage') {
        sh "docker push mytest4:5000/dao-2048:${env.BUILD_NUMBER}"
    }
    
}
