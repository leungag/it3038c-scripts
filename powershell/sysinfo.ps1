<<<<<<< HEAD
﻿function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 
write-host(getIP)

$IP = getIP 

Write-Host(“This machine’s IP is $IP”) 

Write-Host(“This machine’s IP is {0}” -f $IP) 
$user = $env:USERNAME
$hostname = $env:COMPUTERNAME
$psVersion = $psVersionTable.PSVersion.Major
$formattedDate = $currentDate.ToString("dddd, MMMM d,yyyy")

$BODY = "This machine's IP is $IP. The User is $user.Hostname is $hostname . PowerShell Version $psVersion . Today's Date is $formattedDate"

Send-MailMessage -To "leungag@mail.uc.edu" -From "aleung.dlg.23.4@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 
=======
﻿function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 
write-host(getIP)

$IP = getIP 

Write-Host(“This machine’s IP is $IP”) 

Write-Host(“This machine’s IP is {0}” -f $IP) 
$user = $env:USERNAME
$hostname = $env:COMPUTERNAME
$psVersion = $psVersionTable.PSVersion.Major
$formattedDate = $currentDate.ToString("dddd, MMMM d,yyyy")

$BODY = "This machine's IP is $IP. The User is $user.Hostname is $hostname . PowerShell Version $psVersion . Today's Date is $formattedDate"

Send-MailMessage -To "leungag@mail.uc.edu" -From "aleung.dlg.23.4@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 
>>>>>>> 4f3ddc99a54f9d607b5b5a54aa1916e3eadc508f
