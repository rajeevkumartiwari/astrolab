import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from logic.solar_positions import (
    get_sun_position, get_earth_position, get_moon_position,
    get_mercury_position, get_venus_position, get_mars_position,
    get_jupiter_position, get_saturn_position, get_uranus_position,
    get_neptune_position
)
from astropy.time import Time, TimeDelta


def plot_solar_system():
    plt.ion()
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Hide grid lines and ticks
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Remove axis labels
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')

    # Turn off scientific tick formatting
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])

    ax.tick_params(axis='both', which='both', bottom=False, top=False,
               labelbottom=False, left=False, right=False, labelleft=False)
    
    for spine in ax.spines.values():
        spine.set_visible(False)

    start_time = Time('2025-01-01 00:00:00')
    steps = 365
    delta = TimeDelta(365 / steps, format='jd')
    current_time = start_time - delta

    while True:
        # Get positions of all celestial bodies

        current_time += delta
        sun_pos = get_sun_position(current_time)
        mercury_pos = get_mercury_position(current_time)
        venus_pos = get_venus_position(current_time)
        earth_pos = get_earth_position(current_time)
        moon_pos = get_moon_position(current_time)
        mars_pos = get_mars_position(current_time)
        jupiter_pos = get_jupiter_position(current_time)
        saturn_pos = get_saturn_position(current_time)
        uranus_pos = get_uranus_position(current_time)
        neptune_pos = get_neptune_position(current_time)
        # pluto_pos = get_pluto_position(current_time)
        
        print('refreshing plot')
        
        ax.clear()

        # axis_limit_km = 5e9
        # for axis in [ax.set_xlim, ax.set_ylim, ax.set_zlim]:
        #     axis(-axis_limit_km, axis_limit_km)

        ax.title.set_text('Live Solar System')
        ax.set_xlabel('X (km)')
        ax.set_ylabel('Y (km)')
        ax.set_zlabel('Z (km)')
        ax.set_box_aspect([1,1,1])

        # Plot all bodies with appropriate colors and sizes
        ax.scatter(0, 0, 0, color='black', s=10, label='Barycenter')
        ax.text(0, 0, 0, 'Barycenter', color='black')
        ax.scatter(sun_pos.x.value, sun_pos.y.value, sun_pos.z.value, color='yellow', s=200, label='Sun')
        ax.scatter(mercury_pos.x.value, mercury_pos.y.value, mercury_pos.z.value, color='gray', s=8, label='Mercury')
        ax.scatter(venus_pos.x.value, venus_pos.y.value, venus_pos.z.value, color='orange', s=15, label='Venus')
        ax.scatter(earth_pos.x.value, earth_pos.y.value, earth_pos.z.value, color='blue', s=20, label='Earth')
        ax.scatter(moon_pos.x.value, moon_pos.y.value, moon_pos.z.value, color='lightgray', s=5, label='Moon')
        ax.scatter(mars_pos.x.value, mars_pos.y.value, mars_pos.z.value, color='red', s=15, label='Mars')
        ax.scatter(jupiter_pos.x.value, jupiter_pos.y.value, jupiter_pos.z.value, color='brown', s=100, label='Jupiter')
        ax.scatter(saturn_pos.x.value, saturn_pos.y.value, saturn_pos.z.value, color='gold', s=80, label='Saturn')
        ax.scatter(uranus_pos.x.value, uranus_pos.y.value, uranus_pos.z.value, color='lightblue', s=40, label='Uranus')
        ax.scatter(neptune_pos.x.value, neptune_pos.y.value, neptune_pos.z.value, color='darkblue', s=40, label='Neptune')
        # ax.scatter(pluto_pos.x.value, pluto_pos.y.value, pluto_pos.z.value, color='darkgray', s=5, label='Pluto')

        ax.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
        plt.pause(1)

