
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

tag = 'bradtest'
java_path = '/home/liquibase/certain/travis/lib/'
dbname = 'bradtest'
db_driver = '--classpath=/home/liquibase/certain/travis/lib/postgresql-9.3-1100.jdbc4.jar'
source_path = '--changeLogFile=/home/liquibase/certain/travis/certain/changelog.xml'
url='--url jdbc:postgresql://'
url2='/' + dbname
username='admin'
password='3e3p0pCs'


def liquibased(host, tag):
        target = url + host + url2
        command =  'java -jar ' + java_path +'liquibase.jar ' + db_driver + ' ' + source_path + ' ' + target + ' --username ' + username + ' --password ' + password + ' update'
        subprocess.check_call(command, shell=True)
        subprocess.check_call(command + ' tag ' + tag, shell=True)



liquibased('postgresql01', 'brad')


