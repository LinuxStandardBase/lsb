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
    if grpent.gr_name in lsbGroups:
        if grpent.gr_gid != lsbGroups[grpent.gr_name]:
            print 'GID for group %s does not match specification' %grpent.gr_name
            print 'found: ', grpent.gr_gid, ',', ' expected: ', lsbGroups[grpent.gr_name]
            sys.exit(1)
