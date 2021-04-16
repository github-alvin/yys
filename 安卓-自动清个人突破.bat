@ECHO OFF
setlocal EnableDelayedExpansion
color 3e
title yys auto tool
 
PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas
 
::填写自己的设备号（--android后）
python main.py --android 34104c43 auto 2
 
echo 执行完毕,任意键退出
 
pause >nul
exit
