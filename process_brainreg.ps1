# brainreg_script.ps1

<# 
NOTES TO READ:

You need to have brainreg from brainglobe installed on your conda environemt:
	- https://brainglobe.info/documentation/brainreg/index.html

Your images will have to have been de-skulled before running this.

Set the directories you want to process here
These can be the "main" directory and it will recursively go through any subsdirectories 

This script assumes:
 	- the images you want to register are called output_img.tif
	- the atlas you want to use is the allen_mouse_100um brain atlas 
	- the orientation (the upper most left part of the brain) is posterior-superior-left
	- resolution is 128x128x128 um^3.
#>


$directories = @(
    'path\to\directory'
)

foreach ($dir in $directories) {
    Get-ChildItem -Path $dir -Directory -Recurse | ForEach-Object {
        $currentDir = $_.FullName
        $outputFile = Join-Path -Path $currentDir -ChildPath "output_img.tif"
        
        if (Test-Path $outputFile) {
            Write-Host "Processing directory: $currentDir"
            Set-Location $currentDir
            brainreg output_img.tif registration -v 128 128 128 --orientation psl --atlas allen_mouse_100um
        }
    }
}