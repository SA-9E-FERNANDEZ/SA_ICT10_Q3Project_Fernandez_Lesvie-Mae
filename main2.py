from pyscript import display, document

def intrams_checker(e):
    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""

    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade = int(document.getElementById("level").value)
    section = document.getElementById("section").value

    if registration != "registered":
        display("You are not eligible yet. Please complete the online registration first.", target="output")

    elif clearance != "cleared":
        display("You are not eligible yet. Kindly go to the clinic and get your medical clearance.", target="output")

    elif grade < 7 or grade > 10:
        display("You are not eligible. Only students from Grades 7 to 10 can join.", target="output")

    else:
        if section == "emerald":
            team = "Green Hornets"
            img = "green hornets.jpg"

        elif section == "ruby":
            team = "Red Bulldogs"
            img = "red bulldogs.jpg"

        elif section == "sapphire":
            team = "Yellow Tigers"
            img = "yellow tigers.jpg"

        else:
            team = "Blue Bears"
            img = "blue bears.jpg"

        display(f"Congratulations! You are eligible to join the Intramurals. Your team is the {team}!", target="output")
        document.getElementById("image").innerHTML = f"<img src='./{img}' width='260'>"