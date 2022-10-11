#from tkinter.simpledialog import askstring
from pkg_resources import resource_string
from collections import namedtuple
from string import ascii_uppercase
import json
import sys
#import pandas as pd

from tkinter import *
import tkinter as tk #module for the gui

#we create the main window
mainWindow = Tk()
mainWindow.geometry('450x450')
mainWindow.title('Location Finder')
mainWindow.resizable(0,0)
mainWindow.config(bg='white')  
#mainWindow.withdraw()

#the input
#User_input = askstring(title="Location",
                        #prompt= "Put any the iata code for International airport")


#define the text to speech file
ASCII_UPPERCASE = set(ascii_uppercase)
Airport = namedtuple('Airport', ['name', 'city', 'country', 'iata', 'icao', 'lat', 'lon', 'alt', 'tz', 'dst', 'tzdb'])
Other = namedtuple('Other', ['iata', 'name', 'country', 'subdiv', 'type', 'lat', 'lon'])

# Name       Name of airport. May or may not contain the City name.
# City       Main city served by airport. May be spelled differently from Name.
# Country    Country or territory where airport is located.
# IATA       3-letter FAA code, for airports located in Country "United States of America" and 3-letter IATA code,
#            for all other airports. Blank if not assigned.
# ICAO       4-letter ICAO code and Blank if not assigned.
# Latitude   Decimal degrees, usually to six significant digits. Negative is South, positive is North.
# Longitude  Decimal degrees, usually to six significant digits. Negative is West, positive is East.
# Altitude   In feet!
# Timezone   Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
# DST        Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia),
#            Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
# Tz database time zone   Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".

# Note: Rules for daylight savings time change from year to year and from country to country. The current data is an
# approximation for 2009, built on a country level. Most airports in DST-less regions in countries that generally
# observe DST (eg. AL, HI in the USA, NT, QL in Australia, parts of Canada) are marked incorrectly.

AIRPORT_LIST = json.loads(resource_string('pyairports', 'data/airport_list.json'))
OTHER_LIST = json.loads(resource_string('pyairports', 'data/other_list.json'))
airport = pd.read_csv('airports.csv')
print(airport)


class AirportNotFoundException(Exception):
    pass


class Airports(object):

    def __init__(self):

        self.airports = {
            _[3].upper(): Airport(*_) for _ in AIRPORT_LIST
        }

        self.other = {
            _[0].upper(): Other(*_) for _ in OTHER_LIST
        }

    @staticmethod
    def _validate(country):
        if not isinstance(country, (str, 'utf-8')):
            raise ValueError("iata must be a string, it is a {0}".format(type(country)))
        country = country.strip().upper()
        if not len(country) == 3:
            raise ValueError("iata must be three characters")
        return country

    def airport_iata(self, country):
        return self.lookup(country, self.airports)

    def other_iata(self, iata):
        return self.lookup(iata, self.other)

    def is_valid(self, iata):
        iata = self._validate(iata)
        return iata in self.airports or iata in self.other

    def lookup(self, iata, table=None):
        iata = self._validate(iata)

        if not self.is_valid(iata):
            raise AirportNotFoundException("iata not found in either airport list: {0}".format(iata))

        if table is None:
            # Prefer self.airports over self.other
            return self.airports.get(iata) or self.other.get(iata)
        elif iata not in table:
            raise AirportNotFoundException("iata not found: {0}".format(iata))

        return table.get(iata)


def main():  # pragma: no cover
    from argparse import ArgumentParser
    parser = ArgumentParser("Airport lookup by IATA code")
    parser.add_argument("iata", action="store")
    args = parser.parse_args()
    airports = Airports()
    try:
        print(airports.lookup(args.name))
    except AirportNotFoundException:
        print("Not in core airport list")

if __name__ == "__main__":  # pragma: no cover
    Airport()

  


#Label
name=Label(mainWindow,text="Enter Airport IATA code.", font='gotham 9 bold')
name.pack()
name.place(height=30,width=410,y=20,x=20)
name.place(height=30,width=410,y=20,x=20)


#text input area
User_input = Text(mainWindow,wrap='word')
User_input.pack()
User_input.place(height=300,width=410,y=50,x=20)

#scrollbar

input = Button(mainWindow, text= 'Search airport', bg='Green', fg='white', command=Airports) 



input.pack()
input.place(height=50,width=210,y=350,x=20)

#main loop would be run constantly as
mainWindow = tk.TK()
myapp = Airport(mainWindow)
mainWindow.mainloop()

