FROM python:2.7
WORKDIR /root

COPY waiter.py /tmp

RUN apt update && apt install -y ansible vim less

RUN echo export PAGER=less >> /root/.profile
RUN echo export EDITOR=vi >> /root/.profile

RUN echo set -o vi >> /root/.bashrc
RUN echo alias more=less >> /root/.bashrc

cmd ["python", "/tmp/waiter.py"]
