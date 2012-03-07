from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

def getLexers():
	lexerlist =  [lexer[1][0] for lexer in get_all_lexers()]
	lexerlist.sort()
	return lexerlist

def code2html(code, lang):
	lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True)
	formatter = HtmlFormatter(
			linenos=True,
			encoding='utf-8',
			noclasses='True'
			)
	return highlight(code, lexer, formatter)

def output_head():
    return  '''
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <title>O_O</title>
    </head>
    <body>
    '''

def output_end():
    return '</body>'+'</html>'

def colorCode(code, lang):
	return output_head()+code2html(code,lang)+output_end()
