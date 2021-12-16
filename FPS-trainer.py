import tkinter as tk
from random import choice


# Make the window
window = tk.Tk() # Start the window
window.title('Simple FPS trainer') # Window title
window.geometry("500x300") # Window size
window.configure(bg="lightgray") # Window background


# Make the scoring table
label = tk.Label(
    window,
    bg="black",
    fg="white",
    font=('arial',15)
)

label.pack(fill='x')

# Make the button to start the game
start_button = tk.Button(
    window, 
    font=("arial", 15), 
    width=20,
    text='Press here to start',
    command=start
)

start_button.pack(expand=True)


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


# Game over screen
def game_over():
    pass


def add_points(event):
    global points

    bind = event.keysym.lower()

    # Add points to the scoreboard (+1 = keyboard +2 = button)
    points += 1 if bind in keybinds['keyboard'] else 2


    scoring_label() # Update the points in the label

    random_keybind() # Add a new random button


# Edit the scoring table
def scoring_label():
    global time
    global points

    scoreboard_str = f'Time remaining: {time}               {points} points' # Text 
    label.configure(text=scoreboard_str) # Edit the scoring table


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
    events = list(keybinds.keys()) # Make a list of the possible bind options
    event = choice(events) # Choose if its a keyboard or a button bind

    bind = choice(keybinds[event]) # Choose a random bind 
    
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

    bind_button.pack(expand=True)

    # If the keybind is for the keyboard
    if event == "keyboard": 
        bind_button['text'] = text # Text inside the button
        window.bind(bind, add_points) # Bind for the points

    # If the keybind is for the button
    else:
        bind_button['text'] = text # Text inside the button
        bind_button.bind(bind, add_points) # Bind for the points


# Starts the game
def start():
    start_button.destroy() # Destroy the start button
    countdown() # Starts the countdown
    random_keybind() # Add a random button




# If the code starts
if __name__ == "__main__":
    scoring_label()
    window.mainloop()