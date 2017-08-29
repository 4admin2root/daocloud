FROM python:2.7-alpine

ENV ROBOT_VERSION=3.0.2 \
    ROBOT_SL_VERSION=2.9.2 \
    ROBOT_SL2_VERSION=1.8.0 \
    PIP_URL=https://mirrors.aliyun.com/pypi/simple/
EXPOSE 9000
RUN set -x \
    && pip install robotframework==$ROBOT_VERSION -i $PIP_URL \
    && pip install robotframework-seleniumlibrary==$ROBOT_SL_VERSION -i $PIP_URL \
    && pip install robotframework-selenium2library==$ROBOT_SL2_VERSION -i $PIP_URL 
ENTRYPOINT ["sleep 10"]
