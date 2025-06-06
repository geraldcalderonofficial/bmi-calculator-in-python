#Calculate Body Mass Index (BMI) using feet, inches, and pounds.

def calculate_bmi(feet, inches, pounds):
    """Calculates BMI given height in feet and inches, and weight in pounds."""

    total_inches = (feet * 12) + inches
    bmi = (pounds / (total_inches ** 2)) * 703

    return bmi

def interpret_bmi(bmi):
    """Interprets the BMI value and returns a category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    try:
        feet = int(input("Enter your height in feet: "))
        inches = int(input("Enter your height in inches: "))
        pounds = float(input("Enter your weight in pounds: "))

        bmi_value = calculate_bmi(feet, inches, pounds)
        bmi_category = interpret_bmi(bmi_value)

        print(f"Your BMI is: {bmi_value:.2f}")
        print(f"Category: {bmi_category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")
