def get_grade_point(grade):
    grade = grade.upper().strip()
    scale = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 0
    }
    return scale.get(grade, None)


def save_to_file(gpa, courses):
    with open("gpa_result.txt", "w") as f:
        f.write("===== GPA Result =====\n\n")
        # Adjusted column spacing to fit course names nicely
        f.write(f"{'Course':<15} {'Credit Unit':<15} {'Grade':<10} {'Quality Points'}\n")
        f.write("-" * 55 + "\n")
        # We now unpack 4 items: name, credit, grade, and qp
        for name, credit, grade, qp in courses:
            f.write(f"{name:<15} {credit:<15} {grade:<10} {qp}\n")
        f.write("-" * 55 + "\n")
        f.write(f"\nFinal GPA: {gpa}\n")
    print("\nResult saved to gpa_result.txt")


def main():
    print("===== University GPA Calculator =====\n")

    while True:
        try:
            num_courses = int(input("How many courses did you offer this semester? "))
            if num_courses <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    total_credit_units = 0
    total_quality_points = 0
    courses = []

    for i in range(1, num_courses + 1):
        print(f"\n--- Course {i} ---")
        
        # Asks for the actual course name or code
        course_name = input("  Course Name/Code (e.g., MTH101): ").strip().upper()
        if not course_name:
            course_name = f"Course {i}"  # Fallback if they leave it empty

        while True:
            try:
                credit_unit = int(input("  Credit Unit: "))
                if credit_unit <= 0:
                    print("  Credit unit must be greater than 0.")
                    continue
                break
            except ValueError:
                print("  Invalid input. Please enter a whole number.")

        while True:
            grade_input = input("  Letter Grade (A/B/C/D/E/F): ")
            grade_point = get_grade_point(grade_input)
            if grade_point is None:
                print("  Invalid grade. Please enter A, B, C, D, E, or F.")
                continue
            break

        quality_points = credit_unit * grade_point
        total_credit_units += credit_unit
        total_quality_points += quality_points
        
        # Appends the course_name to the tuple inside the list
        courses.append((course_name, credit_unit, grade_input.upper(), quality_points))
        
    # Avoids Error just in case total_credit_units is 0
    gpa = round(total_quality_points / total_credit_units, 2) if total_credit_units > 0 else 0.00

    print("\n===== Result =====")
    print(f"Total Credit Units  : {total_credit_units}")
    print(f"Total Quality Points: {total_quality_points}")
    print(f"Your GPA            : {gpa}")

    save_to_file(gpa, courses)


if __name__ == "__main__":
    main()