grammar nim;

start: (expr NEWLINE)*;

// expr: NOT;

module: (stmt ((';' | INDENT) stmt)*)?;
comma: ',' COMMENT?;
semicolon: ';' COMMENT?;
colon: ':' COMMENT?;
colcom: ':' COMMENT?;
prefixOperator: operator;
optInd: COMMENT? INDENT?;
optPar: (INDENT)?;
simpleExpr: arrowExpr (operator optInd arrowExpr)* pragma?;
arrowExpr: assignExpr (operator optInd assignExpr)*;
assignExpr: orExpr (operator optInd orExpr)*;
orExpr: andExpr (OP3 optInd andExpr)*;
andExpr: cmpExpr (OP4 optInd cmpExpr)*;
cmpExpr: sliceExpr (OP5 optInd sliceExpr)*;
sliceExpr: ampExpr (OP6 optInd ampExpr)*;
ampExpr: plusExpr (OP7 optInd plusExpr)*;
plusExpr: mulExpr (OP8 optInd mulExpr)*;
mulExpr: dollarExpr (OP9 optInd dollarExpr)*;
dollarExpr: primary (operator optInd primary)*;
OP3: OR_OPERATOR | XOR_OPERATOR | XOR | OR;
OP4: AND;
OP5:
	EQUALS_OPERATOR
	| LESS_THAN
	| GREATER_THAN
	| NOT_OPERATOR
	| NOTIN
	| IS
	| ISNOT
	| OF
	| NOT;
OP6: '..';
OP7: AND_OPERATOR;
OP8: MINUS_OPERATOR | ADD_OPERATOR;
OP9:
	MUL_OPERATOR
	| DIV_OPERATOR
	| DIV
	| MOD
	| MODULUS
	| SHL
	| SHR;
symbol:
	'`' (
		IDENTIFIER
		| literal
		| (operator | '(' | ')' | '[' | ']' | '{' | '}' | '=')+
	)+ '`'
	| IDENTIFIER;
exprColonEqExpr: expr (':' | '=' expr)?;
exprList: expr (comma expr)*;
exprColonEqExprList:
	exprColonEqExpr (comma exprColonEqExpr)* (comma)?;
dotExpr: expr '.' optInd (symbol | '[:' exprList ']');
explicitGenericInstantiation:
	'[:' exprList ']' ('(' exprColonEqExpr ')')?;
qualifiedIdent: symbol ('.' optInd symbol)?;
setOrTableConstr: '{' ((exprColonEqExpr comma)* | ':') '}';
castExpr:
	'cast' '[' optInd typeDesc optPar ']' '(' optInd expr optPar ')';
parKeyw:
	'discard'
	| 'include'
	| 'if'
	| 'while'
	| 'case'
	| 'try'
	| 'finally'
	| 'except'
	| 'for'
	| 'block'
	| 'const'
	| 'let'
	| 'when'
	| 'var'
	| 'mixin';
par:
	'(' optInd (
		complexOrSimpleStmt (';' complexOrSimpleStmt)*
		| ';' complexOrSimpleStmt (';' complexOrSimpleStmt)*
		| pragmaStmt
		| simpleExpr (
			(
				'=' expr (
					';' complexOrSimpleStmt (
						';' complexOrSimpleStmt
					)*
				)?
			)
			| (
				':' expr (
					',' exprColonEqExpr (',' exprColonEqExpr)*
				)?
			)
		)
	) optPar ')';
literal:
	| INT_LIT
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
generalizedLit: GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT;
identOrLiteral:
	generalizedLit
	| symbol
	| literal
	| par
	| arrayConstr
	| setOrTableConstr
	| castExpr;
tupleConstr: '(' optInd (exprColonEqExpr comma?)* optPar ')';
arrayConstr: '[' optInd (exprColonEqExpr comma?)* optPar ']';
primarySuffix:
	'(' (exprColonEqExpr comma?)* ')' doBlock?
	| doBlock
	| '.' optInd symbol generalizedLit
	// | '[' optInd indexExprList optPar ']' | '{' optInd indexExprList optPar '}'
	| ('`' | IDENTIFIER | literal | 'cast' | 'addr' | 'type') expr;
condExpr:
	expr colcom expr optInd ('elif' expr colcom expr optInd)* 'else' colcom expr;
ifExpr: 'if' condExpr;
whenExpr: 'when' condExpr;
pragma: '{.' optInd (exprColonExpr comma?)* optPar ('.}' | '}');
identVis: symbol operator?;
identVisDot: symbol '.' optInd symbol operator?;
identWithPragma: identVis pragma?;
identWithPragmaDot: identVisDot pragma?;
exprColonExpr: expr COLON expr;
declColonEquals:
	identWithPragma (comma identWithPragma)* comma? (
		':' optInd typeDesc
	)? ('=' optInd expr)?;
identColonEquals:
	IDENTIFIER (comma IDENTIFIER)* comma? (':' optInd typeDesc)? (
		'=' optInd expr
	)?;
inlTupleDecl:
	'tuple' '[' optInd (identColonEquals (comma semicolon)?)* optPar ']';
