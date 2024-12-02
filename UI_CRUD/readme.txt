run this REST API flask project with postgre sql Database:

Install postgre sql:

Here’s a step-by-step guide to installing and setting up PostgreSQL on Ubuntu and setting the default password to 123:

Step 1: Update System Packages -
$ sudo apt update && sudo apt upgrade -y

Step 2: Install PostgreSQL -
$ sudo apt install postgresql postgresql-contrib -y

Step 3: Start and Enable PostgreSQL Service - 
$ sudo systemctl start postgresql
$ sudo systemctl enable postgresql

Step 4: Switch to PostgreSQL User - 
$ sudo -i -u postgres

Step 5: Access PostgreSQL Shell - 
$ psql

Step 6: Set Default Password - 
$ ALTER USER postgres PASSWORD '123';
Exit the psql shell:
$ \q
Exit the postgres user shell:
$ exit

Step 7: Allow Password Authentication - 
Edit the PostgreSQL configuration file to ensure password-based login is enabled:
1. Open the configuration file:
$ sudo nano /etc/postgresql/16/main/pg_hba.conf
2. Locate the following line:
$ local   all             postgres                                peer
3. Change peer to md5:
$ local   all             postgres                                md5
Save and exit (Ctrl+X, then y)

Step 8: Restart PostgreSQL -
Apply the changes by restarting PostgreSQL:
$ sudo systemctl restart postgresql

Step 9: Test the Configuration -
$ psql -U postgres -h localhost
 - Enter the password 123 when prompted.


Step 10. Create the New Database - 
Before running your Flask app, create the database in PostgreSQL. You can do this via the psql command-line tool:
$ psql -U postgres
$ CREATE DATABASE crud;

--------------------------------------------------------------------------------------------------


Verify the Changes = 
Test the connection:

$ psql -U postgres -h localhost -d crud

Using Flask-Migrate (Preferred for Production)
Flask-Migrate allows schema migrations with better control:

for creating tables:

Initialize migrations in your project:

$ flask db init
$ flask db migrate -m "Initial migration"
$ flask db upgrade

That's it...

Run your application using

$ flask run --host=0.0.0.0

you can visit =>  http://<your-instance-public-ip>:5000

perform some post put and delete task and check the table in the database with 

$ psql -U postgres -d your_database
$ SELECT * FROM items;


Thank You....