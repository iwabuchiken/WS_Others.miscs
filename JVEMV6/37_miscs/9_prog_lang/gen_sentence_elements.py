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

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import os, math, random, subprocess

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
        ops        
    ###################'''
    test_1()
    

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
