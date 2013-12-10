<<<<<<< HEAD

#!/usr/bin/python
# Calls liquibase against a target database
#
# BMW 12/9/2013
#java -jar liquibase.jar --classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar --driver=org.postgresql.Driver  --changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml  -$
#
# Use:  liquibased(host, tag)
#
import subprocess
import sys
from optparse import OptionParser

#declarations
java_path = '/home/liquibase/certain/travis/lib/'
dbname = 'bradtest'
db_driver = '--classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar'
source_path = '--changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml'
url='--url jdbc:postgresql://'
url2='/' + dbname
username='admin'
password='3e3p0pCs'

#handle arguments
parser = OptionParser()
parser.add_option("-o", dest="host",
                  help="host for liquibase")
parser.add_option("-t",
                  dest="tag",
                  help="tag for liquibase")

(options, args) = parser.parse_args()


def liquibased(host, tag):
        target = url + host + url2
        command =  'java -jar ' + java_path +'liquibase.jar ' + db_driver + ' ' + source_path + ' ' + target + ' --username ' + username + ' --password ' + password + ' update'
        print command
        subprocess.check_call(command, shell=True)
        subprocess.check_call(command + ' tag ' + tag, shell=True)

print options.host + ' ' + options.tag
liquibased(options.host, options.tag)




=======
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
backup_dir = '/certain_software/pbackup/postgresql'
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
    call('pg_dump ' + row[0] + psql + gpg + backup_dir + '/'+ row[0] + starttimestr + '.gpg --encrypt --recipient ' + gpgprofile, shell=True)
duration = datetime.datetime.now() - starttime
syslog.syslog('PG Backup Completed. Duration: ' + str(duration) )
call('find ' + backup_dir + ' -mtime +5 -name *.gpg -exec rm {} \;', shell=True)
>>>>>>> parent of 3727f8b... Corrrected nagios logging error





