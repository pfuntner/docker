FROM python:2.7
WORKDIR /root

COPY waiter.py /tmp
COPY setup.py /tmp

COPY bin /root/bin
RUN chmod -R +rx bin

RUN apt update && apt install -y vim less openssh-server sudo sshpass 
RUN pip install pyyaml requests
RUN systemctl enable ssh
RUN mkdir -p /run/sshd

COPY .ssh/* /root/.ssh/
RUN chmod -R 700 .ssh

cmd ["python", "/tmp/waiter.py"]
