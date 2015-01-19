# -*- coding: Latin-1 -*-
"""
PySourceColor: color Python source code
"""

"""
 PySourceColor.py

----------------------------------------------------------------------------

 A python source to colorized html/css/xhtml converter.
 Hacked by M.E.Farmer Jr. 2004, 2005
 Python license

----------------------------------------------------------------------------

 - HTML markup does not create w3c valid html, but it works on every
   browser i've tried so far.(I.E.,Mozilla/Firefox,Opera,Konqueror,wxHTML).
 - CSS markup is w3c validated html 4.01 strict,
   but will not render correctly on all browsers.
 - XHTML markup is w3c validated xhtml 1.0 strict,
   like html 4.01, will not render correctly on all browsers.

----------------------------------------------------------------------------

Features:

 -Three types of markup:
    html (default) 
    css/html 4.01 strict
    xhtml 1.0 strict

 -Can tokenize and colorize:
    12 types of strings
    2 comment types
    numbers
    operators
    brackets
    math operators
    class / name
    def / name
    decorator / name
    keywords
    arguments class/def/decorator
    linenumbers
    names
    text

 -Eight colorschemes built-in:
    null
    mono
    lite (default)
    dark 
    dark2
    idle
    viewcvs
    pythonwin

 -Header and footer
    set to '' for builtin header / footer.
    give path to a file containing the html
        you want added as header or footer.

 -Arbitrary text and html
    html markup converts all to raw (TEXT token)
    #@# for raw -> send raw text.
    #$# for span -> inline html and text.
    #%# for div -> block level html and text.

 -Linenumbers
    Supports all styles. New token is called LINENUMBER.
    Defaults to NAME if not defined.

 Style options
 
 -ALL markups support these text styles:
         b = bold
         i = italic
         u = underline
 -CSS and XHTML has limited support  for borders:
     HTML markup functions will ignore these.
     Optional: Border color in RGB hex
     Defaults to the text forecolor.
         #rrggbb = border color
     Border size:
         l = thick
         m = medium
         t = thin
     Border type:
         - = dashed
         . = dotted
         s = solid
         d = double
         g = groove
         r = ridge
         n = inset
         o = outset
     You can specify multiple sides,
     they will all use the same style.
     Optional: Default is full border.
         v = bottom
         < = left
         > = right
         ^ = top
     NOTE: Specify the styles you want.
           The markups will ignore unsupported styles
           Also note not all browsers can show these options

 -All tokens default to NAME if not defined
     so the only absolutely critical ones to define are:
     NAME, ERRORTOKEN, PAGEBACKGROUND

----------------------------------------------------------------------------

Example usage::

 # import
 import PySourceColor as psc
 psc.convert('c:/Python22/PySourceColor.py', colors=psc.idle, show=1)

 # from module import *
 from PySourceColor import *
 convert('c:/Python22/Lib', colors=lite, markup="css",
          header='#$#<b>This is a simpe heading</b><hr/>')

 # How to use a custom colorscheme, and most of the 'features'
 from PySourceColor import *
 new = {
   ERRORTOKEN:             ('bui','#FF8080',''),
   DECORATOR_NAME:         ('s','#AACBBC',''),
   DECORATOR:              ('n','#333333',''),
   NAME:                   ('t.<v','#1133AA','#DDFF22'),
   NUMBER:                 ('','#236676','#FF5555'),
   OPERATOR:               ('b','#454567','#BBBB11'),
   MATH_OPERATOR:          ('','#935623','#423afb'),
   BRACKETS:               ('b','#ac34bf','#6457a5'),
   COMMENT:                ('t-#0022FF','#545366','#AABBFF'),
   DOUBLECOMMENT:          ('<l#553455','#553455','#FF00FF'),
   CLASS_NAME:             ('m^v-','#000000','#FFFFFF'),
   DEF_NAME:               ('l=<v','#897845','#000022'),
   KEYWORD:                ('.b','#345345','#FFFF22'),
   SINGLEQUOTE:            ('mn','#223344','#AADDCC'),
   SINGLEQUOTE_R:          ('','#344522',''),
   SINGLEQUOTE_U:          ('','#234234',''),
   DOUBLEQUOTE:            ('m#0022FF','#334421',''),
   DOUBLEQUOTE_R:          ('','#345345',''),
   DOUBLEQUOTE_U:          ('','#678673',''),
   TRIPLESINGLEQUOTE:      ('tv','#FFFFFF','#000000'),
   TRIPLESINGLEQUOTE_R:    ('tbu','#443256','#DDFFDA'),
   TRIPLESINGLEQUOTE_U:    ('','#423454','#DDFFDA'),
   TRIPLEDOUBLEQUOTE:      ('li#236fd3b<>','#000000','#FFFFFF'),
   TRIPLEDOUBLEQUOTE_R:    ('tub','#000000','#FFFFFF'),
   TRIPLEDOUBLEQUOTE_U:    ('-', '#CCAABB','#FFFAFF'),
   LINENUMBER:             ('ib-','#ff66aa','#7733FF'),]
   TEXT:                   ('','#546634',''), 
   PAGEBACKGROUND:         '#FFFAAA',
     }
 if __name__ == '__main__':
     import sys
     convert(sys.argv[1], './xhtml.html', colors=new, markup='xhtml', show=1,
             linenumbers=1)
     convert(sys.argv[1], './html.html', colors=new, markup='html', show=1,
             linenumbers=1)

"""

