import tkinter as tk
from random import choice
window = tk.Tk()


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


# Edit the scoring table
def scoring_label():
    global time
    global points

    scoring_table_str = f'Time remaining: {time}               {points} points' # Text 
    label.configure(text=scoring_table_str) # Edit the scoring table


# Countdown to 0
def countdown():
    global time

    # If the user has time left
    if time >= 0:
        time -= 1 # Decrease the time
        scoring_label() # Change the time on the lable

        window.after(1000, countdown) # After every second this function is called again
    else:
        game_over() # Game over screen


# Get a random keybind the user must make (with keyboard or click x amount of times on the button)
def random_keybind():
    events = list(keybinds.keys())
    event = choice(events)
    random_bind = choice(keybinds[event])

    # If the keybind is for the keyboard
    if event == "keyboard":
        text = 'press ' + random_bind
    
    # If the keybind is for the button
    else:
        text = random_bind['text']


    # Make a button on a random position with the text what the user must do
    test = tk.Button(
        window, 
        font=("arial", 15), 
        width=20,
        text=text
    )

    test.pack(expand=True)


# Starts the game
def start():
    start_button.destroy() # Destroy the start button
    countdown() # Starts the countdown
    random_keybind()

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




# If the code starts
if __name__ == "__main__":
    scoring_label()
    window.mainloop()