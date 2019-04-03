# Generated from nim.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0082")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\4\6\4\32")
        buf.write("\n\4\r\4\16\4\33\3\5\6\5\37\n\5\r\5\16\5 \3\6\3\6\3\7")
        buf.write("\3\7\3\7\2\2\b\2\4\6\b\n\f\2\4\3\2\22\35\7\2FF__dnppv")
        buf.write("y#\2\23\3\2\2\2\4\26\3\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2")
        buf.write("\n\"\3\2\2\2\f$\3\2\2\2\16\17\5\4\3\2\17\20\7\5\2\2\20")
        buf.write("\22\3\2\2\2\21\16\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2")
        buf.write("\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\26\27\7\t\2")
        buf.write("\2\27\5\3\2\2\2\30\32\7w\2\2\31\30\3\2\2\2\32\33\3\2\2")
        buf.write("\2\33\31\3\2\2\2\33\34\3\2\2\2\34\7\3\2\2\2\35\37\7x\2")
        buf.write("\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\t")
        buf.write("\3\2\2\2\"#\t\2\2\2#\13\3\2\2\2$%\t\3\2\2%\r\3\2\2\2\5")
        buf.write("\23\33 ")
        return buf.getvalue()


class nimParser ( Parser ):

    grammarFileName = "nim.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "' '", "<INVALID>", "'and'", 
                     "'var'", "'or'", "'not'", "'div'", "'shl'", "'shr'", 
                     "'xor'", "'mod'", "'is'", "'isnot'", "'of'", "'='", 
                     "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", "'|'", "'<'", 
                     "'>'", "'!'", "'^'", "'.'", "':'", "','", "';'", "'addr'", 
                     "'as'", "'asm'", "'bind'", "'block'", "'break'", "'case'", 
                     "'cast'", "'concept'", "'const'", "'continue'", "'converter'", 
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

    symbolicNames = [ "<INVALID>", "DIGIT", "SPACE", "NEWLINE", "AND", "VARIABLE", 
                      "OR", "NOT", "DIV", "SHL", "SHR", "XOR", "MOD", "IS", 
                      "ISNOT", "OF", "EQUALS_OPERATOR", "ADD_OPERATOR", 
                      "MUL_OPERATOR", "MINUS_OPERATOR", "DIV_OPERATOR", 
                      "BITWISE_NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
                      "LESS_THAN", "GREATER_THAN", "NOT_OPERATOR", "XOR_OPERATOR", 
                      "DOT", "COLON", "COMMA", "SEMI_COLON", "ADDR", "AS", 
                      "ASM", "BIND", "BLOCK", "BREAK", "CASE", "CAST", "CONCEPT", 
                      "CONST", "CONTINUE", "CONVERTER", "DEFER", "DISCARD", 
                      "DISTINCT", "DO", "ELIF", "ELSE", "END", "ENUM", "EXCEPT", 
                      "EXPORT", "FINALLY", "FOR", "FROM", "FUNC", "IF", 
                      "IMPORT", "IN", "INCLUDE", "INTERFACE", "ITERATOR", 
                      "LET", "MACRO", "METHOD", "MIXIN", "NIL", "NOTIN", 
                      "OBJECT", "OUT", "PROC", "PTR", "RAISE", "REF", "RETURN", 
                      "STATIC", "TEMPLATE", "TRY", "TUPLE", "TYPE", "USING", 
                      "WHEN", "WHILE", "YIELD", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", 
                      "MODULUS", "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", 
                      "BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "FLOAT_LIT", "FLOAT32_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT64_LIT", "FLOAT64_SUFFIX", "EXP", "HEXDIGIT", 
                      "OCTDIGIT", "BINDIGIT", "TRIPLESTR_LIT", "CHAR_LIT", 
                      "STR_LIT", "RSTR_LIT", "GENERALIZED_STR_LIT", "GENERALIZED_TRIPLESTR_LIT", 
                      "H", "INDENT", "AT", "COMMENT", "MULTI_LINE_COMMENT", 
                      "IDENTIFIER", "LETTER" ]

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
    SPACE=2
    NEWLINE=3
    AND=4
    VARIABLE=5
    OR=6
    NOT=7
    DIV=8
    SHL=9
    SHR=10
    XOR=11
    MOD=12
    IS=13
    ISNOT=14
    OF=15
    EQUALS_OPERATOR=16
    ADD_OPERATOR=17
    MUL_OPERATOR=18
    MINUS_OPERATOR=19
    DIV_OPERATOR=20
    BITWISE_NOT_OPERATOR=21
    AND_OPERATOR=22
    OR_OPERATOR=23
    LESS_THAN=24
    GREATER_THAN=25
    NOT_OPERATOR=26
    XOR_OPERATOR=27
    DOT=28
    COLON=29
    COMMA=30
    SEMI_COLON=31
    ADDR=32
    AS=33
    ASM=34
    BIND=35
    BLOCK=36
    BREAK=37
    CASE=38
    CAST=39
    CONCEPT=40
    CONST=41
    CONTINUE=42
    CONVERTER=43
    DEFER=44
    DISCARD=45
    DISTINCT=46
    DO=47
    ELIF=48
    ELSE=49
    END=50
    ENUM=51
    EXCEPT=52
    EXPORT=53
    FINALLY=54
    FOR=55
    FROM=56
    FUNC=57
    IF=58
    IMPORT=59
    IN=60
    INCLUDE=61
    INTERFACE=62
    ITERATOR=63
    LET=64
    MACRO=65
    METHOD=66
    MIXIN=67
    NIL=68
    NOTIN=69
    OBJECT=70
    OUT=71
    PROC=72
    PTR=73
    RAISE=74
    REF=75
    RETURN=76
    STATIC=77
    TEMPLATE=78
    TRY=79
    TUPLE=80
    TYPE=81
    USING=82
    WHEN=83
    WHILE=84
    YIELD=85
    OPEN_PAREN=86
    CLOSE_PAREN=87
    OPEN_BRACE=88
    CLOSE_BRACE=89
    OPEN_BRACK=90
    CLOSE_BRACK=91
    MODULUS=92
    INT_LIT=93
    HEX_LIT=94
    DEC_LIT=95
    OCT_LIT=96
    BIN_LIT=97
    INT8_LIT=98
    INT16_LIT=99
    INT32_LIT=100
    INT64_LIT=101
    UINT_LIT=102
    UINT8_LIT=103
    UINT16_LIT=104
    UINT32_LIT=105
    UINT64_LIT=106
    FLOAT_LIT=107
    FLOAT32_LIT=108
    FLOAT32_SUFFIX=109
    FLOAT64_LIT=110
    FLOAT64_SUFFIX=111
    EXP=112
    HEXDIGIT=113
    OCTDIGIT=114
    BINDIGIT=115
    TRIPLESTR_LIT=116
    CHAR_LIT=117
    STR_LIT=118
    RSTR_LIT=119
    GENERALIZED_STR_LIT=120
    GENERALIZED_TRIPLESTR_LIT=121
    H=122
    INDENT=123
    AT=124
    COMMENT=125
    MULTI_LINE_COMMENT=126
    IDENTIFIER=127
    LETTER=128

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
            if not(((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (nimParser.NIL - 68)) | (1 << (nimParser.INT_LIT - 68)) | (1 << (nimParser.INT8_LIT - 68)) | (1 << (nimParser.INT16_LIT - 68)) | (1 << (nimParser.INT32_LIT - 68)) | (1 << (nimParser.INT64_LIT - 68)) | (1 << (nimParser.UINT_LIT - 68)) | (1 << (nimParser.UINT8_LIT - 68)) | (1 << (nimParser.UINT16_LIT - 68)) | (1 << (nimParser.UINT32_LIT - 68)) | (1 << (nimParser.UINT64_LIT - 68)) | (1 << (nimParser.FLOAT_LIT - 68)) | (1 << (nimParser.FLOAT32_LIT - 68)) | (1 << (nimParser.FLOAT64_LIT - 68)) | (1 << (nimParser.TRIPLESTR_LIT - 68)) | (1 << (nimParser.CHAR_LIT - 68)) | (1 << (nimParser.STR_LIT - 68)) | (1 << (nimParser.RSTR_LIT - 68)))) != 0)):
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





