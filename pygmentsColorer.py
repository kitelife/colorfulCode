from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers,get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles
import fileoperation

def getLexers():
	lexerlist =  [lexer[1][0] for lexer in get_all_lexers()]
	lexerlist.sort()
	return lexerlist

def getStyles():
	stylelist =  [style for style in get_all_styles()]
	stylelist.sort()
	return stylelist

def colorCode(code, lexer, style='default'):
	formatter = HtmlFormatter(
			linenos=True,
			encoding='utf-8',
			noclasses='True',
			style=style
			)
	result=''
	try:
		result= highlight(code, lexer, formatter)
	except UnicodeDecodeError, e:
		return 'UnicodeDecodeError: Maybe encode of the file is not UTF-8'
	except:
		return 'Error!'
	else:
		return result

def getColorCode(code, lang, style):
	lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True)
	return colorCode(code,lexer,style)

def getColorfilecontent(filename):
	code = fileoperation.getFilecontent(filename)
	lexer = get_lexer_for_filename(filename)
	return colorCode(code, lexer)

