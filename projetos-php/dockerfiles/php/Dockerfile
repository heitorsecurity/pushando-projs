# Instalar sistema PHP com Alpine em imagem docker
FROM php:8.3-fpm-alpine3.21

# Instalar dependencias de sistema
RUN apk add --no-cache \
    bash \
    curl \
    libpng-dev \
    libzip-dev \
    zlib-dev

# Instalar extensoes PHP
RUN docker-php-ext-install gd \
    && docker-php-ext-install zip

# Ultima versao do Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Instalar node e npm
RUN apk add --no-cache nodejs npm

# Setando um diretor de trabalho para carregar as paginas
WORKDIR /var/www

# Expondo a porta 9000 para acessar a imagem docker
EXPOSE 9000