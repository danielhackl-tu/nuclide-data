import csv
import os
import nuclide_data  # Importieren des Moduls

# Erstellen Sie eine Liste der Nuclide und deren Halbwertszeiten
nuclide_half_lives = []

for (Z, A), nuclide in nuclide_data.nist_nuclides.items():
    print(f"Verarbeite Nuclide Z={Z}, A={A}")  # Debug-Ausgabe
    print(f"Nuclide Daten: {nuclide}")  # Debug-Ausgabe
    # Überprüfen Sie, ob der Schlüssel 'half-life' im Nuclide-Dictionary vorhanden ist
    if 'half-life' in nuclide:
        half_life = nuclide['half-life']
        nuclide_half_lives.append([Z, A, half_life])
    else:
        print(f"Keine Halbwertszeit für Nuclide Z={Z}, A={A}")

# Überprüfen Sie, ob die Liste der Halbwertszeiten gefüllt ist
if not nuclide_half_lives:
    print("Keine Halbwertszeiten gefunden.")
else:
    # Speichern Sie die Liste als .csv Datei
    csv_file = os.path.join(nuclide_data.basepath, "nuclide_half_lives.csv")
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Z", "A", "Half-life (s)"])
        writer.writerows(nuclide_half_lives)

    print(f"Halbwertszeiten wurden in {csv_file} gespeichert.")