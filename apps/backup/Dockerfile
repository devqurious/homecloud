FROM nginx:latest
ENV LANG C.UTF-8
ENV NOTVISIBLE "in users profile"

RUN apt-get update && \
	apt-get install -y openssh-server rsync && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile

# We need this dir to store the authorized_keys file which will contain a list of all the public keys
# of all the clients that will be backing up their data to this container.
RUN mkdir -p /root/.ssh
RUN chown root:root /root/.ssh

# This is public key of the machine that will initiate the rsync (mini2020). If this is not there
# the user will need to enter the password of the root user...which is a problem if you want to 
# rsync from cron.
RUN echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCuirNZmzquliz0LbrBNvHTAMnjoHcNLf/3Tio5lWpe3zvAxJZKLvGwaUMYHnYrIovLKke0d1n6rNqO4Q4azdiVT6MPRTlLUp1grPheLt2Eb8QT3d3YJq77QCXUX31qlJL2lW2KEFlybmxWUJxxrHVNHEnqhzjzABl4yrPS7odoKmXTMHrpqnPSKuOtVa/l2bVf8nAizA7IaFfEei7Uj6ByUzBGDFUOHop5Vmi9gRrKJHxsLwfQfr46J9eFV4TbkxEMe045AN4yjuMva5O9/8smHsJQKTzJbtzdMblCMnMovd+uWxOEql1LARhgtvYJi/NQzzUY2VetsxvG5rNB9wntQfhwEA33fJfDXDXQcVdLS5qEYzGm8lukBoOTJLZFgAeYGGQeHWO+ZoGYjxEwZRU/g8ojF/Hj14PEdCcMRPJ921vgTzlD9OKf2IhbFjWHGwrZZMSEzbM6rLqAS1icPoif7dRKAyGnaycW8reR3HFVuu7ojnK1741fUY00lRt0yCbYaMYsFUlzZjMmOvggjrcUYi14Q482+rADCe1AWw+F+9/JO68+0544DZiSTTZJ6f/hD4Foyx1Uyjzy6sKe01tnIqVT1dDalkc8fK192uFo9Jn4VxdM+oYwsIKlicTZ7RzyvGU2y7PLtE23ml4Dyu7mMHHJBK3pbBaQNf1cAOfbQw== dev@aquriousmind.com" >> /root/.ssh/authorized_keys

# For the nginx file browser
RUN ln -sf /data /usr/share/nginx/html/data

COPY entrypoint.sh /entrypoint.sh
COPY default.conf /etc/nginx/conf.d

RUN chmod 744 /entrypoint.sh

# SSH, RSync and NGinx
EXPOSE 22
EXPOSE 873
EXPOSE 80

# Taken together, this has the effect of /entrypoint.sh rsync_server
CMD ["rsync_server"]
ENTRYPOINT ["/entrypoint.sh"]
