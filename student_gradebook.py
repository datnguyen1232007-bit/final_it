import json
import os

DATA_FILE = "gradebook.json"


# ---------------------- FILE HANDLING ----------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------- CORE FUNCTIONS ----------------------
def add_course(gradebook):
    code = input("Enter course code: ").upper().strip()

    if code in gradebook:
        print(" Course already exists!")
        return

    name = input("Enter course name: ").strip()
    try:
        credits = int(input("Enter credits: ").strip())
        score = float(input("Enter score (0–100): ").strip())
    except ValueError:
        print("Invalid number format!")
        return

    semester = input("Enter semester (e.g., 2024A): ").strip()

    gradebook[code] = {
        "name": name,
        "credits": credits,
        "semester": semester,
        "score": score
    }

    save_data(gradebook)
    print("Course added successfully!")


def update_course(gradebook):
    code = input("Enter course code to update: ").upper().strip()

    if code not in gradebook:
        print("Course not found!")
        return

    print("Leave a field empty to keep the current value.")

    name = input(f"New name ({gradebook[code]['name']}): ").strip()
    credits = input(f"New credits ({gradebook[code]['credits']}): ").strip()
    semester = input(f"New semester ({gradebook[code]['semester']}): ").strip()
    score = input(f"New score ({gradebook[code]['score']}): ").strip()

    if name:
        gradebook[code]["name"] = name
    if credits:
        try:
            gradebook[code]["credits"] = int(credits)
        except ValueError:
            print(" Invalid credits, keeping old value.")
    if semester:
        gradebook[code]["semester"] = semester
    if score:
        try:
            gradebook[code]["score"] = float(score)
        except ValueError:
            print("Invalid score, keeping old value.")

    save_data(gradebook)
    print("Course updated successfully!")


def delete_course(gradebook):
    code = input("Enter course code to delete: ").upper().strip()

    if code not in gradebook:
        print("Course not found!")
        return

    del gradebook[code]
    save_data(gradebook)
    print("Course deleted successfully!")


def compute_gpa(gradebook):
    if not gradebook:
        print("No courses available.")
        return

    total_points = 0
    total_credits = 0

    for c in gradebook.values():
        total_points += c["score"] * c["credits"]
        total_credits += c["credits"]

    gpa = total_points / total_credits
    print(f"Your GPA is: {gpa:.2f}")


def display_courses(gradebook):
    if not gradebook:
        print("No courses to display.")
        return

    print("\n====== COURSE LIST ======")
    for code, c in gradebook.items():
        print(f"{code} | {c['name']} | {c['credits']} credits | {c['semester']} | Score: {c['score']}")
    print("=========================\n")


# ---------------------- MAIN MENU ----------------------
def main():
    gradebook = load_data()

    while True:
        print("\n===== STUDENT GRADEBOOK CLI =====")
        print("1. Add a course")
        print("2. Update a course")
        print("3. Delete a course")
        print("4. Display all courses")
        print("5. Compute GPA")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_course(gradebook)
        elif choice == "2":
            update_course(gradebook)
        elif choice == "3":
            delete_course(gradebook)
        elif choice == "4":
            display_courses(gradebook)
        elif choice == "5":
            compute_gpa(gradebook)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
