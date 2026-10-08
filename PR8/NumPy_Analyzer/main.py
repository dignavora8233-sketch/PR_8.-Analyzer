from analyzer import DataAnalytics


obj = DataAnalytics()


while True:

    print("\nWelcome to the NumPy Analyzer!")
    print("=" * 40)

    print("1. Create a NumPy Array")
    print("2. Indexing and Slicing")
    print("3. Mathematical Operations")
    print("4. Combine or Split Arrays")
    print("5. Search, Sort, or Filter")
    print("6. Aggregates and Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.create_array()

    elif choice == "2":
        obj.indexing_slicing()

    elif choice == "3":
        obj.mathematical_operations()

    elif choice == "4":
        obj.combine_split()

    elif choice == "5":
        obj.search_sort_filter()

    elif choice == "6":
        obj.statistics()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")