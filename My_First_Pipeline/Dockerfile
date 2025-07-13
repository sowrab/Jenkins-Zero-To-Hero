FROM node:16-bullseye

#install Python and dependecies
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install flask
WORKDIR /app
COPY . /app

RUN npm install

EXPOSE 3000

CMD ["node", "app/server.js"]
