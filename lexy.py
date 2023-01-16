import ply.lex as lex

reserved = {
    'amskil'      : 'ID',
    'siggz'       : 'PRINT',
    'imidn ayugan': 'INT',
    'tabddit'     : 'BREAK', 
    'yudf'        : 'INPUT',
    'niy'         : 'ELSE',
    'marka'       : 'VAR_TYPE',
    'askkil'      : 'char', 
    'yuda'        : 'RETURN', 
    'isul'        : 'CONTINUE',     
    'i'           : 'FOR',
    'asynt'       : 'FUNCTION',
    'xmi'         : 'IF',
    'kada'        :'WHILE',
    'tiyzi'       : 'SIZEOF',
    'imidn tasiht': 'FLOATTYPE',
    'amgin'       : 'BOOL',
    'amdadd'      : 'TRUE',
    'azgal'       : 'FALSE',
    'd'           : 'AND',
    'mad'         : 'OR',
    'walu'        :'NONE',
    'lqqm'        :'APPEND',
    'ars'         :'CLEAR',  
    'asmil'       :'CLASS',
    'algamt'      :'LIST',
    'ikks'        :'POP',  
    'ifrn'        : 'SORT',
    'amttay'      : 'REVERSE'
}

tokens =[
    "GTH",
    "LTH",
    "GTHOREQUAL",
    "LTHOREQUAL",
    "EQUALEQUAL",
    "NOTEQUAL",
    'NUMBER',
    'FLOAT_CONST',
    'INT_CONST',
    'STRING',
    'PLUS',
    'MINUS',
    'MODULO',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'RBRACE',
    'LBRACE',
    'SEMICOL',
    'EQUALS',
    'COMMA',
    'QUOTES',
    'DEUXPOINTS',
    'INCREMENTATION',
    'DECREMENTATION',
    'TO',
    'POINT',
    'functionname'
]+ list(reserved.values())
t_EQUALEQUAL = r'=='
t_GTH        = r'>'
t_LTH        = r'<'
t_GTHOREQUAL = r'>='
t_LTHOREQUAL = r'<='
t_NOTEQUAL   = r'!='
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_SEMICOL    = r';'
t_EQUALS     = r'='
t_MODULO     = r'%'
t_COMMA      = r'\,'
t_QUOTES = r'\"'
t_DEUXPOINTS = r':'
t_INCREMENTATION=r'\+\+'
t_DECREMENTATION=r'--'
t_TO=r'\.\.'
t_POINT=r'\.'
def t_LBRACE(t):
    r'\{'
    t.type = 'LBRACE'      
    return t

t_ignore  = r' \t'
t_ignore_COMMENT = r'\#.*'

def t_STRING(t):
    r'\".([a-zA-Z_0-9]|[^\S\n\t])*.\"'
    return t

def t_error(t):
    print("tazglt taguri ihdiklah: '%s'" % t.value[0])
    t.lexer.skip(1)

def t_RBRACE(t):
    r'\}'
    t.type = 'RBRACE'    
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved.get(t.value)  
    return t

def t_NUMBER(t):
    r'-?[0-9]*\.?[0-9]+((E|e)(\+|-)?[0-9]+)?'
    try:
        t.value = int(t.value)
        t.type = 'INT'
        return t
    except ValueError:
        pass

    try:
        t.value = float(t.value)
        t.type = 'FLOATTYPE'
        return t
    except ValueError:
        pass

lexer = lex.lex()

def build_lexer(source_code):
    lexer.input(source_code)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            print("akki 3awn rebbi d ar timlilt")
            break  
        print(tok)
data="""siggz("hello")
"""
#build_lexer(data)