from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles

def getLexers():
	lexerlist =  [lexer[1][0] for lexer in get_all_lexers()]
	lexerlist.sort()
	return lexerlist

def getStyles():
	stylelist =  [style for style in get_all_styles()]
	stylelist.sort()
	return stylelist

def code2html(code, lang, style):
	lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True)
	formatter = HtmlFormatter(
			linenos=True,
			encoding='utf-8',
			noclasses='True',
			style=style
			)
	return highlight(code, lexer, formatter)

def output_head():
    return  '''
<!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <title>O_O</title>
        <!--<link rel="stylesheet" type="text/css" href="http://www.peerat.com/code/style.css" />-->
    </head>
    <body>
    '''

def output_end():
    return '</body>'+'</html>'

def colorCode(code, lang, style):
	return code2html(code,lang,style)
