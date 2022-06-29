FROM node:alpine
WORKDIR /usr/src
COPY package.json .
COPY package-lock.json .
COPY .env .
RUN npm i
RUN npm install cors
RUN npm install -g ts-node typescript
RUN npm install -g @types/node
COPY src/ ./src
COPY app.ts .