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
		NEWLINE=1, NOT=2, CHAR_LIT=3, STR_LIT=4, INT_LIT=5, INT8_LIT=6, INT16_LIT=7, 
		INT32_LIT=8, INT64_LIT=9, UINT_LIT=10, UINT8_LIT=11, UINT16_LIT=12, UINT32_LIT=13, 
		UINT64_LIT=14, FLOAT_LIT=15, FLOAT32_LIT=16, FLOAT64_LIT=17, RSTR_LIT=18, 
		TRIPLESTR_LIT=19, NIL=20;
	public static final int
		RULE_start = 0, RULE_expr = 1, RULE_character_literals = 2, RULE_string_literals = 3, 
		RULE_literal = 4;
	public static final String[] ruleNames = {
		"start", "expr", "character_literals", "string_literals", "literal"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "NEWLINE", "NOT", "CHAR_LIT", "STR_LIT", "INT_LIT", "INT8_LIT", 
		"INT16_LIT", "INT32_LIT", "INT64_LIT", "UINT_LIT", "UINT8_LIT", "UINT16_LIT", 
		"UINT32_LIT", "UINT64_LIT", "FLOAT_LIT", "FLOAT32_LIT", "FLOAT64_LIT", 
		"RSTR_LIT", "TRIPLESTR_LIT", "NIL"
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
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NOT) {
				{
				{
				setState(10);
				expr();
				setState(11);
				match(NEWLINE);
				}
				}
				setState(17);
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
			setState(18);
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
			while (_la==CHAR_LIT) {
				{
				{
				setState(20);
				match(CHAR_LIT);
				}
				}
				setState(25);
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
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STR_LIT) {
				{
				{
				setState(26);
				match(STR_LIT);
				}
				}
				setState(31);
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
		enterRule(_localctx, 8, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CHAR_LIT) | (1L << STR_LIT) | (1L << INT_LIT) | (1L << INT8_LIT) | (1L << INT16_LIT) | (1L << INT32_LIT) | (1L << INT64_LIT) | (1L << UINT_LIT) | (1L << UINT8_LIT) | (1L << UINT16_LIT) | (1L << UINT32_LIT) | (1L << UINT64_LIT) | (1L << FLOAT_LIT) | (1L << FLOAT32_LIT) | (1L << FLOAT64_LIT) | (1L << RSTR_LIT) | (1L << TRIPLESTR_LIT) | (1L << NIL))) != 0)) ) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26%\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3"+
		"\3\3\3\4\7\4\30\n\4\f\4\16\4\33\13\4\3\5\7\5\36\n\5\f\5\16\5!\13\5\3\6"+
		"\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\5\26\2\"\2\21\3\2\2\2\4\24\3\2\2\2\6"+
		"\31\3\2\2\2\b\37\3\2\2\2\n\"\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2\16\20\3"+
		"\2\2\2\17\f\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2"+
		"\2\2\23\21\3\2\2\2\24\25\7\4\2\2\25\5\3\2\2\2\26\30\7\5\2\2\27\26\3\2"+
		"\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\7\3\2\2\2\33\31\3\2"+
		"\2\2\34\36\7\6\2\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2"+
		" \t\3\2\2\2!\37\3\2\2\2\"#\t\2\2\2#\13\3\2\2\2\5\21\31\37";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}