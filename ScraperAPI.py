import requests

#Jobboerse API
url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/app/jobs"

# HTTP-Header fuer API Anfrage
headers = {
    'X-API-Key': 'jobboerse-jobsuche',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.115',

}

# Suchergebnisse, limitiert auf Seite 1-14
for page in range (1,15):
    params = {
        'angebotsart' : '34',
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
        print("Treffer:", data.get("maxErgebnisse", 0))

        # Ergebnisse werden ausgegeben
        if "ergebnisliste" in data:
            for job in data["ergebnisliste"][:25]:
                titel = job.get("stellenangebotsTitel")
                beschreibung = job.get("stellenangebotsBeschreibung")
                vertragsdauer = job.get ("vertragsdauer")
                print("-", titel, ":", beschreibung, ",", vertragsdauer)
        else:
            print("(keine Stellenangebote auf dieser Seite)")
    else:
        print("Fehler:", response.text)



