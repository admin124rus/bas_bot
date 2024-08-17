FROM ubuntu:16.04
 
# tzdata for timzone
RUN apt-get update -y
RUN apt-get install -y tzdata
 
# timezone env with default
ENV TZ Asia/India