extTupleDecl:
	'tuple' COMMENT? (
		INDENT identColonEquals (INDENT identColonEquals)*
	)?;
tupleClass: 'tuple';
paramList:
	'(' (declColonEquals ((comma SEMI_COLON) declColonEquals)*)? ')';
paramListArrow: paramList? ('->' optInd typeDesc)?;
paramListColon: paramList? (':' optInd typeDesc)?;
doBlock: 'do' paramListArrow pragma* colcom stmt;
procExpr: 'proc' paramListColon pragma* ('=' COMMENT? stmt)?;
distinct: 'distinct' optInd typeDesc;
forStmt:
	'for' (identWithPragma (comma identWithPragma)*) 'in' expr colcom stmt;
forExpr: forStmt;
expr: (
		blockExpr
		| ifExpr
		| whenExpr
		| caseStmt
		| forExpr
		| tryExpr
	)
	| simpleExpr;
typeKeyw:
	'var'
	| 'out'
	| 'ref'
	| 'ptr'
	| 'shared'
	| 'tuple'
	| 'proc'
	| 'iterator'
	| 'distinct'
	| 'object'
	| 'enum';
primary:
	typeKeyw typeDesc
	| prefixOperator* identOrLiteral primarySuffix*
	| 'bind' primary;
typeDesc: simpleExpr;
typeDefAux: simpleExpr | 'concept' typeClass;
postExprBlocks:
	':' stmt? (
		INDENT doBlock
		| INDENT 'of' exprList ':' stmt
		| INDENT 'elif' expr ':' stmt
		| INDENT 'except' exprList ':' stmt
		| INDENT 'else' ':' stmt
	)*;
exprStmt:
	simpleExpr (
		( '=' optInd expr colonBody?)
		| (
			expr (comma expr)* doBlock*
			|
			// macroColon
		)
	)?;
importStmt:
	'import' optInd expr (
		(comma expr)* 'except' optInd (expr (comma expr)*)
	);
includeStmt: 'include' optInd expr (comma expr)*;
fromStmt: 'from' IDENTIFIER 'import' optInd expr (comma expr)*;
returnStmt: 'return' optInd expr?;
raiseStmt: 'raise' optInd expr?;
yieldStmt: 'yield' optInd expr?;
discardStmt: 'discard' optInd expr?;
breakStmt: 'break' optInd expr?;
continueStmt: 'break' optInd expr?;
condStmt:
	expr colcom stmt COMMENT? (INDENT 'elif' expr colcom stmt)* (
		INDENT 'else' colcom stmt
	)?;
ifStmt: 'if' condStmt;
whenStmt: 'when' condStmt;
whileStmt: 'while' expr colcom stmt;
ofBranch: 'of' exprList colcom stmt;
ofBranches:
	ofBranch (INDENT ofBranch)* (INDENT 'elif' expr colcom stmt)* (
		INDENT 'else' colcom stmt
	)?;
caseStmt:
	'case' expr ':'? COMMENT? (
		INDENT ofBranches
		// DED
		| INDENT ofBranches
	);
tryStmt:
	'try' colcom stmt (INDENT? 'except' | 'finally') (
		INDENT? 'except' exprList colcom stmt
	)* (INDENT? 'finally' colcom stmt)?;
tryExpr:
	'try' colcom stmt (optInd 'except' | 'finally') (
		optInd 'except' exprList colcom stmt
	)* (optInd 'finally' colcom stmt)?;
exceptBlock: 'except' colcom stmt;
blockStmt: 'block' symbol? colcom stmt;
blockExpr: 'block' symbol? colcom stmt;
staticStmt: 'static' colcom stmt;
deferStmt: 'defer' colcom stmt;
asmStmt: 'asm' pragma? (STR_LIT | RSTR_LIT | TRIPLESTR_LIT);
genericParam:
	symbol (comma symbol)* (colon expr)? ('=' optInd expr)?;
genericParamList:
	'[' optInd (genericParam ((comma semicolon) genericParam)*)? optPar ']';
pattern: '{' stmt '}';
indAndComment: (INDENT COMMENT)? | COMMENT?;
routine:
	optInd identVis pattern? genericParamList? paramListColon pragma? (
		'=' COMMENT? stmt
	)? indAndComment;
commentStmt: COMMENT;
// section(p) : COMMENT? p / (IND{>} (p / COMMENT) (IND{=} (p / COMMENT))* DED);
constant:
	identWithPragma (colon typeDesc)? '=' optInd expr indAndComment;
enum:
	'enum' optInd (
		symbol optInd ('=' optInd expr COMMENT?)? comma?
	)+;
objectWhen:
	'when' expr colcom objectPart COMMENT? (
		'elif' expr colcom objectPart COMMENT?
	)* ('else' colcom objectPart COMMENT?)?;
objectBranch: 'of' exprList colcom objectPart;
objectBranches:
	objectBranch (INDENT objectBranch)* (
		INDENT 'elif' expr colcom objectPart
	)* (INDENT 'else' colcom objectPart)?;
objectCase:
	'case' identWithPragma ':' typeDesc ':'? COMMENT? (
		INDENT objectBranches
		// DED
		| INDENT objectBranches
	);
