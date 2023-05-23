school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
print(school_report.values())
print()
prumerna_znamka = sum(school_report.values())/len(school_report)
print(f"Průměrá zmánka je: {prumerna_znamka}.")
print(school_report.items())

for predmet, znamka in school_report.items():
    if znamka ==1:
        print("\t" + predmet)

predmet, znamka = ("Český jazyk", 1)
print("predmet:", predmet)

