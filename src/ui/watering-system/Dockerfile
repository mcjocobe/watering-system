FROM node:lts-alpine as build-stage
COPY . .

RUN npm install -g http-server

RUN npm i beercss && npm i material-dynamic-colors

RUN npm install

RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
