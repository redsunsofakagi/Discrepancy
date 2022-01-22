import time
import threading

import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()

# Tested with .jpg and .png
IMAGE_PATH = "Scene1.png"

# Create a pillow image and a tkinter image. convert to RGBA to add alpha channel to image
image = Image.open(IMAGE_PATH).convert("RGBA")
image_tk = ImageTk.PhotoImage(image)

# We'll fade to whatever the background is here (black, white, orange, etc)
label = tkinter.Label(root, image=image_tk, bg="black")
label.pack()

'''def fade_image():
    global image, image_tk, label
    # Walk backwards through opacities (255 is opaque, 0 is transparent)
    for i in range(255, 0, -5):
        image.putalpha(i) # Set new alpha
        image_tk = ImageTk.PhotoImage(image) # Cretae new image_tk
        label.configure(image=image_tk)
        label.update()
        label.pack(side='top')
        # Sleep some time to make the transition not immediate
        time.sleep(0.01)
    
# Put image fading in a thread so it doesn't block our GUI
fade_thread = threading.Thread(target=fade_image)
tkinter.Button(root, text="Fade To Black", command=fade_thread.start).pack()
'''
for i in range(255, 0, -5):
        image.putalpha(i) # Set new alpha
        image_tk = ImageTk.PhotoImage(image) # Cretae new image_tk
        label.configure(image=image_tk)
        label.update()
        label.pack(side='top')
        # Sleep some time to make the transition not immediate
        time.sleep(0.01)
root.mainloop()
