import tkinter as tk
from tkinter import simpledialog
import random

# Data Setup
ages = ['Teen', 'Young Adult', 'Adult', 'Elder']
full_time_jobs = ['Astronaut', 'Athlete', 'Business', 'Criminal', 'Culinary', 'Entertainer', 'Painter', 'Secret Agent', 'Tech Guru', 'Writer',
                  'Detective', 'Doctor', 'Scientist', 'Critic', 'Politician', 'Social Media', 'Veterinarian', 'Gardener', 'Florist', 'Actor',
                  'Education', 'Engineer', 'Law', 'Civil Designer', 'Freelancer', 'Animal Caretaker']
part_time_jobs = ['Barista', 'Fast Food Employee', 'Lifeguard', 'Retail', 'Babysitter']  # Part-time jobs for teens
aspirations = ['Bodybuilder', 'Painter Extraordinaire', 'Musical Genius', 'Bestselling Author', 'Public Enemy', 'Chief of Mischief',
               'Successful Lineage', 'Big Happy Family', 'Super Parent', 'Master Chef', 'Master Mixologist', 'Fabulously Wealthy',
               'Mansion Baron', 'Renaissance Sim', 'Nerd Brain', 'Computer Whiz', 'City Native', 'Serial Romantic', 'Soulmate',
               'Freelance Botanist', 'The Curator', 'Angling Ace', 'Outdoor Enthusiast', 'Jungle Explorer', 'Party Animal',
               'Friend of the World', 'Leader of the Pack', 'Good Vampire', 'StrangerVille Mystery', 'World-Famous Celebrity', 'Academic']
traits = ['Active', 'Ambitious', 'Art Lover', 'Bookworm', 'Bro', 'Cheerful', 'Clumsy', 'Creative', 'Dance Machine', 'Evil', 'Family-Oriented',
          'Foodie', 'Geek', 'Genius', 'Gloomy', 'Glutton', 'Good', 'Goofball', 'Hates Children', 'Hot-Headed', 'Insane', 'Jealous',
          'Kleptomaniac', 'Lazy', 'Loner', 'Loves Outdoors', 'Materialistic', 'Mean', 'Music Lover', 'Neat', 'Noncommittal', 'Outgoing',
          'Paranoid', 'Perfectionist', 'Romantic', 'Self-Assured', 'Slob', 'Snob', 'Squeamish', 'Unflirty']

# Functions
def generate_sim(number_of_sims):
    sims_info = ""
    for _ in range(number_of_sims):
        age = random.choice(ages)
        if age == 'Teen':
            job = random.choice(part_time_jobs)  # Teens get part-time jobs
            selected_traits = random.sample(traits, 2)  # Teens get two traits
        else:
            job = random.choice(full_time_jobs + part_time_jobs)  # Adults and others get full-time and part-time jobs
            selected_traits = random.sample(traits, 3)  # Other ages get three traits
        aspiration = random.choice(aspirations)
        sims_info += f"Age: {age}\nJob: {job}\nAspiration: {aspiration}\nTraits: {', '.join(selected_traits)}\n\n"
    result_label.config(text=sims_info)

def get_sims_number():
    number_of_sims = simpledialog.askinteger("Input", "How many Sims do you want to generate? (1-8)", minvalue=1, maxvalue=8)
    if number_of_sims is not None:  # Check if user did not cancel the input dialog
        generate_sim(number_of_sims)

def setup_window():
    global result_label
    window = tk.Tk()
    window.title("SIMply Random Generator")
    
    tk.Label(window, text="Welcome to the SIMply Random Household Generator!").pack(pady=10)
    tk.Button(window, text="Generate Sims", command=get_sims_number).pack(pady=5)
    
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)
    
    window.mainloop()

# Run the app
setup_window()