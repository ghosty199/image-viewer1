from tkinter import*
from tkinter import filedialog
import random
root=Tk()
from PIL import Image, ImageTk
root.geometry("500x500")
root.title("image viewer")
root.configure(background = "black")

label_image = Label(root, bg="white", highlightthickness=500)
label_image.place(relx=0.5, rely=0.4, anchor=CENTER)
img=ImageTk.PhotoImage(Image.open("jupiter.jpg"))




img_path=""



def open_image():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])    
    print(img_path)
    im=Image.open( img_path )
    img=ImageTk.PhotoImage(im)
    label_image["image"]=img
    
    
    

button1=Button(root,text="open image",command=open_image)
button1.place(relx=0.5, rely=0.1, anchor=CENTER)


button2=Button(root,text="rotate image", command=rotate_image)
button2.place(relx=0.5, rely=0.9, anchor=CENTER)






























root.mainloop()