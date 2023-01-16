from re import S
import ply.yacc as yacc 
from lexy import tokens,build_lexer

#dictionnaire de variables

vars = {}
functions = {}

########### precedences #####

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

###############numbers###########

def p_expression_NUMBER(p):
    '''expression : INT 
                | FLOATTYPE'''
    p[0] = p[1]
    
def p_factor_NUMBER(p):
    '''factor : INT 
              | FLOATTYPE'''
    p[0] = p[1]
    
def p_term_NUMBER(p):
    '''term : INT 
            | FLOATTYPE'''    
    p[0] = p[1]


############### string #############

def p_expression_STRING(p):
    'expression : STRING'
    p[0] = p[1]

################ boolean ####################

def p_expression_BOOLEAN(p):
    'expression : BOOL'
    p[0] = p[1]


############## incrementation/decrementation vars int #############


def p_DECREMENTATION(p):
    '''expression : ID DECREMENTATION
                  | INT DECREMENTATION  
    '''
    try:
        p[0]=int(p[1]) - 1
    except:
        vars[p[1]]=vars[p[1]] - 1 
        p[0]=vars[p[1]]

      
def p_INCREMENTATION(p):
    '''expression : ID INCREMENTATION
                  | INT INCREMENTATION  
    '''
    try:
        p[0]=int(p[1]) + 1
    except:
        vars[p[1]]=vars[p[1]] + 1
        p[0]=vars[p[1]] 


############################# operations vars expressions #############  
def p_binary_operators(p):

    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
       p[0] = p[1] + p[3]
    elif p[2] == '-':
       p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        try:
            p[0] = p[1] / p[3]
        except:
            print("nn")

def p_binary_operators_id(p):

    '''expression : ID PLUS expression
                  | ID MINUS expression
                  | ID TIMES expression
                  | ID DIVIDE expression'''
    if p[2] == '+':
       p[0] = vars[p[1]] + p[3]
    elif p[2] == '-':
       p[0] = vars[p[1]] - p[3]
    elif p[2] == '*':
        p[0] = vars[p[1]] * p[3]
    elif p[2] == '/':
        try:
            p[0] = vars[p[1]] / p[3]
        except:
            print("nnnnn")

############################ concatenation ##########################

def p_concat(p):
    '''expression : ID PLUS STRING'''
    a = vars[p[1]][:len(p[3])-1] +p[3][1:]
    p[0]=a

################################ printing vars and expressions ###############

def p_print_str(p):
    'expression : PRINT LPAREN  STRING RPAREN'
    p[0]=p[3][1:len(p[3])-1]
def p_assign(p):
    'expression : ID EQUALS expression'
    p[0]=p[3]
    vars[p[1]]=p[3]
def p_assignid(p):
    'expression : ID EQUALS ID'
    vars[p[1]]=vars[p[3]]  
    p[0]=vars[p[1]]  
def p_print_var(p):
    'expression : PRINT LPAREN  ID RPAREN'
    p[0]=vars[p[3]]
def p_print_exp(p):
    'expression : PRINT LPAREN  expression RPAREN'
    p[0]=p[3]

##############################IF-IFELSE-AND-OR###########################

def p_if_statement(p):
    '''expression : IF LPAREN condition RPAREN LBRACE expression RBRACE
    '''
    if(p[3]==True):
        p[0]=p[6]
    else:
        p[0]=None
def p_ifand_statement(p):
    '''expression : IF LPAREN condition AND condition RPAREN LBRACE expression RBRACE
    '''
    if(p[3]==True and p[5]==True):
        p[0]=p[8]
    else:
        p[0]=None
def p_ifor_statement(p):
    '''expression : IF LPAREN condition OR condition RPAREN LBRACE expression RBRACE
    '''
    if (p[3]==True or p[5]==True):
        p[0]=p[8]
    else:
        p[0]=None
def p_ifelse_statement(p):
    '''expression : IF LPAREN condition RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE
    '''
    if(p[3]==True):
        p[0]=p[6]
    else:
        p[0]=p[10]       
def p_condition(p):
    '''condition : INT EQUALEQUAL INT
                 | INT GTH INT
                 | INT LTH INT
                 | INT GTHOREQUAL INT
                 | INT LTHOREQUAL INT
    '''
    p[0]=False
    if(p[2]=="=="):
        if(p[1]==p[3]) : 
            p[0] = True
    elif(p[2]=="<"):
        if(p[1]<p[3]) : 
            p[0] = True
    elif(p[2]==">"):
        if(p[1]>p[3]) : 
            p[0] = True
    elif(p[2]=="<="):
        if(p[1]<=p[3]) : 
            p[0] = True
    elif(p[2]==">="):
        if(p[1]>=p[3]) : 
            p[0] = True
