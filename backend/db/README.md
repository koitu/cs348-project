### MySQL usage notes
for the original `Entities.sql` and `Relationships.sql` files see milestone 1

To select the database to work on
```
use cs348;
```

To show tables in current database
```
show tables;
```

Delete and create database
```
delete database cs348;
create database cs348;
```

Make sure to commit changes using `con.commit()` or set `autocommit=True` when connecting