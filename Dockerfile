
# multi-stage build, build frontend, will be thrown away
FROM node:14.16.0-alpine as build
WORKDIR /frontend
COPY /frontend/package.json ./
COPY /frontend/yarn.lock ./
RUN yarn install --silent
COPY /frontend ./
RUN yarn run build

# things that go to the container start here
FROM ubuntu:latest
# extract frontend build
COPY --from=build /frontend/build ./frontend/build


WORKDIR /backend
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -qq update
# install quietly: -qq ; ignore dpkg output by directing it to /dev/null ; debconf error can be safely ignored
RUN apt-get -qq install -y python3-pip python3-dev build-essential > /dev/null

COPY /backend ./
RUN pip3 install -qq -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]
