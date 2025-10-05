import re #allows to work with regular expression

#+ is one or more occurences

token_specification = [
    ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9]*'), #
    ('INTEGER', r'\d+'), #any integers whole numbers, \d is digits
    ('WHITESPACE', r'\s+'), #catches all whitespace's, newlines, and tabs
    ('UNKNOWN', r'.'), #anything that doesnt match the other patterns
    ]

def lexer(source_code):
    try:
        with open(source_code, 'r') as file:
            content = file.read()
            
            single_regex_string = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
            
            matches = re.finditer(single_regex_string, content)
            
            for i in matches:
              print(f"Found '{i.group()}' at position {i.start()}: {i.end()}")
            
            
            
            
    except FileNotFoundError:
        print("the file was not found")
        

lexer("input_sourcecode.txt")
