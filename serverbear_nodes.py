#!/usr/bin/python
from subprocess import Popen, PIPE

minion_filter = raw_input("Enter minion filter:")
email = raw_input("Enter Email:")

print Popen(['sudo', 'salt',
             minion_filter,
             'cmd.run',
             "wget -N https://raw.github.com/Crowd9/Benchmark/master/sb.sh"
             ], stdout=PIPE).stdout.read()

cmd = "screen -d -m bash sb.sh 'Baozishan' '{{grains.id}}' '%s'" % email
print Popen(['sudo', 'salt', minion_filter,
             'cmd.retcode',
             'template=jinja',
             cmd
             ], stdout=PIPE).stdout.read()
