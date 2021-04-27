import tkinter as tk
from PIL import Image, ImageTk
from SQLinteractions import retrieve_pass
from functools import partial
	
def main():
    config= {'title':"Passwordinator",        #this was so helpful in doing multiple arguments!
             'canWidth':'800',                      #https://www.geeksforgeeks.org/python-passing-dictionary-as-arguments-to-function/
	     'canHeight':'400',
	     'numCol': '1',
	     'numRow': '5',
	             }
    root = tk.Tk()
    mainwindow= window(root,**config)
    return None
	
def promptChanger(root, canvas, prompttxt, buttontxt):
    #prompt#
    prompt= tk.StringVar()
    prompt_label= tk.Label(root, text= prompttxt)
    prompt_label.grid(column=0, row=0)
	    
    #entry#
    entry= tk.Entry(root)
    canvas.create_window(200,100, window=entry)
    entry.grid(column= 0, row= 1)

    #button#
    button_text= tk.StringVar()
    button = tk.Button(root, textvariable= button_text, command= partial(getInput,root,entry))
    button_text.set(buttontxt)
    button.grid(column= 0, row= 2)
    print(entry.get())
	 
	    
def getInput(root, entry):
    entryinput= entry.get()
    clear= entry.delete(0, 'end')
    return entryinput
	            
def findPass():
    root= tk.Tk()
    config= {'title':"Generating new pass...",        
	             'canWidth':'400',                      
	             'canHeight':'200',
	             'numCol': '1',
	             'numRow': '3',
	             'prompt1': '',
	             'prompt2': '',
	             }
    winTitle= config.get('title')
    winWidth = config.get('canWidth')
    winHeight = config.get('canHeight')
    winCol= config.get('numCol')
    winRow= config.get('numRow')
    root.title(winTitle)
    root.geometry("{}x{}".format(winWidth,winHeight))
    canvas= tk.Canvas(root)
    canvas.grid(columnspan = winCol, rowspan= winRow) 
	######### end setup ##############    
    searchReady=False
    searchParameters=[]
    #labelchanger#
    if not searchReady:
        if len(searchParameters) == 0:
            prompt1= promptChanger(root, canvas, "Enter Email Please", "Enter")
            print(prompt1)
            searchParameters.append(prompt1)
            print(searchParameters)

class window():
    def __init__(self, root, title,canWidth,canHeight, numCol, numRow):
        root = root
        winTitle= title
        winWidth = canWidth
        winHeight =canHeight
        winCol= numCol
        winRow= numRow
        self.root=  root
        self.root.title(title)
        self.root.geometry("{}x{}".format(canWidth,canHeight))
        self.root.canvas= tk.Canvas(root)
        self.root.grid= self.root.canvas.grid(columnspan = numCol, rowspan= numRow)

        
        logoimg = ImageTk.PhotoImage(Image.open("passwordinator logo.png"))
        logoLabel = tk.Label(image = logoimg)
        logoLabel.image = logoimg
        logoLabel.grid(column=1,row=0)

        #self.logoLabel.grid(
        
        
	##New Account button##
        NewAccount_button= self.root.button=Button(root,'New Account',1,2,findPass)
	##Reset Pass button##
        ResetPass_button= self.root.button=Button(root,'Reset Password', 1,3,findPass)
	 
	##Find a pass button##
        FindPass_button= self.root.button=Button(root, 'Find a Password', 1,4,findPass)

	        
	 ###############STAY LAST##############
        self.root.mainloop()
	
class Button:
    def __init__(self,root,buttonname, colPos, rowPos, command): #maybe add function?
        self.root = root
        button_text= tk.StringVar()
        button = self.button = tk.Button(root, textvariable= button_text, command= lambda:command(),bg= "#8946e7", fg="#FFFFFF")
        button_text.set(buttonname)
        button.grid(column= colPos, row= rowPos)
        #self.root.StringVar() ##idk if i need to add tk
	        
main()
