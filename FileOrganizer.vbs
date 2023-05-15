'CreateObject("Wscript.Shell").Run "C:\Alarm Clock Using Python With Source Code\FileOrganizer.bat",0,True'
Set WshShell=CreateObject("Wscript.Shell")
Wshshell.Run chr(34) & "C:\Notifier\FileOrganizer.bat" & chr(34),0
Set WshShell = Nothing