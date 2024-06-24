set /p Input=Enter some text: 
powershell Unlock-ADAccount  -Identity %Input% > C:\serverbot\fallnet\espinaca.txt
powershell "Get-ADUser -Identity %Input% -Properties LockedOut | Format-Table Name,LockedOut -A"
pause