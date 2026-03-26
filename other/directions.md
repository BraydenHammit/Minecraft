If you are able to use GitHub Desktop and VS Code, click Code -> Local -> Open With GitHub Desktop. 
Then, after you clone it and wait for it to download, open it in VS Code and run (Windows) "python minecraftMain.py" or (MacBook) "python3 minecraftMain.py".
When the game updates, click Fetch Origin in GitHub Desktop, then click Pull from Origin.                                                                                                 

If you are using a Chromebook or other device that cannot open VS Code fork the repository. 
Then, click Code -> Codespaces -> +.
This will create a new codespace; when it is done downloading, make sure there is a port 6080.
If there is not, make a new port with number 6080. 
Then run "export DISPLAY=:1" and "python3 minecraftMain.py", then open the port.
To update the game, run "git pull origin main" in the terminal.
Unfortunately, sounds do not work on these devices.
