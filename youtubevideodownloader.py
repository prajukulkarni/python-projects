from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")
#root.configure(bg='light pink')
root['background']= '#856ff9'

Label(root, text="YouTube Video Downloader", font='callibary 20 bold').pack()

link = StringVar()

Label(root, text="Paste Link Here:" , font='times 20 bold').place(x=160 ,  y=60)

link_enter = Entry(root, width=57 , textvariable= link) .place(x=32 , y=90)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()

    Label(root, text='DOWNLOADED' , font='callibary  15') .place(x=180 , y=210)
Button(root, text='Download' , font='callibary 20 bold' , bg='cyan' , padx=2 , command=Downloader) .place(x=180 , y = 150)

root.mainloop()
    

 
