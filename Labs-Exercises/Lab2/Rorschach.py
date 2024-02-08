import os 
import random
import csv
from PIL import Image
import pandas as pd
# read with pandas
class Rorschach:
    def choose_image():
        file = random.choice(os.listdir(r"/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Lab2/Images"))
        image = Image.open(f"/Users/daniel/Documents/GitHub/Harp151/Labs-Exercises/Lab2/Images/{file}", "r")
        image.show()
        return file
    

    def user_store_input():
        user_input = input("Tell me what you think about these images:")
        csv_file = open("Rorscach_Input.csv", "w", newline="", encoding="utf-8")    # creating csv
        csv_writer = csv.writer(csv_file), 
        csv_writer.writerow(["USER NAME", "USER INPUT"]) # first time creates columns, second times populates columns
        csv_file.close()

    if __name__ == "__main__":
        # for x in range(0,5):
            # choose_image()
            user_store_input()
    # get user input about images (after they open) => stores input in CSV files