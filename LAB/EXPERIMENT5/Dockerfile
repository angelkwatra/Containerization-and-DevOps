FROM node:18

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
ENV NODE_ENV=production
ENV PORT=3000
ENV APP_VERSION=1.0.0