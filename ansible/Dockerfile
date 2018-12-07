FROM python:2.7
# FROM ubuntu
WORKDIR /tmp
COPY waiter.py /tmp
RUN apt update && apt install -y ansible
cmd ["python", "waiter.py"]
# cmd ["bash"]