objectPart:
	INDENT objectPart (INDENT objectPart)*
	// DED
	| objectWhen
	| objectCase
	| 'nil'
	| 'discard'
	| declColonEquals;
object: 'object' pragma? ('of' typeDesc)? COMMENT? objectPart;
typeClassParam: ('var' | 'out')? symbol;
typeClass:
	typeClassParam (',' typeClassParam)* (pragma)? (
		'of' (typeDesc (',' typeDesc)*)?
	)? INDENT stmt;
typeDef:
	identWithPragmaDot genericParamList? '=' optInd typeDefAux indAndComment?;
varTuple:
	'(' optInd identWithPragma (comma identWithPragma)* optPar ')' '=' optInd expr;
colonBody: colcom stmt doBlock*;
variable: (varTuple identColonEquals) colonBody? indAndComment;
bindStmt: 'bind' optInd qualifiedIdent (comma qualifiedIdent)*;
mixinStmt:
	'mixin' optInd qualifiedIdent (comma qualifiedIdent)*;
pragmaStmt: pragma (':' COMMENT? stmt)?;
simpleStmt: (
		(
			returnStmt
			| raiseStmt
			| yieldStmt
			| discardStmt
			| breakStmt
			| continueStmt
			| pragmaStmt
			| importStmt
			// | exportStmt
			| fromStmt
			| includeStmt
			| commentStmt
		) exprStmt
	) COMMENT?;
complexOrSimpleStmt: (
		ifStmt
		| whenStmt
		| whileStmt
		| tryStmt
		| forStmt
		| blockStmt
		| staticStmt
		| deferStmt
		| asmStmt
		| 'proc' routine
		| 'method' routine
		| 'iterator' routine
		| 'macro' routine
		| 'template' routine
		| 'converter' routine
		| 'type' (typeDef) // section
		| 'const' (constant) // section
		| ('let' | 'var' | 'using') (variable) // section
		| bindStmt
		| mixinStmt
	)
	| simpleStmt;
stmt: (
		INDENT complexOrSimpleStmt ((INDENT ';')) complexOrSimpleStmt //DED
	)*
	| simpleStmt (';' simpleStmt)*;

character_literals: CHAR_LIT+;
string_literals: STR_LIT+;

DIGIT: [0-9];
INDENT: (SPACE SPACE SPACE SPACE)+;
NOT_INDENT:
	INDENT* (SPACE | SPACE SPACE | SPACE SPACE SPACE) -> skip;
SPACE: ' ' -> skip;
NEWLINE: [\n\r]+ -> skip;

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
operator:
	EQUALS_OPERATOR
	| ADD_OPERATOR
	| MUL_OPERATOR
	| MINUS_OPERATOR
	| DIV_OPERATOR
	| BITWISE_NOT_OPERATOR
	| AND_OPERATOR
	| OR_OPERATOR
	| LESS_THAN
	| GREATER_THAN
	| NOT_OPERATOR
	| XOR_OPERATOR;
EQUALS_OPERATOR: '=' | '==';
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
	'\"' (
		[\p\r\c\l\f\t\v\\\"\'\-]
		| [\\] [0-9]+
		| ' '
		| ','
		| '.'
		| ':'
		| '/'
		| ']'
		| '['
		| ', '
		| [\a\b\e]
		| [\x] H H
		| SPACE
		| [a-zA-Z0-9?!@#$%^&*()_+=`~}{]
	)* '\"';
RSTR_LIT: ('r' | 'R') STR_LIT;
GENERALIZED_STR_LIT: IDENTIFIER STR_LIT;
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER TRIPLESTR_LIT;

WS: [ \t]+ -> skip;
AT: 'at' | '@';
COMMENT: INDENT? '#' ~('\r' | '\n' | '#')* -> skip;
MULTI_LINE_COMMENT:
	INDENT? (
		('#' MULTI_LINE_COMMENT2 '#')
		| ('#' OPEN_BRACK MULTI_LINE_COMMENT2 CLOSE_BRACK '#')
		| MULTI_LINE_COMMENT2
	) -> skip;

MULTI_LINE_COMMENT2:
	(
		('#' MULTI_LINE_COMMENT2 '#')
		| ('#' OPEN_BRACK MULTI_LINE_COMMENT2 CLOSE_BRACK '#')
		| SINGLE_MULTI_LINE_COMMENT
	) -> skip;

SINGLE_MULTI_LINE_COMMENT:
	'#' OPEN_BRACK .* CLOSE_BRACK '#' -> skip;

IDENTIFIER: '$'? LETTER (['_']* (LETTER | DIGIT))*;
H: [A-Fa-f0-9];

LETTER: [a-zA-Z];

// literal: INT_LIT | INT8_LIT | INT16_LIT | INT32_LIT | INT64_LIT | UINT_LIT | UINT8_LIT |
// UINT16_LIT | UINT32_LIT | UINT64_LIT | FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT | STR_LIT | RSTR_LIT
// | TRIPLESTR_LIT | CHAR_LIT | NIL;
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