@echo off
@echo
@echo Power Plan
powercfg -import "C:\Bitsum Highest Performance.pow" 00000000-0000-0000-0000-000000000000
powercfg -setactive "00000000-0000-0000-0000-000000000000"
@echo
pause