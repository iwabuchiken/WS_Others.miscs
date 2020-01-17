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
pushd C:\WORKS_2\WS\WS_Others.miscs\misc_files
start diary_2020-01.odt


REM =================================
REM 	browser
REM 	2020/01/17 15:41:52
REM =================================
REM set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=東和+日誌&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"
REM set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo^=東和+日誌&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"
set url_1="http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=東和+日誌&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"

REM set url_1="http%3A%2F%2Fbenfranklin.chips.jp%2Fcake_apps%2FCake_IFM11%2Fimages%2Findex_2%3Ffilter_memo%3D%E6%9D%B1%E5%92%8C%2B%E6%97%A5%E8%AA%8C%26RBs_AND_OR_Memo%3DAND%26sort%3Dfile_name%26direction%3Ddesc"

pushd C:\WORKS_2\Programs\opera
REM launcher.exe http://localhost/Eclipse_Luna/Cake_IFM11/ifm
launcher.exe %url_1%
REM launcher.exe "http://benfranklin.chips.jp/cake_apps/Cake_IFM11/images/index_2?filter_memo=東和+日誌&RBs_AND_OR_Memo=AND&sort=file_name&direction=desc"


:end_of_end

pause
