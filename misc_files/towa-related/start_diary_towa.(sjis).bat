@echo off

REM opening message
echo starting start.bat // C:\WORKS_2\WS\WS_Others.miscs\misc_files

REM =================================
REM 	log file
REM 	browser
REM =================================

REM =================================
REM 	log file
REM 	2020/01/17 15:40:31
REM =================================
pushd C:\WORKS_2\WS\WS_Others.miscs\misc_files\towa-related
start diary_towa_2020.odt


REM =================================
REM 	browser
REM 	2020/01/17 15:41:52
REM 	ref : ï∂éöâªÇØ https://www.adminweb.jp/command/display/index5.html
REM =================================
REM set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=ìåòa+ì˙éè&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"
REM set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo^=ìåòa+ì˙éè&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"
set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=ìåòa+ì˙éè&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"
set url_2="http://benfranklin.chips.jp/PHP_server/D-2/time_calc.php"

set url_3=http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/view/40124

set url_4=http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/view/39970

set url_5="https://mail.google.com/mail/ca/u/0/#search/diary+towa?compose=jrjtXFBVVNZLVRnTMtvQHtvHNkmwMrDwznhgwmRJBRCWzJCjjsnhwJdfwrdlXzhNdTLvLHJJ"

rem : stopwatch
set url_6="https://stopwatch-app.com"

REM set url_1="http%3A%2F%2Fbenfranklin.chips.jp%2Fcake_apps%2FCake_IFM11%2Fimages%2Findex_2%3Ffilter_memo%3D%E6%9D%B1%E5%92%8C%2B%E6%97%A5%E8%AA%8C%26RBs_AND_OR_Memo%3DAND%26sort%3Dfile_name%26direction%3Ddesc"

pushd C:\WORKS_2\Programs\opera
REM launcher.exe http://localhost/Eclipse_Luna/Cake_IFM11/ifm
REM launcher.exe %url_1%
launcher.exe %url_1% %url_2% %url_3% %url_4% %url_5% %url_6%

REM launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=ìåòa+ì˙éè&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"


:end_of_end

rem pause
