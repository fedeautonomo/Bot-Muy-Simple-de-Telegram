del C:\serverbot\fallnet\2.txt
powershell Unlock-ADAccount  -Identity %1 > C:\serverbot\fallnet\espinaca.txt
powershell "Get-ADUser -Identity %1 -Properties LockedOut | Format-Table Name,LockedOut -A > 'C:\serverbot\fallnet\2.txt'"