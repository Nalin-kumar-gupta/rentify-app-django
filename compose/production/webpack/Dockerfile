FROM node:16-buster-slim

ENV NODE_ENV=development

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

COPY ./compose/production/webpack/start.sh /start-webpack.sh
RUN sed -i 's/\r$//g' /start-webpack.sh
RUN chmod +x /start-webpack.sh

RUN npm run build

EXPOSE 8080

ENTRYPOINT ["/start-webpack.sh"]