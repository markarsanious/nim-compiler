grammar nim;

start: (expr NEWLINE)*;

expr: NOT;

character_literals: CHAR_LIT*;
string_literals: STR_LIT*;

NEWLINE: [\r\n]+;
IDENTIFIER: LETTER+ ('_' (LETTER | DIGIT))*;
DIGIT: [0-9];
LETTER: [a-zA-Z];

AND: 'and';
VARIABLE: 'var';
OR: 'or';
NOT: 'not';
DIV: 'div';
SHL: 'shl';
SHR: 'shr';
XOR: 'xor';
MOD: 'mod';
IS: 'is';
ISNOT: 'isnot';
OF: 'of';
OPERATOR: EQUALS_OPERATOR | ADD_OPERATOR | MUL_OPERATOR | MINUS_OPERATOR | DIV_OPERATOR | BITWISE_NOT_OPERATOR | AND_OPERATOR | OR_OPERATOR | LESS_THAN | GREATER_THAN | NOT_OPERATOR | XOR_OPERATOR;
EQUALS_OPERATOR: '=';
ADD_OPERATOR: '+';
MUL_OPERATOR: '*';
MINUS_OPERATOR: '-';
DIV_OPERATOR: '/';
BITWISE_NOT_OPERATOR: '~';
AND_OPERATOR: '&';
OR_OPERATOR: '|';
LESS_THAN: '<';
GREATER_THAN: '>';
NOT_OPERATOR: '!';
XOR_OPERATOR: '^';
DOT: '.';
COLON: ':';
COMMA: ',';
SEMI_COLON: ';';
ADDR: 'addr';
AS: 'as';
ASM: 'asm';
BIND: 'bind';
BLOCK: 'block';
BREAK: 'break';
CASE: 'case';
CAST: 'cast';
CONCEPT: 'concept';
CONST: 'const';
CONTINUE: 'continue';
CONVERTER: 'converter';
DEFER: 'defer';
DISCARD: 'discard';
DISTINCT: 'distinct';
DO: 'do';
ELIF: 'elif';
ELSE: 'else';
END: 'end';
ENUM: 'enum';
EXCEPT: 'except';
EXPORT: 'export';
FINALLY: 'finally';
FOR: 'for';
FROM: 'from';
FUNC: 'func';
IF: 'if';
IMPORT: 'import';
IN: 'in';
INCLUDE: 'include';
INTERFACE: 'interface';
ITERATOR: 'iterator';
LET: 'let';
MACRO: 'macro';
METHOD: 'method';
MIXIN: 'mixin';
NIL: 'nil';
NOTIN: 'notin';
OBJECT: 'object';
OUT: 'out';
PROC: 'proc';
PTR: 'ptr';
RAISE: 'raise';
REF: 'ref';
RETURN: 'return';
STATIC: 'static';
TEMPLATE: 'template';
TRY: 'try';
TUPLE: 'tuple';
TYPE: 'type';
USING: 'using';
WHEN: 'when';
WHILE: 'while';
YIELD: 'yield';

OPEN_PAREN: '(';
CLOSE_PAREN: ')';
OPEN_BRACE: '{';
CLOSE_BRACE: '}';
OPEN_BRACK: '[';
CLOSE_BRACK: ']';

MODULUS: '%';

literal:
	INT_LIT
	| INT8_LIT
	| INT16_LIT
	| INT32_LIT
	| INT64_LIT
	| UINT_LIT
	| UINT8_LIT
	| UINT16_LIT
	| UINT32_LIT
	| UINT64_LIT
	| FLOAT_LIT
	| FLOAT32_LIT
	| FLOAT64_LIT
	| STR_LIT
	| RSTR_LIT
	| TRIPLESTR_LIT
	| CHAR_LIT
	| NIL;
INT_LIT: HEX_LIT | DEC_LIT | OCT_LIT | BIN_LIT;
HEX_LIT: '0' ('x' | 'X') HEXDIGIT+ ( '_' HEXDIGIT)*;
DEC_LIT: DIGIT+ ( '_' DIGIT+)*;
OCT_LIT: '0' 'o' OCTDIGIT+ ( '_' OCTDIGIT)*;
BIN_LIT: '0' ('b' | 'B') BINDIGIT+ ( '_' BINDIGIT+)*;
INT8_LIT: INT_LIT '\'' ('i' | 'I') '8';
INT16_LIT: INT_LIT '\'' ('i' | 'I') '16';
INT32_LIT: INT_LIT '\'' ('i' | 'I') '32';
INT64_LIT: INT_LIT '\'' ('i' | 'I') '64';
UINT_LIT: INT_LIT '\'' ('u' | 'U');
UINT8_LIT: UINT_LIT '8';
UINT16_LIT: UINT_LIT '16';
UINT32_LIT: UINT_LIT '32';
UINT64_LIT: UINT_LIT '64';
FLOAT_LIT:
	DIGIT+ ('_' DIGIT)* (('.' DIGIT+ ('_' DIGIT)* EXP?) | EXP);
FLOAT32_LIT:
	HEX_LIT '\'' FLOAT32_SUFFIX
	| (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\'' FLOAT32_SUFFIX;
FLOAT32_SUFFIX: ('f' | 'F') '32';
FLOAT64_LIT:
	HEX_LIT '\'' FLOAT64_SUFFIX
	| (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\'' FLOAT64_SUFFIX;
FLOAT64_SUFFIX: ( ('f' | 'F') '64') | 'd' | 'D';

EXP: ('e' | 'E') [+-] DIGIT+ ( [_] DIGIT)*;
HEXDIGIT: DIGIT | [A-Fa-f];
OCTDIGIT: [0-7];
BINDIGIT: [0-1];

TRIPLESTR_LIT: '"""' .* '"""';
CHAR_LIT:
	'\'\\t\''
	| '\'\\r\''
	| '\'\\c\''
	| '\'\\n\''
	| '\'\\l\''
	| '\'\\f\''
	| '\'\\v\''
	| '\'\\\\\''
	| '\'\\\"\''
	| '\'\\\'\''
	| '\'\\a\''
	| '\'\\b\''
	| '\'\\e\''
	| '\'\\x\''
	| ('\'' [0-9a-zA-Z] '\'');
STR_LIT:
	'"' ([\p\r\c\n\l\f\t\v\\\"\'] | [\'0-9\'] | [\a\b\e\xHH])* '"';
RSTR_LIT: 'r' '"' ( '\\' [btnfr"'\\] | ~[\r\n\\"])* '"';
GENERALIZED_STR_LIT: IDENTIFIER STR_LIT;
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER TRIPLESTR_LIT;
H: [a-f0-9];

INDENTATION: '    ';

AT: 'at' | '@';
COMMENT: '#' ~('\r' | '\n' | '#')*;
MULTI_LINE_COMMENT: '#' OPEN_BRACK .* CLOSE_BRACK '#'