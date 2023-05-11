% SQL and Python access to DATABASE

This document will show you how to use simple SQL queries to read data from the DATABASE database and load it Python objects, using either the Microsoft Transact-SQL (T-SQL) [SELECT statement](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-transact-sql) [^1] or the SQLAlchemy ORM [*select()* function](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html). 

[^1]: Microsoft Transact-SQL, also known as T-SQL, is Microsoft SQL Server's version of the [SQL language](https://en.wikipedia.org/wiki/SQL). 

# Important information

Before you get started using Python to access data in the DATABASE database, there are a few points you should know. These will help you determine if you should proceed with reading this document, or if you should find an alternative path to achieve your goals.

## Prerequisite knowledge

We do not cover the basics of Python or SQL in this document. You need to know a little bit about the basics of Python and the principles upon which [relational databases](https://www.oracle.com/ca-en/database/what-is-a-relational-database/) like SQL databases are based. If you do not already have some basic Python skills, I suggest you read my document, *Python: the Minimum You Need to Know*, or a similar tutorial. 

## Limited to PC 

This document assumes the reader is using a Microsoft-provided Windows PC. It shows you how to use your Microsoft ID to connect from your Windows PC to DATABASE with your existing permissions. So, Python can only access DATABASE when running on your own laptop.

If you plan to write applications that run on a server, you will need to create an application key and work with the DATABASE team to set up authentication for the application. You will also need to work with IT to ensure your application is secure and uses Microsoft data appropriately. You will also use different database connection information to authenticate a server application with DATABASE. Most servers run Linux so you will likely also need to learn about the Linux operating system. These topics are outside the scope of this document.

## Data handling

DATABASE contains sensitive data about Microsoft items. To reduce security risks, access only the specific data elements that you need and do not save any data to disk. Keep all your data in Python objects in memory so that, when your program is finished, the data disappears.

## Relevance

The topics covered in this document may not be relevant to most people working in the Analytics team because it ends where most will start: with data already retrieved from a database and stored in data frames. 

If you work in the Microsoft Analytics Platform, the IT teams will have created a system for you that maintains one or more DataBricks data frames and keeps them in sync with the DATABASE database. Then, you will mostly work with the DataBricks PySpark API to transform and analyze the data. 

However, knowing how the DATABASE database may be accessed from a Python program may help some in the Analytics team at some point. 

# Set up your Python environment

Before you start working through this tutorial, install Python on your laptop. Then, start a Python virtual environment and install the required Python packages in it.

## Install Python on your Windows laptop

Start by installing Python on your laptop, if it is not already installed. Go to the [Python web page](https://www.python.org/) for the most up-to-date information about installing python on your operating system.

On a Windows laptop, it is easiest to install Python from the Windows Store. 

>**NOTE:** At the time this document was written, Python 3.11 code could crash when run in Jupyter notebooks because it enables frozen modules, which seem to cause problems with the current version of Jupyter notebook. Work around this problem by installing Python 3.10 or by  turning off frozen modules when you create your Python virtual environment using the *-Xfrozen_modules=off* option.

## Create a Python virtual environment

If you have not already created a Python virtual environment, run the following commands to create one and activate it:

```powershell
> mkdir data-science-folder
> cd data-science-folder
> python -Xfrozen_modules=off -m venv env
> .\env\Scripts\activate
(env) > 
```

## Install Python database drivers

Next, install [*pyodbc*](https://mkleehammer.github.io/pyodbc/), the open-source Python ODBC driver for SQL Server. This provides the Python interface to the Windows ODBC driver. 

```powershell
(env) > pip install pyodbc 
```

Also, install the Azure Identity module to support authenticating your access to the DATABASE database.

```powershell
(env) > pip install azure-identity
```

Then, install SQLAchemy with the following command. SQLAlchemy is a more advanced library that provides many functions that make interacting with databases easier for Python programmers.

```powershell
(env) > pip install SQLAlchemy
```

## Spark

[Azure Databricks](https://azure.microsoft.com/en-us/products/databricks/) is based on Spark so it is probably best to learn how to use Spark in a Python program because the Microsoft Analytics Platform uses Databricks. 

[Spark](https://spark.apache.org/) is an open-source data analytics tool that maps functions onto large data sets stored in data frames. It is typically deployed on a cluster of computers. 

PySpark provides a [Python API](https://spark.apache.org/docs/latest/api/python/index.html) and a [Pandas API](https://spark.apache.org/docs/3.2.0/api/python/user_guide/pandas_on_spark/). Spark also [does a lot more](https://www.toptal.com/spark/introduction-to-apache-spark) than just process data in data frames.

Unfortunately, Spark requires that you install a lot of prerequisite software, including Java, on your Windows PC. It is also difficult to configure and get working on a Windows PC. So, we will use Pandas instead of Spark in the tutorials in this document.

>**NOTE:** It may be possible to [install an already-configured Pyspark container on your PC](https://realpython.com/pyspark-intro/#installing-pyspark) and use Spark running on the container. That's a good topic for future investigation but, for sake of time and effort, we will not include it in this document.

## Install Pandas

Pandas is a popular data analysis framework. It is easy to install and run on a single PC. The Pandas API is different than the Spark API but Spark offers a "Pandas mode" that allows one to enter commands into Spark using the Pandas API. So, you can use what you learn about Pandas when you upgrade to Spark.

Install Pandas:

```powershell
(env) > pip install pandas
```

## Install Jupyterlab

This document uses a [Jupyter notebook](https://jupyter.org/) as an advanced [REPL](https://codewith.mu/en/tutorials/1.0/repl) that makes it easier to demonstrate the Python code used to access data from a database and display the results. If you prefer to use a simple text editor or another REPL, you can still follow along with this tutorial.

If you wish to install Jupyterlab, run the following command:

```powershell
(env) > pip install jupyterlab
```

Create a new Jupyter notebook and start it using the commands below:

```powershell
(env) > create-notebook my_notebook
(env) > jupyter notebook my_notebook.ipynb
```

A new Jupyterlab notebook will open in a browser window.

![An example of the Jupyter Notebook user interface](./Images/Jupyter-Notebook.png){width=80%}

When using Jupyter lab, create new cells using the *B* keyboard shortcut and then write the example code into the cell. Run the code by running the cell. The objects you create in each cell persist and can be used in the next cell. 

## Next steps

Now, you are ready to start working through the tutorials in this document. You may start with using raw T-SQL statements with the Python ODBC driver or you may skip ahead to the SQLAlchemy topic to learn how to access DATABASE information using a connection managed by SQLAlchemy and to create Python objects that represent database elements.

# Python ODBC driver and T-SQL

You can use the *pyodbc* Python library to connect to and read data from an SQL Server database. Create a connection object by passing the necessary database and user information to the pyodbc driver's *connect()* function. You will create T-SQL statements, stored as strings, and pass them to the connection object's  driver. 

## Connect to DATABASE database

To use the *pyodbc* driver, import the pyodbc module and create a database connection string that you can pass into the driver's *connect()* function. 

```python
import pyodbc

server = 'database-server.database.windows.net'
database = 'database-name'
username ='your.name@microsoft.com'
Authentication='ActiveDirectoryInteractive'
driver= '{ODBC Driver 18 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+
                      ';SERVER='+server+
                      ';PORT=1433;DATABASE='+database+
                      ';UID='+username+
                      ';AUTHENTICATION='+Authentication
                      )

cursor = conn.cursor()
```

The DATABASE database server address and database name are not given to all items so I will not include them in this document. The DATABASE team will give you the server and database names when they provide you with access. Replace the text in the *server* and *database* variables with the real DATABASE server and database information.

The example above, when run, creates an interactive login session in a new web browser window. Enter your Microsoft password into the password prompt.

![Interactive login window](./Images/login.png){width=90%}

Enter your Microsoft password into the password prompt. 

### Alternative to connection strings (on Windows)

Another way to create a connection string is to [create a Data Source  (DSN)](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows) using the *ODBC Data Sources* app. This is a Windows-only feature and it lets you avoid entering database information in your code. 

It's probably better to enter the information as a connection string in your code or to use [environment variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3) if you do not want to hard-code database and use information in your code. 

Just to be complete, we record the procedure for creating and using a DSN in *Appendix A: Data Source Names*.

## Check that the connection is successful

A quick way to check that the connection is working is to get teh database server;s version information. Create a simple T-SQL statement using the [T-SQL *@@VERSION* function](https://learn.microsoft.com/en-us/sql/t-sql/functions/version-transact-sql-configuration-functions?view=sql-server-ver16).

```python
statement = "SELECT @@version;"

cursor.execute(statement) 

print(cursor.fetchone())
```

This should print the version of SQL Server software running on DATABASE. 

## Read database schemas information

You need information about the which DATABASE database schemas are available to you. Read the database documentation, or use Python code to analyze the database using one of the three procedures shown below.

### Schema names returned by the *cursor.tables()* method

Using the *pyodbc* connection object, create an instance of the [pyodbc cursor](https://github.com/mkleehammer/pyodbc/wiki/Cursor) using the connection's *cursor()* function

```python
cursor = conn.cursor()
```

Then, iterate through all tables in the object returned by the cursor's *tables()* method.

```python
for table_name in cursor.tables():
    print(table_name)
```

This lists all tables in a table with columns showing the database name, schema name, and table name. You see many rows listed. The available schemas are in the second column.

```
('xxxx', 'sys', 'xxxx', 'TABLE', None)
('xxxx', 'sys', 'xxx', 'TABLE', None)
('xxxx', 'xxxx', 'xxxx', 'VIEW', None)
...
```

Above works if you have no idea what is in the database. But, it shows lots schemas and tables that you may not have access to. 

### Get data from the *INFORMATION_SCHEMA.VIEWS* table

To get information about DATABASE schemas that you have permission to read, look for the system table called INFORMATION_SCHEMA.VIEWS. The [Microsoft T-SQL documentation](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-) states that the INFORMATION_SCHEMA.VIEWS table contains a column named *TABLE_SCHEMA* that shows all the schemas available to the user in the database.

Create a T-SQL statement that selects the TABLE_SCHEMA column in the table and sorts data alphabetically:

```python
statement = """
SELECT DISTINCT
  TABLE_SCHEMA
FROM INFORMATION_SCHEMA.VIEWS
ORDER BY TABLE_SCHEMA
"""
```

Then execute the statement using the cursor's *execute()* function. This places the data results in the cursor. You can get all the results at once using the cursor object's *fetchall()* method

```python
cursor.execute(statement)

print(cursor.fetchall())
```

This shows the DATABASE schemas that you have permission to read.

```
[xxxxxxx]
```

Interestingly, [Microsoft's SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/system-information-schema-views/system-information-schema-views-transact-sql?view=sql-server-ver16) states that the only reliable way to gather information is to query the *sys.objects* catalog view. I found the *INFORMATION_SCHEMA.VIEWS* table to be simpler to use and to contain accurate information. But, to be complete, I discuss the *sys.objects* catalog view below.

### Get data from the *sys.objects* table

Another way to get schema information is to query the [sys.objects](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-objects-transact-sql?view=sql-server-ver16) catalog view in the SQL Server database. 

The T-SQL statement below [^2] finds all the scheme IDs in the *sys.objects* view and then finds their schema names in the *sys.schema* table by joining on the schema ID.

[^2]: Statement copied from StackOverflow post *[SQL Server - Return SCHEMA for sysobjects](https://stackoverflow.com/a/917431)* (917431)

```python
statement = """
SELECT DISTINCT sys.schemas.name AS schema_name
FROM sys.objects 
INNER JOIN sys.schemas ON sys.objects.schema_id = sys.schemas.schema_id
ORDER BY schema_name
"""

cursor.execute(statement)
schema_list = cursor.fetchall()
print(schema_list)
```

The schema information is the same as was gathered from the *INFORMATION_SCHEMA.VIEWS* table.

```
[xxxxxx]
```

### Recommended information gathering tool

We recommend using the [cursor object's methods](https://code.google.com/archive/p/pyodbc/wikis/Cursor.wiki) to gether database information. It is easier to get information from cursor methods about table columns, primary keys, and table relationships, as you will see below.


## Read database table names

The next step is to choose one of the database schemas and list all tables in it that you have permission to read.

### Table names returned by the *cursor.tables()* method

Use the cursor object's *tables()* method again but pass it a schema parameter so it lists only tables from the schema you are interested in exploring. In this example, you will generate a list of tables in the *xxxx* schema.

```python
cursor = conn.cursor()

for row in cursor.tables(schema='xxxx'):
    print(row[2], sep=", ")
```

In this example, we wanted the table name from each row. We knew that the tables names were in the third column so we iterated through each row and generated the output seen below: 

```
xxxxxx
```

### Alternative approaches using SQL queries

As before, when we listed schema names, you can query either the *INFORMATION_SCHEMA.VIEWS* table or the *sys.objects* catalog view. 

To get the table name information from the *INFORMATION_SCHEMA.VIEWS* table, create the following SQL statement and then execute it.

```python
statement = """
SELECT
  TABLE_NAME
FROM INFORMATION_SCHEMA.VIEWS
WHERE TABLE_SCHEMA = 'xxxxxxx'
ORDER BY TABLE_NAME
"""

cursor.execute(statement)
for row in cursor.fetchall():
    print(*row)
```

As another alternative, to get the table name information from the *sys.objects* catalog view, create the following SQL statement and then execute it.

```python
statement = """
SELECT sys.objects.name AS table_name
FROM sys.objects 
INNER JOIN sys.schemas ON sys.objects.schema_id = sys.schemas.schema_id
WHERE sys.schemas.name = 'xxxxx'
"""

cursor.execute(statement)
for row in cursor.fetchall():
    print(*row)
```


## Read columns in database tables

Finally, we need the list of columns in each table we plan to use, along with some of their attributes.

### Column information returned by the *cursor.columns()* method

In this example, we will get information about the columns in one of the tables. Choose the table named *Interesting Table* from the *xxxx* schema. Use the *cursor.columns()* method to get a list of table information. In the example below, you get the headers for the returned information from the *cursor.description* attribute. The column name, type, and size are in the fourth, sixth, and seventh column of the returned results.

```python
column_list = (
    cursor.columns(
        table='Interesting Table', 
        schema='xxxx')
    .fetchall()
)

# headers
headers = [h[0] for h in cursor.description]
print(f'{headers[3]:{25}}{headers[5]:{20}}{headers[6]:{11}}')

# data
for row in column_list:
    print(f'{row[3]:{25}}{row[5]:{20}}{row[6]:{6}}')
```

The output print out column information until all 313 columns from the table are listed.

```
column_name              type_name           column_size
xx                       varchar                 10
...
```


### Alternative approaches using SQL queries

As before, when we listed table names, you can query either the *INFORMATION_SCHEMA.COLUMNS* table or the *sys.objects* catalog view. 

To get the column name information from the *INFORMATION_SCHEMA.COLUMNS* table, create the following SQL statement and then execute it.

```python
statement = """
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Interesting Table'
"""
```

As another alternative, to get the column name information from the *sys.objects* catalog view, create the following SQL statement and then execute it.

```python
statement = """
SELECT 
   sys.columns.name AS column_name, 
   sys.types.name AS column_type, 
   sys.columns.max_length AS length
FROM sys.objects 
INNER JOIN sys.columns ON sys.objects.object_id = sys.columns.object_id
INNER JOIN sys.types ON sys.types.system_type_id = sys.columns.system_type_id
WHERE sys.objects.name = 'Interesting Table'
AND sys.types.name != 'sysname'
"""
```

You can see that using the column object's methods is consistently the simpler way to get information about the database schema.

## Find table constraints

Normally, database tables are defined with constraints such as a primary key and foreign keys.

Use the cursor object's *primaryKeys()* and *foreignKeys()* methods to determine if any columns in the table are primary keys or foreign keys:

```python
table = 'Interesting Table'
schema = 'xxxx'

primary_keys = cursor.primaryKeys(table=table, schema=schema).fetchall()
print(f"{table}:  Primary Keys = {primary_keys}")

foreign_keys = cursor.foreignKeys(table=table, schema=schema).fetchall()
print(f"{table}:  Foreign Keys = {foreign_keys}")
```

You will see that the *Interesting Table* view has no primary or foreign keys. 

```
Interesting Table:  Primary Keys = []
Interesting Table:  Foreign Keys = []
```

In fact, none of the views in the DATABASE database have primary keys defined. This acceptable when you are only reading data from the database. The primary key, foreign keys, and other constrains define relationships between tables in a relational database. Knowing the database relationship information is helpful, but not necessary, when reading information from tables. 

## Read data from selected columns in a table

Now that you have found the schemas, tables, and columns that contain the data you are interested in, you can select the specific data you need using T-SQL statements with the pyodbc driver's *cursor.execute()* method.

For example, to gather a little bit of data about five randomly-selected items, run teh following code:

```python
statement = """
SELECT TOP 5 "Two", "Five", "Three", "Four"
FROM xxxx."Interesting Table"
ORDER BY NEWID()
"""

cursor.execute(statement)

headers = [h[0] for h in cursor.description]
print(*headers, sep=", ")

data_list = cursor.fetchall()
for row in data_list:
    print(*row, sep=", ")
```

The output lists the selected data and will be different each time the statement is executed.

```
zzzzz
```

## Convert data to a Pandas data frame

Data analysts will usually find it more convenient to work in a data frame framework like Pandas. You can easily convert results returned from the pyodbc driver into data frames using the *pandas.DataFrame.from_records()* method, as shown below.

```python
import pandas as pd

statement = """
SELECT TOP 5 "Two", "Five", "Three", "Four"
FROM xxxx."Interesting Table"
ORDER BY NEWID()
"""

cursor.execute(statement)

headers = [h[0] for h in cursor.description]
data_list = cursor.fetchall()

dataframe = pd.DataFrame.from_records(data_list, columns=headers)
print(dataframe)
```

The program prints the new data frame below. You can see at least one of the benefits of working with data frames is that they format data well when printing.

```
zzzz
```

## Read data directly to a Pandas data frame

You can also use Pandas to directly read data from the *pyodbc* driver. This is more efficient when reading large amounts of data. Use the *Pandas.read_sql()* method and pass it the SQL statement and the database connection object created by the pyodbc driver.

```python
data = pd.read_sql(statement, conn)
print(data)
```

You can see pandas read in another five random rows directly into a dataframe.

```
zzzzz
```

But this also produces a warning in Jupyter Notebooks:

```
UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
  data = pd.read_sql(statement, conn)
```

We'll discuss SQLAlchemy more in the next chapter. If you wish to use Pandas to read from the database, and are familiar with T-SQL syntax, then you only need to know how to set up an SQLAlchemy engine. After that, you can use Pandas with raw T-SQL queries just like the example above.

## Read entire tables into Pandas dataframes

If you have enough memory on your PC, you can read entire tables from DATABASE into Pandas for analysis. The *Pandas.read_sql_table()* method does not work with DATABASE database views. You need to create an SQL statement that requests all data in the view and run it with the *Pandas.read_sql()* method.

Do not run the following code unless you really want all the data in a table. DATABASE database tables can be very large and it can take hours to download all the data. 

To download all rows in the ** table into a Pandas data frame, run the following code.

```python
statement = 'SELECT * FROM xxxx."Interesting Table"'

data = pd.read_sql(statement, conn)

print(data.head(3))
```

You can download multiple DATABASE database tables into different data frames and then use Pandas to perform joins, filtering, pivot tables, data cleaning, and other analysis operations.

# SQLAlchemy ORM

[SQLAlchemy](https://www.sqlalchemy.org/SQLAlchemy) is an [Object Relational Mapper (ORM)](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements. SQLAlchemy provides a standard interface that allows developers to create system-agnostic code that communicates with a wide variety of data engines. [^3] 

You only need to learn a little bit about SQLAlchemy to read data from the DATABASE database. You will learn how to gather information about an existing database's schemas and to build complex, powerful SQL queries that read data from tables and views.

[^3]: From https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/ on March 23, 2023

## Why use SQLAlchemy to generate query statements?

The SQL language is relatively easy to use for simple database table queries. So, why would a Python programmer want to use SQLAlchemy ORM to build the SQL statements?

When working with large and complex databases, users must ensure their SQL statements are optimized. Un-optimized queries can produce the same data as optimized queries but may use up significantly more resources. The SQLAlchemy ORM will output query statements using industry standard optimizations.

Different SQL servers support variations on the SQL language so an SQL statement that works on SQLite might not work on Microsoft SQL Server or on Azure Databricks. Programmers can configure the SQLAlchemy ORM to create different SQL statements for different data storage systems, as long as they avoid using proprietary SQL functions. 

Finally, Python programmers may prefer to use SQLAlchemy to create query statements because it allows them to use Python code to express database queries. They may invest their time learning SQLAlchemy instead of learning [multiple SQL language dialects](https://towardsdatascience.com/how-to-find-your-way-through-the-different-types-of-sql-26e3d3c20aab). They may even use [SQLAlchemy instead of the DataBricks API](https://pypi.org/project/sqlalchemy-databricks/) when working with the Microsoft Analytics Platform.


## Connect to the DATABASE database

Create the [connection string](https://dev.to/chrisgreening/connecting-to-a-relational-database-using-sqlalchemy-and-python-1619#deconstructing-the-database-url) that tells SQLAlchemy which database driver to use, the location of the database, and how to authenticate access to it. 

```python
from azure.identity import InteractiveBrowserCredential

server_name = 'database-server.database.windows.net'
database_name = 'database-nme'
user_name = 'user.name@microsoft.com'
connection_string = (
    f"Driver={{ODBC Driver 18 for SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Authentication=ActiveDirectoryInteractive;"
    f"UID={user_name};PWD=''"
)
```

Replace the text in the *server_name*, *database_name*, and *user_name* variables with the real DATABASE server, database, and user information.

> **NOTE:** SQLAlchemy does not work with the Windows Data Source Name (DSN). Use the connection string, above, in your SQLAlchemy connection code.

Next, import the *create_engine()* function from SQLAlchemy and use it to create an [engine](https://docs.sqlalchemy.org/en/20/core/engines_connections.html) object which includes a connection to the database specified in the URL passed to the *create_engine* function.

```python
from sqlalchemy import create_engine
import pyodbc

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")
```

A login browser window will pop up when you perform your first database operation; either when you execute the *pandas.read_sql()* function described immediately below, or when you try to inspect your database schema for the first time.

## Read data directly to Pandas data frame

, in the previous chapter when we used the *pyodbc* driver's connection with the Pandas *read_sql()* method, Pandas raised a warning saying you should use an SQLAlchemy connection, instead. Now, we have an SQLAlchemy engine defined so let's try using it with Pandas to read data directly from the DATABASE database.

```python
import pandas as pd

statement = """
SELECT TOP 5 "Two", 
             "Five", 
             "Three", 
             "Four"
FROM xxxx."Interesting Table"
"""

data = pd.read_sql(statement, engine)
print(data)
```

In the output, the program prints the data frame.

```
zzzz
```

### Is this all you need to know?

Most data scientists, especially those comfortable working with raw T-SQL statements, will be happy to stop at this point and proceed to analyze data in the data frames they created from the entire contents of the DATABASE database view, or views. 

However, if you want to work mostly in Python and employ the power of SQLAlchemy to select the data you need from the database before you import it into a data frame, you may want to learn more about how to use the SQLAlchemy ORM. 


## Use SQLAlchemy to read schemas in a database

First, you need to understand the structure of the database. You need to determine what tables exist and what data each table contains. Hopefully, you have documentation that provides this information. If not, you can acquire this information with a few lines of Python code.

Use the [SQLAlchemy *inspection* function](https://docs.sqlalchemy.org/en/20/core/inspection.html#module-sqlalchemy.inspection) to gather information about database schema, tables, and columns. This will be helpful when you need to create SQLAlchemy ORM classes or Table objects in your Python program. 

```python
from sqlalchemy import inspect

inspector = inspect(engine)

schema_list = inspector.get_schema_names()
print(schema_list )
```

The output is shown below

```
[zzzz]
```

The schema list is different than when you used the *pyodbc* driver because we looked through the INFORMATION_SCHEMA.VIEWS table or the *cursor* object when we used the ODBC driver so, in that case, you saw only the views that you have permission to read. In this case, you see all schemas in the DATABASE database, even the ones you do not have permission to read.

There [does not seem to be a way to read the](https://stackoverflow.com/questions/64260249/how-to-read-a-table-from-information-schema-using-sql-alchemy) [INFORMATION_SCHEMA.VIEWS table](https://github.com/sqlalchemy/sqlalchemy/blob/main/lib/sqlalchemy/dialects/mssql/information_schema.py) using SQLAlchemy's *inspect()* function.

To get a list of onl;y the schemas you have permission to read, ue a raw T-SQL statement with SQLAlchemy and read it with Pandas (because we already showed you how to get database information using Pandas). See the example below:

```python
statement = """
SELECT DISTINCT
  TABLE_SCHEMA
FROM INFORMATION_SCHEMA.VIEWS
ORDER BY TABLE_SCHEMA
"""

data = pd.read_sql(statement, engine)
print(data)
```

The output shows only the database schemas that you have permission to read.

```
zzzz
```


## Read database tables in a schema

Get a list of the tables available in the schema you wish to explore. Use the *inspector* instance's *get_table_names()* method to list the tables in the *xxxx* schema.

```python
table_list = inspector.get_table_names(schema='xxxx')

print(table_list)
```

The output is an empty list. 

```
[]
```

The list is empty because DATABASE does not allow you to access its tables directly. It provides you with database views, instead. This allows the DATABASE administrators to better manage security and access. Views are treated mostly like tables by SQLAlchemy, except that they do not have primary keys or relationship information so that makes the SQLAlchemy ORM a bit more difficult to configure. You'll see this later when you reflect the database metadata. 

To get a list of views available in the *xxxx* schema, use the *get_view_names()* method.

```python
table_list = inspector.get_view_names(schema='xxxx')

print(table_list)
```

This outputs a list of seventeen views.

```
['Interesting Table', ]
```

## Read column information from a database table

Views are treated like tables in the database metadata so you may use the *inspector* instance's *get_columns()* method to list columns in a specified view, in a specified schema.  

```python
columns_list = inspector.get_columns(
    'Interesting Table', 
    schema='xxxx')
print(*columns_list[0].keys(), sep=", ")
for x in columns_list:
    print(*x.values(), sep=", ")
```

The output shows the columns and their attributes such as data type, nullability, and default value.

```
zzzz
...
```

The output continues to print out column information until all 313 columns are listed.

## Declare *Table* objects

The SQLAlchemy documentation recommends you use [Declarative Mapping](https://docs.sqlalchemy.org/en/20/orm/declarative_mapping.html) to manually build SQLAlchemy Table objects or ORM classes that enable programmers to access table data. 

Describing database information in your Python program as classes enables other program maintainers learn about the database by reading the Python code. This makes it easier for Python programmers to maintain the code. It also makes a program more robust because changes in the DATABASE database schema will either have no effect on your program, or will cause an obvious error. Declarative Mapping is also much faster than using database reflection, which we will discuss later, every time you run your Python program.

In the examples below, you declare a subset of the *xxxx.Interesting Table* view's columns so you can access data in them as Python objects.

### Declaring a *Table* object

When you inspected the database schema, you saw the column information for each table. Use this information to describe a *Table* object that defines the columns you want programmers to be able to access.

```python
from sqlalchemy import MetaData, Table, Column, String

metadata = MetaData()

interesting_table = Table(
    'Interesting Table',
    metadata,
    Column('One', String(10), primary_key=True),
    Column('Two', String(8)),
    Column('Three', String(256)),
    Column('Four', String(48)),
    Column('Five', String(100)),
    schema='xxxx'
)
```

In the example above, you created an empty [metadata object](https://docs.sqlalchemy.org/en/20/core/metadata.html). Then, you used the SQLAlchemy Table class to add table schema, name, and column information to the metadata. This metadata will be used by SQLAlchemy when you want to select data from the database. You can define more tables if you need them.

You do not need to specify which columns is the primary key when you create a Table object, but you probably should. When you want to address the columns in the table, you need to get them from the table's *columns* attribute which also is available via the alias, *c*. For example, execute the following code to list some data from the table:

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

stmt = select(
    interesting_table.columns['Two'], 
    interesting_table.c['Three'], 
    interesting_table.c['Four']).limit(5)

with Session(engine) as session:
    result = session.execute(stmt)
    columns = result.keys()
    data = result.all()

print(*columns, sep=", ")
for x in data:
     print(*x, sep=", ")
```

This will print out the following output:

```
zzzzzz
```

### Declaring a table as an SQLAlchemy ORM Class

You can [declare a table](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html) as an ORM class. ORM classes are used similarly to Table objects, except an SQLAlchemy ORM class *must* include a primary key. 

Using SQLAlchemy ORM classes simplifies the *select()* statement syntax a little bit because the columns are defined directly by class attributes. For example, when selecting data, you do not need to index the *columns* attribute as you did in the earlier example when you used a Table object. 

> **NOTE:** You can use SQLAlchemy with Table objects. But, if you want to use the SQLAlchemy ORM in the "proper" way, you should use tables defined in ORM classes. All examples later in this chapter assume you defined ORM classes.

As an example of declaring an ORM class, declare the same table as in the example above but as a class:

```python
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Interesting_Table(Base):
    __tablename__ = "Interesting Table"
    __table_args__ = {"schema": "xxxx"}
    
    one = mapped_column("One", String(10), primary_key=True)
    two = mapped_column("Two", String(8))
    three = mapped_column("Three", String(256))
    four = mapped_column("Four", String(48))
    five = mapped_column("Five", String(100))
```

In the example above, The Base class contains an empty *Base.metadata* object. Then, you used the SQLAlchemy Table class to add table schema, name, and column information to *Base.metadata*.

After creating the class *Interesting_Table*, you can access the defined database fields by calling the class attribute associated with each one. For example, access data in the *two* column using the statement, `select(Interesting_Table.two)`.

Execute the following code to list some data from the table:

```python
stmt = select(
    Interesting_Table.two, 
    Interesting_Table.three, 
    Interesting_Table.four).limit(5)

with Session(engine) as session:
    result = session.execute(stmt)
    columns = result.keys()
    data = result.all()

print(*columns, sep=", ")
for x in data:
     print(*x, sep=", ")
```

This produces the following output. You can see that the column keys have been changed so they match the class attributes you defined. This is the other difference you get when defining an ORM class and, it's actually useful when converting database results into data frames.

```
zzzzz
```


### Get table metadata via database reflection

Instead of explicitly declaring table metadata using Declarative Mapping, you could employ [database reflection](https://betterprogramming.pub/reflecting-postgresql-databases-using-python-and-sqlalchemy-48b50870d40f), which is the process of automatically building new objects based on an existing database's schema information. It is useful when writing simple, single-use scripts like the ones in this document. But, it takes time to reflect the database tables. If you are writing more complex programs, you should use the declarative mapping process described earlier to get better performance.

Normally, you would expect that you could use the [SQLAlchemy Automap extension](https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html) to map database tables and relationships to SQLAlchemy ORM classes. However, SQLAlchemy can only map the DATABASE views into *Table* objects because the DATABASE database access is restricted. 

DATABASE users typically do not have access to database tables. Access to DATABASE is provided by database views created by the DATABASE team. These views have no primary keys defined. Since ORM classes must have a primary key, SQLAlchemy's automap extension will map the views into table objects but will not automatically create classes that represent tables. You may manually create classes from the mapped Table columns, instead.

There are multiple [reflection schemes](https://docs.sqlalchemy.org/en/20/core/reflection.html#metadata-reflection-schemas) that programmers may employ. 

You can reflect  in a schema, which takes a long time: five or six minutes.

```python
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

metadata = MetaData()
metadata.reflect(engine, views=True, schema="xxxx")
metadata.reflect(engine, views=True, schema="supplemental")
Base = automap_base(metadata=metadata)
Base.prepare()
```

You used SQLAlchemy's *automap_base* function to create a [declarative base class instance](https://docs.sqlalchemy.org/en/20/orm/extensions/automap.html#basic-use) named *Base* and then used its *prepare* method to automatically map, or *reflect*, the database schema metadata.

```python
print(*Base.metadata.tables.keys(), sep="\n")
```

You see the *Base.metadata* object contains information about all the tables in the *supplemental* and *xxxx* schemas.

```
xxxx.Interesting Table
...
```

Database reflection is faster way if you specify the tables you want to reflect in each schema, so you do not gather data you do not need.

```python
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

metadata = MetaData()
metadata.reflect(engine, views=True, schema="xxxx", only=['Interesting Table'])

Base = automap_base(metadata=metadata)
Base.prepare(engine)
```

Now, if you print the metadata, you see it only contains information about the two tables you specified.

```python
print(*Base.metadata.tables.keys(), sep="\n")
```

The output shows two table names:

```
xxxx.Interesting Table
```

You will notice that the reflection took much less time; about 30 seconds, this time.

Now, you can access tables using the *Base.metadata* object. For example, the *Interesting Table* table can be accessed with the statement, `Base.metadata.tables['xxxx.Interesting Table']`. You can assign tables to new variables to make them wasier to work with in your code:

```python
interesting_table = Base.metadata.tables['xxxx.Interesting Table']
```

Now, you can get table data from the new table variable. For example:

```python
print(interesting_table.name)
```

The above cose lists the name of each table. So, we know the variable points to the correct table information in the *Base.metadata* object.

```
Interesting Table
```

You can access table column information from the table variable you just created. For example, you can get column names:

```python
print(interesting_table.columns.keys())
```

The *columns.key()* method listed the column names in the *Interesting Table* table. 

```
xxzz ,...]
```

It is possible to build select statements by indexing table columns. For example, the following statement selects five rows from three columns from the *Interesting Table* table:

```python
stmt = select(
    interesting_table.columns['Two'], 
    interesting_table.columns['Three'],
    interesting_table.columns['Four']
).limit(5)
```

But we want to use the SQLAlchemy ORM, which means we need to represent tables as ORM classes. One way to do this is to use Declarative Mapping, which we described earlier. 

Another way to do this is to build a class from reflected table metadata, as shown below. You cannot use [normal table reflection techniques](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapping-declaratively-with-reflected-tables) because the DATABASE views do not have primary keys, and use spaces in their column names. Instead, we simply [create ORM class attributes](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#alternate-attribute-names-for-mapping-table-columns) that point to table columns metadata.

```python
class Interesting_Table(Base):
    __table__ = interesting_table
    
    one = interesting_table.columns['One']
    two = interesting_table.columns['Two']
    three = interesting_table.columns['Three']
    four = interesting_table.columns['Four']
    five = interesting_table.columns['Five']
```

The class shown above defines attributes associated with specific table columns, [including a primary key](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapping-to-an-explicit-set-of-primary-key-columns). While you still have to define the specific columns you want to use in the class, each column already has all its attributes, such as data types or nullability, defined from the reflected metadata. 

Now that tables are represented as class attributes, you can select data in table columns using the syntax of class attributes, as shown below:

```python
stmt = select(
    Interesting_Table.two, 
    Interesting_Table.three, 
    Interesting_Table.four
).limit(5)
```

The class attribute syntax is easier to work with compared to the table metadata index syntax and it is the same as if you were working with either reflected tables or tables defined using Declarative Mapping.

### Recommendation

Is above example any better than declarative mapping? Since we cannot automatically reflect ORM classes from DATABASE views, it may be better to define tables using Declarative Mapping after you have decided which columns you need for your application.

## Read data from selected columns in a table

Use the SQLAlchemy [*select()* function](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html) to create SQL SELECT statements and that read rows from tables in the database. The *select()* function returns an instance of the SQLAlchemy *Select* class, which offers methods that can be chained together to provide all the information the Select object needs to output an SQL query.

Use the SQLAlchemy guides, [*Using Select Statements*](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html) and the [*ORM Querying Guide*](https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html) as references when you need to look up additional methods to build the SQL queries you need.

The following code builds an SQL query that selects the first five rows in the DATABASE database's *Interesting Table* table. 

```python
stmt = select(
    Interesting_Table.two, 
    Interesting_Table.three, 
    Interesting_Table.four
).limit(5)
```

The *stmt** variable name is assigned to the SQLAlchemy Select object returned by the *Select()* function. Pass it to the Session object to get the results of the generated SQL query from the database.


```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    result = session.execute(stmt)
    headers = result.keys()
    data = result.all()

print(*headers, sep=", ")
for x in data:
     print(*x, sep=", ")
```

You will see data from the first five rows of the selected columns in the printed output:

```
yyyy
```

## Convert data to a Pandas data frame

Data analysts will usually find it more convenient to work in a data frame framework like Pandas. You can easily convert results returned from SQLAlchemy ORM select statement results into data frames using the *Pandas.DataFrame()* class, as shown below

```python
df1 = pd.DataFrame(data, columns=headers)
print(df1)
```

The converted dataframe was printed out, as shown below:

```
yyyy
```

## Do operations in SQL database

### in Python

You can use the SQLAlchemy *func()* function to call native functions that will run on the SQL Server. In the following example, we call SQL Server's *COUNT()* function to count the number of items in the table. Then we filter that count by country and/or status, using the *where()* method. 

```python
from sqlalchemy import func

stmt0 = (select(func.count(Interesting_Table
                           .one)))

stmt1 = (
    stmt0
    .where(Interesting_Table
           .two == "Canada")
    .where(Interesting_Table
            .three == "Active")
)

stmt2 = (stmt0
        .where(Interesting_Table
               .three == "Active"))

with Session(engine) as session:
    result = session.scalar(stmt0)
    print(f"Total Rows in table:  {result}")
    result = session.scalar(stmt2)
    print(f"Total Active in table:  {result}")
    result = session.scalar(stmt1)
    print(f"Total Active in Canada:  {result}")
```

```
Total Rows in table:  10000
Total Active in table:  9000
Total Active in Canada:  1000
```

If you have very large data sets, you can imagine how useful it can be to filter data before it is loaded into Python objects.

### SQL functions

The SQAlchemy *func()* function has many methods that allow you to run [SQL functions](https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16) on the SQL server. [^4] To select data from a random sample of five items, run the SQL Server's [*NEWID()* T-SQL function](https://learn.microsoft.com/en-us/sql/t-sql/functions/newid-transact-sql?view=sql-server-ver16#d-query-random-data-with-the-newid-function). Create a statement like the following:

[^4]: Each version of SQL support different functions. For example, if you wanted to analyze data from a random sample of five items, you would use the *NEWID()* T-SQL function. But, other SQL database engines provide functions like *RANDOM()* or *RAND()* to do the same thing. You have to know what functions are available on the server you are using, and using functions may make your code less universal.

```python
stmt = (
    select(
        Interesting_Table.two, 
        Interesting_Table.three, 
        Interesting_Table.four)
    .order_by(func.newid())
    .limit(5)
)

with Session(engine) as session:
    result = session.execute(stmt)
    columns = result.keys()
    data = result.all()

print(*columns, sep=", ")
for x in data:
     print(*x, sep=", ")
```

Every time you execute the statement, you get a different set of data. One iteration of the results is shown below.

```
yyyy
```
### Convert SDQLAlchemy database results to Pandas data frame

As you can see, programmers can use a *Select* instance's methods to perform complex queries and can chain these instance methods.

The results of an SQL query can be converted to a Pandas data frame using the *pandas.DataFrame* class.

For example, create an SQL statement that groups items by country, counts the number of items in each country, and sorts the results in descending order. Then convert the result into a Pandas data frame.


```python
from sqlalchemy import desc

statement = (
    select(Interesting_Table.country_office_name,
           func.count(Interesting_Table.item_id).label("Num_Items")
           )
    .group_by(Interesting_Table.three)
    .order_by(desc("Num_Items"))
)

with Session(engine) as session:
    result = session.execute(statement)
    headers = result.keys()
    results = result.fetchall()

countries = pd.DataFrame(results, columns=headers)
print(countries)
```

```
zzzz
```


## Joining DATABASE tables

You can create SQL statements that join data in multiple tables using the [SQLAlchemy *Select* class's *join()* and *join_from()* methods](https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#joins).

However, because the DATABASE views do not have primary keys and do not have relationships defined between views, it is probably better to get the data you need by loading selected data from multiple tables into separate data frames and then using Pandas to join the data frames according to your needs.

If you really want to perform joins on the SQL server, then you should build your SQLAlechemy ORM model using [Declarative Mapping](https://docs.sqlalchemy.org/en/20/orm/declarative_mapping.html) and carefully define the primary keys and relationships constraints such as foreign keys in the table classes you create. Or, you can manually specify columns on which to join tables in the *select* statement.

## Read entire tables into Pandas dataframes

As we saw in the pyodbc driver section, you can read entire tables from DATABASE into Pandas for analysis. The *Pandas.read_sql_table()* method does not work with DATABASE database views. The *Pandas.read_sql()* method will work but you must create Table objects using Declarative Mapping or database reflection and then pass the table to the SQLAlchemy *select()* function.

### Using declarative mapping

Do not run the following code unless you really want all the data in a table. DATABASE database tables can be very large and it can take hours to download all the data. To download all rows in the *Interesting Table* table into a Pandas data frame, run the following code.

```python
metadata = MetaData()

Interesting_Table = Table(
    'Interesting Table',
    metadata,
    Column('One', String(10), key='one', primary_key=True),
    Column('Two', String(8), key='two'),
    Column('Three', String(256), key='three'),
    Column('Four', String(48), key='four'),
    Column('Five', String(100), key='five'),
    # ...
    # add 308 more columns to this table
    # ...
    schema='xxxx'
)

statement = select(Interesting_Table).limit(2)

data = pd.read_sql(statement, engine)
print(data.head(3))
```

Using Declarative Mapping to define a table with 313 columns is a lot of work and is not practical for short, single-use scripts like this. But, maybe you have already carefully defined the columns you need in SQLAlchemy Table objects and maintain them in another file for use in more complex programs. 

### Using database reflection

If you are just exploring data and performance is not an issue, consider using database reflection. The following code reflects the metadata for the table we want and passes it to the SQLAlchemy *select()* function. 

When reading data with Pandas, you do not need to create an ORM class. You can define the reflected table simply by indexing it in the *Base.metadata* object.

Again, don't run this code unless you want to wait about an hour for the process to finish and you have at least 2 GB of memory free on your PC.

```python
metadata = MetaData()
metadata.reflect(engine, 
                 views=True, 
                 schema="xxxx", 
                 only=['Interesting Table'])

Base = automap_base(metadata=metadata)
Base.prepare(engine)

Int_Tbl = (Base.metadata
                .tables['xxxx.Interesting Table'])

statement = select(Int_Tbl)

data = pd.read_sql(statement, engine)
print(data.head(3))
```

### Using raw T-SQL is simpler

Actually, it is simpler to use a raw T-SQL query statement to select all information in an DATABASE view, like we did at the start of the SQLAlchemy chapter. The following statement will read all rows from the *Interesting Table* into a pandas data frame:

```python
statement = 'SELECT * FROM xxxx."Interesting Table"'

data = pd.read_sql(statement, engine)
print(data.head(6))
```

You can download multiple DATABASE database tables into different data frames and then use Pandas to perform joins, filtering, pivot tables, data cleaning, and other analysis operations.


# Conclusion

We showed you two tools that make it easier for Python programs to access data in the DATABASE database. 

We first demonstrated the *pyodbc* library. Using the *pyodbc* database connection and its cursor function, along with statements generated in T-SQL syntax, we can select data from the DATABASE database and store it in Python objects. We can also convert database data into Pandas data frames for further analysis.

Next, we demonstrated the *SQLAlchemy* package. You can use an SQLAlchemy connection along with raw T-SQL statements to read data from the DATABASE database directly into a Pandas data frame. You can also use the SQLAlchemy package's *Select* class to build SQL statements in a "pythonic" way, which allows Python programmers to work in Python and avoid learning the details of SQL syntax. 

## Summary of recommendations

Because you are just reading data from DATABASE, you should use the driver which is best supported by the data analysis library you are using. For example, if you are using Pandas, you would create a database connection using SQLAlchemy. 

Most data scientists will need to learn SQL. Raw T-SQL statements can be used with either *pyodbc* or *SQLAlchemy* functions. So, we recommend you learn the basics of T-SQL *SELECT* statements and then  create T-SQL statements to get data, regardless of the database driver you use. 

Although you don't need to use the SQLAlchemy ORM model to generate SQL statements in simple programs, you may still decide to learn how to use the SQLAlchemy ORM if you create complex programs. If you are a Python programmer who does not want to use raw SQL syntax in your Python, you might want to use the SQLAlchemy ORM. SQLAlchemy's features are helpful if you work with multiple developers on the same project.

