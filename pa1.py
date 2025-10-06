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
            
            tokens = []
            
            
            for i in matches:
              #print(f"Found '{i.group()}' at position {i.start()}: {i.end()}")
              for name, value in i.groupdict().items():
                if value and name != "WHITESPACE":
                  #print(f"{name:<12} {value}")
                  tokens.append((name, value)) #appending as a tuple
                
                  
            
            #print(tokens)  


            return tokens
              
            
            
            
    except FileNotFoundError:
        print("the file was not found")
        

t = lexer("input_sourcecode.txt")

with open('output_file.txt', 'w') as file:
  for token_type, lexeme in t:
      line = f"{token_type:<12} {lexeme}\n"
      file.write(line)
  


