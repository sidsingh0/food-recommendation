FROM node:18 AS frontend

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8080

CMD [ "npm", "run", "preview" ]