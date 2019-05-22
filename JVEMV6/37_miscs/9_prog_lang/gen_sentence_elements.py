# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\gen_sentence_elements.py
orig : C:\WORKS_2\WS\WS_Others.prog\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\ops\gen_random_string.py
at : 2019/04/09 10:34:32

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\
python gen_sentence_elements.py

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

from mm.libs_mm import libs
# from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, math, random, subprocess

###############################################
#
#	VARS (GLOBAL)
#
###############################################
numOf_Nouns_Chosen = 8
numOf_Verbs_Chosen = 5
numOf_Expressions_Chosen = 5

numOf_Topics_Chosen = 3

numOf_Adverbs_Chosen = 5
numOf_Ajectives_Chosen = 5

charOf_Join_For_Words = ";"
#charOf_Join_For_Categories = " / "
charOf_Join_For_Categories__Display = "\n"
charOf_Join_For_Categories__Clip = " / "



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

def test_2__Korean():

#_20190411_091337:head

    '''###################
        step : 0.1
            prep : vars
    ###################'''

#    numOf_Nouns_Chosen = 4
#    numOf_Verbs_Chosen = 4
#    numOf_Expressions_Chosen = 4
#    
#    numOf_Adverbs_Chosen = 4
#    numOf_Ajectives_Chosen = 4
    
    '''###################
        step : 1
            load files
    ###################'''
    '''###################
        step : 1.1
            build : paths
    ###################'''
    dpath_Data_Files = "C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\37_miscs\\9_prog_lang"
    
    fname_Data_Nouns = "data_nouns.dat"
    fname_Data_Verbs = "data_verbs.dat"
    fname_Data_Expressions = "data_expressions.dat"
    
    fname_Data_Topics = "data_topics.dat"
    
    fname_Data_Adverbs = "data_adverbs.dat"
    fname_Data_Ajectives = "data_ajectives.dat"
    
    # paths
    fpath_Data_Nouns = os.path.join(dpath_Data_Files, fname_Data_Nouns)
    fpath_Data_Verbs = os.path.join(dpath_Data_Files, fname_Data_Verbs)
    fpath_Data_Expressions = os.path.join(dpath_Data_Files, fname_Data_Expressions)
    fpath_Data_Topics = os.path.join(dpath_Data_Files, fname_Data_Topics)
    
    fpath_Data_Adverbs = os.path.join(dpath_Data_Files, fname_Data_Adverbs)
    fpath_Data_Ajectives = os.path.join(dpath_Data_Files, fname_Data_Ajectives)
    #_20190411_092504:fix
    
    '''###################
        step : 1.2
            validate
    ###################'''
    # nouns
    if not os.path.isfile(fpath_Data_Nouns) : #if not os.path.isfile(fpath_Data_Nouns)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Nouns
                        ), file=sys.stderr)
        
        return
    
    # verbs    
    if not os.path.isfile(fpath_Data_Verbs) : #if not os.path.isfile(fpath_Data_Verbs)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Verbs
                        ), file=sys.stderr)
        
        return
    
    # expressions
    if not os.path.isfile(fpath_Data_Expressions) : #if not os.path.isfile(fpath_Data_Expressions)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Expressions
                        ), file=sys.stderr)
        
        return

    # topics
    if not os.path.isfile(fpath_Data_Topics) : #if not os.path.isfile(fpath_Data_Topics)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Topics
                        ), file=sys.stderr)
        
        return

    # adverbs
    if not os.path.isfile(fpath_Data_Adverbs) : #if not os.path.isfile(fpath_Data_Adverbs)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Adverbs
                        ), file=sys.stderr)
        
        return

    # ajectives
    if not os.path.isfile(fpath_Data_Ajectives) : #if not os.path.isfile(fpath_Data_Ajectives)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Ajectives
                        ), file=sys.stderr)
        
        return


    '''###################
        step : 1.2
            file : read
    ###################'''
    # load : files
    fin_Nouns = open(fpath_Data_Nouns, "r")
    fin_Verbs = open(fpath_Data_Verbs, "r")
    fin_Expressions = open(fpath_Data_Expressions, "r")
    fin_Topics = open(fpath_Data_Topics, "r")
    
    fin_Adverbs = open(fpath_Data_Adverbs, "r")
    fin_Ajectives = open(fpath_Data_Ajectives, "r")
    
    # read lines
    lo_Nouns = fin_Nouns.readlines()
    lo_Verbs = fin_Verbs.readlines()
    lo_Expressions = fin_Expressions.readlines()
    lo_Topics = fin_Topics.readlines()
    
    lo_Adverbs = fin_Adverbs.readlines()
    lo_Ajectives = fin_Ajectives.readlines()
    
    # lines : strip
    # also, the last element ---> omit (return only line)
    lo_Nouns = [x.strip() for x in lo_Nouns[:-1]]
    lo_Verbs = [x.strip() for x in lo_Verbs[:-1]]
    lo_Expressions = [x.strip() for x in lo_Expressions[:-1]]
    lo_Topics = [x.strip() for x in lo_Topics[:-1]]
