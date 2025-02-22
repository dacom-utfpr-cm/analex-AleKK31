from automata.fa.Moore import Moore
import string
import sys, os
from myerror import MyError
error_handler = MyError('LexerErrors')

global check_cm
global check_key

moore = Moore(
    estados = [f'q{i}' for i in range(70)],

    alfabeto = list(string.ascii_letters) + 
                list(string.digits) + 
                ['+','!', '-', '*', '/', '<', '>', '=', '(', ')', '[', ']', '{', '}', ';', ',', '\n', ' '],

    palavras = ['INT', 'FLOAT', 'VOID', 'ID', 'NUMBER',
                'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                'IF', 'ELSE', 'WHILE', 'RETURN',
                'GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL', 'EQUALS', 'DIFFERENT', 'ATTRIBUTION',
                'LPAREN', 'RPAREN', 'LBRACKETS', 'RBRACKETS', 'LBRACES', 'RBRACES', 'COMMA', 'SEMICOLON'],

    transicoes = {
            'q0': { 'w': 'q2', 'i': 'q1', 'e': 'q18', 'f': 'q23', 'r': 'q29', 'v': 'q36', '-': 'q41', '+': 'q3', '*': 'q42', '/': 'q43',
                    '!': 'q52', '(': 'q55', ')': 'q56', '[': 'q57', ']': 'q58', '{': 'q59', '}': 'q60', '<': 'q4', '>': 'q44', '=': 'q49',
                    ';': 'q61', ',': 'q62', ' ': 'q0', '\n': 'q0',
                    **{c: 'q63' for c in string.ascii_letters if c not in {'w', 'i', 'e', 'f', 'r', 'v'}},  
                    **{c: 'q65' for c in string.digits}},

            'q1': {' ' : 'q64', 'n': 'q10', 'f': 'q13'},

            'q2': {' ' : 'q64','h': 'q5'},

            'q3': {' ': 'q0'},

            'q4': {'=': 'q16', ' ': 'q15'},

            'q5': {**{c: 'q64' for c in string.ascii_letters if c != 'i'},'i': 'q6'},

            'q6': {**{c: 'q64' for c in string.ascii_letters if c != 'l'},'l': 'q7'},

            'q7': {**{c: 'q64' for c in string.ascii_letters if c != 'e'},'e': 'q8'},

            'q8': {' ': 'q9'},

            'q9': {'\n': 'q0'},

            'q10': {**{c: 'q64' for c in string.ascii_letters if c != 't'},'t': 'q11'},

            'q11': {' ': 'q12'},

            'q12': {'\n': 'q0'},

            'q13': {' ': 'q14'},

            'q14': {'\n': 'q0'},

            'q15': {'\n': 'q0'},

            'q16': {' ': 'q0'},

            'q18': {' ': 'q64','l': 'q19'},

            'q19': {**{c: 'q64' for c in string.ascii_letters if c != 's'},'s': 'q20'},

            'q20': {**{c: 'q64' for c in string.ascii_letters if c != 'e'},'e': 'q21'},

            'q21': {' ': 'q22'},

            'q22': {'\n': 'q0'},

            'q23': {' ' : 'q64','l': 'q24'},

            'q24': {**{c: 'q64' for c in string.ascii_letters if c != 'o'},'o': 'q25'},

            'q25': {**{c: 'q64' for c in string.ascii_letters if c != 'a'},'a': 'q26'},

            'q26': {**{c: 'q64' for c in string.ascii_letters if c != 't'},'t': 'q27'},

            'q27': {' ': 'q28'},

            'q28': {'\n': 'q0'},

            'q29': {' ' : 'q64', 'e': 'q30'},

            'q30': {**{c: 'q64' for c in string.ascii_letters if c != 't'},'t': 'q31'},

            'q31': {**{c: 'q64' for c in string.ascii_letters if c != 'u'},'u': 'q32'},

            'q32': {**{c: 'q64' for c in string.ascii_letters if c != 'r'},'r': 'q33'},

            'q33': {**{c: 'q64' for c in string.ascii_letters if c != 'n'},'n': 'q34'},

            'q34': {' ': 'q35'},

            'q35': {'\n': 'q0'},

            'q36': {' ' : 'q64','o': 'q37'},

            'q37': {**{c: 'q64' for c in string.ascii_letters if c != 'i'},'i': 'q38'},

            'q38': {**{c: 'q64' for c in string.ascii_letters if c != 'd'},'d': 'q39'},

            'q39': {' ': 'q40'},

            'q40': {'\n': 'q0'},

            'q41' : {' ': 'q0'},

            'q42' : {' ': 'q0'},

            'q43' : {'*': 'q67',' ': 'q0'},

            'q44' : {'=' : 'q46', ' ' : 'q45'},

            'q45' : {'\n': 'q0'},

            'q46' : {' ' : 'q0'},

            'q48' : {' ': 'q0'},

            'q49' : {'=' : 'q48', ' ' : 'q50'},

            'q50' : {'\n': 'q0'},

            'q52' : {'=' : 'q53'},

            'q53' : {' ': 'q0'},

            'q55' : {' ': 'q0'},

            'q56' : {' ': 'q0'},

            'q57' : {' ': 'q0'},

            'q58' : {' ': 'q0'},

            'q59' : {' ': 'q0'},

            'q60' : {' ': 'q0'},

            'q61' : {' ': 'q0'},
            
            'q62' : {' ': 'q0'},

            'q63': {**{c: 'q64' for c in string.ascii_letters + string.digits}, 
                    **{c: 'q0' for c in [' ', '\n', '+', '-', '*', '/', '<', '>', '=', '(', ')', '[', ']', '{', '}', ';', ',']}},

            'q64': {**{c: 'q64' for c in string.ascii_letters + string.digits},  
                    **{c: 'q0' for c in [' ', '\n', '+', '-', '*', '/', '<', '>', '=', '(', ')', '[', ']', '{', '}', ';', ',']} },

            'q65': {c: 'q66' for c in string.digits},  

            'q66': {c: 'q66' for c in string.digits}, 
            
            'q66': {c: 'q0' for c in [' ', '\n', '+', '-', '*', '/', '<', '>', '=', '(', ')', '[', ']', '{', '}', ';', ',']}, 
            
            'q67': {c: 'q68' for c in string.printable},  

            'q68': {'*': 'q69', **{c: 'q68' for c in string.printable if c not in ["*"]}},  

            'q69': {'/': 'q0', **{c: 'q68' for c in string.printable if c not in "/"}},  
    },

    inicial_q='q0',
    
    tabela_q = {
            'q0': '', 'q1': '', 'q2': '', 'q3': 'PLUS', 'q4': '', 'q5': '', 'q6': '', 'q7': '', 'q8': 'WHILE', 'q9': 'WHILE',
            'q10': '', 'q11': 'INT', 'q12': 'INT', 'q13': '', 'q14': 'IF', 'q15': 'LESS', 'q16': 'LESS_EQUAL', 'q18': '', 'q19': '', 
            'q20': '', 'q21': 'ELSE', 'q22': 'ELSE', 'q23': '', 'q24': '', 'q25': '', 'q26': '', 'q27': 'FLOAT', 'q28': 'FLOAT', 'q29': '', 
            'q30': '', 'q31': '', 'q32': '', 'q33': '', 'q34': 'RETURN', 'q35': 'RETURN', 'q36': '', 'q37': '', 'q38': '', 'q39': 'VOID', 
            'q40': 'VOID', 'q41': 'MINUS', 'q42': 'TIMES', 'q43': 'DIVIDE', 'q44': '', 'q45': 'GREATER', 'q46': 'GREATER_EQUAL', 'q48': 'EQUALS', 'q49': '', 
            'q50': 'ATTRIBUTION', 'q52': '', 'q53': 'DIFFERENT', 'q55': 'LPAREN', 'q56': 'RPAREN', 'q57': 'LBRACKETS', 'q58': 'RBRACKETS', 'q59': 'LBRACES', 
            'q60': 'RBRACES', 'q61': 'SEMICOLON', 'q62': 'COMMA', 'q63': 'ID', 'q64': 'ID', 'q65': 'NUMBER', 'q66': 'NUMBER', 'q67': '', 'q68': '', 'q69': ''
    }
)

