#! /usr/bin/python
import datetime
import psycopg2
import syslog
from subprocess import call
# Postgres Backup Script
# Backs up and encrypts PG databases.
# Requires passwordless authentication for user. (e.g. .pgpass)

#Definitions

host = '10.89.132.74'
user = 'admin'
gpgprofile = 'CertainSystem'
backup_dir = '/certain_software/pbackup/postgresql/'
psql = ' -U ' + user + ' -h ' + host
gpg = '|gpg -o '
starttime = datetime.datetime.now()
starttimestr = str(starttime.day) + str(starttime.month) + str(starttime.year) + str(starttime.hour) + str(starttime.minute)

#Execution

try:
    conn = psycopg2.connect("dbname='postgres' user='admin' host='10.89.132.74' password='3e3p0pCs'")
    syslog.syslog('PG Backup Started')
except:
    print "I am unable to connect to the database"
    syslog.syslog('PG Backup Script DB Connection Error')

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database WHERE datistemplate = FALSE AND datname <> 'webtest'""")
rows = cur.fetchall()
for row in rows:
    print 'Processsing Database: ' + row[0]
    #call('pg_dump ' + row[0] + psql + gpg + backup_dir + row[0] + starttimestr + '.gpg --encrypt --recipient ' + gpgprofile, shell=True)
duration = datetime.datetime.now() - starttime
syslog.syslog('PG Backup Completed. Duration: ' + str(duration) )
call('find ' + backup_dir +' -mtime +5 -name *.gpg -exec rm {} \;', shell=True)
