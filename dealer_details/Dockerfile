FROM node:22-slim

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY server.js ./
COPY utils/dealers.json ./utils/dealers.json

EXPOSE 8080

CMD [ "npm", "start" ]
