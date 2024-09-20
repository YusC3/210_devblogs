$folderName = Get-Date -Format "dd_MMMM"

New-Item -Path $folderName -ItemType Directory
New-Item -Path "$folderName\README.md" -ItemType File
New-Item -Path "$folderName\Resources.md" -ItemType file
New-Item -Path "$folderName\src" -ItemType Directory