__all__ = ['ERRORTOKEN','DECORATOR_NAME', 'DECORATOR', 'ARGS', 'EXTRASPACE',
       'NAME', 'NUMBER', 'OPERATOR', 'COMMENT', 'MATH_OPERATOR',
       'DOUBLECOMMENT', 'CLASS_NAME', 'DEF_NAME', 'KEYWORD', 'BRACKETS',
       'SINGLEQUOTE','SINGLEQUOTE_R','SINGLEQUOTE_U','DOUBLEQUOTE',
       'DOUBLEQUOTE_R', 'DOUBLEQUOTE_U', 'TRIPLESINGLEQUOTE', 'TEXT', 
       'TRIPLESINGLEQUOTE_R', 'TRIPLESINGLEQUOTE_U', 'TRIPLEDOUBLEQUOTE',
       'TRIPLEDOUBLEQUOTE_R', 'TRIPLEDOUBLEQUOTE_U', 'PAGEBACKGROUND',
       'LINENUMBER', 'CODESTART', 'CODEEND', 'PY', 'TOKEN_NAMES', 'CSSHOOK',
       'null', 'mono', 'lite', 'dark','dark2', 'pythonwin','idle', 
       'viewcvs', 'Usage', 'cli', 'str2stdout', 'path2stdout', 'Parser',
       'str2file', 'str2html', 'str2css', 'str2markup', 'path2file',
       'path2html', 'convert', 'walkdir', 'defaultColors', 'showpage',
       'pageconvert','tagreplace', 'MARKUPDICT']
__title__ = 'PySourceColor'
__version__ = "2.1a"
__date__ = '25 April 2005'
__author__ = "M.E.Farmer Jr."
__credits__ = '''This was originally based on a python recipe
submitted by J�rgen Hermann to ASPN. Now based on the voices in my head.
M.E.Farmer 2004, 2005
Python license
'''
import os
import sys
import time
import glob
import getopt
import keyword
import token
import tokenize
import traceback
try :
    import cStringIO as StringIO
except:
    import StringIO
