import tkinter as tk

class OnlinePoemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Online Literary Works")

        # Set background and foreground colors
        fg_color = "#FFFFFF"  # White background
        bg_color = "#008000"  # Green text
        

        # Title label
        tk.Label(master, text="Online Literary Works", font=("Times New Roman", 16), bg="green", fg=fg_color).pack(pady=10)

        # Frame for writer selection
        writer_frame = tk.Frame(master, bg="yellow green")
        writer_frame.pack()

        # Writer label
        tk.Label(writer_frame, text="Select Writer:", bg="yellow green", fg=fg_color, font="Arial").grid(row=0, column=0)

        # Dropdown menu for selecting writer
        self.writer_var = tk.StringVar(master)
        self.writer_var.set("Select Writer")  # Default value
        self.writers = ["Thyrone Glenn"]
        writer_menu = tk.OptionMenu(writer_frame, self.writer_var, *self.writers)
        writer_menu.config(bg="yellow green", fg=fg_color, font="Arial")  # Set background and foreground colors for the menu
        writer_menu.grid(row=0, column=1)

        # Frame for poem selection
        poem_frame = tk.Frame(master, bg="yellow green")
        poem_frame.pack(pady=10)

        # Poem label
        self.poem_label = tk.Label(poem_frame, text="Select Poem/Speech:", bg="yellow green", fg=fg_color, font="Arial")
        self.poem_label.grid(row=0, column=0)

        # Dropdown menu for selecting poem
        self.poem_var = tk.StringVar(master)
        self.poem_var.set("Select Poem/Speech")  # Default value
        self.poem_menu = tk.OptionMenu(poem_frame, self.poem_var, "")
        self.poem_menu.config(bg="yellow green", fg=bg_color,font="Arial")  # Set background and foreground colors for the menu
        self.poem_menu.grid(row=0, column=1)

        # Button to read selected poem
        tk.Button(master, text="Read Poem/Speech", command=self.read_poem, bg="yellow green", fg=fg_color,font="Arial").pack(pady=10,padx=5)

        # Label to display selected poem
        self.poem_display_label = tk.Label(master, text="", bg="green", fg=fg_color,font="Arial", wraplength=400, justify="left")
        self.poem_display_label.pack(pady=10)

        # Dictionary to store poems of each writer
        self.writer_poems = {
            "Thyrone Glenn": {  
                "The Poem of Love": ("""
In your eyes, like sparkling stars, I see,
A love that sets my weary heart so free.
In every glance, a tale of destiny,
That binds us close, in sweet serenity.

Your love, a beacon in the darkest night,
Guiding me through shadows, into light.
With every touch, you make my spirit soar,
And fill my world with joy forevermore.

Each day, I feel the depth of your embrace,
A river of love, a boundless grace.
In your presence, I find my truest bliss,
A treasure trove of love, sealed with a kiss.

So precious to me, your love divine,
A gift from heaven, forever mine.
Together, we'll walk this earthly plane,
Bound by love's eternal, unbroken chain.

In your heart, I find my sacred home,
Where I am cherished, never alone.
No flower's scent could match the love you bring,
As vast as the sky, as endless as the spring.

So let us journey, hand in hand,
Through life's twists and turns, across the land.
For in your love, I've found my truest friend,
A love that knows no bounds, until the very end.
"""),
                "Special Occasion Speech": ("""
Ladies and gentlemen, welcome! Today, amidst the joy and camaraderie, I stand before you with a heart full of gratitude. Your presence and support have made this occasion truly special. Together, we embark on a journey of love and unity, nurturing the bonds that bring us together as families and friends.

As we gather here today, let us acknowledge the hurdles we've overcome to reach this moment. Despite the challenges, we've persevered, drawing strength from each other and our shared commitment to celebrating life's milestones. Our resilience shines through as a testament to the power of love and determination.

In the tapestry of life, this celebration stands as a vibrant thread, woven with the memories we create and the dreams we aspire to achieve. It's a reminder of the blessings we've been bestowed and the prosperity we cultivate as a community. Together, we honor the past, embrace the present, and look forward to a future filled with hope and promise.

Thank you all for being a part of this special occasion. May our hearts be filled with joy and our spirits lifted high as we revel in the beauty of this moment.
""")
            },
            "Writer 1": {
                "The Poem of Love": ""
            },
            "Writer 2": {
"Special Occasion Speech": ""
            }
            
            }
        

        # Update poems menu based on writer selection
        self.writer_var.trace("w", self.update_poems)

    def update_poems(self, *args):
        writer = self.writer_var.get()
        self.poem_label.config(text="Select Poem/Speech:")
        self.poem_var.set("Select Poem/Speech")  # Reset to default value
        menu = self.poem_menu["menu"]
        menu.delete(0, "end")  # Clear previous items
        
        if writer in self.writer_poems:
            poems = list(self.writer_poems[writer].keys())
            for poem in poems:
                menu.add_command(label=poem, command=lambda p=poem: self.poem_var.set(p))

    def read_poem(self, *args):
        writer = self.writer_var.get()
        poem_title = self.poem_var.get()
        poem_text = self.writer_poems.get(writer, {}).get(poem_title, "")
        if writer != "Select Writer" and poem_title != "Select Poem/Speech":
            self.poem_display_label.config(text=poem_text)
        else:
            self.poem_display_label.config(text="Please select a writer and a poem first.")

root = tk.Tk()
root.config(bg="green")
app = OnlinePoemGUI(root)
root.mainloop()