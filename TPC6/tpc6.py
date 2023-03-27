import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'INT',
    'VAR_NAME',
    'SEMICOLON',
    'IS_FUNCTION',
    'FUNCTION_NAME',
    'PAROPEN',
    'PARCLOSE',
    'ARGS',
    'COMMA',
    'BRACESOPEN',
    'BRACESCLOSE',
    'EQUALS',
    'NUMBER',
    'WHILE',
    'COMPARATOR_SYMBOL',
    'OPERATORS',
    'PROGRAM',
    'FOR',
    'IN',
    'RANGE',
    'IF',
    'SQBRACKETSOPEN',
    'SQBRACKETSCLOSE'
)

# Regular expression rules for simple tokens

t_SEMICOLON = r';'
t_COMMA = r'\,'
t_BRACESOPEN = r'{'
t_BRACESCLOSE = r'}'
t_PAROPEN = r'\('
t_PARCLOSE = r'\)'
t_EQUALS = r'\='
t_SQBRACKETSOPEN = r'\['
t_SQBRACKETSCLOSE = r'\]'

# A regular expression rule with some action code
def t_ignore_singleLine(t):
    r'\/\/.*?\n'
    pass

def t_ignore_multipleLine(t):
    r'\/\*(.|\n)*?\*\/'
    pass

def t_INT(t):
    r'\bint\b'
    return t

def t_PROGRAM(t):
    r'program\s+([a-zA-Z_][\w_]*)'
    return t


def t_IS_FUNCTION(t):
    r'\bfunction '
    return t

def t_FUNCTION_NAME(t):
    r'[a-zA-Z_][\w_]*(?=\()'
    return t


def t_ARGS(t):
    r'[a-zA-Z_][\w_]*(?=\,|\))'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_COMPARATOR_SYMBOL(t):
    r'(>|<|==|>=|<=)'
    return t

def t_OPERATORS(t):
    r'(\+|\-|\*|\/)'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_RANGE(t):
    r'\[\d+\.\.\d+\]'
    return t

def t_IF(t):
    r'if'
    return t

def t_VAR_NAME(t):
    r'[a-zA-Z_][\w_]*'
    return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)


t_ignore=' \t\n'

lexer = lex.lex()

data = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}

/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/

int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};

// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer.input(data)
while tok := lexer.token():
    print(tok)