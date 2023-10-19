# Programme which retrieves an integer ‘n’ entered by the user and which displays all prime integers less than n
n = int(input("Entrer le nombre d'élèves de la classe  "))
notes = []
for i in range(n):
    note = float(input(f"Entrez les notes {i + 1} : "))
    notes.append(note)
m= sum(notes) / n
for i in range(0,9):
    if(m<note):
        x=x+1
print(f"Les notes supérieures à la moyenne ({m}) sont :{x} ")