#If you do not have pandas or matplotlib installed you will need to 
#import pandas in Terminal.  Open VS Code, open Terminal and type: 
#py -m pip install pandas matplotlib


import pandas as pd
import matplotlib.pyplot as plt

# Input your dataset
data = {
     

 "Movie": [
        "Home Alone", "Home Alone", "Home Alone", "Home Alone", "Home Alone",
        "Home Alone", "Fast & Furious", "Home Alone", "Jumanji", "It",
        "Fast & Furious", "Home Alone", "Home Alone", "It", "Fast & Furious",
        "Home Alone", "Fast & Furious", "Home Alone", "Home Alone", "Home Alone",
        "Fast & Furious", "Fast & Furious", "Home Alone", "Jumanji", "Fast & Furious" ],
    
"Genre": [
        "Adventure", "Action", "Comedy", "Suspense", "Comedy",
        "Horror", "Horror", "Adventure", "Suspense", "Horror",
        "Adventure", "Horror", "Action", "Drama", "Action",
        "Action", "Action", "Action", "Drama", "Action",
        "Action", "Comedy", "Action", "Action", "Adventure"],
    
"Grade": [
        10, 10, 11, 10, 11,
        10, 10, 10, 10, 11,
        10, 10, 11, 11, 11,
        10, 10, 10, 10, 10,
        10, 10, 10, 10, 10],
    
"MoviesPerWeek": [
        1, 0, 0, 0, 1,
        0, 1, 0, 0, 1,
        1, 1, 2, 6, 20,
        0, 2, 0, 2, 0,
        1, 2, 2, 0, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("Movie Preference Dataset (25 Students):")
print(df)


# Bar Graph of Genres
# ---------------------------
genre_counts = df["Genre"].value_counts()

plt.figure()
genre_counts.plot(kind="bar", color="skyblue")
plt.title("Favorite Movie Genres (25 Students)")
plt.xlabel("Genre")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# Scatter Plot - Movies Watched vs Grade
# ---------------------------
plt.figure()
plt.scatter(df["Grade"], df["MoviesPerWeek"], color="green")
plt.xlabel("Grade Level")
plt.ylabel("Movies Watched Per Week")
plt.title("Movies Watched vs Grade Level")
plt.grid(True)
plt.tight_layout()
plt.show()
