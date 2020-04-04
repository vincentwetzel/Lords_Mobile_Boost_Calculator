@echo off

:: Change the CWD to make sure it is the same as the script.
:: This matters the script is being run from an external source such as a Razer macro hotkey.
CD /D %~dp0
start pythonw %~dp0\Lords_Mobile_Boost_Calculator.pyw

::pause
exit