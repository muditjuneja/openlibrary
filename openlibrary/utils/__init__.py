"""Generic utilities"""

from urllib import quote_plus

to_drop = set(''';/?:@&=+$,<>#%"{}|\\^[]`\n\r''')

def str_to_key(s):
    return ''.join(c if c != ' ' else '_' for c in s.lower() if c not in to_drop)

def url_quote(s):
    return quote_plus(s.encode('utf-8')) if s else ''
