import pandas as pd

# Load CSV file
df = pd.read_csv("Book1.csv")

def display_all_books():
    print("\n--- Complete Book Report ---")
    print(df)

def books_by_author():
    author = input("Enter author name: ")
    result = df[df['author'].str.lower() == author.lower()]
    print(result if not result.empty else "No books found!")

def books_by_publisher():
    publisher = input("Enter publisher name: ")
    result = df[df['publisher'].str.lower() == publisher.lower()]
    print(result if not result.empty else "No books found!")

def cheapest_and_costliest():
    cheapest = df.loc[df['price'].idxmin()]
    costliest = df.loc[df['price'].idxmax()]
    
    print("\nCheapest Book:", cheapest['title'], "-", cheapest['price'])
    print("Costliest Book:", costliest['title'], "-", costliest['price'])

def sort_by_year():
    sorted_df = df.sort_values(by='year')
    print(sorted_df)

# Menu
while True:
    print("\n--- Book Menu ---")
    print("1. Display All Books")
    print("2. Books by Author")
    print("3. Books by Publisher")
    print("4. Cheapest & Costliest Book")
    print("5. Sort by Year")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        display_all_books()
    elif choice == '2':
        books_by_author()
    elif choice == '3':
        books_by_publisher()
    elif choice == '4':
        cheapest_and_costliest()
    elif choice == '5':
        sort_by_year()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")