# Do not edit
NAME = token.NAME
NUMBER = token.NUMBER
COMMENT = tokenize.COMMENT
OPERATOR = token.OP
ERRORTOKEN = token.ERRORTOKEN
ARGS = token.NT_OFFSET + 1
DOUBLECOMMENT = token.NT_OFFSET + 2
CLASS_NAME = token.NT_OFFSET + 3
DEF_NAME = token.NT_OFFSET + 4
KEYWORD = token.NT_OFFSET + 5
SINGLEQUOTE = token.NT_OFFSET + 6
SINGLEQUOTE_R = token.NT_OFFSET + 7
SINGLEQUOTE_U = token.NT_OFFSET + 8
DOUBLEQUOTE = token.NT_OFFSET + 9
DOUBLEQUOTE_R = token.NT_OFFSET + 10
DOUBLEQUOTE_U = token.NT_OFFSET + 11
TRIPLESINGLEQUOTE = token.NT_OFFSET + 12
TRIPLESINGLEQUOTE_R = token.NT_OFFSET + 13
TRIPLESINGLEQUOTE_U = token.NT_OFFSET + 14
TRIPLEDOUBLEQUOTE = token.NT_OFFSET + 15
TRIPLEDOUBLEQUOTE_R = token.NT_OFFSET + 16
TRIPLEDOUBLEQUOTE_U = token.NT_OFFSET + 17
PAGEBACKGROUND = token.NT_OFFSET + 18
DECORATOR = token.NT_OFFSET + 19
DECORATOR_NAME = token.NT_OFFSET + 20
BRACKETS = token.NT_OFFSET + 21
MATH_OPERATOR = token.NT_OFFSET + 22
LINENUMBER = token.NT_OFFSET + 23
TEXT = token.NT_OFFSET + 24
PY = token.NT_OFFSET + 25
CODESTART = token.NT_OFFSET + 26
CODEEND = token.NT_OFFSET + 27
CSSHOOK = token.NT_OFFSET + 28
EXTRASPACE = token.NT_OFFSET + 29

# markup classname lookup
MARKUPDICT = {
        ERRORTOKEN:             'py_err',
        DECORATOR_NAME:         'py_decn',
        DECORATOR:              'py_dec',
        ARGS:                   'py_args',
        NAME:                   'py_name',
        NUMBER:                 'py_num',
        OPERATOR:               'py_op',
        COMMENT:                'py_com',
        DOUBLECOMMENT:          'py_dcom',
        CLASS_NAME:             'py_clsn',
        DEF_NAME:               'py_defn',
        KEYWORD:                'py_key',
        SINGLEQUOTE:            'py_sq',
        SINGLEQUOTE_R:          'py_sqr',
        SINGLEQUOTE_U:          'py_squ',
        DOUBLEQUOTE:            'py_dq',
        DOUBLEQUOTE_R:          'py_dqr',
        DOUBLEQUOTE_U:          'py_dqu',
        TRIPLESINGLEQUOTE:      'py_tsq',
        TRIPLESINGLEQUOTE_R:    'py_tsqr',
        TRIPLESINGLEQUOTE_U:    'py_tsqu',
        TRIPLEDOUBLEQUOTE:      'py_tdq',
        TRIPLEDOUBLEQUOTE_R:    'py_tdqr',
        TRIPLEDOUBLEQUOTE_U:    'py_tdqu',
        BRACKETS:               'py_bra',
        MATH_OPERATOR:          'py_mop',
        LINENUMBER:             'py_lnum',
        TEXT:                   'py_text',
        }
