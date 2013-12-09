  GNU nano 2.0.9                                                       File: liquibased.py

#!/usr/bin/python
# Calls liquibase against a target database
#
# BMW 12/9/2013
#java -jar liquibase.jar --classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar --driver=org.postgresql.Driver  --changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml  -$
#
# Use:  liquibased(host, tag)
#
from subprocess import call
import sys

java_path = '/home/liquibase/certain/travis/lib/'
dbname = 'certain'
db_driver = '--classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar'
source_path = '--changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml'
url='--url jdbc:postgresql://'
url2='/' + dbname
username='admin'
password='3e3p0pCs'


def liquibased(host, tag):
#    try:
        target = url + host + url2
        command =  'java -jar ' + java_path +'liquibase.jar ' + db_driver + ' ' + source_path + ' ' + target + ' --username ' + username + ' --password ' + password + ' update'
        print command
        call(command, shell=True)
        print target

#    except:
#        print 'Something Went Wrong!!'
#        e = sys.exc_info()[0]
#        print ( "<p>Error: %s</p>" % e )

liquibased('postgresql01', 'brad')







