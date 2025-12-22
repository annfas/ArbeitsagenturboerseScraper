import requests
from bs4 import BeautifulSoup

urlstring = "https://www.rosinenpicker.de/jobs?search=Informatik&job_geo_location=Leipzig&radius=5&Suchen=Suchen&lat=51.339695500000&lon=12.373074700000&country=undefined&administrative_area_level_1=undefined"
response = requests.get(urlstring)

soup = BeautifulSoup(response.content, 'html.parser')
joblist = []
job = soup.find_all('div', class_ ='ergebnisliste-container')
for container in job:
    jobname = container.select_one('h3.sr-only')


    jobname_text = jobname.text.strip () if jobname else "N/A"

    jobs = {
        "Name": jobname_text
    }
    joblist.append(job)

print (soup.prettify())