#     lo_Nouns = [x.strip() for x in lo_Nouns]
#     lo_Verbs = [x.strip() for x in lo_Verbs]
    lo_Adverbs = [x.strip() for x in lo_Adverbs[:-1]]
    lo_Ajectives = [x.strip() for x in lo_Ajectives[:-1]]
    
    # lengh
    lenOf_LO_Nouns = len(lo_Nouns)
    lenOf_LO_Verbs = len(lo_Verbs)
    lenOf_LO_Expressions = len(lo_Expressions)
    lenOf_LO_Topics = len(lo_Topics)
    
    lenOf_LO_Adverbs = len(lo_Adverbs)
    lenOf_LO_Ajectives = len(lo_Ajectives)
    
    '''###################
        step : 1.x
            file : close
    ###################'''
    fin_Nouns.close()
    fin_Verbs.close()
    fin_Expressions.close()
    fin_Topics.close()
    
    fin_Adverbs.close()
    fin_Ajectives.close()
    
    

    '''######################################
        step : 2
            choose : words
    ######################################'''
    '''###################
        step : 2.1
            choose : nouns
    ###################'''
    lo_Nouns_Chosen = []
    
    flg_Unique = False
    
    for i in range(0, numOf_Nouns_Chosen):
    
        # choose
#         while not flg_Unique :
        while True :
            
            noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns - 1)]
            
            #ref https://stackoverflow.com/questions/7936125/python-find-out-if-an-element-in-a-list-has-a-specific-string
            if not noun_Chosen in lo_Nouns_Chosen : #if not noun_Chosen in lo_Nouns_Chosen
                
                break
            
            #/if not noun_Chosen in lo_Nouns_Chosen
            
        #/while not flg_Unique :
#         noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns - 1)]
#         noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns)]
        
        # append
        lo_Nouns_Chosen.append(noun_Chosen)
        
    #/for i in range(0, numOf_Nouns_Chosen):


    '''###################
        step : 2.2
            choose : verbs
    ###################'''
    lo_Verbs_Chosen = []
    
    for i in range(0, numOf_Verbs_Chosen):
    
        # choose
        while True:
            
            verb_Chosen = lo_Verbs[random.randint(0, lenOf_LO_Verbs - 1)]
            
            if not verb_Chosen in lo_Verbs_Chosen : #if not nou_
                
                break
            
            #/if not nou_

        
        # append
        lo_Verbs_Chosen.append(verb_Chosen)
        
    #/for i in range(0, numOf_Verbs_Chosen):

    '''###################

        step : 2.3
            choose : expression
    ###################'''
    lo_Expressions_Chosen = []
    
    for i in range(0, numOf_Expressions_Chosen):
    
        # choose
        while True :
            
            expression_Chosen = lo_Expressions[random.randint(0, lenOf_LO_Expressions - 1)]
            
            if not expression_Chosen in lo_Expressions_Chosen : #if not expression_Chosen in lo_Expressions_Chosen
                
                break
            
            #/if not expression_Chosen in lo_Expressions_Chosen
            
        #/while True
