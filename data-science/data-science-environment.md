# Learning Data Science

This document outlines what I learned during my first first few weeks studying the tools associated with data science, such as databases, and Python frameworks like [SQLalchemy](https://www.sqlalchemy.org/), [Pandas](https://pandas.pydata.org/), and [Numpy](https://numpy.org/). 

Working with already-existing data stored in databases requires a significant amount of knowledge, so most data science books and blog avoid databases and work with simpler-to-use data sources like Excel files, CSV files, and text files. Instead of starting with these simpler examples, for which there are already [many](https://alongrandomwalk.com/2020/09/14/read-and-write-files-with-jupyter-notebooks/) [tutorials](https://www.digitalocean.com/community/tutorials/data-analysis-and-visualization-with-pandas-and-jupyter-notebook-in-python-3) [available](https://www.datacamp.com/tutorial/python-excel-tutorial), data scientists need to first learn how to [access data from a database](https://realpython.com/tutorials/databases/).

Unfortunately, most of the beginner-level information about databases that is available on books and online is targeted at application developers and describes how to create new databases that support applications. Available tutorials focus on designing and building an empty database that will store data and retrieve generated by an application.

But, data scientists usually need to read large amounts of data from already-existing databases. They need to study an already-existing database's schema so they can understand how to best analyze the data stored in it. They do not usually write data to the database or change its design.

This document's goal is to help a beginner to access and analyze data from an already-existing database.

# Learning materials

In this document, I am working through the examples provided in the book, *[Practical Data Science with Jupyter](https://nokia.percipio.com/books/f016a0a0-91bd-4ebf-852c-54f929f9f446)* by Prateek Gupta, published in 2021. The book is available in [Skillsoft Percipio](https://nokia.percipio.com/) so it is free for Nokians to read. It is concisely written and serves as a good book for beginners who want to learn how to use Python-related tools in data science.

However, it, and every other "Python for data science" book I looked at, does a very poor job covering how to use data stored in databases.

# Set up your environment

Many data scientists use [Jupyterlab](https://jupyter.org/) to develop and present their data science projects. This document uses JupyterLab as an advanced REPL that will run the Python code used to access data from a database and analyze it.

To use Jupyterlab, you must:

* Install Python on your Windows laptop
* Create a new folder for your data science learning projects
* Create a Python virtual environment and activate it
* Install JupyterLab in your virtual environment and run JupyterLab


## Install Python on your Windows laptop

There are many ways to [install Python on Windows](https://learn.microsoft.com/en-us/windows/python/beginners#install-python). I recommend installing it from the *Microsoft Store*. Open the Microsoft Store app and search for Python. Install the latest version. [Python 3.11](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-ca&gl=ca&activetab=pivot%3Aoverviewtab&rtc=1) was the latest version at the time I wrote this notebook so all examples use Python 3.11.

## Create a new folder

Open the [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=us) app.

Create a new folder that will store your virtual environment, notebook files, and other files you create while learning about data science. Navigate to your home folder, or to a subdirectory of your choice and create a folder named *data-science*:

```powershell
> mkdir data-science
```

## Create a Python virtual environment

Navigate into the folder you created and create a Python virtual environment. I chose to call mine, *env*.

```powershell
> cd data-science
> python -m venv env
```

Next, activate the virtual environment.

```powershell
> .\env\Scripts\activate
(env) > 
```

## Install and run JupyterLab

Install JupyterLab in the virtual environment. JupyterLab installs a lot of modules so you should keep it in a virtual environment to avoid messing up your Windows system.

```powershell
(env) > pip install jupyterlab
```

Run JupyterLab.

```powershell
(env) > jupyter notebook
```

The terminal will show multiple URLs that you can copy and paste into a web browser. Because you installed JupyterLab in a virtual environment, use one of the *localhost* URLs, like the following

```
http://localhost:8888/?token=678b6891879b80fc02488701d553b1a2b4
```

The token is needed the first time you use a new browser to access JupyterLab. After using it once, it is cached in the browser and you can connect to JupyterLab in the future with just the simple URL: 

```
http://localhost:8888
```

The Jupyter Notebook web interface looks like the image below.

![Jupyter Notebook user interface](./Images/JupyterNotebook001.png)

## Alternative interfaces

### Jupyter Lab

You can also use the JupyterLab interface, instead. If you want to open notebooks using the JupyterLab interface, start the Jupyter server with the following command, instead of using the `jupyter notebook` command:

```
(env) > jupyter-lab
```

JupyterLab is the newer interface and has more features but the original Notebook interface is all most people need.

### VS Code

Also, you can [edit Jupyter Notebooks in the VS Code editor](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). Install the VSCode [Python extension]() and [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), then open the Notebook file in VS Code. The virtual environment must already be activated and the JupyterLab server must already be started.

# Get Data

To learn about the basics of data science, you need data. Eventually, you need to learn how to work with many sources of data, such as:

* Databases: mostly SQL databases
* Excel and CSV files stored on a secure SharePoint site
* APIs of external services
* Web scraping

While you work in the Analytics team, most of the data you will access will come from a database or a file on a secure SharePoint site. Most of our data comes from the HRDP data lake.

When you are at the beginning of your learning, it may be best to use a "dummy" database so you do not accidentally cause issues with a production database. 

## Data sources

If you cannot get access to HRDP when you start experimenting with data science tools like Python and SQLAlchemy, use another available database for practice. There is lots of data [available to the public](https://www.dropbase.io/post/top-11-open-and-public-data-sources) that you may want to analyze as you learn more about data science. We want to learn how to analyze data stored in a database so we need data available in that format.

The best solution is to install an SQL database engine like [SQLite](https://www.sqlite.org/index.html) on your PC and download a database backup from a public repository. [Kaggle](https://www.kaggle.com/) offers many [database files that are suitable for learning data science](https://www.kaggle.com/datasets?search=SQL), like the [Formula1 SQLite database](https://www.kaggle.com/datasets/davidcochran/formula-1-race-data-sqlite). Other, more business-focused databases like the [Northwind database](https://github.com/jpwhite3/northwind-SQLite3), or the [Chinook database](https://github.com/lerocha/chinook-database), may also be interesting.

In this document, we will use the Formula 1 database from Kaggle. Go to the [kaggle.com](https://www.kaggle.com/) website and select *Datasets* from the top menu. The select the *Filters* on the right side of the search field and select the *SQLite* file type and set the maximum file size to 10 MB. The Formula 1 database should be on the first page of results.

Download the *[Formula 1 Race Data (SQLite)](https://www.kaggle.com/datasets?search=Formula+1&fileType=sqlite&sizeEnd=10%2CMB)* file to your computer.

# Python and databases

Once you start using databases in Python, you start learning more about advanced Python features such as [object-oriented programming](https://www.freecodecamp.org/news/object-oriented-programming-in-python/), [data classes](https://docs.python.org/3.11/library/dataclasses.html) and [type hints](https://towardsdatascience.com/type-hints-in-python-everything-you-need-to-know-in-5-minutes-24e0bad06d0b). I leave these topics to your own study.

# SQLite Database Engine

[SQLite](https://www.sqlite.org/index.html) is part of the Python standard library. It provides a file-based SQL database engine that does not require the programmer to install any additional Python packages. However, you need to know the SQL query language when writing programs that use the *sqlite* Python module.

In this document, we read data from the Formula 1 Race Data SQLite database file but we will use another Python package, *SQLAlchemy*, to read it instead of the built-in *sqlite* module.

## SQLAlchemy

[SQLAlchemy](https://www.sqlalchemy.org/) is a Python package that helps programmers interact with SQL databases, without having to learn the SQL Query language. If you use the SQLAlchemy package, which has a learning curve of its own, then you do not need to worry about learning the [SQL language differences](https://towardsdatascience.com/how-to-find-your-way-through-the-different-types-of-sql-26e3d3c20aab) between the various SQL databases like MySQL, PostgreSQL, and Microsoft SQL Server, that different data sources may use.

### Install SQLALchemy

In your virtual environment, install SQLAchemy with the following command:

```powershell
(env) > pip install SQLAlchemy
```

### Connect to the database

Start a new Jupyter Notebook. In the first cell, enter the following code to open a connection with the database.

```python
from sqlalchemy import create_engine, inspect

engine = create_engine(r"sqlite:///C:/Users/blinklet/Documents/Formula1.sqlite")
inspector = inspect(engine)

print(inspector.get_table_names())
```

Run the cell. You should see the output displayed as a list containing the table names in the Formula 1 database.

```python
['circuits', 'constructor_results', 'constructor_standings', 'constructors', 'driver_standings', 'drivers', 'laptimes', 'pitstops', 'qualifying', 'races', 'results', 'seasons', 'status']
```

You know the connection works because you were able to get the list of table names. Now, let's find out some more information about the database.

### Exploring the database structure

Create a new cell in the Jupyter notebook, enter the following code, and run it.

```python
print(inspector.get_schema_names())
```

The output shows there is one database schema, named *main*.

Create a new cell in the Jupyter notebook, enter the following code, and run it.

```python
print(inspector.get_schema_names(schema_name='main'))
```

This is similar to the code we used to verify our connection to the SQLite database was working. It prints out the database table names. This time, we passed in the schema name as a parameter but that is only necessary if you have multiple database schemas.

If you want to see all the information about each column in all the database tables, run the following code:

```python
for tbl in inspector.get_table_names():
    print(inspector.get_columns(schema_name='main',table_name=tbl))
```

But, in this example, you only want the column names so create a new cell in the Jupyter notebook, enter the following code, and run it.

```python
for tbl in inspector.get_table_names():
    print(f"Table = {tbl}")
    for col in inspector.get_columns(schema_name="main",table_name=tbl):
        star = ""
        if col['primary_key'] == 1:
            star = "*"
        print(f"{star}{col['name']}{star}", end = ", ")
    print("\n")
```

The output shows all the tables, with a list of each table's column names. Primary key columns are highlighted by asterisks. The output looks like the output shown below:

```
Table = circuits
*circuitId*, circuitRef, name, location, country, lat, lng, alt, url, 

Table = constructor_results
*constructorResultsId*, raceId, constructorId, points, status, 

Table = constructor_standings
*constructorStandingsId*, raceId, constructorId, points, position, positionText, wins, , 

Table = constructors
constructorId, constructorRef, name, nationality, url, , 

Table = driver_standings
*driverStandingsId*, raceId, driverId, points, position, positionText, wins, 

Table = drivers
*driverId*, driverRef, number, code, forename, surname, dob, nationality, url, 

Table = laptimes
raceId, driverId, lap, position, time, milliseconds, 

Table = pitstops
raceId, driverId, stop, lap, time, duration, milliseconds, 

Table = qualifying
*qualifyId*, raceId, driverId, constructorId, number, position, q1, q2, q3, 

Table = races
*raceId*, year, round, circuitId, name, date, time, url, 

Table = results
resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId, 

Table = seasons
year, url, 

Table = status
*statusId*, status,
```


