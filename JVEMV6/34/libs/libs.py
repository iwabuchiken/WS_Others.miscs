import inspect
import os

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
# from __builtin__ import str
from sympy.physics.vector.printing import params

def linenum(depth=0):
#     print "line"
    
    #ref https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number 'answered Jul 25 '11 at 1:31'
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                        # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
#     return info.filename                       # __FILE__     -> Test.py
    #     print info.filename                       # __FILE__     -> Test.py
    #     print info.function                       # __FUNCTION__ -> Main
    #     print info.lineno                         # __LINE__     -> 13
    return info.lineno                         # __LINE__     -> 13

    
    '''
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno
    
    '''

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"

    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    return info.filename                       # __FILE__     -> Test.py
#     print info.filename                       # __FILE__     -> Test.py
#     print info.function                       # __FUNCTION__ -> Main
#     print info.lineno                         # __LINE__     -> 13
    
    '''    
        frame = inspect.currentframe(0)
    #     frame = inspect.currentframe(depth+1)
        
        return os.path.basename(frame.f_code.co_filename)
    #     return frame.f_code.co_filename
    '''
#/def thisfile(depth=0):

def get_opt(arg_ary):
    
#     print "[%s:%d] args =>" % (thisfile(), linenum())
    
#     print arg_ary
    
    # validate
    if len(arg_ary) < 1 :
        
        print ("[%s:%d] no args" % (thisfile(), linenum()))
        
        return (None, None)
    
    # return tuple
    result = []
    # loop
    for elem in arg_ary :
        
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
        if elem.startswith('-E') and len(elem) > 2 :
            
            #ref append https://stackoverflow.com/questions/1878470/add-tuple-to-list-of-tuples-in-python
            #ref slice http://www.pythonweb.jp/tutorial/string/index11.html
            result.append(('-E', elem[2:]))
    
        elif elem.startswith('-s') and len(elem) > 2 :
            
            result.append(('-s', elem[2:]))
    
        elif elem.startswith('-e') and len(elem) > 2 :
            
            result.append(('-e', elem[2:]))
    
        elif elem.startswith('-t') and len(elem) > 2 :
            
            result.append(('-t', elem[2:]))
    
        elif elem.startswith('-V') and len(elem) > 2 :
            
            result.append(('-V', elem[2:]))
    
        elif elem.startswith('--') and len(elem) > 2 :
            
            if elem == '--PLOT_GO' :
                
                result.append(('PLOT_GO', ''))
#                 result.append('PLOT_GO')
    
            elif elem == '--SAVE_IMAGE_GO' :
                
                result.append(('SAVE_IMAGE_GO', ''))
    
    return result

def get_opt_2(arg_ary, keychars):
    
#     print "[%s:%d] args =>" % (thisfile(), linenum())
#       
#     print arg_ary
#      
#     print list(keychars)
    
    # validate
    if len(arg_ary) < 1 :
        
        print ("[%s:%d] no args" % (thisfile(), linenum()))
        
        return (None, None)
    
    # return tuple
    result = []
    # loop
    for elem in arg_ary :
        
#         print "[%s:%d] elem = '%s'" % (thisfile(), linenum(), elem)
            
        #ref list http://nekoyukimmm.hatenablog.com/entry/2015/10/01/223148
        for char in list(keychars) :
            
#             print "[%s:%d] elem = '%s' / char = '%c'" % (thisfile(), linenum(), elem, char)
            
            
            if elem.startswith('-' + char) \
                    and len(elem) > 2 \
                    and not elem.startswith("--"):
#             if elem.startswith(char) and len(elem) > 2 :
#             if elem.startswith(char) and len(elem) > 2 :
                if not '-' + char in [x[0] for x in result] : result.append(('-' + char, elem[2:]))
                
#                 print "[%s:%d] '-' + char : appended => '%s'" % (thisfile(), linenum(), elem[2:])
                
            
            elif elem.startswith('--') and len(elem) > 2 :
                
                if not (elem[2:], '') in result : result.append((elem[2:], ''))
             
#                 print "[%s:%d] '--' : appended => '%s'" % (thisfile(), linenum(), elem[2:])
             
#             if elem == '--PLOT_GO' : result.append(('PLOT_GO', ''))
                
            #ref append https://stackoverflow.com/questions/1878470/add-tuple-to-list-of-tuples-in-python
            #ref slice http://www.pythonweb.jp/tutorial/string/index11.html
                
                
#         #ref https://www.tutorialspoint.com/python/string_startswith.htm
#         if elem.startswith('-E') and len(elem) > 2 :
#             
#             #ref append https://stackoverflow.com/questions/1878470/add-tuple-to-list-of-tuples-in-python
#             #ref slice http://www.pythonweb.jp/tutorial/string/index11.html
#             result.append(('-E', elem[2:]))
#     
#         elif elem.startswith('-s') and len(elem) > 2 :
#             
#             result.append(('-s', elem[2:]))
#     
#         elif elem.startswith('-e') and len(elem) > 2 :
#             
#             result.append(('-e', elem[2:]))
#     
#         elif elem.startswith('-t') and len(elem) > 2 :
#             
#             result.append(('-t', elem[2:]))
#     
#         elif elem.startswith('-V') and len(elem) > 2 :
#             
#             result.append(('-V', elem[2:]))
#     
#         elif elem.startswith('--') and len(elem) > 2 :
#             
#             if elem == '--PLOT_GO' :
#                 
#                 result.append(('PLOT_GO', ''))
# #                 result.append('PLOT_GO')
#     
#             elif elem == '--SAVE_IMAGE_GO' :
#                 
#                 result.append(('SAVE_IMAGE_GO', ''))
    
    return result

'''
    @param string_type
            serial    "20160604_1934"
'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())
    str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
        str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():
