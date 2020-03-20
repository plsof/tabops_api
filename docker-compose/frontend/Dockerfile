FROM nginx
ADD dist.tar.gz /usr/share/nginx/html/
RUN mkdir /usr/share/nginx/html/media/
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
