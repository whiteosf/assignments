# Querying the Chinook DB

## Instructions

You'll be creating a `VIEW` for each of the following queries. Once you've used an appropriate `SELECT` statement and generated a result set that you feel answers the question, save that query as a `VIEW` as follows:

**Example**: How many tracks have "rock" somewhere in the title?

```sql
select count(*) from tracks where name like '%rock%';
```

Once we feel like our query is correct, we can save the results as a `VIEW` as follows:

```sql
create view example as
select count(*) from tracks where name like '%rock%';
```

`VIEW` objects show up just like tables in your database.

For the questions below, name each view according to the number of the question it solves. For example, your answer to question 1 should be called `sol_1`.

## Queries

1. List all unique albums that are represented in the "Grunge" playlist.
2. How much total money was billed for the TV Show genre?
3. In which countries does Jane Peacock represent clients?
4. How many customers have no company listed?
5. What is the average amount of money spent by customers with gmail addresses?
