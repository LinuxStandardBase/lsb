#!/usr/bin/python

import pwd
import sys

#	FIXME: does not run on CentOS 6.5
#	TBD: rework this to follow: man 5 passwd layout
#	TBD: hijack the GECOS field to add a bitmap:
#		MUST be present			0000 0001
#		MUST match LSB_pw_name		0000 0010
#		MUST match LSB_pw_uid		0000 0100
#		MUST match LSB_pw_gid		0000 1000
#	Query: do we care about homes?
#
#	sources for assignments in RHT space: 
#		cat `rpm -ql setup | grep uidgid`
#
#	conflict: RHT uses group: 65534 for nobody
#	possible conflict: some distributions use 'admin' for 'root'
#
lsbUsers = {
    'root'   : (0,0),
    'nobody' : (65534,65533),
}

for pwent in pwd.getpwall():
    if pwent.pw_name in lsbUsers:
        if (pwent.pw_uid, pwent.pw_gid) != lsbUsers[pwent.pw_name]:
            print 'UID and/or GID for user %s do not match specification' %pwent.pw_name
            print 'found: (', pwent.pw_uid, ',', pwent.pw_gid, ') expected: ', lsbUsers[pwent.pw_name]
            sys.exit(1)

#	TBD: get rid of un-sourced numeric constants
#	TBD: check for the inverse case of a username found 
#		but not matching 
