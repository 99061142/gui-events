import tkinter as tk
window = tk.Tk()


time = 20 # Starting value for the time
points = 0 # Starting value for the points


# Game over screen
def game_over():
    pass


# Edit the scoring table
def scoring_lbl():
    global time
    global points

    scoring_table_str = f'Time remaining: {time}               {points} points' # Text 
    scoring_table.configure(text=scoring_table_str) # Edit the scoring table


# Countdown to 0
def countdown():
    global time

    # If the user has time left
    if time >= 0:
        time -= 1 # Decrease the time
        scoring_lbl() # Change the time on the lable

        window.after(1000, countdown) # After every second this function is called again
    else:
        game_over() # Game over screen


# Starts the game
def start():
    start_button.destroy() # Destroy the start button
    countdown() # Starts the countdown


window.title('Simple FPS trainer') # Window title
window.geometry("500x300") # Window size
window.configure(bg="lightgray") # Window background


# Make the scoring table
scoring_table = tk.Label(
    window,
    bg="black",
    fg="white",
    font=('arial',15)
)

scoring_table.pack(fill='x')

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
    scoring_lbl()
    window.mainloop()