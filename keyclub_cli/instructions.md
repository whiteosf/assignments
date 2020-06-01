# Key Club Database CLI

The North Bergen High School chapter of [Key Club International](https://www.keyclub.org/) needs you to automate
its tracking of student volunteer hours. Additionally, the club needs to submit monthly and annual reports summarizing their service to the community. You will design the database and implement a simple command line interface for adding data and generating reports.

## Database
`keyclub.sqlite` is a [SQLite](https://sqlite.org) database with the following schema:
![keyclub.sqlite schema](img/kc_schema.png)

For clarification, the `officer` field in the `students` table is a boolean. It will hold a 1 if that student is *currently* an officer and a 0 otherwise. This defaults to 0.

For every school event where Key Club is active, there is always an officer present. Under `events`, the `officer_id` field is the `student_id` of the officer in charge for that event.

## Reports
The administration will need the following reports:
* Total service hours for the current service year
* Total service hours for the current month