def p_condition_id(p):
    '''condition : ID EQUALEQUAL INT
                 | ID GTH INT
                 | ID LTH INT
                 | ID GTHOREQUAL INT
                 | ID LTHOREQUAL INT
    '''
    p[0]=False
    if(p[2]=="=="):
        if(vars[p[1]]==p[3]) : 
            p[0] = True
    elif(p[2]=="<"):
        if(vars[p[1]]<p[3]) : 
            p[0] = True
    elif(p[2]==">"):
        if(vars[p[1]]>p[3]) : 
            p[0] = True
    elif(p[2]=="<="):
        if(vars[p[1]]<=p[3]) : 
            p[0] = True
    elif(p[2]==">="):
        if(vars[p[1]]>=p[3]) : 
            p[0] = True


################################ for loop ? while #######################

def p_while(p):
    '''expression : WHILE LPAREN ID EQUALEQUAL INT RPAREN LBRACE instruction RBRACE
                   | WHILE LPAREN ID GTH INT RPAREN LBRACE instruction RBRACE
                   | WHILE LPAREN ID LTH INT RPAREN LBRACE instruction RBRACE
                   | WHILE LPAREN ID GTHOREQUAL INT RPAREN LBRACE instruction RBRACE
                   | WHILE LPAREN ID LTHOREQUAL INT RPAREN LBRACE instruction RBRACE
    '''
    if(p[4]=="=="):
        while(vars[p[3]]==p[5]):
            check(p[8])
    elif(p[4]=="<"):
        while(vars[p[3]]<p[5]):
            check(p[8])    
    elif(p[4]==">"):
        while(vars[p[3]]>p[5]):
            check(p[8])   
    elif(p[4]=="<="):
        while(vars[p[3]]<=p[5]):
            check(p[8])           
    elif(p[4]==">="):
        while(vars[p[3]]>=p[5]):
            check(p[8]) 
       

def p_instruction(p):
    '''instruction : expression
                   | expression COMMA instruction
    '''
    a=[]
    for i in range(1,len(p),2):
        a.append(p[i])
    p[0]=a
    
def p_for(p):
    '''expression : FOR INT TO INT DEUXPOINTS instruction
    '''
    for i in range(p[2],p[4]):
        check(p[6])

def check(li):
    for j in li:
        if(type(j) is not list):
            print(j)
        else:
            check(j)   

############################ input with messages #################

def p_yudf(p):
    '''expression : INPUT LPAREN STRING COMMA ID RPAREN'''
    var=input(p[3][1:len(p[3])-1])
    vars[p[5]]=var
    p[0]=var

########################### arrays ###############################

def p_list(p):
    '''expression : LIST ID SEMICOL'''    
    vars[p[2]]=[]
    p[0]=[]

def p_item(p):
    '''item : INT
            | STRING
    '''
    p[0]=p[1]

def p_listadd(p):
    '''expression : ID POINT APPEND LPAREN item RPAREN
    '''
    vars[p[1]].append(p[5])
    p[0]=p[5]

def p_listclear(p):
    '''expression : ID POINT CLEAR LPAREN RPAREN
    '''
    vars[p[1]].clear()
    p[0]=vars[p[1]]

def p_listdrop(p):
    '''expression : ID POINT POP LPAREN INT RPAREN
    '''
    dropped=vars[p[1]][p[5]]
    vars[p[1]].pop(p[5])
    p[0]=dropped 

def p_listsort(p):
    '''expression : ID POINT SORT LPAREN RPAREN
    '''
    vars[p[1]].sort()
    p[0]=vars[p[1]]

def p_listreverse(p):
    '''expression : ID POINT REVERSE LPAREN RPAREN
    '''
    vars[p[1]].reverse()
    p[0]=vars[p[1]]

############################# funcions ##########################
def p_function_create(p):
    '''expression : FUNCTION ID LPAREN RPAREN LBRACE instruction RBRACE 
    '''
    functions[p[2]]=[]
    functions[p[2]].extend(p[6])


def p_function_create_args(p):
    '''expression : FUNCTION ID LPAREN ARGS RPAREN LBRACE instruction RBRACE 
    '''
    functions[p[2]]=[]
    functions[p[2]].extend(p[7])

def p_args(p):
    '''ARGS : expression 
            | expression COMMA ARGS
    '''
    a=[]
    for i in range(1,len(p),2):
        a.append(p[i])
    p[0]=a

def p_call_function(p):
    '''expression : FUNCTION ID LPAREN RPAREN SEMICOL'''
    l = functions[p[2]]
    check(l)

def p_call_function_args(p):
    '''expression : FUNCTION ID LPAREN ARGS RPAREN SEMICOL'''
    l = functions[p[2]]
    ar=check2(p[4])
    check3(l)
args=[]
def check2(li):
    global args
    for j in li:
        if(type(j) is not list):
            args.append(j)
        else:
            check2(j) 
    return args

def check3(li):
    global args
    for j in li:
        if(type(j) is not list):
            for i in range(len(args)):
                if "$"+str(i+1) in j:
                    j=str(args[i])
                break
            print(j)
        else:
            check3(j) 
############################# simulation ########################
s='''asynt b (){ siggz("mon nom est ") , siggz("$1") }
asynt b ("mohamed") ;
'''
build_lexer(s)
parser=yacc.yacc() 
def run_parser(s):
    for line in s.splitlines():
        result = parser.parse(line)
        print(result)

run_parser(s)
print("**************************")
#print(vars)
