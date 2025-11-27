# Remove current folder from USER PATH
$Current = (Get-Location).Path
$OldPath = [Environment]::GetEnvironmentVariable("Path", "User")

# Convert PATH to list, remove matches
$PathList = $OldPath -split ';' | Where-Object { $_ -and ($_ -ne $Current) }

$NewPath = ($PathList -join ';')

[Environment]::SetEnvironmentVariable("Path", $NewPath, "User")

Write-Host "Removed from PATH (if present): $Current"
