Follow tutorial
https://dev.to/saluminati/dockerize-wordpress-with-themes-plugins-and-common-configuration-2am4

https://developer.wordpress.com/2022/11/14/seetup-local-development-environment-for-wordpress/


https://www.wpbeginner.com/wp-tutorials/how-to-move-live-wordpress-site-to-local-server/


# Stop Wordpress from trying to use FTP to get backups and plugins

After WP install, edit *wordpress/wp-config.php* file and add following to end of file:

```
define('FS_METHOD', 'direct');
```

Save file

# Give Wordpress access to */var/www/html/* folder

Ensure the *wordpress* directory is owned by *www-data* user:

```
sudo chown -R www-data:www-data wordpress
```

# Add updraft plugin

Go to plugins tab, find updraft plugin and install it

Set it up to connect to existing DropBox account (could also use local files if you copied them to your hard drive)

Settings

select Dropbox, press save

click setup link

log into DropBox


Then, at bottom of updraft screen, see "Existing backups"

# Error

Looks like plugins or something not compatible with PHP 8.2. Get old container with PHP 7.4???


docker pull wordpress:php7.4
wordpressdevelop/php:7.4-fpm

Or, downgrade PHP on the latest wordpress   

* https://linux.how2shout.com/how-to-install-php-7-4-on-ubuntu-22-04-lts-jammy-linux/
* https://webdock.io/en/docs/perfect-server-stacks/upgrade-or-downgrade-php/upgrading-or-downgrading-php-versions

```
$ docker exec -it wordpress bash
# apt update
# apt install software-properties-common
# apt install python3-launchpadlib
# add-apt-repository ppa:ondrej/php -y
# apt update
# apt install php7.4
# apt install php7.4-{cli,common,curl,zip,gd,mysql,xml,mbstring,json,intl}
# update-alternatives --config php
```

# clear volume

To start over: must also delete the docker volume *wordpress_db_data*

```
$ docker volume ls
$ docker volume rm wordpress_db_data
```

# The Standard Theme is the problem!!!

If I activate the standard theme, the web site fails. It seems to be incompatible with PHP 8.2. As soon as Bluehost updates their servers to Ubuntu 22 or 24, I am toast!!! (PHP 8.x is in Ubuntu 22 and 24)

https://support.rebel.com/hc/en-us/articles/360047782954-How-do-I-fix-a-WordPress-website-broken-by-a-PHP-upgrade-Classic-Hosting