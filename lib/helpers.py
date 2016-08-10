from .expression import EXP
from .config import cnf

def set_scope(scope='all'):
    scopes = ['pci', 'sox']

    if scope != 'all' and scope not in scopes:
        msg('Invalid scope option', True, True)

    if scope == 'all':
        msg('Setting scope: all')
        return EXP

    msg('Setting cope: %s' % scope)
    return EXP[scope]

def banner():
    if cnf['SILENT'] is False and cnf['BANNER'] is True:
        print('####################################################')
        print('#                    ESGOTO SCAN                   #')
        print('####################################################')

def msg(_s='', _exit=False, _error=False, _fnc=None):
    if cnf['SILENT'] is False:
        print(_s)
        if _fnc is not None:
            _fnc()

    if _exit:
        exit(0 if _error is False else -1)
