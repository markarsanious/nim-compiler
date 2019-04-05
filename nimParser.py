# Generated from nim.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0086")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\4\6\4\32")
        buf.write("\n\4\r\4\16\4\33\3\5\6\5\37\n\5\r\5\16\5 \3\6\3\6\3\7")
        buf.write("\3\7\3\7\2\2\b\2\4\6\b\n\f\2\4\3\2\24\37\7\2HHadppu\177")
        buf.write("\u0081\u0081#\2\23\3\2\2\2\4\26\3\2\2\2\6\31\3\2\2\2\b")
        buf.write("\36\3\2\2\2\n\"\3\2\2\2\f$\3\2\2\2\16\17\5\4\3\2\17\20")
        buf.write("\7\7\2\2\20\22\3\2\2\2\21\16\3\2\2\2\22\25\3\2\2\2\23")
        buf.write("\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\26")
        buf.write("\27\7\13\2\2\27\5\3\2\2\2\30\32\7b\2\2\31\30\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\7\3\2\2\2\35")
        buf.write("\37\7c\2\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2")
        buf.write("\2\2!\t\3\2\2\2\"#\t\2\2\2#\13\3\2\2\2$%\t\3\2\2%\r\3")
        buf.write("\2\2\2\5\23\33 ")
        return buf.getvalue()


