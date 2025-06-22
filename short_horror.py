from gtts import gTTS
import os
import tkinter as tk
import random

root = tk.Tk()
root.title("👻 Horror Story Generator")
root.geometry("800x500+200+100")
root.config(bg="#1E1E1E")
root.resizable(False, False)

# Header
header_frame = tk.Frame(root, width=800, height=70, bg="#2E2E2E")
header_frame.place(x=0, y=0)

title_label = tk.Label(header_frame, text="🩸 SHORT HORROR STORY 🕯️", font=("Chiller", 28, "bold"), bg="#2E2E2E", fg="#FF3C38")
title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

divider = tk.Frame(root, bg="#FF3C38", height=5, width=800)
divider.place(x=0, y=70)

# Horror Stories
stories = [ """The Birthday Call
I got a call from my grandmother on my birthday. She sang the same song she used to when I was a child—sweet and off-key.
The thing is, she died last year, and I had personally scattered her ashes by the lake.
I checked the caller ID—it was her old landline. Confused, I visited her house out of impulse,
only to find the phone off the hook, swinging slowly. On the table was a fresh cake, my name written in her handwriting.
Beside it was a note: 'Don’t forget to blow out the candles before he comes.'
And I swear I saw candlelight flickering in the dark hallway behind me.""" , 

"""Under the Floorboards
My wife always complained about the creaking floors, so I finally agreed to fix them.
As I pulled up the planks, I noticed a hollow compartment—something not in the house blueprints.
Inside was a small, locked box and hundreds of deep scratches across the wood, like someone had tried to claw their way out.
I cracked the box open to find a bundle of photos—all of me, sleeping, eating, showering… taken from impossible angles.
On the back of one photo was written: “Almost done learning how to be you.” Since then,
I’ve started hearing noises at night—my voice whispering from underneath the bed. I haven’t dared to look yet.""",

"""The Reflection
I was brushing my teeth when I noticed something strange in the mirror. My reflection was slightly out of sync,
lagging by a second as if buffering real life. I turned away, heart racing,
and watched it continue brushing for a moment before freezing and smiling. That night,
every mirror in the house was cracked down the center, except the one in the bathroom.
In it, the reflection now moves only when I’m not looking. I covered it with a towel. In the morning,
the towel was gone, and written on the glass in condensation was: “Let me out.”""",

"""The Lost Voice Message
My phone lit up with a voice message while I was in the shower. I played it back expecting a spam call,
but what I heard made me freeze—my own voice, screaming for help, crying and begging. The voice on the recording was me,
and it was unmistakably recent, wearing the same words I said to my friend yesterday.
I ran outside, panicking, and as I passed a mirror by the hallway, I caught my reflection… but it wasn’t screaming.
It was smiling. That version of me hasn’t stopped mimicking everything I do—but now he’s started blinking at different times.""",

"""The Last Photo
Scrolling through old photos on my camera roll, I noticed one I didn’t take—me sleeping, timestamped last night.
I live alone, in a locked apartment with no windows near my bed. I checked the angle, confused, 
then noticed something in the corner. A shadowy figure, blurry and mid-motion, half-phased into the wall. 
I deleted it in panic, but it kept reappearing every time I opened the gallery, closer each time. Now,
I can feel breathing at my neck while I sleep. This morning, a new photo appeared: I was awake in bed,
looking directly at the camera—and I don’t remember posing."""
]

story_text = tk.Text(root, font=("Chiller", 18), wrap="word", bg="#2B2B2B", fg="#FFFFFF", bd=4, relief=tk.RIDGE, insertbackground="#FF3C38", padx=10, pady=10)
story_text.place(x=50, y=90, width=700, height=290)

def tell_story():
    story = random.choice(stories)
    story_text.delete("1.0", tk.END)
    story_text.insert(tk.END, story)

def speak_story():
    story = story_text.get("1.0", tk.END).strip()
    if story:
        tts = gTTS(text=story, lang='en')
        tts.save("story.mp3")
        os.system("afplay story.mp3")
        os.remove("story.mp3")

btn_frame = tk.Frame(root, bg="#1E1E1E", width=600, height=50)
btn_frame.place(x=150, y=400)

tell_button = tk.Button(btn_frame, text="🔮 Tell Me a Story", font=("Chiller", 16, "bold"), bg="#A40606", fg="#FFFFFF", padx=20, pady=10, command=tell_story)
tell_button.place(x=0, y=0)

speak_button = tk.Button(btn_frame, text="🔊 Speak", font=("Chiller", 16, "bold"), bg="#A40606", fg="#FFFFFF", padx=20, pady=10, command=speak_story)
speak_button.place(x=280, y=0)

footer = tk.Label(root, text="Built in the dark... with Python & ChatGPT ☠️", font=("Arial", 10), bg="#1E1E1E", fg="#888")
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()