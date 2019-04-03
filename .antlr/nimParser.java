// Generated from /home/ameniawy/Documents/SEM_10/Compiler Lab/nim-compiler/nim.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class nimParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DIGIT=1, SPACE=2, NEWLINE=3, AND=4, VARIABLE=5, OR=6, NOT=7, DIV=8, SHL=9, 
		SHR=10, XOR=11, MOD=12, IS=13, ISNOT=14, OF=15, EQUALS_OPERATOR=16, ADD_OPERATOR=17, 
		MUL_OPERATOR=18, MINUS_OPERATOR=19, DIV_OPERATOR=20, BITWISE_NOT_OPERATOR=21, 
		AND_OPERATOR=22, OR_OPERATOR=23, LESS_THAN=24, GREATER_THAN=25, NOT_OPERATOR=26, 
		XOR_OPERATOR=27, DOT=28, COLON=29, COMMA=30, SEMI_COLON=31, ADDR=32, AS=33, 
		ASM=34, BIND=35, BLOCK=36, BREAK=37, CASE=38, CAST=39, CONCEPT=40, CONST=41, 
		CONTINUE=42, CONVERTER=43, DEFER=44, DISCARD=45, DISTINCT=46, DO=47, ELIF=48, 
		ELSE=49, END=50, ENUM=51, EXCEPT=52, EXPORT=53, FINALLY=54, FOR=55, FROM=56, 
		FUNC=57, IF=58, IMPORT=59, IN=60, INCLUDE=61, INTERFACE=62, ITERATOR=63, 
		LET=64, MACRO=65, METHOD=66, MIXIN=67, NIL=68, NOTIN=69, OBJECT=70, OUT=71, 
		PROC=72, PTR=73, RAISE=74, REF=75, RETURN=76, STATIC=77, TEMPLATE=78, 
		TRY=79, TUPLE=80, TYPE=81, USING=82, WHEN=83, WHILE=84, YIELD=85, OPEN_PAREN=86, 
		CLOSE_PAREN=87, OPEN_BRACE=88, CLOSE_BRACE=89, OPEN_BRACK=90, CLOSE_BRACK=91, 
		MODULUS=92, INT_LIT=93, HEX_LIT=94, DEC_LIT=95, OCT_LIT=96, BIN_LIT=97, 
		INT8_LIT=98, INT16_LIT=99, INT32_LIT=100, INT64_LIT=101, UINT_LIT=102, 
		UINT8_LIT=103, UINT16_LIT=104, UINT32_LIT=105, UINT64_LIT=106, FLOAT_LIT=107, 
		FLOAT32_LIT=108, FLOAT32_SUFFIX=109, FLOAT64_LIT=110, FLOAT64_SUFFIX=111, 
		EXP=112, HEXDIGIT=113, OCTDIGIT=114, BINDIGIT=115, TRIPLESTR_LIT=116, 
		CHAR_LIT=117, STR_LIT=118, RSTR_LIT=119, GENERALIZED_STR_LIT=120, GENERALIZED_TRIPLESTR_LIT=121, 
		H=122, INDENT=123, AT=124, COMMENT=125, MULTI_LINE_COMMENT=126, IDENTIFIER=127, 
		LETTER=128;
	public static final int
		RULE_start = 0, RULE_expr = 1, RULE_character_literals = 2, RULE_string_literals = 3, 
		RULE_operator = 4, RULE_literal = 5;
	public static final String[] ruleNames = {
		"start", "expr", "character_literals", "string_literals", "operator", 
		"literal"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, "' '", null, "'and'", "'var'", "'or'", "'not'", "'div'", "'shl'", 
		"'shr'", "'xor'", "'mod'", "'is'", "'isnot'", "'of'", "'='", "'+'", "'*'", 
		"'-'", "'/'", "'~'", "'&'", "'|'", "'<'", "'>'", "'!'", "'^'", "'.'", 
		"':'", "','", "';'", "'addr'", "'as'", "'asm'", "'bind'", "'block'", "'break'", 
		"'case'", "'cast'", "'concept'", "'const'", "'continue'", "'converter'", 
		"'defer'", "'discard'", "'distinct'", "'do'", "'elif'", "'else'", "'end'", 
		"'enum'", "'except'", "'export'", "'finally'", "'for'", "'from'", "'func'", 
		"'if'", "'import'", "'in'", "'include'", "'interface'", "'iterator'", 
		"'let'", "'macro'", "'method'", "'mixin'", "'nil'", "'notin'", "'object'", 
		"'out'", "'proc'", "'ptr'", "'raise'", "'ref'", "'return'", "'static'", 
		"'template'", "'try'", "'tuple'", "'type'", "'using'", "'when'", "'while'", 
		"'yield'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'%'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "DIGIT", "SPACE", "NEWLINE", "AND", "VARIABLE", "OR", "NOT", "DIV", 
		"SHL", "SHR", "XOR", "MOD", "IS", "ISNOT", "OF", "EQUALS_OPERATOR", "ADD_OPERATOR", 
		"MUL_OPERATOR", "MINUS_OPERATOR", "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", 
		"AND_OPERATOR", "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "NOT_OPERATOR", 
		"XOR_OPERATOR", "DOT", "COLON", "COMMA", "SEMI_COLON", "ADDR", "AS", "ASM", 
		"BIND", "BLOCK", "BREAK", "CASE", "CAST", "CONCEPT", "CONST", "CONTINUE", 
		"CONVERTER", "DEFER", "DISCARD", "DISTINCT", "DO", "ELIF", "ELSE", "END", 
		"ENUM", "EXCEPT", "EXPORT", "FINALLY", "FOR", "FROM", "FUNC", "IF", "IMPORT", 
		"IN", "INCLUDE", "INTERFACE", "ITERATOR", "LET", "MACRO", "METHOD", "MIXIN", 
		"NIL", "NOTIN", "OBJECT", "OUT", "PROC", "PTR", "RAISE", "REF", "RETURN", 
		"STATIC", "TEMPLATE", "TRY", "TUPLE", "TYPE", "USING", "WHEN", "WHILE", 
		"YIELD", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACK", 
		"CLOSE_BRACK", "MODULUS", "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", 
		"BIN_LIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", "UINT_LIT", 
		"UINT8_LIT", "UINT16_LIT", "UINT32_LIT", "UINT64_LIT", "FLOAT_LIT", "FLOAT32_LIT", 
		"FLOAT32_SUFFIX", "FLOAT64_LIT", "FLOAT64_SUFFIX", "EXP", "HEXDIGIT", 
		"OCTDIGIT", "BINDIGIT", "TRIPLESTR_LIT", "CHAR_LIT", "STR_LIT", "RSTR_LIT", 
		"GENERALIZED_STR_LIT", "GENERALIZED_TRIPLESTR_LIT", "H", "INDENT", "AT", 
		"COMMENT", "MULTI_LINE_COMMENT", "IDENTIFIER", "LETTER"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "nim.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public nimParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StartContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(nimParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(nimParser.NEWLINE, i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOT) {
				{
				{
				setState(12);
				expr();
				setState(13);
				match(NEWLINE);
				}
				}
				setState(19);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(nimParser.NOT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(NOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Character_literalsContext extends ParserRuleContext {
		public List<TerminalNode> CHAR_LIT() { return getTokens(nimParser.CHAR_LIT); }
		public TerminalNode CHAR_LIT(int i) {
			return getToken(nimParser.CHAR_LIT, i);
		}
		public Character_literalsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_character_literals; }
	}

	public final Character_literalsContext character_literals() throws RecognitionException {
		Character_literalsContext _localctx = new Character_literalsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_character_literals);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(22);
				match(CHAR_LIT);
				}
				}
				setState(25); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CHAR_LIT );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class String_literalsContext extends ParserRuleContext {
		public List<TerminalNode> STR_LIT() { return getTokens(nimParser.STR_LIT); }
		public TerminalNode STR_LIT(int i) {
			return getToken(nimParser.STR_LIT, i);
		}
		public String_literalsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_literals; }
	}

	public final String_literalsContext string_literals() throws RecognitionException {
		String_literalsContext _localctx = new String_literalsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_string_literals);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(27);
				match(STR_LIT);
				}
				}
				setState(30); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==STR_LIT );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperatorContext extends ParserRuleContext {
		public TerminalNode EQUALS_OPERATOR() { return getToken(nimParser.EQUALS_OPERATOR, 0); }
		public TerminalNode ADD_OPERATOR() { return getToken(nimParser.ADD_OPERATOR, 0); }
		public TerminalNode MUL_OPERATOR() { return getToken(nimParser.MUL_OPERATOR, 0); }
		public TerminalNode MINUS_OPERATOR() { return getToken(nimParser.MINUS_OPERATOR, 0); }
		public TerminalNode DIV_OPERATOR() { return getToken(nimParser.DIV_OPERATOR, 0); }
		public TerminalNode BITWISE_NOT_OPERATOR() { return getToken(nimParser.BITWISE_NOT_OPERATOR, 0); }
		public TerminalNode AND_OPERATOR() { return getToken(nimParser.AND_OPERATOR, 0); }
		public TerminalNode OR_OPERATOR() { return getToken(nimParser.OR_OPERATOR, 0); }
		public TerminalNode LESS_THAN() { return getToken(nimParser.LESS_THAN, 0); }
		public TerminalNode GREATER_THAN() { return getToken(nimParser.GREATER_THAN, 0); }
		public TerminalNode NOT_OPERATOR() { return getToken(nimParser.NOT_OPERATOR, 0); }
		public TerminalNode XOR_OPERATOR() { return getToken(nimParser.XOR_OPERATOR, 0); }
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUALS_OPERATOR) | (1L << ADD_OPERATOR) | (1L << MUL_OPERATOR) | (1L << MINUS_OPERATOR) | (1L << DIV_OPERATOR) | (1L << BITWISE_NOT_OPERATOR) | (1L << AND_OPERATOR) | (1L << OR_OPERATOR) | (1L << LESS_THAN) | (1L << GREATER_THAN) | (1L << NOT_OPERATOR) | (1L << XOR_OPERATOR))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT_LIT() { return getToken(nimParser.INT_LIT, 0); }
		public TerminalNode INT8_LIT() { return getToken(nimParser.INT8_LIT, 0); }
		public TerminalNode INT16_LIT() { return getToken(nimParser.INT16_LIT, 0); }
		public TerminalNode INT32_LIT() { return getToken(nimParser.INT32_LIT, 0); }
		public TerminalNode INT64_LIT() { return getToken(nimParser.INT64_LIT, 0); }
		public TerminalNode UINT_LIT() { return getToken(nimParser.UINT_LIT, 0); }
		public TerminalNode UINT8_LIT() { return getToken(nimParser.UINT8_LIT, 0); }
		public TerminalNode UINT16_LIT() { return getToken(nimParser.UINT16_LIT, 0); }
		public TerminalNode UINT32_LIT() { return getToken(nimParser.UINT32_LIT, 0); }
		public TerminalNode UINT64_LIT() { return getToken(nimParser.UINT64_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(nimParser.FLOAT_LIT, 0); }
		public TerminalNode FLOAT32_LIT() { return getToken(nimParser.FLOAT32_LIT, 0); }
		public TerminalNode FLOAT64_LIT() { return getToken(nimParser.FLOAT64_LIT, 0); }
		public TerminalNode STR_LIT() { return getToken(nimParser.STR_LIT, 0); }
		public TerminalNode RSTR_LIT() { return getToken(nimParser.RSTR_LIT, 0); }
		public TerminalNode TRIPLESTR_LIT() { return getToken(nimParser.TRIPLESTR_LIT, 0); }
		public TerminalNode CHAR_LIT() { return getToken(nimParser.CHAR_LIT, 0); }
		public TerminalNode NIL() { return getToken(nimParser.NIL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			_la = _input.LA(1);
			if ( !(((((_la - 68)) & ~0x3f) == 0 && ((1L << (_la - 68)) & ((1L << (NIL - 68)) | (1L << (INT_LIT - 68)) | (1L << (INT8_LIT - 68)) | (1L << (INT16_LIT - 68)) | (1L << (INT32_LIT - 68)) | (1L << (INT64_LIT - 68)) | (1L << (UINT_LIT - 68)) | (1L << (UINT8_LIT - 68)) | (1L << (UINT16_LIT - 68)) | (1L << (UINT32_LIT - 68)) | (1L << (UINT64_LIT - 68)) | (1L << (FLOAT_LIT - 68)) | (1L << (FLOAT32_LIT - 68)) | (1L << (FLOAT64_LIT - 68)) | (1L << (TRIPLESTR_LIT - 68)) | (1L << (CHAR_LIT - 68)) | (1L << (STR_LIT - 68)) | (1L << (RSTR_LIT - 68)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0082\'\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\3\2\3\2\7\2\22\n\2\f\2\16\2"+
		"\25\13\2\3\3\3\3\3\4\6\4\32\n\4\r\4\16\4\33\3\5\6\5\37\n\5\r\5\16\5 \3"+
		"\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\4\3\2\22\35\7\2FF__dnppvy\2#\2"+
		"\23\3\2\2\2\4\26\3\2\2\2\6\31\3\2\2\2\b\36\3\2\2\2\n\"\3\2\2\2\f$\3\2"+
		"\2\2\16\17\5\4\3\2\17\20\7\5\2\2\20\22\3\2\2\2\21\16\3\2\2\2\22\25\3\2"+
		"\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\23\3\2\2\2\26\27\7\t"+
		"\2\2\27\5\3\2\2\2\30\32\7w\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2"+
		"\2\33\34\3\2\2\2\34\7\3\2\2\2\35\37\7x\2\2\36\35\3\2\2\2\37 \3\2\2\2 "+
		"\36\3\2\2\2 !\3\2\2\2!\t\3\2\2\2\"#\t\2\2\2#\13\3\2\2\2$%\t\3\2\2%\r\3"+
		"\2\2\2\5\23\33 ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}