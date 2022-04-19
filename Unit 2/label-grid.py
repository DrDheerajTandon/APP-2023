from tkinter import *
window = Tk()
window.title('Label Using Pack')
window.geometry('300x400')
label = Label(window,text='Hello')
label.pack(side='bottom')
window.mainloop()