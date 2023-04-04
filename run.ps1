# Open the first terminal window
Start-Process powershell -ArgumentList '-NoExit','-Command "Write-Host `"Backend Terminal`";; cd .\backend; python app.py"'

# Open the second terminal window
Start-Process powershell -ArgumentList '-NoExit','-Command "Write-Host `"Frontend Terminal`";; cd .\frontend; npm start"'