import phonenumbers

from phonenumbers import carrier, geocoder, timezone
try :
    MobileNumber = input("Enter the Mobile Number including the country code")

    MobileNumber = phonenumbers.parse(MobileNumber)

    print("Time Zone : ", timezone.time_zones_for_number(MobileNumber))

    print("Career Name : ", carrier.name_for_number(MobileNumber, 'en'))

    print("GeoCode : ", geocoder.description_for_number(MobileNumber, 'en'))

    print("Valid Number : ", phonenumbers.is_valid_number(MobileNumber))

    print("Checking Possbility of the Number : ", phonenumbers.is_possible_number(MobileNumber))
except:
    print("Error")
