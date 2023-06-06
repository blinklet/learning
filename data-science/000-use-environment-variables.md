Environment variables are dynamic values that are set outside of the program, either through the operating system's command line interface, through a configuration file or, in the case of cloud environments, via a web interface. They are essentially key-value pairs that provide configuration information to the application and are accessible during its execution.

Environment variables are part of the operating system environment in which the Python program runs. They can store various types of information, such as paths to important directories, credentials, API keys, database connection strings, or any other configuration values used by the program.

<!--more-->

# Accessing environment variables

In Python programs, you access environment variables through the [*os* module in the Python Standard Library](https://docs.python.org/3/library/os.html#os.getenv), which provides functions for interacting with the operating system. 

To get the value of an environment variable, use the `os.getenv()` function. For example:

```python
value = os.getenv("VARIABLE_NAME")
```

The `os.getenv()` function retrieves the value of the specified environment variable. If the variable doesn't exist, it returns `None`.

# Why use environment variables

There are good reasons to use environment variables instead of just hard coding program configuration information in your program's source code or in a separate configuration file. 

1. Security

   When writing code that will be part of an open-source projects, or may be stored in a public Git repository, you do not want to provide your passwords, database credentials, API keys, and other sensitive information to anyone who looks at your code.

   Environment variables offer a more secure way to store the secrets your program needs to access sensitive resources like databases and APIs. Your program reads the secrets from its environment when the it runs

2. Separates configuration from code

   Environment variables are set outside of the Python script, in the platform or operating system on which the program runs, so they provide a convenient way to manage configuration settings for Python programs. You can change configuration settings in the program's environment without modifying your source code. This makes it easy to deploy the program to different environments like development, test, or production, each of which may use different resources.

# How to set environment variables for your program

Environment variables are typically stored outside the source code repository, and are set when operators set up the environment in which your python program is deployed. This can be automated on some platforms but individual developers will usually have to set environment variables themselves and [the procedure will be different](https://www.twilio.com/blog/how-to-set-environment-variables-html) for different operating systems or cloud platforms.

To keep from losing or forgetting secrets, developers will usually encrypt and store their program secrets in some type of digital vault like [Bitwarden](https://bitwarden.com/), [1Password](https://1password.com/), or [Vault](https://developer.hashicorp.com/vault/docs/what-is-vault) and then they nay manually assign those secrets to environment variables before they test their programs. 

If you plan to deploy your program in the cloud, you may store secrets in a tool like [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts) or [Google Secrets Manager](https://cloud.google.com/architecture/security-foundations/keys-secret-management), which would then automatically set up environment variables when you deploy your program on their platforms.

## *Dotenv* files

When developing your Python program on your local computer, it is easiest to store secrets locally in a [*dotenv* file](https://dev.to/nicat/using-dotenv-env-in-python-4l49) that is not included in your source code repository. Personally, I would both create a *dotenv* file and store the secrets in my password manager so I do not lose them if I delete the project's source code repository on my local PC.

You must be sure to add the ".env" file type to your *.gitignore* file so it is never included in your public Git repository especially if, for example, if you use a public remote repository like [GitHub](https://github.com/). Then, use the *[python-dotenv](https://pypi.org/project/python-dotenv/)* package in your program to load variables from either the *dotenv* file or from the environment.

Other programmers who may use your code still need to know which variables need to be set. Add an [example *.env* file](https://www.twilio.com/blog/environment-variables-python) with a name such as ".env.example" to your repository that contains the list of variables that the project requires, but does not include their real values. This provides guidance to your users, without giving away sensitive information. [^1]

[^1]: From Twilio blog post [Working with Environment Variables in Python](https://www.twilio.com/blog/environment-variables-python), accessed in June 2023


# How to use a *.env* file

[Put program environment variables in a local "dotenv" file](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1#) so you can test your program with any operating system. Use the *[python-dotenv](https://pypi.org/project/python-dotenv/)* package to load variables from the *.env* file into your Python program's environment when the program runs.

## Install the *python-dotenv* package

Install *python-dotenv* package in your virtual environment.

```bash
(env) $ pip install python-dotenv
```

## Create the *.env* file

Next, create a two files named *.env* and *env.example* in the project's root folder. The contents of the *.env.example* file would look like the following and the contents of the *.env* file would have the same variable names, but contain the actual values needed for your program to work.

```
DB_SERVER=server.name.com
DB_NAME=database_name
DB_UID=username
DB_PWD=password
```

Save the files.

## Except *.env* files from source control

Add ".env" to the *.gitignore* file in your project folder to ensure your secrets are not recorded in the Git database. This is a critical step required to protect your secrets. 

# How to use environment variables in your program

The *dotenv* module in the *[python-dotenv](https://pypi.org/project/python-dotenv/)* package offers you flexibility in handling environment variables. You may be operating in an environment in which the environment variables have already been set. If that is the case, the *dotenv* module will use the already-set environment variables and will not overwrite them with the values in the *.env* file, unless explicitly told to do so. 

## Set environment variables at run time

To use the environment variables in program, import the *dotenv.load_dotenv()* function into your program and call it.

```
from dotenv import load_dotenv

load_dotenv()
```

The *Load_dotenv()* function exports the environment variables in the *.env* file into the program's environment, if they do not already exist. From this point on, you can read environment variables as you usually would, using the *os.getenv()* function.

Normally, the *load_dotenv()* function will not overwrite existing environment variables. You may include the parameter *override=True* so that, if you already have environment variables configured of if you changed the values in your *.env* file, they will be changed when you call the *load_dotenv(override=True)* function. 

## Read environment variables

Use the *os.getenv()* builtin function in your program to get the value associated with each environment variable. 

For example:

```python
import os

DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_UID = os.getenv('DB_UID')
DB_PWD = os.getenv('DB_PWD')
```

Now you can use the values to run your program. For example, you might use the values from the above example to build a database connection string that enables you to access data from a database server.

# Conclusion

Use a *.env* file to store program configurations and secrets when you are developing your Python program or using it for your own benefit. Use other methods for setting environment variables when you move your program to a production environment like a cloud server. Most cloud and platform vendors provide a key vault and a user interface that allows programmers to set environment variables in a secure way. 

Environment variables enable you to write more flexible and configurable Python programs that can adapt to different environments without requiring code changes. They provide a convenient way to separate configuration details from your code, making it easier to manage different deployment scenarios. And, most importantly, they enable you to conveniently test your program in your development environment while protecting your system's secrets from being published in your public source code repositories.