# might help users that want to create custom schemes
TOKEN_NAMES= {
       ERRORTOKEN:'ERRORTOKEN',
       DECORATOR_NAME:'DECORATOR_NAME',
       DECORATOR:'DECORATOR',
       ARGS:'ARGS',
       NAME:'NAME',
       NUMBER:'NUMBER',
       OPERATOR:'OPERATOR',
       COMMENT:'COMMENT',
       DOUBLECOMMENT:'DOUBLECOMMENT',
       CLASS_NAME:'CLASS_NAME',
       DEF_NAME:'DEF_NAME',
       KEYWORD:'KEYWORD',
       SINGLEQUOTE:'SINGLEQUOTE',
       SINGLEQUOTE_R:'SINGLEQUOTE_R',
       SINGLEQUOTE_U:'SINGLEQUOTE_U',
       DOUBLEQUOTE:'DOUBLEQUOTE',
       DOUBLEQUOTE_R:'DOUBLEQUOTE_R',
       DOUBLEQUOTE_U:'DOUBLEQUOTE_U',
       TRIPLESINGLEQUOTE:'TRIPLESINGLEQUOTE',
       TRIPLESINGLEQUOTE_R:'TRIPLESINGLEQUOTE_R',
       TRIPLESINGLEQUOTE_U:'TRIPLESINGLEQUOTE_U',
       TRIPLEDOUBLEQUOTE:'TRIPLEDOUBLEQUOTE',
       TRIPLEDOUBLEQUOTE_R:'TRIPLEDOUBLEQUOTE_R',
       TRIPLEDOUBLEQUOTE_U:'TRIPLEDOUBLEQUOTE_U',
       BRACKETS:'BRACKETS',
       MATH_OPERATOR:'MATH_OPERATOR',
       LINENUMBER:'LINENUMBER',
       TEXT:'TEXT',
       PAGEBACKGROUND:'PAGEBACKGROUND',
       }

######################################################################
# Edit colors and styles to taste
# Create your own scheme, just copy one below , rename and edit.
# Custom styles must at least define NAME, ERRORTOKEN, PAGEBACKGROUND,
# all missing elements will default to NAME.
# See module docstring for details on style attributes.
######################################################################
# Copy null and use it as a starter colorscheme.
null = {# tokentype: ('tags border_color', 'textforecolor', 'textbackcolor')
        ERRORTOKEN:             ('','#000000',''),# Error token
        DECORATOR_NAME:         ('','#000000',''),# Decorator name
        DECORATOR:              ('','#000000',''),# @ symbol
        ARGS:                   ('','#000000',''),# class,def,deco arguments
        NAME:                   ('','#000000',''),# All other python text
        NUMBER:                 ('','#000000',''),# 0->10
        OPERATOR:               ('','#000000',''),# ':','<=',';',',','.','==', etc
        MATH_OPERATOR:          ('','#000000',''),# '+','-','=','','**',etc
        BRACKETS:               ('','#000000',''),# '[',']','(',')','{','}'
        COMMENT:                ('','#000000',''),# Single comment
        DOUBLECOMMENT:          ('','#000000',''),## Double comment
        CLASS_NAME:             ('','#000000',''),# Class name
        DEF_NAME:               ('','#000000',''),# Def name
        KEYWORD:                ('','#000000',''),# Python keywords
        SINGLEQUOTE:            ('','#000000',''),# 'SINGLEQUOTE'
        SINGLEQUOTE_R:          ('','#000000',''),# r'SINGLEQUOTE'
        SINGLEQUOTE_U:          ('','#000000',''),# u'SINGLEQUOTE'
        DOUBLEQUOTE:            ('','#000000',''),# "DOUBLEQUOTE"
        DOUBLEQUOTE_R:          ('','#000000',''),# r"DOUBLEQUOTE"
        DOUBLEQUOTE_U:          ('','#000000',''),# u"DOUBLEQUOTE"
        TRIPLESINGLEQUOTE:      ('','#000000',''),# '''TRIPLESINGLEQUOTE'''
        TRIPLESINGLEQUOTE_R:    ('','#000000',''),# r'''TRIPLESINGLEQUOTE'''
        TRIPLESINGLEQUOTE_U:    ('','#000000',''),# u'''TRIPLESINGLEQUOTE'''
        TRIPLEDOUBLEQUOTE:      ('','#000000',''),# """TRIPLEDOUBLEQUOTE"""
        TRIPLEDOUBLEQUOTE_R:    ('','#000000',''),# r"""TRIPLEDOUBLEQUOTE"""
        TRIPLEDOUBLEQUOTE_U:    ('','#000000',''),# u"""TRIPLEDOUBLEQUOTE"""
        TEXT:                   ('','#000000',''),# non python text 
        LINENUMBER:             ('>ti#555555','#000000',''),# Linenumbers
        PAGEBACKGROUND:         '#FFFFFF'# set the page background
        }

