https://shahayush.com/2020/03/web-pelican-pt1-setup/

learning how to use Pelican:

Pelican docs
https://docs.getpelican.com/en/3.6.3/index.htmlhttps://docs.getpelican.com/en/3.6.3/index.html

"Build and Deploy a Website or Blog using Pelican" by Vimalkumar Velayudhan
https://www.youtube.com/playlist?list=PLWtiSQ22KrCKwvkZ5iFzSL_SnHVN3LjMI

"DragonPy Meetup August 2020 Roman Luštrik How I Automated my Deployment of Static Pages with Pelican"
https://www.youtube.com/watch?v=T1tmZevDbtg&list=PL_UZskMt8L0UK6c0OUxl6FYsd40Drvwvn

"Dr. Jekyll and Mr. Pelican: A Comparison of Static Site Generators" by Lucy Wyman
https://www.youtube.com/watch?v=4Yonwd98XW8

"Getting started with Pelican: A Python-based static site generator"
https://opensource.com/article/19/1/getting-started-pelican

"How to Create Your First Static Site with Pelican and Jinja2"
https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html


* http://chdoig.github.io/create-pelican-blog.html
* https://duncanlock.net/blog/2013/05/17/how-i-built-this-website-using-pelican-part-1-setup/
* https://snipcart.com/blog/pelican-blog-tutorial-search-comments







# Blog plan

## Initial setup

Using default themes, set up a blog and add a couple of posts. Add images and pages.

Then discuss that, to go further, we need to pick a theme and some of our decisions (and Markdown syntax) will be determined by the theme we choose.


## Themes
maybe save themes for a separate post because there are three ways to set up themes

1. Use the instructions in pelican-themes, where you use Git to copy the entire repo and point your config file to a specific folder
2. Use `pelican-themes --install` to copy files to a theme folder in your virtuakl environment
3. Manually ciopy theme file to a folder in the blog project (the folder is named "themes") and point to it in your config file
  * I think the last option is best because, if you choose to modify the theme files, any changes you make are tracked in your own source control system. 
  * You can also use themes that are not part of the pelican-themes project



# Create a static web site with Pelican and Python

