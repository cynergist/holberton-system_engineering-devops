# 0x14. MySQL

## Resources
[What is a database?](https://searchsqlserver.techtarget.com/definition/database) </br >
[Developing a SQL Server Backup Strategy](https://www.databasejournal.com/features/mssql/developing-a-sql-server-backup-strategy.html) </br >
[How To Set Up Master Slave Replication in MySQL](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql) </br >
[How To Choose a Redundancy Plan To Ensure High Availability](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication) </br >

## Tasks
0. Install MySQL // get MySQL installed on both `web-01` and `web-02` servers.

1. Let us in! // create a user and password for both MySQL databases which will allow the checker access to them.

2. If only you could see what I've seen with your eyes // have a database with at least one table and one row in your primary MySQL server (`web-01`) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Ensure that `holberton_user` has `SELECT` permissions on `nexus6` so that we can check that the table exists and is not empty.

3. Quite an experience to live in fear, isn't it? // Before getting started with the primary-replica synchronization, one more thing needs to be in place. On your primary MySQL server (`web-01`), create a new user for the replica server.

- The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you'd like.
- `replica_user` must have the appropriate permissions to replicate your primary MySQL server.
- `holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.

4. Setup a Primary-Replica infrastructure using MySQL //
- MySQL primary must be hosted on `web-01` - do not use the bind-address, just comment out this parameter
- MySQL replica must be hosted on `web-02`
- Setup replication for the MySQL database named `tyrell_corp`
- Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`
- Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`

5. MySQL backup // a Bash script that generates a MySQL dump and creates a compressed archive out of it.

Requirements:

- The MySQL dump must contain all MySQL databases
- The MySQL dump must be named `backup.sql`
- The MySQL dump file has to be compressed to a `tar.gz` archive
- This archive must have the following name format: `day-month-year.tar.gz`
- The user to connect to the MySQL database must be `root`
- The Bash script accepts one argument that is the password used to connect to the MySQL database