FROM centos
RUN yum install -y \
    yum-utils &&\ 
    yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo &&\
    yum -y install docker-ce-cli &&\
    yum clean all
CMD ["sleep", "1000"] 
