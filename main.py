import phonenumbers
from phn import Number

from phonenumbers import geocoder
Ch_numebr = phonenumbers.parse(Number, "CH")
print(geocoder.description_for_number(Ch_numebr, "en"))

from phonenumbers import carrier
service = phonenumbers.parse(Number, "RO")
print(carrier.name_for_number(service, "en"))