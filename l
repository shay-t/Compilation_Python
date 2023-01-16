################Les Fonctions #############
functions = {}

#######Body de la fonction########

def p_instruction_list(p):
    '''
        instruction_list : statement
                        | instruction_list statement
                        | expression
                        | instruction_list expression
    '''
  
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[2]]
        else:
            p[1].append(p[2])
        p[0] = p[1]

######Arguments for appel#########
def p_argument_list(p):
    '''
        argument_list : expression
                      | argument_list VIRGULE expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]


############Parametre Fonction############

def p_parameter_list(p):
    '''
    parameter_list : expression
                   | parameter_list VIRGULE expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if(not isinstance(p[1], list)):
            p[1] = [p[3]]
        else:
            p[1].append(p[3])
        p[0] = p[1]

         #
##########La fonction avec et sans return##########
def p_fonction(p):
    '''
    fonction : FCT ID LPAREN parameter_list RPAREN LACCOL instruction_list RACCOL
         | FCT ID LPAREN RPAREN LACCOL instruction_list RACCOL
         | FCT ID LPAREN parameter_list RPAREN LACCOL instruction_list return RACCOL
         | FCT ID LPAREN RPAREN LACCOL instruction_list return RACCOL
    '''

    if(len(p) == 8):
        functions[p[2]] = p[6]
        
    elif(len(p) == 9) and (p[4]==')') : 
        
        functions[p[2]] = p[7]
        
    elif(len(p) == 9) and (p[4]!=')') : 
            functions[p[2]] = p[7]
            
    elif(len(p) == 10) : 
        functions[p[2]] = p[8] 

#########Fonction qui retourne ID###########
def p_fonction_return_id(p):
    '''
    fonction_return_id : FCT ID LPAREN parameter_list RPAREN LACCOL instruction_list return_id RACCOL
                   | FCT ID LPAREN RPAREN LACCOL instruction_list return_id RACCOL
    '''

    if(len(p) == 10):
        functions[p[2]] = p[8]
        
    elif(len(p) == 9) : 
        functions[p[2]] = p[7]

############Appel Fonction##########"
def p_appel(p):
    '''
    appel_fonction : ID LPAREN argument_list RPAREN
               | ID LPAREN  RPAREN
               | ID LPAREN ID RPAREN

    '''

    p[0] = functions[p[1]]
        #p[0] = ('appel_func', p[1])
        #p[0] = ('appel_func', p[1], p[3])


########Return###########
def p_return(p):
    '''
    return : RETURN LPAREN expression RPAREN
    '''
    p[0] = p[3]


#########Return special pour ID#######
def p_return_id(p):
    '''
    return_id : RETURN LPAREN ID RPAREN
    '''
    p[0] = variables[p[3]]