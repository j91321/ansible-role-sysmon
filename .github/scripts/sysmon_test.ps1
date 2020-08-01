$OutputVariable = Get-Service -Displayname "*sysmon*" | Out-String
if(-NOT $OutputVariable -Match "Running") {
	Write-Output "Sysmon service is not running"
	exit 1
}
$OutputVariable = sysmon64.exe -c | Out-String
if($OutputVariable -Match "No rules installed") {
	Write-Output "No rules installed"
	exit 1
}
Write-Output "Sysmon installed succesfully"
