#!/usr/bin/python
import crypt
import random, string
password = raw_input("Enter Password:")
N = 8
salt = ''.join(random.choice(
    string.ascii_letters + string.digits) for _ in range(N))
print crypt.crypt(password, '$6$'+salt)
