import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from logic.solar_positions import (
    get_sun_position, get_earth_position, get_moon_position,
    get_mercury_position, get_venus_position, get_mars_position,
    get_jupiter_position, get_saturn_position, get_uranus_position,
    get_neptune_position
)
from astropy.time import Time, TimeDelta
from astropy.coordinates import CartesianRepresentation
import numpy as np

def log_val(val):
    logVal = np.log10(np.abs(val) + 1) * np.sign(val)
    return logVal


def plot_solar_system():
    plt.ion()
    # fig = plt.figure(figsize=(10, 10))
    fig = plt.figure()
    manager = plt.get_current_fig_manager()

    # For TkAgg backend (common default)
    try:
        # Get screen size (in inches)
        dpi = mpl.rcParams['figure.dpi']
        screen_w, screen_h = plt.get_current_fig_manager().canvas.get_width_height()
        fig.set_size_inches(screen_w / dpi, screen_h / dpi)    
    except Exception:
        fig.set_size_inches(plt.figaspect(1) * 10)  # Fallback: manually scale

    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])

    # Hide grid lines and ticks
    ax.grid(True)
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

    ax.tick_params(axis='both', which='both', bottom=True, top=True,
               labelbottom=True, left=True, right=True, labelleft=True)
    bary_pos = CartesianRepresentation(0, 0, 0, unit='km')

    for spine in ax.spines.values():
        spine.set_visible(False)

    start_time = Time('2025-01-01 00:00:00')
    steps = 365
    delta = TimeDelta(365 / steps, format='jd')
    current_time = start_time - delta
    

    while True:

        # Get positions of all celestial bodies
        # print('refreshing plot')
        
        ax.clear()

        # 🔻 Immediately hide axes, ticks, grid
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])
        ax.tick_params(
            axis='both', which='both',
            bottom=False, top=False,
            labelbottom=False,
            left=False, right=False,
            labelleft=False
        )
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.set_zlabel('')

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

        positions = [
                        sun_pos,
                        mercury_pos,
                        venus_pos,
                        earth_pos, 
                        moon_pos,
                        mars_pos, 
                        jupiter_pos, saturn_pos, 
                        uranus_pos,
                        neptune_pos]
        
        # all_x = np.array([pos.x.to_value('km') for pos in positions])
        # all_y = np.array([pos.y.to_value('km') for pos in positions])
        # all_z = np.array([pos.z.to_value('km') for pos in positions])

        # x_min, x_max = all_x.min(), all_x.max()
        # y_min, y_max = all_y.min(), all_y.max()
        # z_min, z_max = all_z.min(), all_z.max()

        # # Find the center and range for each axis
        # x_center = (x_min + x_max) / 2
        # y_center = (y_min + y_max) / 2
        # z_center = (z_min + z_max) / 2

        # range_x = x_max - x_min
        # range_y = y_max - y_min
        # range_z = z_max - z_min

        # max_range = max(range_x, range_y, range_z) / 2  # to get half-length

        # # Set symmetric limits around each axis center
        # ax.set_xlim(x_center - max_range, x_center + max_range)
        # ax.set_ylim(y_center - max_range, y_center + max_range)
        # ax.set_zlim(z_center - max_range, z_center + max_range)
 
        
        ax.title.set_text('Live Solar System')

        # Plot all bodies with appropriate colors and sizes
        ax.scatter(0, 0, 0, color='black', s=10, label='Barycenter')
        # ax.text(0, 0, 0, 'Barycenter', color='black')
        ax.scatter(log_val(sun_pos.x.value), log_val(sun_pos.y.value), log_val(sun_pos.z.value), color='yellow', s=200, label='Sun')
        ax.scatter(log_val(mercury_pos.x.value), log_val(mercury_pos.y.value), log_val(mercury_pos.z.value), color='gray', s=8, label='Mercury')
        ax.scatter(log_val(venus_pos.x.value), log_val(venus_pos.y.value), log_val(venus_pos.z.value), color='orange', s=15, label='Venus')
        ax.scatter(log_val(earth_pos.x.value), log_val(earth_pos.y.value), log_val(earth_pos.z.value), color='blue', s=20, label='Earth')
        ax.scatter(log_val(moon_pos.x.value), log_val(moon_pos.y.value), log_val(moon_pos.z.value), color='lightgray', s=5, label='Moon')
        ax.scatter(log_val(mars_pos.x.value), log_val(mars_pos.y.value), log_val(mars_pos.z.value), color='red', s=15, label='Mars')
        ax.scatter(log_val(jupiter_pos.x.value), log_val(jupiter_pos.y.value), log_val(jupiter_pos.z.value), color='brown', s=100, label='Jupiter')
        ax.scatter(log_val(saturn_pos.x.value), log_val(saturn_pos.y.value), log_val(saturn_pos.z.value), color='gold', s=80, label='Saturn')
        ax.scatter(log_val(uranus_pos.x.value), log_val(uranus_pos.y.value), log_val(uranus_pos.z.value), color='lightblue', s=40, label='Uranus')
        # print("Neptune:", neptune_pos.x.value, neptune_pos.y.value, neptune_pos.z.value)
        ax.scatter(log_val(neptune_pos.x.value), log_val(neptune_pos.y.value), log_val(neptune_pos.z.value), color='darkblue', s=40, label='Neptune')
        # ax.scatter(pluto_pos.x.value, pluto_pos.y.value, pluto_pos.z.value, color='darkgray', s=5, label='Pluto')

        # ax.plot(
        #     [0, neptune_pos.x.value],
        #     [0, neptune_pos.y.value],
        #     [0, neptune_pos.z.value],
        #     color='cyan',
        #     linestyle='--'
        # )
        ax.legend(bbox_to_anchor=(1.15, 1), loc='upper left')
        plt.pause(.1)