def preprocessamento(input_string):
    formatted_input = ""
    i = 0

    def prox_char():
        return i + 1 < len(input_string)

    while i < len(input_string):
        char = input_string[i]

        if char == '/' and prox_char():
            next_char = input_string[i + 1]
            if next_char == '*':
                formatted_input += f"\n{char}{next_char}\n"
                i += 2
                continue
        if char == '*' and prox_char():
            next_char = input_string[i + 1]
            if next_char == '/':
                formatted_input += f"\n{char}{next_char}\n"
                i += 2
                continue
        if char in ['<', '>', '!', '='] and prox_char():
            next_char = input_string[i + 1]
            if next_char == '=':
                formatted_input += f"\n{char}{next_char}\n"
                i += 2
                continue
        if char in ' (){};,+-*/<>=![]':
            formatted_input += f" \n{char} \n"
        elif char == ' ' or char == '\n':
            formatted_input += char 
        else:
            formatted_input += char 

        i += 1

    formatted_input += '\n' 
    return formatted_input.strip()  

def processamento(input_string):
    tokens = []
    current_state = moore.inicial_q
    token = ""

    for char in input_string:
        if char in moore.alfabeto:
            next_state = moore.transicoes[current_state].get(char, 'q0')
            if next_state == 'q0':  
                if moore.tabela_q.get(current_state):
                    tokens.append(moore.tabela_q[current_state])  
                token = ""  
                current_state = moore.inicial_q
            else:
                token += char  
                current_state = next_state
        else:
            raise IOError(error_handler.newError(char,'ERR-LEX-INV-CHAR'))

    if moore.tabela_q.get(current_state):
        tokens.append(moore.tabela_q[current_state])
    return tokens

def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        # print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True

            # print ("No. of arguments passed is ", len(sys.argv))

    if(len(sys.argv) <= 2 and check_key == True):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
      raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()

        if not check_key:
            print("Definição Máquina")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Tokens:")

        #print(moore.get_output_from_string(source_file))

        tokens = processamento(preprocessamento(source_file))
        for token in tokens:
            print(token)
        
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(e)