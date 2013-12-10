  GNU nano 2.0.9                                                       File: liquibased.py

#!/usr/bin/python
# Calls liquibase against a target database
#
# BMW 12/9/2013
#java -jar liquibase.jar --classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar --driver=org.postgresql.Driver  --changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml  -$
#
# Use:  liquibased(host, tag, database)
#
import subprocess
import sys
import psycopg2
from optparse import OptionParser

#declarations
java_path = '/home/liquibase/certain/travis/lib/'
db_driver = '--classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar'
source_path = '--changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml'
url='--url jdbc:postgresql://'
username='admin'
password='3e3p0pCs'

#handle arguments
parser = OptionParser(usage="%prog [-o] [-t] [-d] (optional: not specified will process all db's)", version="%prog .5")
parser.add_option("-o", dest="host",
                  help="host for liquibase")
parser.add_option("-t",
                  dest="tag",
                  help="tag for liquibase")
parser.add_option("-d",
                  dest="dbname",
                  help="destination database (omit to process all databases)",
                  default="alldatabases")


(options, args) = parser.parse_args()

url2 = '/' + options.dbname

def liquibased(host, tag):
        target = url + host + url2
        command =  'java -jar ' + java_path +'liquibase.jar ' + db_driver + ' ' + source_path + ' ' + target + ' --username ' + username + ' --password ' + password + ' update'
#        print command
        subprocess.check_call(command, shell=True)
        subprocess.check_call(command + ' tag ' + tag, shell=True)


def getportals(host):
    try:
        connection_string = "dbname='certain_system' host=\'" +host+ "\' user='" + username + "\' password='" + password + "\'"
#       conn = psycopg2.connect("dbname='certain_system' user='admin' host='Postgresql01' password='3e3p0pCs'")
        conn = psycopg2.connect(connection_string)
    except:
        print 'whoops'
        print connection_string


