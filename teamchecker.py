from pyscript import document, when

# This function runs when the "Check Team" button is clicked
@when("click", "#checkBtn") #cred to gpt idk what this does but before i used this my page was wonky so apparently it's called a decorator for the browser thing but im unfamiliar with this honestly
def check_team(event):

    # Get selected radio button values
    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    # Get grade input value
    grade_value = document.getElementById("grade").value
    output = document.getElementById("teamOutput")

    # Check if required questions were answered
    if registration is None or medical is None:
        output.innerText = "Please answer all questions."
        return

    # Check if registration and medical clearance are both "yes"
    if registration.value != "yes" or medical.value != "yes":
        output.innerText = "You must complete registration and medical clearance first."
        return

    # Convert grade input into integer
    try:
        grade = int(grade_value)
    except:
        output.innerText = "Please select your grade."
        return

    # Assign team based on grade level
    if grade == 7:
        team = "Yellow Tigers"
    elif grade == 8:
        team = "Blue Bears"
    elif grade == 9:
        team = "Red Bulldogs"
    elif grade == 10:
        team = "Green Hornets"

    # Display final result
    output.innerText = f"Congratulations! You are part of the {team}!"
