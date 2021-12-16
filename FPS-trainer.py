import tkinter as tk
import random


# Make the window
window = tk.Tk() # Start the window
window.title('Simple FPS trainer') # Window title
window.geometry("500x300") # Window size
window.configure(bg="lightgray") # Window background


# Keybinds for the keyboard / button
keybinds = {
    'keyboard': ['w', 'a', 's', 'd', 'space'],
    'button': [
        {'text': 'single-click', 'bind': 'Button-1'}, 
        {'text': 'double-click', 'bind': 'Double-Button-1'}, 
        {'text': 'triple-click', 'bind': 'Triple-Button-1'}
    ]
}


time = 20 # Starting value for the time
points = 0 # Starting value for the points
button = None


# Game over screen
def game_over():
    pass


def add_points(event):
    global points # Points on the scoreboard

    bind = event.keysym.lower() # Bind 

    # Check how many points must be added, and unbind the bind
    if bind in keybinds['keyboard']:
        points += 1 
        window.unbind(f"<{bind}>")

    else:
        points += 2
        button.unbind(f"<{bind}>")


    button.destroy() # Destroy the button

    scoring_label() # Update the points in the scoreboard
    random_keybind() # Add a new random button


# Edit the scoreboard
def scoring_label():
    global time
    global points

    scoreboard_str = f'Time remaining: {time}               {points} points' # Text 
    scoreboard.configure(text=scoreboard_str) # Edit the scoreboard


# Countdown to 0
def countdown():
    global time

    # If the user has time left
    if time > 0:
        time -= 1 # Decrease the time
        scoring_label() # Change the time on the lable

        window.after(1000, countdown) # After every second this function is called again
    else:
        game_over() # Game over screen


# Get a random keybind the user must make (with keyboard or click x amount of times on the button)
def random_keybind():
    global button # Button where the user can read what the bind is

    events = list(keybinds.keys()) # Make a list of the possible bind options
    event = random.choice(events) # Choose if its a keyboard or a button bind

    bind = random.choice(keybinds[event]) # Choose a random bind 


    # If the event is for the keyboard
    if event == "keyboard":
        text = f"press {bind}" # Text inside the button
        bind = f"<{bind}>" # Bind for the keyboard

    # If the event is for the button
    else:
        text = bind['text'] # Text inside the button
        bind = f"<{bind['bind']}>" # Bind for the button


    # Make a button on a random position with the text what the user must do
    bind_button = tk.Button(
        window, 
        font=("arial", 15), 
        width=20
    )
    

    scoreboard_height = scoreboard.winfo_height() # Height of the scoreboard


    width = random.randrange(scoreboard_height, window.winfo_width() // 2) # Random width position
    height = random.randrange(scoreboard_height * 2, window.winfo_height() // 4 * 3) # Random height position

    bind_button.place(x=width, y=height) # Add the button to the window


    # If the keybind is for the keyboard
    if event == "keyboard": 
        bind_button['text'] = text # Text inside the button
        window.bind(bind, add_points) # Bind for the points

    # If the keybind is for the button
    else:
        bind_button['text'] = text # Text inside the button
        bind_button.bind(bind, add_points) # Bind for the points

    button = bind_button # Add the created button to the global button 

# Starts the game
def start():
    start_button.destroy() # Destroy the start button
    countdown() # Starts the countdown
    random_keybind() # Add a random button


# Make the scoreboard
scoreboard = tk.Label(
    window,
    bg="black",
    fg="white",
    font=('arial',15)
)

scoreboard.pack(fill='x')

# Make the button to start the game
start_button = tk.Button(
    window, 
    font=("arial", 15), 
    width=20,
    text='Press here to start',
    command=start
)

start_button.pack(expand=True)




# If the code starts
if __name__ == "__main__":
    scoring_label()
    window.mainloop()