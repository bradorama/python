#!/usr/bin/python
# Calls liquibase against a target database
# 
# BMW 12/9/2013
#java -jar liquibase.jar --classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar --driver=org.postgresql.Driver  --changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml  --url="jdbc:postgresql://postgresql01/certain"  --username=admin  --password=3e3p0pCs  update
#
# Use:  liquibased(host, tag, database)
#
import subprocess
import sys
import psycopg2
from optparse import OptionParser
import syslog

#declarations
java_path = '/home/liquibase/certain/travis/lib/'
db_driver = '--classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar'
source_path = '--changeLogFile=/home/liquibase/certain/travis/50x_db/db/certain/changelog.xml' 
url='--url jdbc:postgresql://'
url2= '/'
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
parser.add_option("-m",
		  dest="mode",
                  help="Mode for deployment (S afe mode or U pdate)",
		  default="S")
		

(options, args) = parser.parse_args()

def liquibased(host, tag, database):
        target = url + host + url2 + database
        command =  'java -jar ' + java_path +'liquibase.jar ' + db_driver + ' ' + source_path + ' ' + target + ' --username ' + username + ' --password ' + password 
	if options.mode == 'U':
		 exec_command = command + ' update'
	elif options.mode == 'S':
		 exec_command = command + ' updateSQL'
	elif options.mode == 'R':
		 command + ' rollback' + options.tag
        subprocess.check_call(exec_command, shell=True)
	syslog.syslog( host + '.' + database + ' updated Successfully.')
        #subprocess.check_call(command + ' tag ' + tag, shell=True)  Not Needed


def getportals(host):
    try:
	connection_string = "dbname='certain_system' host=\'" +host+ "\' user='" + username + "\' password='" + password + "\'"
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
	cur.execute("""SELECT prtl_code FROM portals WHERE prtl_is_active = TRUE""")
	rows = cur.fetchall()
	return rows
    except Exception, e:
        print e[0]
        

if options.dbname == 'alldatabases':
    syslog.syslog('Starting a Global LB Deployment on: ' + options.host + ' Mode:' + options.mode)
    rows = getportals(options.host)
    for row in rows:
	    try:
	        print 'Processing: ' + row[0]
	        liquibased(options.host, options.tag, row[0])
            except Exception, e:
		syslog.syslog('***ERROR***  LB Deployment Failure on database: ' + row[0])
else:
    print 'Processing: ' + options.dbname
    syslog.syslog('Starting a direct LB Deployment on: ' + options.host + '.' + options.dbname + ' Mode:' + options.mode)
    liquibased(options.host, options.tag, options.dbname)