mono = {
        ERRORTOKEN:             ('s#FF0000','#FF8080',''),
        DECORATOR_NAME:         ('bu','#000000',''),
        DECORATOR:              ('b','#000000',''),
        ARGS:                   ('b','#555555',''),
        NAME:                   ('','#000000',''),
        NUMBER:                 ('b','#000000',''),
        OPERATOR:               ('b','#000000',''),
        MATH_OPERATOR:          ('b','#000000',''),
        BRACKETS:               ('b','#000000',''),
        COMMENT:                ('i','#999999',''),
        DOUBLECOMMENT:          ('b','#999999',''),
        CLASS_NAME:             ('bu','#000000',''),
        DEF_NAME:               ('b','#000000',''),
        KEYWORD:                ('b','#000000',''),
        SINGLEQUOTE:            ('','#000000',''),
        SINGLEQUOTE_R:          ('','#000000',''),
        SINGLEQUOTE_U:          ('','#000000',''),
        DOUBLEQUOTE:            ('','#000000',''),
        DOUBLEQUOTE_R:          ('','#000000',''),
        DOUBLEQUOTE_U:          ('','#000000',''),
        TRIPLESINGLEQUOTE:      ('','#000000',''),
        TRIPLESINGLEQUOTE_R:    ('','#000000',''),
        TRIPLESINGLEQUOTE_U:    ('','#000000',''),
        TRIPLEDOUBLEQUOTE:      ('i','#000000',''),
        TRIPLEDOUBLEQUOTE_R:    ('i','#000000',''),
        TRIPLEDOUBLEQUOTE_U:    ('i','#000000',''),
        TEXT:                   ('','#000000',''),
        LINENUMBER:             ('>ti#555555','#000000',''),
        PAGEBACKGROUND:         '#FFFFFF'
        }

dark = {
        ERRORTOKEN:             ('s#FF0000','#FF8080',''),
        DECORATOR_NAME:         ('b','#FFBBAA',''),
        DECORATOR:              ('b','#CC5511',''),
        ARGS:                   ('b','#DDDDFF',''),
        NAME:                   ('','#DDDDDD',''),
        NUMBER:                 ('','#FF0000',''),
        OPERATOR:               ('b','#FAF785',''),
        MATH_OPERATOR:          ('b','#FAF785',''),
        BRACKETS:               ('b','#FAF785',''),
        COMMENT:                ('','#45FCA0',''),
        DOUBLECOMMENT:          ('i','#A7C7A9',''),
        CLASS_NAME:             ('b','#B666FD',''),
        DEF_NAME:               ('b','#EBAE5C',''),
        KEYWORD:                ('b','#8680FF',''),
        SINGLEQUOTE:            ('','#F8BAFE',''),
        SINGLEQUOTE_R:          ('','#F8BAFE',''),
        SINGLEQUOTE_U:          ('','#F8BAFE',''),
        DOUBLEQUOTE:            ('','#FF80C0',''),
        DOUBLEQUOTE_R:          ('','#FF80C0',''),
        DOUBLEQUOTE_U:          ('','#FF80C0',''),
        TRIPLESINGLEQUOTE:      ('','#FF9595',''),
        TRIPLESINGLEQUOTE_R:    ('','#FF9595',''),
        TRIPLESINGLEQUOTE_U:    ('','#FF9595',''),
        TRIPLEDOUBLEQUOTE:      ('','#B3FFFF',''),
        TRIPLEDOUBLEQUOTE_R:    ('','#B3FFFF',''),
        TRIPLEDOUBLEQUOTE_U:    ('','#B3FFFF',''),
        TEXT:                   ('','#FFFFFF',''),
        LINENUMBER:             ('>mi#555555','#bbccbb','#333333'),
        PAGEBACKGROUND:         '#000000'
        }

