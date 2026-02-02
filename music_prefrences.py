# If you do not have pandas or matplotlib installed you will need to 
# install them in Terminal. Open VS Code, open Terminal and type: 
# py -m pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Input your dataset
data = {
    "Artist": [
        "Malcolm Todd", "Malcolm Todd", "Don Toliver", "Travis Scott", "Malcolm Todd",
        "Malcolm Todd", "TWICE", "Travis Scott", "TWICE", "TWICE",
        "Travis Scott", "Taylor Swift", "TWICE", "Malcolm Todd", "TWICE",
        "Malcolm Todd", "Taylor Swift", "TWICE", "Taylor Swift", "Taylor Swift",
        "Taylor Swift", "TWICE", "Taylor Swift", "Travis Scott", "Taylor Swift",
        "Malcolm Todd"
    ],

    "Genre": [
        "Pop", "Classical", "Rap", "Rap", "Pop",
        "Classical", "Pop", "Rap", "Pop", "Pop",
        "Rap", "Hip-Hop", "Hip-Hop", "Pop", "Pop",
        "Hip-Hop", "Rap", "Pop", "Hip-Hop", "Pop",
        "Pop", "Pop", "Pop", "Pop", "Pop",
        "Hip-Hop"
    ],

    "HoursPerDay": [
        2, 5, 1, 1, 3,
        4, 2, 5, 1, 1,
        4, 5, 5, 3, 5,
        1, 5, 3, 1, 3,
        3, 2, 3, 3, 3,
        1
    ],

    # If you really want a space in the column name, you must use the same string later
    "Time of Day Listened": [
        "Night", "Midnight", "Night", "Evening", "Night",
        "Night", "Night", "Evening", "Morning", "Evening",
        "Evening", "Midnight", "Evening", "Evening", "Evening",
        "Evening", "Midnight", "Evening", "Afternoon", "Morning",
        "Morning", "Night", "Afternoon", "Evening", "Night",
        "Night"
    ],

    # You were using df["Grade"] in the scatter but never defined Grade.
    # Here’s an example Grade list for 26 students:
    "Grade": [
        9, 10, 11, 12, 9,
        10, 11, 12, 9, 10,
        11, 12, 9, 10, 11,
        12, 9, 10, 11, 12,
        9, 10, 11, 12, 9,
        10
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("Music Preference Dataset (26 Students):")
print(df)

# Bar Graph of Genres
# ---------------------------
genre_counts = df["Genre"].value_counts()

plt.figure()
genre_counts.plot(kind="bar", color="skyblue")
plt.title("Favorite Music Genres (26 Students)")
plt.xlabel("Genre")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# Scatter Plot - Grade vs HoursPerDay
# ---------------------------
plt.figure()
plt.scatter(df["Grade"], df["HoursPerDay"], color="green")
plt.xlabel("Grade Level")
plt.ylabel("Music Listened Per Day (Hours)")
plt.title("Music Listened vs Grade Level")
plt.grid(True)
plt.tight_layout()
plt.show()