# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\gen_random_numbers.py
orig : C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\gen_random_japanese_letters.py
at : 2019/04/12 08:45:48

pushd C:\WORKS_2\WS\WS_Others.JVEMV6\JVEMV6\37_miscs\9_prog_lang\
python gen_random_numbers.py

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
    <Usage>
    gen_random_numbers.py [range start] [range end] [num of random numbers]
    '''
    
    print (msg)

def test_1():

#_20190412_084351:head
#_20190412_084356:caller

# python
# import random as rd
# n = 6
# rd.randint(1,n)
# 
# lo_RDINT = []
# for s in range(1,n) : 
#   R = rd.randint(1,n)
# 
# 
#   lo_RDINT.append()
# print(lo_RDINT)

    '''###################
        step : 1
            args
    ###################'''
    '''###################
        step : 1.1
            args : get
    ###################'''
    lo_ARGS = sys.argv
    
    '''###################
        step : 1.2
            args : validate : arg length
    ###################'''
    # len
    lenOf_ARGS__Necessary = 4
    
    if not len(lo_ARGS) == lenOf_ARGS__Necessary : #if not len(lo_ARGS) == 4
    
        #debug
        print()
        print("[%s:%d] arg length ==> not right : %d necessary, %d given" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , lenOf_ARGS__Necessary, len(lo_ARGS)
                ), file=sys.stderr)
        
        # show usage
        print("ARGS", lo_ARGS)
        
        show_Message()
        
        return
    
    #/if not len(lo_ARGS) == 4

    '''###################
        step : 1.2 : 2
            args : validate : arg type
    ###################'''
    # flag
    flg_Error = False
    
    # iterate
    for i in range(1, 4):
        # get : arg
        tmpOf_Arg = lo_ARGS[i]
        
        # judge
        #ref https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float#354073
        if not tmpOf_Arg.isdigit() : #if not lo_ARGS[1].isdigit()
        
            # show message
            print()
            print("[%s:%d] ARGS[%d] ==> not digit : %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                     , i, tmpOf_Arg
                    ), file=sys.stderr)
            
            # set : flag
            flg_Error = True
        
    #/for i in range(1, 4):

    # judge : flag
    if flg_Error == True : #if flg_Error == True
    
#             # show message
#             print()
#             print("[%s:%d] ARGS ==> not proper" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                      
#                     ), file=sys.stderr)
#             print()
            
            # show : usage
            show_Message()
            
            # exit
            return
    
    #/if flg_Error == True

    '''###################
        step : 2
            gen : random numbers
    ###################'''
    '''###################
        step : 2.1
            prep
    ###################'''
    num_Start = int(lo_ARGS[1])
    num_End = int(lo_ARGS[2])
    
    lenOf_Random_Nums = int(lo_ARGS[3])
    
    lo_Genned_Nums = []
    
    '''###################
        step : 2.2
            gen
    ###################'''
    cntOf_Genned_Nums = 0
    
    while True :
        
        # gen
        tmp_Num = random.randint(num_Start, num_End)
        
        # validate
        if tmp_Num in lo_Genned_Nums : #if tmp_Num in lo_Genned_Nums
            
            continue
        
        #/if tmp_Num in lo_Genned_Nums
        
        # append
        lo_Genned_Nums.append(tmp_Num)
        
        # count
        cntOf_Genned_Nums += 1
        
        # judge
        if cntOf_Genned_Nums >= lenOf_Random_Nums : #if cntOf_Genned_Nums >= lenOf_Random_Nums
                        
            break
        
        #/if cntOf_Genned_Nums >= lenOf_Random_Nums

    #/while True :
    
    '''###################
        step : 3
            show
    ###################'''
    '''###################
        step : 3.1
            build : string
    ###################'''
    # string
    strOf_Genned_Nums = " ".join([str(x) for x in lo_Genned_Nums])
    
    '''###################
        step : 3.2
            show
    ###################'''
    # show message
#     print()
#     print("[%s:%d] Random nums ==>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              
#             ), file=sys.stderr)
#     print(lo_Genned_Nums)
    
    #ref C:\WORKS_2\Utils\gen_random_string.20190402_105313.rb
    os.system("echo|set /p=\"%s\" | clip" % (strOf_Genned_Nums))
#     os.system("echo|set /p=\"#{strOf_Random_Chars}\" | clip")

    # show message
    print()
    print("[%s:%d] gen-ed ===>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             
            ), file=sys.stderr)
    
    print(strOf_Genned_Nums)
    
    print("(clipped, as well)")
    
    
    
#_20190412_084400:wl:in-func
    
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