#         expression_Chosen = lo_Expressions[random.randint(0, lenOf_LO_Expressions - 1)]
        
        # append
        lo_Expressions_Chosen.append(expression_Chosen)
        
    #/for i in range(0, numOf_Expressions_Chosen):

    '''###################

        step : 2.4
            choose : Adverbs
    ###################'''
    lo_Adverbs_Chosen = []

    #_20190411_093247:fix
    for i in range(0, numOf_Adverbs_Chosen):
    
        # choose
        while True :
            
            expression_Chosen = lo_Adverbs[random.randint(0, lenOf_LO_Adverbs - 1)]
            
            if not expression_Chosen in lo_Adverbs_Chosen : #if not expression_Chosen in lo_Adverbs_Chosen
                
                break
            
            #/if not expression_Chosen in lo_Adverbs_Chosen
            
        #/while True
        
        # append
        lo_Adverbs_Chosen.append(expression_Chosen)
        
    #/for i in range(0, numOf_Adverbs_Chosen):

    '''###################

        step : 2.5
            choose : Ajectives
    ###################'''
    lo_Ajectives_Chosen = []
    
    for i in range(0, numOf_Ajectives_Chosen):
    
        # choose
        while True :
            
            expression_Chosen = lo_Ajectives[random.randint(0, lenOf_LO_Ajectives - 1)]
            
            if not expression_Chosen in lo_Ajectives_Chosen : #if not expression_Chosen in lo_Ajectives_Chosen
                
                break
            
            #/if not expression_Chosen in lo_Ajectives_Chosen
            
        #/while True
        
        # append
        lo_Ajectives_Chosen.append(expression_Chosen)
        
    #/for i in range(0, numOf_Ajectives_Chosen):

    '''###################
        step : 2.6
            choose : topics
    ###################'''
    lo_Topics_Chosen = []
    
    for i in range(0, numOf_Topics_Chosen):
    
        # choose
        while True :
            
            expression_Chosen = lo_Topics[random.randint(0, lenOf_LO_Topics - 1)]
            
            if not expression_Chosen in lo_Topics_Chosen : #if not expression_Chosen in lo_Topics_Chosen
                
                break
            
            #/if not expression_Chosen in lo_Topics_Chosen
            
        #/while True
        
        # append
        lo_Topics_Chosen.append(expression_Chosen)
        
    #/for i in range(0, numOf_Topics_Chosen):

#     #debug
#     print()
#     print("[%s:%d] lo_Topics_Chosen ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#     print(lo_Topics_Chosen)
#     print()


    '''###################
        step : 3
            show : lines
    ###################'''
    '''###################
        step : 3.1
            build : lines
    ###################'''
#    charOf_Join_For_Words = ";"
#    charOf_Join_For_Categories = " / "
    
    strOf_Nouns = charOf_Join_For_Words.join(lo_Nouns_Chosen)
    strOf_Verbs = charOf_Join_For_Words.join(lo_Verbs_Chosen)
    strOf_Expressions = charOf_Join_For_Words.join(lo_Expressions_Chosen)
    
    strOf_Topics = charOf_Join_For_Words.join(lo_Topics_Chosen)

    strOf_Adverbs = charOf_Join_For_Words.join(lo_Adverbs_Chosen)
    strOf_Ajectives = charOf_Join_For_Words.join(lo_Ajectives_Chosen)
    
#     strOf_Results = " / ".join(\
#     strOf_Results = "\n".join(\

    #strOf_Results = charOf_Join_For_Categories.join(\

    lo_Categories =             [ \
                strOf_Nouns
                , strOf_Verbs
                , strOf_Expressions
                , strOf_Adverbs
                , strOf_Ajectives
                , strOf_Topics
            ]

    lo_Categories = ["* " + x for x in lo_Categories]

    strOf_Results = charOf_Join_For_Categories__Display.join(\
    
            lo_Categories
#            [
#                strOf_Nouns
#                , strOf_Verbs
#                , strOf_Expressions
#                , strOf_Adverbs
#                , strOf_Ajectives
#            ]
    )
#     strOf_Results = " / ".join([strOf_Nouns, strOf_Verbs, strOf_Expressions])

    #debug
    print()
    
    strOf_Chosen_Lang = "Korean"
#     print("[%s:%d] gen word set ==> done" % \
    print("[%s:%d] gen word set ==> done (lang = %s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , strOf_Chosen_Lang
                    ), file=sys.stderr)
    print(strOf_Results)
    print()

#_20190411_091351:wl:in-func

    '''###################
        step : 4
            results --> clip
    ###################'''
    
    #lo_Categories = ["*" + x for x in lo_Categories]
    
    strOf_Results = charOf_Join_For_Categories__Clip.join(\
        
        lo_Categories
        
    )

    strOf_Cmd = "echo %s | clip" % (strOf_Results)


    # calll system
    os.system(strOf_Cmd)


#_20190409_105137:wl:in-func        

    '''###################
        message
    ###################'''

#     print()
#     print("[%s:%d] test_2 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_2__Korean():

def test_1():

