<# para ejecutar en PowerShell de VSCode .\build.ps1 #>
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
Remove-Item -Recurse -Force public
Expand-Archive -Path frontend.zip -DestinationPath public
Remove-Item frontend.zip
.\venv\Scripts\Deactivate.ps1