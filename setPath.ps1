# Add current folder to USER PATH
$Current = Split-Path -Parent $MyInvocation.MyCommand.Definition
$OldPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($OldPath -notlike "*$Current*") {
    $NewPath = "$OldPath;$Current"
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Host "Added to PATH: $Current"
} else {
    Write-Host "Already in PATH."
}

Write-Host "`nPress any key to exit..."
[void][System.Console]::ReadKey($true)
