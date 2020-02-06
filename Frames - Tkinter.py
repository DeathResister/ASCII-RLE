import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.messagebox
import tkinter.scrolledtext
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title_font2 = tkfont.Font(family='Calibri', size=16)
        self.title_fontSub = tk.font.Font(family='Bauhaus 93 Regular', size=16)
        self.title_fontOptions = tkfont.Font(family='Calibri', size=14)
        self.title_fontmainTMenu = tkfont.Font(family='Helvetica', size=20)
        
        self.title_fontDevices = tkfont.Font(family='Didot', size=13)
        self.title_fontT = tkfont.Font(family='Cambria', size=16) 
        self.title("Compreso")
        self.geometry("700x775")

        

        
        # the container is where we'll stack a bunch of frmes
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, enterRLE, displayASCII, convToASCII, convToRLE):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.geometry = "700x575"
        self.geometry(frame.geometry)
        self.controller = controller
        
        label = tk.Label(self, text="Welcome to Compreso!", fg="red", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)
        choicesL = tk.Label(self, text="Please pick an option:", fg="darkblue", font=controller.title_font2)
        choicesL.place(x = 250, y = 50)

        Buttondecomp = tk.Button(self, text="Input RLE to decompress", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("enterRLE"))
        Buttondecomp.place(x = 230, y = 90, width = 250, height = 40)
        
        ButtonDisplayASCII = tk.Button(self, text="Display ASCII Art", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("displayASCII"))
        ButtonDisplayASCII.place(x = 230, y = 150, width = 250, height = 40)
        
        ButtonDecompress = tk.Button(self, text="Decompress To ASCII", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("convToASCII"))
        ButtonDecompress.place(x = 230, y = 210, width = 250, heigh = 40)
        
        ButtonCompress = tk.Button(self, text="Compress To RLE", fg="blue", font=controller.title_fontOptions,
                            command=lambda: controller.show_frame("convToRLE"))
        ButtonCompress.place(x = 230, y = 270, width = 250, height = 40)
        
        
                                                                


class enterRLE(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.geometry = "700x775"
        label = tk.Label(self, text="Enter RLE", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)
        
        leb = tk.Frame(self, height=250)
        leb.pack(expand=True, fill=tk.BOTH, pady=10)
        subLabel = tk.Label(leb, text="Please enter RLE to Decompress: ", fg="darkgreen", font=controller.title_fontSub)
        subLabel.place(x = 180, y = 10, width = 350, height = 40)

        asciiInputted = tk.Text(leb, font=('Consolas', 10), wrap="none", borderwidth=0, width=64, height=14)
        asciiInputted.place(x = 130, y = 70)

        

##        IfileName = tk.Entry(leb)
##        IfileName.place(x = 220, y = 80, width = 250, height = 40)


        submitName = tk.Button(leb, text="Submit",
                               command=lambda: inputRLE())
        submitName.place(x = 220, y = 320, width = 250, height = 40)


        asciiShown = tk.Text(leb, font=('Consolas', 10), wrap="none", state="disabled", borderwidth=0, width=64, height=14)
        asciiShown.place(x = 130, y = 400)
        
        
        def inputRLE():
            rle = asciiInputted.get("1.0", tk.END)
##            print('rel:{}'.format(rle))
            message = []
            content = asciiInputted.get("1.0", tk.END)
            rle = [x.strip() for x in content.split('\n')]
            try:
                for i in range(0, len(rle)):
                    for x in range(0, len(rle[i]), 3): 
                        print(int(rle[i][x:x+2]) * rle[i][x+2], end="")
                        asciiShown.insert(tk.END, str(int(rle[i][x:x+2]) * rle[i][x+2]))
                    print()
                #message = '\n'.join(message)
            except (IndexError, ValueError):
                noFile = tk.messagebox.showerror(title="Error", message="Please Try Again")

            

        


        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: [controller.show_frame("MainMenu"), asciiShown.delete(1.0, tk.END)])
        mButton.place(x = 490, y = 736, width = 200, height = 30)     


class displayASCII(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.geometry = "700x575"
        self.geometry(frame.geometry)
        self.controller = controller
        label = tk.Label(self, text="Display ASCII Art", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)

        leb = tk.Frame(self, height=250)
        leb.pack(expand=True, fill=tk.BOTH, pady=10)
        subLabel = tk.Label(leb, text="Please enter ASCII file to display: ", fg="darkgreen", font=controller.title_fontSub)
        subLabel.place(x = 180, y = 10, width = 350, height = 40)

        IfileName = tk.Entry(leb)
        IfileName.place(x = 220, y = 80, width = 250, height = 40)


        submitName = tk.Button(leb, text="Submit",
                               command=lambda: displayAS())
        submitName.place(x = 220, y = 140, width = 250, height = 40)

        asciiShown = tk.Text(leb, font=('Consolas', 10), wrap="none", borderwidth=0, width=64, height=14)
        asciiShown.place(x = 130, y = 215)        
        
        def displayAS():
            ab = 1
            fileName = IfileName.get()
            while ab == 1:
                try:
                    with open(f"{fileName}.txt") as f:
                        content = f.readlines()#Opens file
                    ab = 0
                except (FileNotFoundError, OSError):
                    noFile = tk.messagebox.showerror(title="No File", message="No file found - Please enter the name of the RLE file: ")
                    ab = 0
            content = [x.strip() for x in content]
            message = []
            f = open(f"{fileName}.txt")
            fileRead = f.read()
            message.append(''.join(fileRead))
            message = '\n'.join(message)

            
            asciiShown.insert('1.0', message)




        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: [controller.show_frame("MainMenu"), asciiShown.delete(1.0, tk.END)])
        mButton.place(x = 490, y = 532, width = 200, height = 30)    



