#!/usr/bin/env python3
#
# desc: check for expressions to find out
# credit card numbers, logins, and pre-defined
# parameters
#
__author__ = "Thiago Ribeiro"

import os
import whoosh
import optparse

from lib.config import cnf
from lib.helpers import set_scope, banner, msg

if __name__ == '__main__':
    banner()
    parser = optparse.OptionParser()

    parser.add_option('-s','--src', help='Source code directory path', dest='src',
        action='store', type='string')
    parser.add_option('-d', '--dst', help='Index destination directory', dest='dst',
        action='store', type='string')
    parser.add_option('-p', '--scp', help='Set scope [pci, sox]. Default: [all]', dest='scp',
        action='store', type='string', default='all')

    (opts, args) = parser.parse_args()

    for opt in ['src', 'dst']:
        if not opts.__dict__[opt]:
            msg(("\nOoops! You need to set --%s to continue. Type -h for options" % opt), True, True)

    _indexdir = '%s/%s' % (cnf['INDEX_DIR'], opts.dst)
    _sourcedir = '%s/%s' % (cnf['TMP_DIR'], opts.src)

    if not os.path.exists(_sourcedir):
        msg(('Invalid source directory %s' % _sourcedir), True, True)

    # Check indexer directory
    if os.path.exists(_indexdir):
        _replace = ''
        while(_replace not in ['y','n']):
            _replace = input('Do you want replace %s? [y/n] ' % _indexdir)

        if _replace == 'n':
            msg('Aborting scan...', True, True)

        # Drops indexer
        os.rmdir(_indexdir)

    # Creates the indexer directory
    os.mkdir(_indexdir)

    # Load the scope to scan
    _scope = set_scope(opts.scp)
