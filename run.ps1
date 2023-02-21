# Open the first terminal window
Start-Process powershell -ArgumentList '-NoExit','-Command "Write-Host `"Terminal 1`";; cd .\backend; python app.py"'

# Open the second terminal window
Start-Process powershell -ArgumentList '-NoExit','-Command "Write-Host `"Terminal 2`";; cd .\frontend; npm start"'