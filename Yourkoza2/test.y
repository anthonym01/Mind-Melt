let age equal 18
let drinking_age equal 21

! Check if you are underage
if age < drinking_age then
    show "You are too young to drink"
else
    show "Have a good one my guy"
end

show age


def p_expression(p):
    """
    expression : expression PLUS term
               | expression MINUS term
               | term
               | expression POWER term
               | NOT expression
               | LPAREN expression RPAREN
               | NUMBER MINUS term
               | REAL MINUS term
               | CHARACTER PLUS term
               | list
    """
    #if len(p) == 4:
    #    if p[2] == '+':
    #        p[0] = p[1] + p[3]
    #    elif p[2] == '-':
    #        p[0] = p[1] - p[3]
    #    elif p[2] == '**':  # Handle power operator
    #        p[0] = p[1] ** p[3]
    #elif len(p) == 3:
    #    if p[1] == 'not':  # Handle NOT operator
    #        p[0] = not p[2]
    #    elif p[1] == '-':  # Handle unary minus
    #        p[0] = -p[2]
    #    elif p[1] == '+':  # Handle unary plus
    #        p[0] = p[2]
    #else:
    #    p[0] = p[1]
    if len(p) == 4:
        p[0] = ('expression', p[1], p[2], p[3])
    if len(p) == 3:
        p[0] = ('expression', p[1], p[2])
    else:
        p[0] = p[1]