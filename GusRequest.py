import requests
import json
import pickle
class API():
    def __init__(self, level = 2, value ={}):
        self.key = "1d820df8-7011-42cf-f7d9-08d872c797ed"
        self.Value = value
        self.BaseString = "https://bdl.stat.gov.pl/api/v1/"
        self.DataString = "data/by-variable/"
        # 0 - Poziom Polski
        # 1 - Poziom Makroregionów
        # 2 - Poziom Województw
        # 3 - Poziom Regionów
        # 4 - Poziom  Podregionów
        # 5 - Poziom  Powiatów
        # 6 - Poziom  Gmin
        self.level= level
        self.response = []
        self.typ = "format=json"

    def DataRequest(self,s):
        string = f"{self.BaseString}{self.DataString}{s}?{self.typ}&unit-level={self.level}&page-size=100"
        print(string)
        req = requests.get(string)
        self.response.append(req)
        return req


    def SaveResponses(self):
        for val, rep in zip(self.Value,self.response):
            rep = rep.json()
            with open(f"{val}.json", "w") as f:
                json.dump(rep, f)

    def RqestDict(self):
        if not self.Value: self.Value = dict
        for value in self.Value:
            self.DataRequest(self.Value[value])
        self.SaveResponses()




if __name__ == "__main__":
    ValueDict = {
        #Ceny
        "Wskaznik ceny mieszkania":217234,
        "Wskaznik ceny ogółem": 217230,
        #mieszkania
        "Dodatki mieszkaniowe liczba":54861,
        "Dodatki mieszkaniowe kwota":54857,
        "mieszkania na 1000 mieszkańców":410600,
        "Liczba sprzedanych lokali mieszkalnych ogólem": 633101,
        "Liczba trazakcji kupna sprzedarzy lokali mieszkalnych ogółem": 633097,
        "średnia cena lokli mieszkalnych ogółem":633181,
        "średnia cean za m2 lokali mieszkalnych ogółem": 633161,
        "mediana cean za m2 lokali mieszkalnych ogółem":633677,
        "Wartoś sprzedanych lokali mieszkalnych":63321,
        "Mediana cen za 1 m2 lokali mieszkalnych sprzedanych w ramach transakcji rynkowych": 633677,
        "Przeciętna powierzchnia użytkowa 1 mieszkania": 747064,
        "Drogi gminne i powiatowe o twardej nawierzchni na 100 km2": 395402,
        "przeciętna powierzchnia użytkowa 1 mieszkania	":747064,
        "nowe budynki mieszkalne na 1000 ludności":747066,
        "pozwolenia wydane na mieszkania":747242,
        "budynki mieszkalne pozwolenia i zgłoszenia z projektem":747325,
        #wynagrodzenia i praca
        "Przeciętne wynagrodzenie brutto": 64428,
        "Stopa bezrobocia": 60270,
        "Liczba nowych miejsc pracy":452355,
        "Liczba zlikfidownych miejsc pracy":452356,
        "Lekarze (personel pracujący ogółem) na 10 tys. ludności": 454185,
        "Liczba osób zatrudnionych w warunkach zagrożenia na 1000 osób zatrudnionych w badanej zbiorowości": 450366,
        "absolwenci na 10 tys ludnosci ":475966,
        "studenci na 10 tes ludnosci ":60194,
        #atrakyjnosc
        "placowki gastronomiczne ogolem":146273,
        "stopien wykorzystania hoteli ":59678,
        "turysci zagraniczni ogółem":148074,
        "Udział parków, zieleńców i terenów zieleni osiedlowej w powierzchni ogółem": 395921,
        "Liczba osób na placówkę (centrum kultury, dom kultury, ośrodek kultury, klub, swietlicę)": 1539660,
        #sytulacja spoleczna
        "Przestępstwa stwierdzone przez Policję ogółem na 1000 mieszkańców": 398594,
        "Liczba prób (zachowań) samobójczych na 100 tys. ludności": 1365344,
        #przedsiebiorsta
        "Nakłady na badania i rowzoj": 101203,
        "pracujacy w R+B na 1000 pracujacych":567829,
        "średni udział przedsiębiorstw innowacyjnych w ogólnej liczbie przedsiębiorstw":458598,
    }


    testdict = {"Liczba sprzedanych lokali mieszkalnych ogólem": 633101}
    api = API(value=testdict)

    api.RqestDict()