#_20190409_105129:head
#_20190409_105133:caller

    '''###################
        step : 0.1
            prep : vars
    ###################'''

    numOf_Nouns_Chosen = 4
    numOf_Verbs_Chosen = 4
    numOf_Expressions_Chosen = 4
    
    '''###################
        step : 1
            load files
    ###################'''
    '''###################
        step : 1.1
            build : paths
    ###################'''
    dpath_Data_Files = "C:\\WORKS_2\\WS\\WS_Others.JVEMV6\\JVEMV6\\37_miscs\\9_prog_lang"
    
    fname_Data_Nouns = "data_nouns.dat"
    fname_Data_Verbs = "data_verbs.dat"
    fname_Data_Expressions = "data_expressions.dat"
    
    # paths
    fpath_Data_Nouns = os.path.join(dpath_Data_Files, fname_Data_Nouns)
    fpath_Data_Verbs = os.path.join(dpath_Data_Files, fname_Data_Verbs)
    fpath_Data_Expressions = os.path.join(dpath_Data_Files, fname_Data_Expressions)
    
    '''###################
        step : 1.2
            validate
    ###################'''
    if not os.path.isfile(fpath_Data_Nouns) : #if not os.path.isfile(fpath_Data_Nouns)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Nouns
                        ), file=sys.stderr)
        
        return
        
    if not os.path.isfile(fpath_Data_Verbs) : #if not os.path.isfile(fpath_Data_Verbs)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Verbs
                        ), file=sys.stderr)
        
        return

    if not os.path.isfile(fpath_Data_Expressions) : #if not os.path.isfile(fpath_Data_Expressions)
        
        print()
        print("[%s:%d] file ==> NOT exist : '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , fpath_Data_Expressions
                        ), file=sys.stderr)
        
        return

    '''###################
        step : 1.2
            file : read
    ###################'''
    # load : files
    fin_Nouns = open(fpath_Data_Nouns, "r")
    fin_Verbs = open(fpath_Data_Verbs, "r")
    fin_Expressions = open(fpath_Data_Expressions, "r")
    
    # read lines
    lo_Nouns = fin_Nouns.readlines()
    lo_Verbs = fin_Verbs.readlines()
    lo_Expressions = fin_Expressions.readlines()
    
    # lines : strip
    # also, the last element ---> omit (return only line)
    lo_Nouns = [x.strip() for x in lo_Nouns[:-1]]
    lo_Verbs = [x.strip() for x in lo_Verbs[:-1]]
    lo_Expressions = [x.strip() for x in lo_Expressions[:-1]]
#     lo_Nouns = [x.strip() for x in lo_Nouns]
#     lo_Verbs = [x.strip() for x in lo_Verbs]
    
    # lengh
    lenOf_LO_Nouns = len(lo_Nouns)
    lenOf_LO_Verbs = len(lo_Verbs)
    lenOf_LO_Expressions = len(lo_Expressions)
    
    '''###################
        step : 1.x
            file : close
    ###################'''
    fin_Nouns.close()
    fin_Verbs.close()
    fin_Expressions.close()
    

#     #debug
#     print()
#     print("[%s:%d] lo_Nouns ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#     print(lo_Nouns)
#     print()

    '''######################################
        step : 2
            choose : words
    ######################################'''
    '''###################
        step : 2.1
            choose : nouns
    ###################'''
    lo_Nouns_Chosen = []
    
    flg_Unique = False
    
    for i in range(0, numOf_Nouns_Chosen):
    
        # choose
#         while not flg_Unique :
        while True :
            
            noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns - 1)]
            
            #ref https://stackoverflow.com/questions/7936125/python-find-out-if-an-element-in-a-list-has-a-specific-string
            if not noun_Chosen in lo_Nouns_Chosen : #if not noun_Chosen in lo_Nouns_Chosen
                
                break
            
            #/if not noun_Chosen in lo_Nouns_Chosen
            
        #/while not flg_Unique :
#         noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns - 1)]
#         noun_Chosen = lo_Nouns[random.randint(0, lenOf_LO_Nouns)]
        
        # append
        lo_Nouns_Chosen.append(noun_Chosen)
        
    #/for i in range(0, numOf_Nouns_Chosen):


    '''###################
        step : 2.2
            choose : verbs
    ###################'''
    lo_Verbs_Chosen = []
    
    for i in range(0, numOf_Verbs_Chosen):
    
        # choose
        while True:
            
            verb_Chosen = lo_Verbs[random.randint(0, lenOf_LO_Verbs - 1)]
            
            if not verb_Chosen in lo_Verbs_Chosen : #if not nou_
                
                break
            
            #/if not nou_

        
        # append
        lo_Verbs_Chosen.append(verb_Chosen)
        
    #/for i in range(0, numOf_Verbs_Chosen):

    '''###################

        step : 2.3
            choose : expression
    ###################'''
    lo_Expressions_Chosen = []
    
    for i in range(0, numOf_Expressions_Chosen):
    
        # choose
        while True :
            
            expression_Chosen = lo_Expressions[random.randint(0, lenOf_LO_Expressions - 1)]
            
            if not expression_Chosen in lo_Expressions_Chosen : #if not expression_Chosen in lo_Expressions_Chosen
                
                break
            
            #/if not expression_Chosen in lo_Expressions_Chosen
            
        #/while True
