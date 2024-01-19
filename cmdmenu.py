import linklib
import webbrowser
from pathlib import Path
import cutie
import sys
import os
while True:
    if not os.path.exists("./out"):
        os.mkdir("./out")
    print("What do you want to do?")
    options = ["1. Create Matrx code", "2. Read Matrx code", "3. Exit from program"]
    choice = cutie.select(options)
    if choice == 0:
        while True:
            print("Choose a name for the file")
            name = input("\n>> ")
            print("Type the link of the website or the text you want to save")
            link = input("\n>> ")
            linklib.matrixlink(link, name)
            break
    elif choice == 1:
        while True:
            print("Type the name of the saved Matrx (no extension, only name)")
            name = input("\n>> ")
            link = linklib.getlink("out/"+name+".png")
            sels = ["1. Save as txt", "2. Open in web browser"]
            print("What do you want to do")
            choice = cutie.select(sels)
            if choice == 0:
                num = input("Choose the name of the file\n>> ")
                file = Path(f"out/{num}.txt")
                file.write_text(link)
                break
            elif choice == 1:
                webbrowser.open(link)
                break
    elif choice == 2:
        sys.exit(0)
    else:
        continue
