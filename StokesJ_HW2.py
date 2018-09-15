#Stokes, Jeff - CS451-551
#HW2 - Computing Geodisic Distance

from geopy.distance import distance
from geopy.geocorders import Nominatim


geolocator = Nominatim()

loc_a  = raw_input('Enter first addresss: ')

loc = geolocator.geocode(loc_a)

if not loc:
	print ('Location not found in Nominatim')
else:
	loc_b = raw_input('Enter second address: ')

	d = distance((loc.latitude, loc.longitude), (lob_b.latitude, lob_b.longitude)).miles

	print ('Disntance between ', loc_a, ' and ', lob_b, ' is:\n', d)