class nimParser ( Parser ):

    grammarFileName = "nim.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "' '", "<INVALID>", "'and'", "'var'", "'or'", "'not'", 
                     "'div'", "'shl'", "'shr'", "'xor'", "'mod'", "'is'", 
                     "'isnot'", "'of'", "<INVALID>", "'+'", "'*'", "'-'", 
                     "'/'", "'~'", "'&'", "'|'", "'<'", "'>'", "'!'", "'^'", 
                     "'.'", "':'", "','", "';'", "'addr'", "'as'", "'asm'", 
                     "'bind'", "'block'", "'break'", "'case'", "'cast'", 
                     "'concept'", "'const'", "'continue'", "'converter'", 
                     "'defer'", "'discard'", "'distinct'", "'do'", "'elif'", 
                     "'else'", "'end'", "'enum'", "'except'", "'export'", 
                     "'finally'", "'for'", "'from'", "'func'", "'if'", "'import'", 
                     "'in'", "'include'", "'interface'", "'iterator'", "'let'", 
                     "'macro'", "'method'", "'mixin'", "'nil'", "'notin'", 
                     "'object'", "'out'", "'proc'", "'ptr'", "'raise'", 
                     "'ref'", "'return'", "'static'", "'template'", "'try'", 
                     "'tuple'", "'type'", "'using'", "'when'", "'while'", 
                     "'yield'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "DIGIT", "INDENT", "NOT_INDENT", "SPACE", 
                      "NEWLINE", "AND", "VARIABLE", "OR", "NOT", "DIV", 
                      "SHL", "SHR", "XOR", "MOD", "IS", "ISNOT", "OF", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "NOT_OPERATOR", 
                      "XOR_OPERATOR", "DOT", "COLON", "COMMA", "SEMI_COLON", 
                      "ADDR", "AS", "ASM", "BIND", "BLOCK", "BREAK", "CASE", 
                      "CAST", "CONCEPT", "CONST", "CONTINUE", "CONVERTER", 
                      "DEFER", "DISCARD", "DISTINCT", "DO", "ELIF", "ELSE", 
                      "END", "ENUM", "EXCEPT", "EXPORT", "FINALLY", "FOR", 
                      "FROM", "FUNC", "IF", "IMPORT", "IN", "INCLUDE", "INTERFACE", 
                      "ITERATOR", "LET", "MACRO", "METHOD", "MIXIN", "NIL", 
                      "NOTIN", "OBJECT", "OUT", "PROC", "PTR", "RAISE", 
                      "REF", "RETURN", "STATIC", "TEMPLATE", "TRY", "TUPLE", 
                      "TYPE", "USING", "WHEN", "WHILE", "YIELD", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACK", 
                      "CLOSE_BRACK", "MODULUS", "TRIPLESTR_LIT", "CHAR_LIT", 
                      "STR_LIT", "RSTR_LIT", "GENERALIZED_STR_LIT", "GENERALIZED_TRIPLESTR_LIT", 
                      "WS", "AT", "COMMENT", "MULTI_LINE_COMMENT", "MULTI_LINE_COMMENT2", 
                      "SINGLE_MULTI_LINE_COMMENT", "IDENTIFIER", "H", "LETTER", 
                      "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", "BIN_LIT", 
                      "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "FLOAT_LIT", "FLOAT32_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT64_LIT", "FLOAT64_SUFFIX", "EXP", "HEXDIGIT", 
                      "OCTDIGIT", "BINDIGIT" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_character_literals = 2
    RULE_string_literals = 3
    RULE_operator = 4
    RULE_literal = 5

    ruleNames =  [ "start", "expr", "character_literals", "string_literals", 
                   "operator", "literal" ]

    EOF = Token.EOF
    DIGIT=1
    INDENT=2
    NOT_INDENT=3
    SPACE=4
    NEWLINE=5
    AND=6
    VARIABLE=7
    OR=8
    NOT=9
    DIV=10
    SHL=11
    SHR=12
    XOR=13
    MOD=14
    IS=15
    ISNOT=16
    OF=17
    EQUALS_OPERATOR=18
    ADD_OPERATOR=19
    MUL_OPERATOR=20
    MINUS_OPERATOR=21
    DIV_OPERATOR=22
    BITWISE_NOT_OPERATOR=23
    AND_OPERATOR=24
    OR_OPERATOR=25
    LESS_THAN=26
    GREATER_THAN=27
    NOT_OPERATOR=28
    XOR_OPERATOR=29
    DOT=30
    COLON=31
    COMMA=32
    SEMI_COLON=33
    ADDR=34
    AS=35
    ASM=36
    BIND=37
    BLOCK=38
    BREAK=39
    CASE=40
    CAST=41
    CONCEPT=42
    CONST=43
    CONTINUE=44
    CONVERTER=45
    DEFER=46
    DISCARD=47
    DISTINCT=48
    DO=49
    ELIF=50
    ELSE=51
    END=52
    ENUM=53
    EXCEPT=54
    EXPORT=55
    FINALLY=56
    FOR=57
    FROM=58
    FUNC=59
    IF=60
    IMPORT=61
    IN=62
    INCLUDE=63
    INTERFACE=64
    ITERATOR=65
    LET=66
    MACRO=67
    METHOD=68
    MIXIN=69
    NIL=70
    NOTIN=71
    OBJECT=72
    OUT=73
    PROC=74
    PTR=75
    RAISE=76
    REF=77
    RETURN=78
    STATIC=79
    TEMPLATE=80
    TRY=81
    TUPLE=82
    TYPE=83
    USING=84
    WHEN=85
    WHILE=86
    YIELD=87
    OPEN_PAREN=88
    CLOSE_PAREN=89
    OPEN_BRACE=90
    CLOSE_BRACE=91
    OPEN_BRACK=92
    CLOSE_BRACK=93
    MODULUS=94
    TRIPLESTR_LIT=95
    CHAR_LIT=96
    STR_LIT=97
    RSTR_LIT=98
    GENERALIZED_STR_LIT=99
    GENERALIZED_TRIPLESTR_LIT=100
    WS=101
    AT=102
    COMMENT=103
    MULTI_LINE_COMMENT=104
    MULTI_LINE_COMMENT2=105
    SINGLE_MULTI_LINE_COMMENT=106
    IDENTIFIER=107
    H=108
    LETTER=109
    INT_LIT=110
    HEX_LIT=111
    DEC_LIT=112
    OCT_LIT=113
    BIN_LIT=114
    INT8_LIT=115
    INT16_LIT=116
    INT32_LIT=117
    INT64_LIT=118
    UINT_LIT=119
    UINT8_LIT=120
    UINT16_LIT=121
    UINT32_LIT=122
    UINT64_LIT=123
    FLOAT_LIT=124
    FLOAT32_LIT=125
    FLOAT32_SUFFIX=126
    FLOAT64_LIT=127
    FLOAT64_SUFFIX=128
    EXP=129
    HEXDIGIT=130
    OCTDIGIT=131
    BINDIGIT=132

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nimParser.ExprContext)
            else:
                return self.getTypedRuleContext(nimParser.ExprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(nimParser.NEWLINE)
            else:
                return self.getToken(nimParser.NEWLINE, i)

        def getRuleIndex(self):
            return nimParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = nimParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==nimParser.NOT:
                self.state = 12
                self.expr()
                self.state = 13
                self.match(nimParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(nimParser.NOT, 0)

        def getRuleIndex(self):
            return nimParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = nimParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(nimParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Character_literalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(nimParser.CHAR_LIT)
            else:
                return self.getToken(nimParser.CHAR_LIT, i)

        def getRuleIndex(self):
            return nimParser.RULE_character_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacter_literals" ):
                listener.enterCharacter_literals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacter_literals" ):
                listener.exitCharacter_literals(self)




    def character_literals(self):

        localctx = nimParser.Character_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_character_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.match(nimParser.CHAR_LIT)
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==nimParser.CHAR_LIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_literalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(nimParser.STR_LIT)
            else:
                return self.getToken(nimParser.STR_LIT, i)

        def getRuleIndex(self):
            return nimParser.RULE_string_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literals" ):
                listener.enterString_literals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literals" ):
                listener.exitString_literals(self)




    def string_literals(self):

        localctx = nimParser.String_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_string_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.match(nimParser.STR_LIT)
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==nimParser.STR_LIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS_OPERATOR(self):
            return self.getToken(nimParser.EQUALS_OPERATOR, 0)

        def ADD_OPERATOR(self):
            return self.getToken(nimParser.ADD_OPERATOR, 0)

        def MUL_OPERATOR(self):
            return self.getToken(nimParser.MUL_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(nimParser.MINUS_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(nimParser.DIV_OPERATOR, 0)

        def BITWISE_NOT_OPERATOR(self):
            return self.getToken(nimParser.BITWISE_NOT_OPERATOR, 0)

        def AND_OPERATOR(self):
            return self.getToken(nimParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(nimParser.OR_OPERATOR, 0)

        def LESS_THAN(self):
            return self.getToken(nimParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(nimParser.GREATER_THAN, 0)

        def NOT_OPERATOR(self):
            return self.getToken(nimParser.NOT_OPERATOR, 0)

        def XOR_OPERATOR(self):
            return self.getToken(nimParser.XOR_OPERATOR, 0)

        def getRuleIndex(self):
            return nimParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = nimParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << nimParser.EQUALS_OPERATOR) | (1 << nimParser.ADD_OPERATOR) | (1 << nimParser.MUL_OPERATOR) | (1 << nimParser.MINUS_OPERATOR) | (1 << nimParser.DIV_OPERATOR) | (1 << nimParser.BITWISE_NOT_OPERATOR) | (1 << nimParser.AND_OPERATOR) | (1 << nimParser.OR_OPERATOR) | (1 << nimParser.LESS_THAN) | (1 << nimParser.GREATER_THAN) | (1 << nimParser.NOT_OPERATOR) | (1 << nimParser.XOR_OPERATOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(nimParser.INT_LIT, 0)

        def INT8_LIT(self):
            return self.getToken(nimParser.INT8_LIT, 0)

        def INT16_LIT(self):
            return self.getToken(nimParser.INT16_LIT, 0)

        def INT32_LIT(self):
            return self.getToken(nimParser.INT32_LIT, 0)

        def INT64_LIT(self):
            return self.getToken(nimParser.INT64_LIT, 0)

        def UINT_LIT(self):
            return self.getToken(nimParser.UINT_LIT, 0)

        def UINT8_LIT(self):
            return self.getToken(nimParser.UINT8_LIT, 0)

        def UINT16_LIT(self):
            return self.getToken(nimParser.UINT16_LIT, 0)

        def UINT32_LIT(self):
            return self.getToken(nimParser.UINT32_LIT, 0)

        def UINT64_LIT(self):
            return self.getToken(nimParser.UINT64_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(nimParser.FLOAT_LIT, 0)

        def FLOAT32_LIT(self):
            return self.getToken(nimParser.FLOAT32_LIT, 0)

        def FLOAT64_LIT(self):
            return self.getToken(nimParser.FLOAT64_LIT, 0)

        def STR_LIT(self):
            return self.getToken(nimParser.STR_LIT, 0)

        def RSTR_LIT(self):
            return self.getToken(nimParser.RSTR_LIT, 0)

        def TRIPLESTR_LIT(self):
            return self.getToken(nimParser.TRIPLESTR_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(nimParser.CHAR_LIT, 0)

        def NIL(self):
            return self.getToken(nimParser.NIL, 0)

        def getRuleIndex(self):
            return nimParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = nimParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(((((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & ((1 << (nimParser.NIL - 70)) | (1 << (nimParser.TRIPLESTR_LIT - 70)) | (1 << (nimParser.CHAR_LIT - 70)) | (1 << (nimParser.STR_LIT - 70)) | (1 << (nimParser.RSTR_LIT - 70)) | (1 << (nimParser.INT_LIT - 70)) | (1 << (nimParser.INT8_LIT - 70)) | (1 << (nimParser.INT16_LIT - 70)) | (1 << (nimParser.INT32_LIT - 70)) | (1 << (nimParser.INT64_LIT - 70)) | (1 << (nimParser.UINT_LIT - 70)) | (1 << (nimParser.UINT8_LIT - 70)) | (1 << (nimParser.UINT16_LIT - 70)) | (1 << (nimParser.UINT32_LIT - 70)) | (1 << (nimParser.UINT64_LIT - 70)) | (1 << (nimParser.FLOAT_LIT - 70)) | (1 << (nimParser.FLOAT32_LIT - 70)) | (1 << (nimParser.FLOAT64_LIT - 70)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





