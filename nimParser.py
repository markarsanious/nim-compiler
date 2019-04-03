# Generated from nim.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\177")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\4\7\4\30\n\4\f")
        buf.write("\4\16\4\33\13\4\3\5\7\5\36\n\5\f\5\16\5!\13\5\3\6\3\6")
        buf.write("\3\6\2\2\7\2\4\6\b\n\2\3\7\2GG``eoqqwz\"\2\21\3\2\2\2")
        buf.write("\4\24\3\2\2\2\6\31\3\2\2\2\b\37\3\2\2\2\n\"\3\2\2\2\f")
        buf.write("\r\5\4\3\2\r\16\7\3\2\2\16\20\3\2\2\2\17\f\3\2\2\2\20")
        buf.write("\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23")
        buf.write("\21\3\2\2\2\24\25\7\n\2\2\25\5\3\2\2\2\26\30\7x\2\2\27")
        buf.write("\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\7\3\2\2\2\33\31\3\2\2\2\34\36\7y\2\2\35\34\3\2\2\2")
        buf.write("\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \t\3\2\2\2!\37")
        buf.write("\3\2\2\2\"#\t\2\2\2#\13\3\2\2\2\5\21\31\37")
        return buf.getvalue()


class nimParser ( Parser ):

    grammarFileName = "nim.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'and'", "'var'", "'or'", "'not'", "'div'", 
                     "'shl'", "'shr'", "'xor'", "'mod'", "'is'", "'isnot'", 
                     "'of'", "'='", "'+'", "'*'", "'-'", "'/'", "'~'", "'&'", 
                     "'|'", "'<'", "'>'", "'!'", "'^'", "'.'", "':'", "','", 
                     "';'", "'addr'", "'as'", "'asm'", "'bind'", "'block'", 
                     "'break'", "'case'", "'cast'", "'concept'", "'const'", 
                     "'continue'", "'converter'", "'defer'", "'discard'", 
                     "'distinct'", "'do'", "'elif'", "'else'", "'end'", 
                     "'enum'", "'except'", "'export'", "'finally'", "'for'", 
                     "'from'", "'func'", "'if'", "'import'", "'in'", "'include'", 
                     "'interface'", "'iterator'", "'let'", "'macro'", "'method'", 
                     "'mixin'", "'nil'", "'notin'", "'object'", "'out'", 
                     "'proc'", "'ptr'", "'raise'", "'ref'", "'return'", 
                     "'static'", "'template'", "'try'", "'tuple'", "'type'", 
                     "'using'", "'when'", "'while'", "'yield'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'    '" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "IDENTIFIER", "DIGIT", "LETTER", 
                      "AND", "VARIABLE", "OR", "NOT", "DIV", "SHL", "SHR", 
                      "XOR", "MOD", "IS", "ISNOT", "OF", "EQUALS_OPERATOR", 
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
                      "CLOSE_BRACK", "MODULUS", "INT_LIT", "HEX_LIT", "DEC_LIT", 
                      "OCT_LIT", "BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", 
                      "INT64_LIT", "UINT_LIT", "UINT8_LIT", "UINT16_LIT", 
                      "UINT32_LIT", "UINT64_LIT", "FLOAT_LIT", "FLOAT32_LIT", 
                      "FLOAT32_SUFFIX", "FLOAT64_LIT", "FLOAT64_SUFFIX", 
                      "EXP", "HEXDIGIT", "OCTDIGIT", "BINDIGIT", "TRIPLESTR_LIT", 
                      "CHAR_LIT", "STR_LIT", "RSTR_LIT", "GENERALIZED_STR_LIT", 
                      "GENERALIZED_TRIPLESTR_LIT", "H", "INDENTATION", "AT" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_character_literals = 2
    RULE_string_literals = 3
    RULE_literal = 4

    ruleNames =  [ "start", "expr", "character_literals", "string_literals", 
                   "literal" ]

    EOF = Token.EOF
    NEWLINE=1
    IDENTIFIER=2
    DIGIT=3
    LETTER=4
    AND=5
    VARIABLE=6
    OR=7
    NOT=8
    DIV=9
    SHL=10
    SHR=11
    XOR=12
    MOD=13
    IS=14
    ISNOT=15
    OF=16
    EQUALS_OPERATOR=17
    ADD_OPERATOR=18
    MUL_OPERATOR=19
    MINUS_OPERATOR=20
    DIV_OPERATOR=21
    BITWISE_NOT_OPERATOR=22
    AND_OPERATOR=23
    OR_OPERATOR=24
    LESS_THAN=25
    GREATER_THAN=26
    NOT_OPERATOR=27
    XOR_OPERATOR=28
    DOT=29
    COLON=30
    COMMA=31
    SEMI_COLON=32
    ADDR=33
    AS=34
    ASM=35
    BIND=36
    BLOCK=37
    BREAK=38
    CASE=39
    CAST=40
    CONCEPT=41
    CONST=42
    CONTINUE=43
    CONVERTER=44
    DEFER=45
    DISCARD=46
    DISTINCT=47
    DO=48
    ELIF=49
    ELSE=50
    END=51
    ENUM=52
    EXCEPT=53
    EXPORT=54
    FINALLY=55
    FOR=56
    FROM=57
    FUNC=58
    IF=59
    IMPORT=60
    IN=61
    INCLUDE=62
    INTERFACE=63
    ITERATOR=64
    LET=65
    MACRO=66
    METHOD=67
    MIXIN=68
    NIL=69
    NOTIN=70
    OBJECT=71
    OUT=72
    PROC=73
    PTR=74
    RAISE=75
    REF=76
    RETURN=77
    STATIC=78
    TEMPLATE=79
    TRY=80
    TUPLE=81
    TYPE=82
    USING=83
    WHEN=84
    WHILE=85
    YIELD=86
    OPEN_PAREN=87
    CLOSE_PAREN=88
    OPEN_BRACE=89
    CLOSE_BRACE=90
    OPEN_BRACK=91
    CLOSE_BRACK=92
    MODULUS=93
    INT_LIT=94
    HEX_LIT=95
    DEC_LIT=96
    OCT_LIT=97
    BIN_LIT=98
    INT8_LIT=99
    INT16_LIT=100
    INT32_LIT=101
    INT64_LIT=102
    UINT_LIT=103
    UINT8_LIT=104
    UINT16_LIT=105
    UINT32_LIT=106
    UINT64_LIT=107
    FLOAT_LIT=108
    FLOAT32_LIT=109
    FLOAT32_SUFFIX=110
    FLOAT64_LIT=111
    FLOAT64_SUFFIX=112
    EXP=113
    HEXDIGIT=114
    OCTDIGIT=115
    BINDIGIT=116
    TRIPLESTR_LIT=117
    CHAR_LIT=118
    STR_LIT=119
    RSTR_LIT=120
    GENERALIZED_STR_LIT=121
    GENERALIZED_TRIPLESTR_LIT=122
    H=123
    INDENTATION=124
    AT=125

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==nimParser.NOT:
                self.state = 10
                self.expr()
                self.state = 11
                self.match(nimParser.NEWLINE)
                self.state = 17
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
            self.state = 18
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
            while _la==nimParser.CHAR_LIT:
                self.state = 20
                self.match(nimParser.CHAR_LIT)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==nimParser.STR_LIT:
                self.state = 26
                self.match(nimParser.STR_LIT)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (nimParser.NIL - 69)) | (1 << (nimParser.INT_LIT - 69)) | (1 << (nimParser.INT8_LIT - 69)) | (1 << (nimParser.INT16_LIT - 69)) | (1 << (nimParser.INT32_LIT - 69)) | (1 << (nimParser.INT64_LIT - 69)) | (1 << (nimParser.UINT_LIT - 69)) | (1 << (nimParser.UINT8_LIT - 69)) | (1 << (nimParser.UINT16_LIT - 69)) | (1 << (nimParser.UINT32_LIT - 69)) | (1 << (nimParser.UINT64_LIT - 69)) | (1 << (nimParser.FLOAT_LIT - 69)) | (1 << (nimParser.FLOAT32_LIT - 69)) | (1 << (nimParser.FLOAT64_LIT - 69)) | (1 << (nimParser.TRIPLESTR_LIT - 69)) | (1 << (nimParser.CHAR_LIT - 69)) | (1 << (nimParser.STR_LIT - 69)) | (1 << (nimParser.RSTR_LIT - 69)))) != 0)):
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





