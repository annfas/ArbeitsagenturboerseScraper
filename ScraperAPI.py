import requests
import csv

#Jobboerse API
url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/app/jobs"

# HTTP-Header fuer API Anfrage
headers = {
    'X-API-Key': 'jobboerse-jobsuche',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.115',

}

# Suchergebnisse, limitiert auf Seite 1-14
alle_ergebnisse = []
for page in range (1,15):
    params = {
        'angebotsart' : '1',
        'was': 'Informatik',
        'wo': 'Leipzig',
        'umkreis': '10',
        'page': page
    }
    response = requests.get (url, headers=headers, params=params)

    # Ausgabe Status Code jeder Seite
    print(f"Seite {page} → Status: {response.status_code}")

    #bei erfolgreicher Prüfung wird die Antwort verarbeitet
    if response.status_code == 200:
        data = response.json()
        # Ergebnisse werden ausgegeben
        if "ergebnisliste" in data:
            for job in data ["ergebnisliste"]:
                gefilterte_infos = {
                    "titel": job.get("stellenangebotsTitel"),
                    "beschreibung": job.get("stellenangebotsBeschreibung"),
                    "vertragsdauer": job.get ("vertragsdauer")
                }
                alle_ergebnisse.append (gefilterte_infos)
        else:
            print("(keine Stellenangebote auf dieser Seite)")
    else:
        print("Fehler:", response.text)

if alle_ergebnisse:
    with open ("stellen_leipzig.csv", "w", newline="", encoding="utf-8") as f:
        spalten = alle_ergebnisse[0].keys()

        writer = csv.DictWriter (f, fieldnames=spalten, delimiter=";")
        writer.writeheader()
        writer.writerows(alle_ergebnisse)

        print (f"Alle {len(alle_ergebnisse)} Jobs wurden gespeichert")




