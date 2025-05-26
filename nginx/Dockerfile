FROM nginx:latest

RUN apk add --no-cache bash curl jq python3
RUN curl -sL https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh > /usr/bin/wait-for-it && chmod +x /usr/bin/wait-for-it
COPY conf.d /etc/nginx/conf.d
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
