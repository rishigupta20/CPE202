from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


operators = ['-', '+', '*', '/', '**', '>>', '<<']
operators1 = ['-', '+']
operators2 = ['*', '/']
operators3 = ['**']
operators4 = ['>>', '<<']


def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    stack = Stack(30)
    new_input = input_str.split()
    if len(input_str) == 0:
        raise PostfixFormatException('Empty input')
    for tok in new_input:
        try:
            tok = int(tok)
            stack.push(tok)
        except:
            try:
                tok = float(tok)
                stack.push(tok)
            except:
                if tok not in operators:
                    raise PostfixFormatException('Invalid token')
            if tok == '+':
                try:
                    val1 = stack.pop()
                    val2 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                val3 = val2 + val1
                stack.push(val3)
            if tok == '-':
                try:
                    val4 = stack.pop()
                    val5 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                val6 = val5 - val4
                stack.push(val6)
            if tok == '*':
                try:
                    val7 = stack.pop()
                    val8 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                val9 = val8 * val7
                stack.push(val9)
            if tok == '/':
                try:
                    val10 = stack.pop()
                    val11 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                if val10 == 0:
                    raise ValueError
                val12 = val11 / val10
                stack.push(val12)
            if tok == '**':
                try:
                    val13 = stack.pop()
                    val14 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                val15 = val14 ** val13
                stack.push(val15)
            if tok == '>>':
                try:
                    val16 = stack.pop()
                    val17 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                try:
                    val18 = val17 >> val16
                except:
                    raise PostfixFormatException('Illegal bit shift operand')
                stack.push(val18)
            if tok == '<<':
                try:
                    val19 = stack.pop()
                    val20 = stack.pop()
                except:
                    raise PostfixFormatException('Insufficient operands')
                try:
                    val21 = val20 << val19
                except:
                    raise PostfixFormatException('Illegal bit shift operand')
                stack.push(val21)
    if stack.num_items > 1:
        raise PostfixFormatException('Too many operands')
    return stack.peek()


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    stack = Stack(30)
    postfix = ''
    new_input = input_str.split()
    for tok in new_input:
        if tok in operators:
            while stack.is_empty() is False and stack.peek() in operators and (
                    (helper_infix_to_postfix(tok)[1] == 'l' and (helper_infix_to_postfix(tok)[
                                                                     0] <= helper_infix_to_postfix(stack.peek())[
                                                                     0])) or ((
                                                                                      helper_infix_to_postfix(tok)[
                                                                                          1] == 'r') and
                                                                              (helper_infix_to_postfix(tok)[0] <
                                                                               helper_infix_to_postfix(stack.peek())[
                                                                                   0]))):
                val = stack.pop()
                postfix += (' ' + str(val))
            stack.push(tok)
        elif tok == '(':
            stack.push(tok)
        elif tok == ')':
            while stack.peek() != '(':
                val1 = stack.pop()
                postfix += (' ' + str(val1))
            stack.pop()
        else:
            postfix += (' ' + str(tok))
    while stack.is_empty() is False:
        val2 = stack.pop()
        postfix += (' ' + str(val2))
    return postfix[1:]


def helper_infix_to_postfix(input_operator):
    pres = 0
    assoc = ''
    if input_operator in operators1:
        pres = 0
        assoc = 'l'
    if input_operator in operators2:
        pres = 1
        assoc = 'l'
    if input_operator in operators3:
        pres = 2
        assoc = 'r'
    if input_operator in operators4:
        pres = 3
        assoc = 'l'
    return [pres, assoc]


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    stack = Stack(30)
    new_input = input_str.split()
    reversed_new_input = new_input[::-1]
    for tok in reversed_new_input:
        if tok in operators:
            val1 = stack.pop()
            val2 = stack.pop()
            string = str(val1) + str(val2) + ' ' + tok
            stack.push(string)
        else:
            stack.push(' ' + str(tok))
    if stack.is_empty() is True:
        return ''
    return stack.peek()[1:]
