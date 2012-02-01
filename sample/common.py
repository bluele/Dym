#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from dym import Dym

def main():
    # Right command line option list.
    ok = ("help", "init", "add", "find", "find-name")
    USAGE = '''
    <USAGE>
        test.py <option>
        
        option:
    ''' \
     + "\t\t%s\n" * len(ok) \
     % ok
    
    if len(sys.argv) < 2:
        raise Exception(USAGE)
    
    target = sys.argv[1]
    if target not in ok:
        lst = Dym(ok).parse(target, 2)
        if len(lst) > 0:
            print "Did you mean this?"
            for opt in lst:
                print "  %s" % opt
        else:
            print "'%s' is not a test-command. See 'help'" % target
        sys.exit(1)

if __name__ == '__main__':
    main()
