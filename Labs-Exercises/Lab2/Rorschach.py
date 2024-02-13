import os 
import random
import csv
from PIL import Image

# read with pandas
class Rorschach_User_Image:

    def choose_image(self):
        file = random.choice(os.listdir(r"/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Lab2/Images"))
        image = Image.open(f"/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Lab2/Images/{file}", "r")
        image.show()
        return file
    
    def csv_input(self):
        csv_file = open("Rorscach_Input.csv", "w", newline="", encoding="utf-8")    # creating csv
        csv_writer = csv.writer(csv_file) 
        csv_writer.writerow(["RESPONSE NUMBER ", "NAME ", " INPUT"]) 

        for i in range(5):
             name = input("What is your name:\n")
             user_input = input("Tell me what you think about these images:\n")
             csv_writer.writerow([i + 1, name, user_input])
        csv_file.close

run = Rorschach_User_Image()
run.choose_image()
run.csv_input()