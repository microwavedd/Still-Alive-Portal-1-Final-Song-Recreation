import subprocess
#Pretty much, what dis does is to make both the song lyrics and the ascii art play at the same time in different cmd instances, to avoid text collision and therefore, ugliness.
def execute():
    # You need to substitute the path to wherever the files "songpace.py" and "asciis.py" are in your machine.
    # More detailed tutorial in the github
    c1 = "python C:/Users/Ingo/Desktop/PortalStillAlive/main/songpace.py"  # Reemplaza "script1.py" con el nombre de tu primer script
    c2 = "python C:/Users/Ingo/Desktop/PortalStillAlive/main/asciispace.py"  # Reemplaza "script2.py" con el nombre de tu segundo script
    p1 = subprocess.Popen(c1, creationflags=subprocess.CREATE_NEW_CONSOLE)
    p2 = subprocess.Popen(c2, creationflags=subprocess.CREATE_NEW_CONSOLE)

    p1.wait()
    p2.wait()

#Pop goes the weasel
execute()