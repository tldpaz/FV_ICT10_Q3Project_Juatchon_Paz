from pyscript import document, when

@when("click", "#checkBtn")
def check_team(event):

    registration = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="medical"]:checked')

    grade_value = document.getElementById("grade").value
    output = document.getElementById("teamOutput")

    # ya make sure that shit is answered yow
    if registration is None or medical is None:
        output.innerText = "Please answer all questions."
        return

    # yay
    if registration.value != "yes" or medical.value != "yes":
        output.innerText = "You must complete registration and medical clearance first."
        return

    # yay
    try:
        grade = int(grade_value)
    except:
        output.innerText = "Please select your grade."
        return

    # yip
    
    if grade == 7:
        team = "Yellow Tigers"
    elif grade == 8:
        team = "Blue Bears"
    elif grade == 9:
        team = "Red Bulldogs"
    elif grade == 10:
        team = "Green Hornets"
    else:
        team = "No team assigned"

    

    output.innerText = f"Congratulations! You are part of the {team}"