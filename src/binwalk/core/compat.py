import sys
import string

PY_MAJOR_VERSION = sys.version_info[0]

if PY_MAJOR_VERSION > 2:
    string.letters = string.ascii_letters


def str2bytes(s):
    if isinstance(s, str):
        return bytes(s, 'latin1')
    return s


def bytes2str(bs):
    if isinstance(bs, bytes):
        return bs.decode('latin1')
    return bs
