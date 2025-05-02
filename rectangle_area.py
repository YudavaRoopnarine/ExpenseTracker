import argparse
import csv
import datetime
import os
import pandas as pd

file_path = os.path.join("data.csv")


def add_expense(id, amount, catagory, date):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([id, amount, catagory, date])

        pd.read_csv('data.csv', on_bad_lines='skip')


def view_expense():
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def delete_expense():
    with open(file_path, 'w') as file:
        pass


def main():
    while True:
        print("\nPlease choose an option:")
        print("1. add_expense")
        print("2. view_expense")
        print("3. delete_expense")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3 or 4): ").strip()

        if choice == '1':
            value1 = input("enter id ")
            value2 = input("enter amount ")
            value3 = input("enter category ")
            value4 = input("enter date ")

            add_expense(value1, value2, value3, value4)

        elif choice == '2':
            view_expense()

        elif choice == '3':
            delete_expense()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
