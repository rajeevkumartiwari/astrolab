from astropy.coordinates import get_body_barycentric_posvel
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import CartesianRepresentation

def get_earth_moon_distance_m():
    now = Time.now()
    moon_pos, _ = get_body_barycentric_posvel('moon', now)
    #print(moon_pos)
    moon_vector = CartesianRepresentation(moon_pos.xyz);
    earth_pos, _ = get_body_barycentric_posvel('earth', now)
    earth_vector = CartesianRepresentation(earth_pos.xyz);
    #print(earth_pos)
    distance = (moon_vector-earth_vector).norm().to(u.m)

    return distance.value

    
