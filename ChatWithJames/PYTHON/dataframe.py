import pandas as pd

michael_jordan = {
    "Name": "Michael Jordan",
    "Nickname": "Air Jordan",
    "Number": 23,
    "Position": "Shooting Guard",
    "Height_m": 1.98,
    "Weight_kg": 98,
    "Birth_Date": "1963-02-17",
    "NBA_Championships": 6,
    "MVP_Awards": 5,
    "All_Star": 14,
    "Career_PPG": 30.1,
    "Career_RPG": 6.2,
    "Career_APG": 5.3,
    "Career_FG_Percent": 49.7
}

df = pd.DataFrame([michael_jordan])

print(df)
