  GNU nano 2.0.9                                                         File: test.py                                                                                                              Modified

#! /usr/bin/python
import datetime
import psycopg2
from subprocess import call
# Postgres Backup Script
# Backs up and encrypts PG databases.
# Requires passwordless authentication for user. (e.g. .pgpass)

#Definitions

host = 'postgresql01'
user = 'admin'
gpgprofile = 'CertainDatabases'
backup_dir = '/home/python/scripts/'
psql = ' -U ' + user + ' -h ' + host
gpg = '|gpg -o '
starttime = datetime.datetime.now()
starttimestr = str(starttime.day) + str(starttime.month) + str(starttime.year) + str(starttime.hour) + str(starttime.minute)

try:
    conn = psycopg2.connect("dbname='gold' user='admin' host='postgresql01' password='3e3p0pCs'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database WHERE datistemplate = FALSE""")
rows = cur.fetchall()
for row in rows:
    print 'Processsing Database: ' + row[0]
    call('pg_dump ' + row[0] + psql + gpg + backup_dir + row[0] + starttimestr + '.gpg --encrypt --recipient ' + gpgprofile, shell=True)
endtime = datetime.datetime.now()
print starttime - endtime

