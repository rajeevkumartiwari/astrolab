from astropy.coordinates import EarthLocation, get_body_barycentric_posvel
from astropy.time import Time
import astropy.units as u
from astropy.coordinates import CartesianRepresentation

def get_sun_position(time):
    sun_pos, _ = get_body_barycentric_posvel('sun', time)
    sun_vector = CartesianRepresentation(sun_pos.xyz)
    return sun_vector

def get_earth_position(time):
    earth_pos, _ = get_body_barycentric_posvel('earth', time)
    earth_vector = CartesianRepresentation(earth_pos.xyz)
    return earth_vector

def get_moon_position(time):
    moon_pos, _ = get_body_barycentric_posvel('moon', time)
    moon_vector = CartesianRepresentation(moon_pos.xyz)
    return moon_vector

def get_mercury_position(time):
    mercury_pos, _ = get_body_barycentric_posvel('mercury', time)
    mercury_vector = CartesianRepresentation(mercury_pos.xyz)
    return mercury_vector

def get_venus_position(time):
    venus_pos, _ = get_body_barycentric_posvel('venus', time)
    venus_vector = CartesianRepresentation(venus_pos.xyz)
    return venus_vector

def get_mars_position(time):
    mars_pos, _ = get_body_barycentric_posvel('mars', time)
    mars_vector = CartesianRepresentation(mars_pos.xyz)
    return mars_vector

def get_jupiter_position(time):
    jupiter_pos, _ = get_body_barycentric_posvel('jupiter', time)
    jupiter_vector = CartesianRepresentation(jupiter_pos.xyz)
    return jupiter_vector

def get_saturn_position(time):
    saturn_pos, _ = get_body_barycentric_posvel('saturn', time)
    saturn_vector = CartesianRepresentation(saturn_pos.xyz)
    return saturn_vector

def get_uranus_position(time):
    uranus_pos, _ = get_body_barycentric_posvel('uranus', time)
    uranus_vector = CartesianRepresentation(uranus_pos.xyz)
    return uranus_vector

def get_neptune_position(time):
    neptune_pos, _ = get_body_barycentric_posvel('neptune', time)
    neptune_vector = CartesianRepresentation(neptune_pos.xyz)
    return neptune_vector 

# def get_pluto_position():
#     now = Time.now()
#     pluto_pos, _ = get_body_barycentric_posvel('pluto', now)
#     pluto_vector = CartesianRepresentation(pluto_pos.xyz)
#     return pluto_vector
