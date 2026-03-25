import pandas as pd

# Create DataFrame
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Tamil Nadu"],
    "Area": [307713, 196244, 342239, 191791, 130058],  # in sq km
    "Population": [124000000, 70000000, 81000000, 68000000, 78000000]
}

df = pd.DataFrame(data)

# Add population density column
df["Density"] = df["Population"] / df["Area"]

def display_states():
    print("\n--- State Information ---")
    print(df)

def largest_area():
    state = df.loc[df["Area"].idxmax()]
    print("State with Largest Area:", state["State"])

def largest_population():
    state = df.loc[df["Population"].idxmax()]
    print("State with Largest Population:", state["State"])

def highest_density():
    state = df.loc[df["Density"].idxmax()]
    print("State with Highest Population Density:", state["State"])

# Menu
while True:
    print("\n--- State Menu ---")
    print("1. Display States")
    print("2. State with Largest Area")
    print("3. State with Largest Population")
    print("4. Population Density of States")
    print("5. State with Highest Density")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        display_states()
    elif choice == '2':
        largest_area()
    elif choice == '3':
        largest_population()
    elif choice == '4':
        print(df[["State", "Density"]])
    elif choice == '5':
        highest_density()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")