class convToASCII(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.geometry = "700x575"
        self.geometry(frame.geometry)
        self.controller = controller
        label = tk.Label(self, text="Decompress To ASCII", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)


        leb = tk.Frame(self, height=250)
        leb.pack(expand=True, fill=tk.BOTH, pady=10)
        subLabel = tk.Label(leb, text="Please enter RLE file to decompress: ", fg="darkgreen", font=controller.title_fontSub)
        subLabel.place(x = 180, y = 10, width = 350, height = 40)

        IfileName = tk.Entry(leb)
        IfileName.place(x = 220, y = 80, width = 250, height = 40)


        submitName = tk.Button(leb, text="Submit",
                               command=lambda: decompressP())
        submitName.place(x = 220, y = 140, width = 250, height = 40)

        asciiShown = tk.Text(leb, font=('Consolas', 10), wrap="none", borderwidth=0, width=64, height=14)
        asciiShown.place(x = 130, y = 215)        
        

        def decompressP():
            fileName = IfileName.get()
            ab = 1
            while ab == 1:
                try:
                    with open(f"{fileName}.txt") as f:
                        content = f.readlines()#Opens file
                    ab = 0
                except (FileNotFoundError, OSError):
                    noFile = tk.messagebox.showerror(title="No File", message="No file found - Please enter the name of the RLE file: ")
                    ab = 0
            content = [x.strip() for x in content]
            message = []
            for i in range(0, len(content)):
                _line = []
                for x in range(0, len(content[i]), 3):
                    row = str(int(content[i][x:x + 2]) * content[i][x + 2])
                    _line.append(row)
                message.append(''.join(_line))
            message = '\n'.join(message)

            asciiShown.insert('1.0', message)





        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: [controller.show_frame("MainMenu"), asciiShown.delete(1.0, tk.END),])
        mButton.place(x = 490, y = 532, width = 200, height = 30)




class convToRLE(tk.Frame):
    def __init__(self, parent, controller):
        self.geometry = "700x575"
        self.geometry(frame.geometry)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Compress To RLE", fg="darkred", font=controller.title_fontmainTMenu)
        label.pack(side="top", fill="x", pady=10)
        
        leb = tk.Frame(self, height=250)
        leb.pack(expand=True, fill=tk.BOTH, pady=10)
        subLabel = tk.Label(leb, text="Please enter ASCII file to compress: ", fg="darkgreen", font=controller.title_fontSub)
        subLabel.place(x = 180, y = 10, width = 350, height = 40)

        IfileName = tk.Entry(leb)
        IfileName.place(x = 220, y = 80, width = 250, height = 40)


        submitName = tk.Button(leb, text="Submit",
                               command=lambda: compressP())
        submitName.place(x = 220, y = 140, width = 250, height = 40)

        asciiShown = tk.Text(leb, font=('Consolas', 10), wrap="none", borderwidth=0, width=78, height=14)
        asciiShown.place(x = 80, y = 215)        
        
        def compressP():
            fileName = IfileName.get()
            rle1 = []
            numletters = 0
            numletters1 = 0
            ab = 1
            while ab == 1:
                try:
                    with open(f"{fileName}.txt") as f:
                        content = f.readlines()#Opens file
                    ab = 0
                except (FileNotFoundError, OSError):
                    noFile = tk.messagebox.showerror(title="No File", message="No file found - Please enter the name of the RLE file: ")
                    ab = 0
                    fileName = IfileName.get()
            content = [x.strip() for x in content]
            for i in range(0,len(content)):
                    numletters1 += len(content[i])
                    count = 0
                    rle = ""
                    for x in range(1,len(content[i])):
                        count += 1
                        if content[i][x] != content[i][x-1]:
                            count1 = count
                            count = 0
                            if count1 < 10:
                                input1 = "0" + str(count1)
                            else:
                                input1 = str(count1)
                            rle = rle + (input1+content[i][x-1])
                    rle = rle + ("01"+content[i][len(content[i])-1])#Compresses data
                    numletters += len(rle)
                    rle1.append(rle)
                    rle1.append("\n")
            nameNewRLE = (f"{fileName} - COMPRESSED VERSION")
            file1 = open(f"{nameNewRLE}.txt","w+")
            for i in range(len(rle1)):
                file1.write(rle1[i])
            file1.close()
            message = f"\nThe Name Of Your Compressed File is '{nameNewRLE}.txt'\nThe Compressed (RLE) version of the original file contains {numletters} characters\n\
The Original uncompressed (ASCII) version of the file contains {numletters1} characters\n\
The difference in characters between the RLE file and the ASCII file is: {numletters1 - numletters}"
                    
            asciiShown.insert('1.0', message)

        mButton = tk.Button(self, text="Go to the Main Menu", fg="red",
                           command=lambda: [controller.show_frame("MainMenu"), asciiShown.delete(1.0, tk.END)])
        mButton.place(x = 490, y = 532, width = 200, height = 30)






if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()





