import geocoder

g = geocoder.ip("me")

print(g)

# print(f"Location: {g.city}, {g.state}, {g.country}")
# print(f"Latitude: {g.latlng[0] if g.latlng else 'Unknown'}")
# print(f"Longitude: {g.latlng[1] if g.latlng else 'Unknown'}")
