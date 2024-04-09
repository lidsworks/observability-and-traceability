# Use the official Composer image as base
FROM composer:latest AS composer

# Set working directory
WORKDIR /app

# Copy composer.json and composer.lock
COPY src/composer.json ./

# Install dependencies
RUN composer install --no-scripts --no-autoloader

# Copy the rest of the application
COPY ./src .

# Run Composer's autoloader
RUN composer dump-autoload --optimize

# Use a lightweight base image
FROM php:latest

ARG NEW_RELIC_LICENSE_KEY

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    unzip

RUN \
    curl -L https://download.newrelic.com/php_agent/release/newrelic-php5-10.19.0.9-linux.tar.gz | tar -C /tmp -zx && \
    export NR_INSTALL_USE_CP_NOT_LN=1 && \
    export NR_INSTALL_SILENT=1 && \
    /tmp/newrelic-php5-*/newrelic-install install && \
    rm -rf /tmp/newrelic-php5-* /tmp/nrinstall* && \
    sed -i \
    -e "s/\"REPLACE_WITH_REAL_KEY\"/${NEW_RELIC_LICENSE_KEY}/" \
    -e 's/newrelic.appname = "PHP Application"/newrelic.appname = "lidm-app-milestone-gateway"/' \
    -e 's/;newrelic.daemon.app_connect_timeout =.*/newrelic.daemon.app_connect_timeout=15s/' \
    -e 's/;newrelic.daemon.start_timeout =.*/newrelic.daemon.start_timeout=5s/' \
    /usr/local/etc/php/conf.d/newrelic.ini

# Set working directory
WORKDIR /var/www/html

# Copy files from composer image
COPY --from=composer /app .
COPY ./src/public ./public

# Expose port 8000 to the host
EXPOSE 8000

# Command to run the PHP built-in server
CMD ["php", "-S", "0.0.0.0:8000", "-t", "."]