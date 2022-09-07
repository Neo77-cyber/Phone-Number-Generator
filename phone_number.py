from cProfile import label
import phonenumbers

from phonenumbers import carrier, geocoder, timezone

mobile = input("Enter Phone number")
mobile = phonenumbers.parse(mobile)


print(timezone.time_zones_for_number(mobile))

print(carrier.name_for_number(mobile, "en"))

print(geocoder.description_for_number(mobile, "en"))

print("Is this number Valid",phonenumbers.is_valid_number(mobile))

print("Is this number possible,",phonenumbers.is_possible_number(mobile))