[Pelican](https://getpelican.com/)

There is a [great tutorial about using Pelican](https://www.fullstackpython.com/blog/generating-static-websites-pelican-jinja2-markdown.html) at the Full Stack Python blog.

## Install Pelican



Create a directory for your web site and create a virtual environment

```bash
$ mkdir my_web_site
$ cd my_web_site
$ pythons -m venv env
$ source env/bin/activate
(env) $
```

Install Pelican with the Markdown [extras](https://stackoverflow.com/questions/46775346/what-do-square-brackets-mean-in-pip-install) enabled:

```bash
(env) $ pip install "pelican[markdown]"
```

## Initialize web site project

```bash
(env) $ pelican-quickstart
```

This script asks some questions and uses your answers to populate the configuration files. I already registered a URL for my web site so I answered "yes" when asked if I want to specify a URL prefix.  I found the correct responses to the question about time zones can be found in the [Wikipedia list of standard time zones](ttps://en.wikipedia.org/wiki/List_of_tz_database_time_zones). I will deploy my website to [Netlify](https://www.netlify.com/)(https://www.netlify.com/blog/2016/10/27/a-step-by-step-guide-deploying-a-static-site-or-single-page-app/) via a [GitHub integration](https://codelapan.com/post/how-to-upload-or-deploy-static-website-on-netlify) so I do not need to use Pelican to upload files so I answered "no" to the question asking me if I wanted to create a Makefile to automate publishing.

```bash
Welcome to pelican-quickstart v4.8.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.
    
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? Learning with Code
> Who will be the author of this web site? Brian Linkletter
> What will be the default language of this web site? [en] 
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) y
> What is your URL prefix? (see above example; no trailing slash) https://learnwithcode.com
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Rome] America/Toronto
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) n
Done. Your new project is available at /home/brian/Projects/python-web-site
```

You can go back and edit the Pelican configuration file later if you need to change any settings. For example, I will have to update the configuration files when I decide the service to which I will upload my web site.

If you look at the directory, you will see that the *pelican-quickstart* script created some new directories and configuration files.

```python
(env) $ ls
content  env   output  pelicanconf.py  publishconf.py 
```

The *content* directory will contain the blog posts. Each post will be a single markdown file. The *pelicanconf.py* and *publishconf.py* arte python scripts that generate configuration information. The *output* file will contain the files generated by Pelican that create the static website. Currently, it is empty.


### Quick test

Create a dummy blog post in the *content* directory to quickly check that the site is working

```bash
(env) $ cd content
(env) $ nano use-environment-variables-python.md
```

```
title: Use environment variables to protect your secrets
slug: use-environment-variables-python
date: 2023-06-07
modified: 2023-06-07

Environment variables are key-value pairs that are are set outside of a Python program but may be accessed by the program during its execution.

# Why use environment variables

There are many reasons to use environment variables instead of just hard-coding program configuration information in your program's source code:

1. Security

   Normally, you do not want to reveal sensitive information like passwords, database credentials, or API keys to anyone who looks at your code. 

# Conclusion

This was a test created by copying content from one of my posts
```

```bash
(env) $ pelican
[22:40:11] WARNING  Watched path does not exist:                       log.py:91
                    /home/brian/Projects/python-web-site/content/image          
                    s                                                           
Done: Processed 1 article, 0 drafts, 0 hidden articles, 0 pages, 0 hidden pages 
and 0 draft pages in 0.09 seconds.
```

```bash
(env) $ pelican --listen
```

You see that the blog shows one post. 

![](./images/blog_test.png)

Hit CTRL-C to stop the server.

Now capture the image of the blog and save it in a new directory named *images* and put the screen capture in there. then add it to the blog post.

# Themes

Next, pick a theme for the blog. The default theme looks OK but bloggers like to customize the blog.

Some themes I like are:

* [*Flex* theme](https://flex.alxd.me/)
  * Simple to set up and looks good
  * Mobile-first theme
  * Author can configure dark or light mode
  * Supports many plugins

* [*Papyrus* theme](https://aleylara.github.io/Papyrus/)
  * Supports viewer-configurable dark and light mode
  * Supports many plugins
  * Allows author to create summaries of posts on main page
  * Looks good on mobile, also

https://out-of-cheese-error.netlify.app/astrochelys#org2054e9a_1
https://github.com/out-of-cheese-error/astrochelys

https://github.com/arulrajnet/attila-demo
https://arulrajnet.github.io/attila/





Use the [pelican-themes](https://docs.getpelican.com/en/latest/pelican-themes.html) command

First, see which themes already exit on your system:

```bash
pelican-themes --list
```
```
notmyidea
simple
```

The default theme is *notmyidea*.

To change themes, add a "THEME" line to the *pelicanconf.py* file. Add the following line to the end of the file:

```
THEME = 'simple'
```

Then run pelican again

```bash
(env) $ pelican
(env) $ pelican --listen
```

You see the them changed to the *simple* theme.

![](./images/theme_test.png)

You can only switch to themes that are installed. To isnatll a theme, copy the theme files to a folder on your PC, usually to the *Downloads* folder. Then use the *pelican-themes* command to copy the theme files to the correct location on your system which is, by default, in your Python virtual environment.

A good place to look for themes is the [Pelican Themes repository](https://github.com/getpelican/pelican-themes) on GitHub.

install the "Flex" theme

get v2.5 of the flex theme files

https://github.com/alexandrevicenzi/Flex/releases/tag/v2.5.0

and store the archive on your PC in the Downloads folder

uncompress the file so all the files are installed in a directory named Flex-2.5.0

```
(env) $ cd ~/Downloads
(env) $ wget https://github.com/alexandrevicenzi/Flex/archive/refs/tags/v2.5.0.zip
(env) $ unzip v2.5.0.zip
```

Use *pelican-themes* to copy the files to the correct location

```
(env) $ pelican-themes --install ~/Downloads/Flex-2.5.0/
```

See that the new theme is installed

```
(env) $ pelican-themes --list
Flex-2.5.0
notmyidea
simple
```

See the locations the themes are installed

```
(env) $ pelican-themes --list -v
```

```
/home/brian/Projects/python-web-site/env/lib/python3.10/site-packages/pelican/themes/notmyidea
/home/brian/Projects/python-web-site/env/lib/python3.10/site-packages/pelican/themes/simple
/home/brian/Projects/python-web-site/env/lib/python3.10/site-packages/pelican/themes/Flex-2.5.0
```

You may delete the downloaded files if you want to save some space. They are not needed anymore

```
(env) $ rm v2.5.0.zip
(env) $ rm -r Flex-2.5.0
```


Now switch to the Flex theme:

Edit the following line in *pelicanconf.py*

```
THEME = 'Flex-2.5.0'
```

Then run pelican again

```bash
(env) $ pelican
(env) $ pelican --listen
```

When starting a Pelican-based blog, you will probably want to install multiple themes so you can experiment with the way your site looks,


Customizing themes
https://www.smashingmagazine.com/2009/08/designing-a-html-5-layout-from-scratch/

https://geekyshacklebolt.wordpress.com/2020/08/18/how-to-use-a-custom-pelican-blog-theme/

Look at customization options for Flex them

https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

You need to add more to the pelicanconf.py file to get a more fine-tunes look



## Images

How to add images to posts. images directory

## Pages or posts

What if I want pages? Like an "about" page




## Publishing

Add publishing info to settings

https://docs.getpelican.com/en/latest/publish.html
https://docs.getpelican.com/en/latest/settings.html



