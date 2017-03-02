node ('mytest1') {
    stage('Create Docker Image') {
        dir('dao-2048') {
            docker.build("mytest4:5000/dao-2048:${env.BUILD_NUMBER}")
        }
    }
}
