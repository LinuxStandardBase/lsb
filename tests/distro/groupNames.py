#!/usr/bin/python

import grp
import sys

#	FIXME: does not run on CentOS 6.5

lsbGroups = {
    'root'    : 0,
    'nobody'  : 65533,
    'nogroup' : 65534,
}

for grpent in grp.getgrall():
    if lsbGroups.has_key(grpent.gr_name):
        if grpent.gr_gid != lsbGroups[grpent.gr_name]:
            print 'GID for group %s does not match specification' %grp
            print 'found: ', gid, ',', ' expected: ', lsbGroups[grp]
            sys.exit(1)
