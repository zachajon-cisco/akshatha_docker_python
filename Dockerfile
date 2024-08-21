FROM python:3.12
RUN apt update
RUN apt upgrade -y
RUN pip3 install aws_requests_auth==0.4.3
RUN pip3 install requests==2.32.3
RUN pip3 install boto3==1.35.2

COPY test-uber-ip.py .

RUN python test-uber-ip.py