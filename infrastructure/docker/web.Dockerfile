FROM node:18-alpine

WORKDIR /app

COPY web/package.json web/package-lock.json* /app/

RUN npm install

COPY web /app

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
