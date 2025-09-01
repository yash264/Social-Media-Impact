import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

n = 10000  

# Categories with weights
genders = ["Male", "Female", "TransGender"]
gender_weights = [0.55, 0.40, 0.05]  

professions = ["Student", "Engineer", "Doctor", "Teacher", "Business", "Artist"]
profession_weights = [0.30, 0.20, 0.10, 0.12, 0.18, 0.10]  

device_types = ["Mobile", "Laptop", "Tablet", "Desktop"]
device_weights = [0.5, 0.25, 0.15, 0.10] 

locations = ["USA", "India", "UK", "Canada", "Australia", "Germany"]
location_weights = [0.15, 0.35, 0.10, 0.15, 0.15, 0.10] 

addiction_levels = ["Low", "Medium", "High", "Severe"]
addiction_weights = [0.2, 0.4, 0.3, 0.1]

platforms = ["Instagram", "Facebook", "YouTube", "TikTok", "Twitter", "Reddit"]
platform_weights = [0.25, 0.15, 0.25, 0.15, 0.10, 0.10]  

effects = ["Anxiety", "Depression", "Sleep Issues", "Cyberbullying", "Reduced Productivity", "No Effect"]
effect_weights = [0.20, 0.15, 0.25, 0.10, 0.20, 0.10] 


# Generate dataset
data = {
    "UserID": [i for i in range(1, n+1)],
    "Gender": [random.choices(genders, weights=gender_weights, k=1)[0] for _ in range(n)],
    "Age": [random.randint(10, 60) for _ in range(n)],
    "Location": [random.choices(locations, weights=location_weights, k=1)[0] for _ in range(n)],
    "Profession": [random.choices(professions, weights=profession_weights, k=1)[0] for _ in range(n)],
    "DeviceType": [random.choices(device_types, weights=device_weights, k=1)[0] for _ in range(n)],
    "SessionTime(min)": [random.randint(5, 180) for _ in range(n)],   
    "DailyUsage(hrs)": [round(random.uniform(0.5, 10), 1) for _ in range(n)],
    "VideosWatched": [random.randint(0, 30) for _ in range(n)],
    "AddictionLevel": [random.choices(addiction_levels, weights=addiction_weights, k=1)[0] for _ in range(n)],
    "Income($)": [random.randint(200, 5000) for _ in range(n)],
    "PrimaryPlatform": [random.choices(platforms, weights=platform_weights, k=1)[0] for _ in range(n)],
    "HarmfulEffect": [random.choices(effects, weights=effect_weights, k=1)[0] for _ in range(n)],
    "ProductivityScore(1-10)": [random.randint(1, 10) for _ in range(n)],
    "Date": [fake.date_between(start_date="-6M", end_date="today") for _ in range(n)]
}


df = pd.DataFrame(data)

df.to_excel("social_media_data.xlsx", index=False, engine="openpyxl")

print("Excel file generated sucessfully.")
print(df.head())


