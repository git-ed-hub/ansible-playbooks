FROM jenkins/jenkins:jdk17
USER root
RUN apt-get update && \
    apt-get install -y python3-pip sshpass && \
    pip3 install ansible
RUN mkdir /etc/ansible


USER jenkins





