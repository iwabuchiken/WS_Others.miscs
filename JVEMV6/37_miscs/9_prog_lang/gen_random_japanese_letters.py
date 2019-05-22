# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\gen_random_japanese_letters.py
orig : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\gen_sentence_elements.py
at : 2019/04/12 08:45:48

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\
python gen_random_japanese_letters.py

<Description>
    1. gen X num of lists of japanese letters
    2. e.g.
        strOf_W_1 = '['ま', 'に', 'う', 'つ', 'ぬ']'
        strOf_W_2 = '['に', 'み']'
        strOf_W_3 = '['し', 'い']'

'''
###############################################
import sys
from _datetime import datetime
from numpy import append

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, math, random, subprocess

###############################################
#
#	VARS (GLOBAL)
#
###############################################
strOf_Letters = "あいうえおかきくけこさしすせそたちつてとなにぬねのまみむめもらりるれろわをんがぎぐげござじずぜぞだづでどばびぶべぼ"
numOf_Letters_Gennend = 20

###############################################
#
#	FUNCS
#
###############################################

###############################################
'''
    @param string_type
            serial    "20160604_193404"
            basic     "2016/06/04 19:34:04"
'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())

    '''###################
        build string        
    ###################'''
    if string_type == "serial" : #if string_type == "serial"
    
        str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    elif string_type == "basic" : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    else : #if string_type == "serial"
    
        str = strftime("%Y/%m/%d %H:%M:%S", localtime(t))
    
    #/if string_type == "serial"
    
    
#     str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        if string_type == "serial" : #if string_type == "serial"
            
            str = "%s_%03d" % (str, int(t % 1 * 1000))
        
        else : #if string_type == "serial"
        
            str = "%s.%03d" % (str, int(t % 1 * 1000))

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
#         str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():


def show_Message() :
    
    msg = '''
    <Options>
    '''
    
    print (msg)

def test_1():

#_20190412_084351:head
#_20190412_084356:caller

    '''###################
        step : 1
            prep : vars
    ###################'''
#     strOf_Letters = "あいうえおかきくけこさしすせそたちつてとなにぬねのまみむめも"
    
    lenOf_StrOf_Letters = len(strOf_Letters)
    
    lo_Chars = list(strOf_Letters)
    
#     numOf_Letters_Gennend = 10
    
    numOf_Halfof_NumOf_Letters_Gennend = int(numOf_Letters_Gennend / 2)
    
    lo_Genned_Letters = []
    
    '''###################
        step : 2
            gen : letters
    ###################'''
    for i in range(0, numOf_Letters_Gennend):
    
        # genned char
        strOf_Genned_Letter = lo_Chars[random.randint(0, lenOf_StrOf_Letters - 1)]
        
        # append
        lo_Genned_Letters.append(strOf_Genned_Letter)
        
    #/for i in range(0, numOf_Letters_Gennend):

    '''###################
        step : 3
            display
    ###################'''
    #debug
    print()
    print("[%s:%d] lo_Genned_Letters ==>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
 
                    ), file=sys.stderr)
    print(lo_Genned_Letters)
    print()

    '''###################
        step : 4
            divide list ==> into words
    ###################'''
    '''###################
        step : 4.1.1
            gen : dividing index : 1
    ###################'''
    numOf_Dividing_Index_1 = random.randint(1, numOf_Letters_Gennend - 2)
    
#     #debug
#     print()
#     print("[%s:%d] numOf_Dividing_Index_1 ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#  
#                     ), file=sys.stderr)
#     print(numOf_Dividing_Index_1)
#     print()

    '''###################
        step : 4.1.2
            gen : dividing index : 2
    ###################'''
    # declare
    numOf_Dividing_Index_2 = -1
    
    # set : value
    if numOf_Dividing_Index_1 > numOf_Halfof_NumOf_Letters_Gennend : #if numOf_Dividing_Index_1 > numOf_Halfof_NumOf_Letters_Gennend
    
        numOf_Dividing_Index_2 = random.randint(0, numOf_Dividing_Index_1 - 1)
    
    else : #if numOf_Dividing_Index_1 > numOf_Halfof_NumOf_Letters_Gennend
    
        numOf_Dividing_Index_2 = random.randint(numOf_Dividing_Index_1 + 1, numOf_Letters_Gennend - 2)
    
    #/if numOf_Dividing_Index_1 > numOf_Halfof_NumOf_Letters_Gennend
    
    
#     numOf_Dividing_Index_2 = random.randint(1, numOf_Letters_Gennend - 2)
    
    #debug
    print()
#     print("[%s:%d] numOf_Dividing_Index_2 ==>" % \
    print("[%s:%d]\nnumOf_Dividing_Index_1 = %d\nnumOf_Dividing_Index_2 = %d\nnumOf_Halfof_NumOf_Letters_Gennend = %d" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , numOf_Dividing_Index_1
                     , numOf_Dividing_Index_2
                     , numOf_Halfof_NumOf_Letters_Gennend
                    ), file=sys.stderr)
#     print(numOf_Dividing_Index_2)
    print()

    '''###################
        step : 4.1.3
            sort indices
    ###################'''
    tmp = numOf_Dividing_Index_1
    
    if numOf_Dividing_Index_1 > numOf_Dividing_Index_2 : #if numOf_Dividing_Index_1 > numOf_Dividing_Index_2
        
        numOf_Dividing_Index_1 = numOf_Dividing_Index_2
        
        numOf_Dividing_Index_2 = tmp
    
    #/if numOf_Dividing_Index_1 > numOf_Dividing_Index_2


    '''###################
        step : 4.2
            gen : index range
    ###################'''
#     strOf_W_1 = lo_Genned_Letters[0 : numOf_Dividing_Index_1]
#     strOf_W_2 = lo_Genned_Letters[numOf_Dividing_Index_1 : numOf_Letters_Gennend - 1]
#     strOf_W_2 = lo_Genned_Letters[numOf_Dividing_Index_1 + 1 : numOf_Letters_Gennend - 1]

    strOf_W_1 = lo_Genned_Letters[0 : numOf_Dividing_Index_1]
    strOf_W_2 = lo_Genned_Letters[numOf_Dividing_Index_1 : numOf_Dividing_Index_2]
    strOf_W_3 = lo_Genned_Letters[numOf_Dividing_Index_2 : numOf_Letters_Gennend - 1]
    
    #debug
    print()
#     print("[%s:%d] strOf_W_1 = '%s', strOf_W_2 = '%s'" % \
    print("[%s:%d] strOf_W_1 = '%s', strOf_W_2 = '%s', strOf_W_3 = '%s'" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_W_1, strOf_W_2
                     , strOf_W_3
                    ), file=sys.stderr)
    print()
    
    #debug
    print()
#     print("[%s:%d] strOf_W_1 = '%s', strOf_W_2 = '%s'" % \
    print("[%s:%d]\nstrOf_W_1 = '%s'\nstrOf_W_2 = '%s'\nstrOf_W_3 = '%s'" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , "".join(strOf_W_1)
                     , "".join(strOf_W_2)
                     , "".join(strOf_W_3)
                    ), file=sys.stderr)
    print()
    
#_20190412_084400:wl:in-func    
    '''###################
        message
    ###################'''

    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
 
                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    test_1()
    
#def exec_prog()

if __name__ == "__main__" :

    '''###################
    	validate : help option		
    ###################'''

    '''###################
    	get options		
    ###################'''

    '''###################
    	evecute		
    ###################'''
    exec_prog()


#     print()
#     
#     print("[%s:%d] done" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