#         expression_Chosen = lo_Expressions[random.randint(0, lenOf_LO_Expressions - 1)]
        
        # append
        lo_Expressions_Chosen.append(expression_Chosen)
        
    #/for i in range(0, numOf_Expressions_Chosen):


#     #debug
#     print()
#     print("[%s:%d] lo_Expressions_Chosen ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#     print(lo_Expressions_Chosen)
#     print()

    '''###################
        step : 3
            show : lines
    ###################'''
    '''###################
        step : 3.1
            build : lines
    ###################'''
    strOf_Nouns = ", ".join(lo_Nouns_Chosen)
    strOf_Verbs = ", ".join(lo_Verbs_Chosen)
    strOf_Expressions = ", ".join(lo_Expressions_Chosen)
    
    strOf_Results = " / ".join([strOf_Nouns, strOf_Verbs, strOf_Expressions])
    

#     #debug
#     print()
#     print("[%s:%d] strOf_Results ==>" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#     print(strOf_Results)
#     print()
    
    
    
    #/if not os.path.isfile(fpath_Data_Nouns)


    '''###################
        step : 4
            results --> clip
    ###################'''
    strOf_Cmd = "echo %s | clip" % (strOf_Results)


    # calll system
    os.system(strOf_Cmd)

    #debug
    print()

    print("[%s:%d] gen word set ==> done" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     
                    ), file=sys.stderr)
    print(strOf_Results)
    print()

#_20190409_105137:wl:in-func        

    '''###################
        message
    ###################'''

#     print()
#     print("[%s:%d] test_1 =======================" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
# 
#                     ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        step : 1
            args
    ###################'''
    #debug
    print()

    print("[%s:%d] sys.argv ==> " % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     
                    ), file=sys.stderr)
    print(sys.argv)
    print()
    
#     return

    '''###################
        step : 1.1
            get : args
    ###################'''
    strOf_Lang__Korean = "Korean"
    strOf_Lang__Korean_Lower = "korean"
    
    strOf_Lang__Chinese = "Chinese"
    strOf_Lang__Chinese_Lower = "chinese"
    
    strOf_Chosen_Lang = ""
    
    if len(sys.argv) > 1 : #if len(sys.argv) > 1 and sys.arg
    
        if sys.argv[1] == strOf_Lang__Korean \
            or sys.argv[1] == strOf_Lang__Korean_Lower : #if sys.argv[1] == strOf_Lang__Korean
        
            strOf_Chosen_Lang = strOf_Lang__Korean
#             strOf_Chosen_Lang = "korean"
        
        elif sys.argv[1] == strOf_Lang__Chinese \
            or sys.argv[1] == strOf_Lang__Chinese_Lower : #if sys.argv[1] == strOf_Lang__Korean
        
            strOf_Chosen_Lang = strOf_Lang__Chinese
        
        else : #if sys.argv[1] == strOf_Lang__Korean
        
            strOf_Chosen_Lang = strOf_Lang__Korean
            

        #/if sys.argv[1] == strOf_Lang__Korean
    
    else : #if len(sys.argv) > 1 and sys.argv
    
        strOf_Chosen_Lang = strOf_Lang__Korean
#         strOf_Chosen_Lang = "korean"
    
    #/if len(sys.argv) > 1 and sys.argv
    
    '''###################
        ops        
    ###################'''
    
    #_20190411_091344:caller
#     if strOf_Chosen_Lang == strOf_Lang__Korean : #if strOf_Chosen_Lang == strOf_Lang__Korean
    if strOf_Chosen_Lang == strOf_Lang__Korean : #if strOf_Chosen_Lang == strOf_Lang__Korean
            
        test_2__Korean()
            
    elif strOf_Chosen_Lang == strOf_Lang__Chinese  : #if strOf_Chosen_Lang == strOf_Lang__Korean
        
        test_2__Chinese()
        
    else : #if strOf_Chosen_Lang == strOf_Lang__Korean
    
        #debug
        print()
    
        print("[%s:%d] unknown lang name ==> '%s'" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                         , strOf_Chosen_Lang
                        ), file=sys.stderr)
#         print(sys.argv)
        print()
        
#ccc
    
    #/if strOf_Chosen_Lang == strOf_Lang__Korean
    
#     test_1()
    

#     print("[%s:%d] exec_prog() => done" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
    
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
