$Month=$args[0]
$Year=$args[1]

$folderMonth = $Month.SubString(0,4)
Write-Host $folderMonth
$folderName = "$folderMonth" + "_" + "$Year"

Write-Host $folderName

New-Item -Path "$folderName" -ItemType Directory
Copy-Item "InitializeDayBlog.ps1" -Destination "$folderName"