#! /usr/bin/python
import datetime
import psycopg2
from subprocess import call

backup_dir = '/home/python/scripts/'
psql = ' -U admin -h postgresql01'
gpg = '|gpg -o '
now = datetime.datetime.now()
datetime = str(now.day) + str(now.month) + str(now.year) + str(now.hour) + str(now.minute)

try:
    conn = psycopg2.connect("dbname='gold' user='admin' host='postgresql01' password='3e3p0pCs'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database WHERE datistemplate = FALSE""")
rows = cur.fetchall()
for row in rows:
    print 'Processsing Database: ' + row[0]
    call('pg_dump ' + row[0] + psql + gpg + backup_dir + row[0] + datetime + '.gpg --encrypt --recipient CertainDatabases', shell=True)

