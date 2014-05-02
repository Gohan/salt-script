#!/usr/bin/python
import crypt
import random, string
from subprocess import Popen, PIPE

def GetPasswordHash():
    password = raw_input("Enter Password:")
    if len(password) == 0:
        clear = raw_input("Clear Password?[Y/n]")
        clear = clear.lower().strip()
        if len(clear) == 0 or clear[0] == 'y':
            return "";
    N = 8
    salt = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(N))
    return crypt.crypt(password, '$6$'+salt)


minion_filter = raw_input("Enter minion filter:");
username = raw_input("Enter username:");
passhash = GetPasswordHash();

print Popen(['sudo', 'salt', minion_filter, 'shadow.set_password', username, '%s' % passhash], stdout=PIPE).stdout.read()
