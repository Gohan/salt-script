#!/usr/bin/python
import crypt
import random, string
from subprocess import Popen, PIPE
password = raw_input("Enter Password:")
N = 8
salt = ''.join(random.choice(
    string.ascii_letters + string.digits) for _ in range(N))
passhash = crypt.crypt(password, '$6$'+salt)

minion_filter = raw_input("Enter minion filter:");
username = raw_input("Enter username:");
print Popen(['sudo', 'salt', minion_filter, 'shadow.set_password', username, '"%s"' % passhash], stdout=PIPE).stdout.read()
