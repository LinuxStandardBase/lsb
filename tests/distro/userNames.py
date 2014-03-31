#!/usr/bin/python

import pwd
import sys

lsbUsers = {
    'root'   : (0,0),
    'nobody' : (65534,65533),
}

for pwent in pwd.getpwall():
    if lsbUsers.has_key(pwent.pw_name):
        if (pwent.pw_uid, pwent.pw_gid) != lsbUsers[pwent.pw_name]:
            print 'UID and or GID for user %s do not match specification' %usr
            print 'found: (', uid, ',', gid, ') expected: ', lsbUsers[usr]
            sys.exit(1)
