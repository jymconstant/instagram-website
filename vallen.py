import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame

# Initialize music
try:
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")  # Optional music file
    pygame.mixer.music.play(-1)
except:
    pass  # If no music file, continue without music

root = tk.Tk()
root.title("Valentine Surprise 💖")
root.geometry("600x700")
root.configure(bg="#ffccd5")

canvas = tk.Canvas(root, width=600, height=700, bg="#ffccd5", highlightthickness=0)
canvas.pack()

# Draw gift box
box_base = canvas.create_rectangle(200, 350, 400, 500, fill="#ff4d6d", outline="")
box_lid = canvas.create_rectangle(190, 320, 410, 370, fill="#c9184a", outline="")
ribbon_v = canvas.create_rectangle(285, 350, 315, 500, fill="white", outline="")
ribbon_h = canvas.create_rectangle(200, 410, 400, 440, fill="white", outline="")

text = canvas.create_text(300, 550, text="🎁 Click the Gift 🎁", font=("Comic Sans MS", 20, "bold"), fill="#800f2f")

hearts = []

def create_heart():
    x = random.randint(50, 550)
    heart = canvas.create_text(x, 700, text="💖", font=("Arial", random.randint(15, 25)))
    hearts.append(heart)

def animate_hearts():
    for heart in hearts:
        canvas.move(heart, 0, -3)
        pos = canvas.coords(heart)
        if pos[1] < 0:
            canvas.delete(heart)
            hearts.remove(heart)
    if random.random() < 0.2:
        create_heart()
    root.after(50, animate_hearts)

def open_gift(event):
    canvas.delete(text)

    # Animate lid opening
    for i in range(30):
        canvas.move(box_lid, 0, -3)
        root.update()
        root.after(20)

    # Show image
    img = Image.open("lyn.jpg")
    img = img.resize((300, 300))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo, bg="#ffccd5")
    img_label.image = photo
    img_label.place(x=150, y=50)

    # Love message
    love_msg = tk.Label(
        root,
        text="💘 Happy belated Valentine's lyn 💘\nYou make my world beautiful!",
        font=("Comic Sans MS", 22, "bold"),
        fg="#d00000",
        bg="#ffccd5"
    )
    love_msg.place(x=60, y=370)

canvas.bind("<Button-1>", open_gift)

animate_hearts()
root.mainloop()
