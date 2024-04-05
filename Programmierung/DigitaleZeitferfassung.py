
import time

WhatToDisplay = 0
CurrentlySelected = ""
MainStatusDisplayed = False
MemberStatusDisplayed = False

# Dictionary to keep track of the scan count for each EPC
# https://www.w3schools.com/python/python_dictionaries.asp
# Maybe Export Dictionary Values to SCV Sheet for working with Graphs and othet Data Managment. JSON might also be a valuable option
MitarbeiterListe = {
    "Paul": "Mitarbeiter01",
    "Greta": "Mitarbeiter02",
    "Gabriel": "Mitarbeiter03"
}

Mitarbeiter01 = {
    "name": "Paul",
    "Lastname": "Stanisch",
    "weeklyWorktime": 39,
    "currentTime": 0,
    "ArrivedTodayAt": None,
    "LeftWorkAt": None,
    "Status": None,
    "Overtime": 0,
    "AvarageBreakTimeInMin": 45
}
Mitarbeiter02 = {
    "name": "Greta",
    "Lastname": "Ohlsen",
    "weeklyWorktime": 39,
    "currentTime": 0,
    "ArrivedTodayAt": None,
    "LeftWorkAt": None,
    "Status": None,
    "Overtime": 0,
    "AvarageBreakTimeInMin": 45
}
Mitarbeiter03 = {
    "name": "Gabriell",
    "Lastname": "IForgor",
    "weeklyWorktime": 39,
    "currentTime": 0,
    "ArrivedTodayAt": None,
    "LeftWorkAt": None,
    "Status": None,
    "Overtime": 0,
    "AvarageBreakTimeInMin": 45
}

def display_status():
    print("\nMitarbeiter Übersicht:")
    print_nested_dict_key(MitarbeiterListe)

def display_worker():
    print("\nMoin Moin\n")
    print(MitarbeiterListe[CurrentlySelected])

def print_nested_dict_key(dictionary):
    for employee_id, employee_name in dictionary.items(): #Have no fucking clue what employee_id does but deleting it causes problems so it has to stay
        employee_data = globals()[employee_name]
        print(f"{employee_data['name']}: {employee_data['Status']}")

display = 0

while True:
    match display:
        case 0:
            if MainStatusDisplayed == False:
                display_status()
                MainStatusDisplayed = True
                MemberStatusDisplayed = False

        case 1:
            if MemberStatusDisplayed == False:
                display_worker()
                MainStatusDisplayed = False
                MemberStatusDisplayed = True
                time.sleep(20)
                display = 0


            


    
