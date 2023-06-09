# Create a static web site with Pelican and Python

There is a [great tutorial about using Pelican](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html) at the Full Stack Python blog.

## Install Pelican

[Pelican](https://getpelican.com/)

Create a folder for your web site and create a virtual environment

```bash
$ mkdir my_web_site
$ cd my_web_site
$ pythons -m venv env
$ source env/bin/activate
(env) $
```

Install Pelican with the Markdown option enabled:

```bash
(env) $ pip install "pelican[markdown]"
```

## Initialize web site project

```bash
(env) $ pelican-quickstart
```

This asks some questions, I have a URL and web site name in mind already so I answered "yes" when asked if I want to specify a URL prefix. However, I do not yet know where I will publish this site so I answered "no" to all the questions asking me where I want to upload my website. The correct responses to the question about time zones can be found in the [Wikipedia list of standard time zones](ttps://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

```bash
Welcome to pelican-quickstart v4.8.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.
    
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? Learning with Code
> Who will be the author of this web site? Brian Linkletter
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) Y
> What is your URL prefix? (see above example; no trailing slash) https://learnwithcode.com
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Rome] America/Toronto
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) n
Done. Your new project is available at /home/brian/Projects/python-web-site
```

You can go back and edit the Pelican configuration file later if you need to change any settings. For example, I will have to update the configuration files when I decide the service to which I will upload my web site.

If you look at the directory, you will see that the *pelican-quickstart* script created some new directories and configuration files.

```python
(env) $ ls
content  env  Makefile  output  pelicanconf.py  publishconf.py  tasks.py
```

### Quick test

Create a dummy blog post to quickly check that the site is working

```bash
(env) $ cd content
(env) $ nano use-environment-variables-python.md
```

```
title: Use environment variables to protect your secrets
slug: use-environment-variables-python
date: 2023-06-07
modified: 2023-06-07

# Use environment variables to protect your secrets

Environment variables are key-value pairs that are are set outside of a Python program but may be accessed by the program during its execution.

<!--more-->

## Why use environment variables

There are many reasons to use environment variables instead of just hard-coding program configuration information in your program's source code or in a separate configuration file. For individual Python programmers, the most relevant reasons are:

1. Security

   Normally, you do not want to reveal sensitive information like passwords, database credentials, or API keys to anyone who looks at your code. This is especially true when writing code that will be part of an open-source project, or may be stored in a public source code repository. 
```

```bash
(env) $ pelican content
[22:40:11] WARNING  Watched path does not exist:                       log.py:91
                    /home/brian/Projects/python-web-site/content/image          
                    s                                                           
Done: Processed 1 article, 0 drafts, 0 hidden articles, 0 pages, 0 hidden pages 
and 0 draft pages in 0.09 seconds.
```

```bash
(env) $ pelican --listen
Serving site at: http://127.0.0.1:8000 - Tap CTRL-C to stop
[22:42:13] INFO     "GET / HTTP/1.1" 200 -                         server.py:121
           INFO     "GET /theme/css/main.css HTTP/1.1" 200 -       server.py:121
           INFO     "GET /theme/css/reset.css HTTP/1.1" 200 -      server.py:121
           INFO     "GET /theme/css/pygment.css HTTP/1.1" 200 -    server.py:121
           INFO     "GET /theme/css/typogrify.css HTTP/1.1" 200 -  server.py:121
           INFO     "GET /theme/css/fonts.css HTTP/1.1" 200 -      server.py:121
           INFO     "GET /theme/fonts/Yanone_Kaffeesatz_400.woff   server.py:121
                    HTTP/1.1" 200 -                                             
           WARNING  Unable to find `/favicon.ico` or variations:       log.py:91
                    /favicon.ico.html                                           
                    /favicon.ico/index.html                                     
                    /favicon.ico
```

Now capture the image of the blog and save it in a new folder named images and put the screencap in there. then add it to the blog post.



