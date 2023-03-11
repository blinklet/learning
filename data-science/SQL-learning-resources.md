https://mystery.knightlab.com/
The SQL Murder Mystery is designed to be both a self-directed lesson to learn SQL concepts and commands and a fun game for experienced SQL users to solve an intriguing crime.

https://www.db4free.net/
click on Signup
Enter DB name, your MySQL username and password, and e-mail (for verification email)
* datascience01
* greygrey1984
* LyJVCi#bS7
* vendors@brianlinkletter.ca
Check email confirmation email
The go to phpMyAdmin to add data to the database
https://www.mysqltutorial.org/mysql-sample-database.aspx
rename so extension is .sql.zip
Import file into myPHP admin. Click on import button at bottomn
(cannot import because probably someone else already used the "classicmodels" database name)



https://accessexperts.com/blog/2021/12/07/wide-world-importer-database-for-access/

https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases#northwind_access

https://pypi.org/project/sqlalchemy-access/



blinklet
testtset001



DSN=SQL-Northwind;APP=Microsoft Office 2003;WSID=DELLNOTEBOOK;DATABASE=Northwind;Network=DBMSSOCN;Address=LOCALHOST;Trusted_Connection=Yes

"Provider='SQLOLEDB';Server='MySqlServer';" & _ 
 "Database='Northwind';Integrated Security='SSPI';"
 

Docker container with Northwind database
https://github.com/pthom/northwind_psql

Try Podman Desktop because Docker Desktop has license issues
https://podman-desktop.io/






# Exploring the database structure

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

To see all the information about each column in all the database tables, run the following code:

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
> PlaylistTrack is an *association table* so it is in the list of tables but not in the list of classes

Schema viewer
https://github.com/schemaspy/schemaspy



Examples of business analytics SQL queries on Chinook Database
https://m-soro.github.io/Business-Analytics/SQL-for-Data-Analysis/L4-Project-Query-Music-Store/

https://medium.com/analytics-vidhya/translating-sql-queries-to-sqlalchemy-orm-a8603085762b