dark2 = {
        ERRORTOKEN:             ('','#FF0000',''),
        DECORATOR_NAME:         ('b','#FFBBAA',''),
        DECORATOR:              ('b','#CC5511',''),
        ARGS:                   ('b','#DDDDDD',''),
        NAME:                   ('','#C0C0C0',''),
        NUMBER:                 ('b','#00FF00',''),
        OPERATOR:               ('b','#FF090F',''),
        MATH_OPERATOR:          ('b','#EE7020',''),
        BRACKETS:               ('b','#FFB90F',''),
        COMMENT:                ('i','#D0D000','#522000'),#'#88AA88','#11111F'),
        DOUBLECOMMENT:          ('i','#D0D000','#522000'),#'#77BB77','#11111F'),
        CLASS_NAME:             ('b','#DD4080',''),
        DEF_NAME:               ('b','#FF8040',''),
        KEYWORD:                ('b','#4726d1',''),
        SINGLEQUOTE:            ('','#8080C0',''),
        SINGLEQUOTE_R:          ('','#8080C0',''),
        SINGLEQUOTE_U:          ('','#8080C0',''),
        DOUBLEQUOTE:            ('','#ADB9F1',''),
        DOUBLEQUOTE_R:          ('','#ADB9F1',''),
        DOUBLEQUOTE_U:          ('','#ADB9F1',''),
        TRIPLESINGLEQUOTE:      ('','#00C1C1',''),#A050C0
        TRIPLESINGLEQUOTE_R:    ('','#00C1C1',''),#A050C0
        TRIPLESINGLEQUOTE_U:    ('','#00C1C1',''),#A050C0
        TRIPLEDOUBLEQUOTE:      ('','#33E3E3',''),#B090E0
        TRIPLEDOUBLEQUOTE_R:    ('','#33E3E3',''),#B090E0
        TRIPLEDOUBLEQUOTE_U:    ('','#33E3E3',''),#B090E0
        TEXT:                   ('','#C0C0C0',''),
        LINENUMBER:             ('>mi#555555','#bbccbb','#333333'),
        PAGEBACKGROUND:         '#000000'
        }

lite = {
        ERRORTOKEN:             ('s#FF0000','#FF8080',''),
        DECORATOR_NAME:         ('b','#BB4422',''),
        DECORATOR:              ('b','#3333AF',''),
        ARGS:                   ('b','#000000',''),
        NAME:                   ('','#333333',''),
        NUMBER:                 ('b','#DD2200',''),
        OPERATOR:               ('b','#000000',''),
        MATH_OPERATOR:          ('b','#000000',''),
        BRACKETS:               ('b','#000000',''),
        COMMENT:                ('','#007F00',''),
        DOUBLECOMMENT:          ('','#608060',''),
        CLASS_NAME:             ('b','#0000DF',''),
        DEF_NAME:               ('b','#9C7A00',''),#f09030
        KEYWORD:                ('b','#0000AF',''),
        SINGLEQUOTE:            ('','#600080',''),
        SINGLEQUOTE_R:          ('','#600080',''),
        SINGLEQUOTE_U:          ('','#600080',''),
        DOUBLEQUOTE:            ('','#A0008A',''),
        DOUBLEQUOTE_R:          ('','#A0008A',''),
        DOUBLEQUOTE_U:          ('','#A0008A',''),
        TRIPLESINGLEQUOTE:      ('','#337799',''),
        TRIPLESINGLEQUOTE_R:    ('','#337799',''),
        TRIPLESINGLEQUOTE_U:    ('','#337799',''),
        TRIPLEDOUBLEQUOTE:      ('','#1166AA',''),
        TRIPLEDOUBLEQUOTE_R:    ('','#1166AA',''),
        TRIPLEDOUBLEQUOTE_U:    ('','#1166AA',''),
        TEXT:                   ('','#000000',''),
        LINENUMBER:             ('>ti#555555','#000000',''),
        PAGEBACKGROUND:         '#FFFFFF'
        }

idle = {
        ERRORTOKEN:             ('s#FF0000','#FF8080',''),
        DECORATOR_NAME:         ('','#900090',''),
        DECORATOR:              ('','#FF7700',''),
        NAME:                   ('','#000000',''),
        NUMBER: 