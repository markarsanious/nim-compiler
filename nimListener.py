# Generated from nim.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .nimParser import nimParser
else:
    from nimParser import nimParser

# This class defines a complete listener for a parse tree produced by nimParser.
class nimListener(ParseTreeListener):

    # Enter a parse tree produced by nimParser#start.
    def enterStart(self, ctx:nimParser.StartContext):
        pass

    # Exit a parse tree produced by nimParser#start.
    def exitStart(self, ctx:nimParser.StartContext):
        pass


    # Enter a parse tree produced by nimParser#expr.
    def enterExpr(self, ctx:nimParser.ExprContext):
        pass

    # Exit a parse tree produced by nimParser#expr.
    def exitExpr(self, ctx:nimParser.ExprContext):
        pass


    # Enter a parse tree produced by nimParser#character_literals.
    def enterCharacter_literals(self, ctx:nimParser.Character_literalsContext):
        pass

    # Exit a parse tree produced by nimParser#character_literals.
    def exitCharacter_literals(self, ctx:nimParser.Character_literalsContext):
        pass


    # Enter a parse tree produced by nimParser#string_literals.
    def enterString_literals(self, ctx:nimParser.String_literalsContext):
        pass

    # Exit a parse tree produced by nimParser#string_literals.
    def exitString_literals(self, ctx:nimParser.String_literalsContext):
        pass


    # Enter a parse tree produced by nimParser#operator.
    def enterOperator(self, ctx:nimParser.OperatorContext):
        pass

    # Exit a parse tree produced by nimParser#operator.
    def exitOperator(self, ctx:nimParser.OperatorContext):
        pass


    # Enter a parse tree produced by nimParser#literal.
    def enterLiteral(self, ctx:nimParser.LiteralContext):
        pass

    # Exit a parse tree produced by nimParser#literal.
    def exitLiteral(self, ctx:nimParser.LiteralContext):
        pass


