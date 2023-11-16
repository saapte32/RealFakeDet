import tkinter as tk
import pickle
import csv
import sklearn
import numpy as np


from tkinter import ttk

def has_numbers(inputString):
    if any(char.isdigit() for char in inputString):
        return 1
    else:
        return 0

def convert(string):
    if string == 'yes':
        return 1
    else:
        return 0
def classify_profile():
    # Add model classification logic here
    # Obtain the values of various input parameters
    username = username_var.get()
    fullname = fullname_var.get()
    url = convert(url_var.get())
    is_business = convert(is_private_var.get())
    joined_recently = convert(joined_recently_var.get())
    is_private = convert(is_private_var.get())
    followers = int(followers_var.get())
    following = int(following_var.get())
    total = followers + following
    
    filename = 'C:/Users/Admin/Documents/Uni/capstone/rf_model.sav'
    model = pickle.load(open(filename,'rb'))
    if(len(fullname) == 0):
        fullname = "a"
    if (total == 0):
        total = 1
    array = np.array([[(followers/total),(following/total),len(username),has_numbers(username),has_numbers(fullname), len(fullname), is_private, joined_recently, is_business, url]])
    # Call your model here and output the results
    result = model.predict(array)
    print(result)
    print("Model output results: real users" if result == 0 else "Model output result: false user")

# Creating Main Windows
root = tk.Tk()
root.title("Profile Classification")

# Create and place various interface elements

username_label = ttk.Label(root, text="Username:")
username_var = tk.StringVar(value="")
username_entry = ttk.Entry(root, textvariable=username_var)

fullname_label = ttk.Label(root, text="Fullname:")
fullname_var = tk.StringVar(value="")
fullname_entry = ttk.Entry(root, textvariable=fullname_var)

url_label = ttk.Label(root, text="URL? (yes/no):")
url_var = tk.StringVar(value="yes")
url_entry = ttk.Entry(root, textvariable=url_var)

is_private_label = ttk.Label(root, text="Is it a private account? (yes/no):")
is_private_var = tk.StringVar(value="yes")
is_private_entry = ttk.Entry(root, textvariable=is_private_var)

joined_recently_label = ttk.Label(root, text="have they joined instagram recently? (yes/no):")
joined_recently_var = tk.StringVar(value="yes")
joined_recently_entry = ttk.Entry(root, textvariable=joined_recently_var)

is_business_label = ttk.Label(root, text="is this a business account? (yes/no):")
is_business_var = tk.StringVar(value="yes")
is_business_entry = ttk.Entry(root, textvariable=is_business_var)

followers_label = ttk.Label(root, text="Number of followers:")
followers_var = tk.StringVar(value="")
followers_entry = ttk.Entry(root, textvariable=followers_var)

following_label = ttk.Label(root, text="Number of following:")
following_var = tk.StringVar(value="")
following_entry = ttk.Entry(root, textvariable=following_var)

classify_button = ttk.Button(root, text="Classify Profile", command=classify_profile)

is_business_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
is_business_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

username_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

fullname_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
fullname_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

url_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
url_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

is_private_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
is_private_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

followers_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
followers_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

following_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
following_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

joined_recently_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
joined_recently_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

classify_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start main event loop
root.mainloop()
