@ECHO OFF
setlocal EnableDelayedExpansion
color 3e
title yys auto tool
 
PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas
 
::填写自己的脚本
python main.py auto 3
 
echo 执行完毕,任意键退出
 
pause >nul
exit
