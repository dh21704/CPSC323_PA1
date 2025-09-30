import re #allows to work with regular expression

#+ is one or more occurences

token_specification = [
    ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9]*'), #
    ('INTEGER', r'\d+'), #any integers whole numbers, \d is digits
    ('WHITESPACE', r'\s+'), #catches all whitespace's, newlines, and tabs
    ('UNKNOWN', r'.'), #anything that doesnt match the other patterns
    ]

def lexer(source_code):
    
