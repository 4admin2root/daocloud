docker run -d -p 8888:8080 -u root -v /root/jenkins_home/:/var/jenkins_home -v $(which docker):/bin/docker jenkins
