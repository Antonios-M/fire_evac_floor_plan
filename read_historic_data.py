import pandas as pd
import numpy as np
import pickle
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.colors as mcolors

# historic_data_room_to_SDDS_mapping = {
#     'Bedroom/ Bedsitting Room': ['BEDROOM', 'ROOM'],
#     'Living Room': ['LIVING_DINING', 'LIVING_ROOM'],
#     'Kitchen': ['KITCHEN'],
#     'External fittings and structures': [],
#     'Dining Room/ Utility Room/ Conservatory': [],
#     'Corridor/ Hall/ Open Plan Area/ Reception Area': ['CORRIDOR', 'LOGGIA'],
#     'Roof/ Roof Space': [],
#     'Other': [],
#     'Bathroom/ Toilet': ['BATHROOM'],
#     'Refuse Store': [],
#     'Stairs/ Under stairs (enclosed area)': [],
#     'Garage': [],
#     'all_room_types_possible': ['BATHROOM', 'LIVING_DINING', 'LIVING_ROOM', 'CORRIDOR', 'LOGGIA', 'KITCHEN', 'BEDROOM', 'ROOM']
# }

df_historic_data = pd.read_csv("historic_data/casualties_in_fires.csv")
df_filtered_only_dwellings = df_historic_data[df_historic_data['INCIDENT_LOCATION_TYPE'] == 'Dwellings']

types_of_start_rooms = df_filtered_only_dwellings['FIRE_START_LOCATION'].unique().tolist()
all_start_rooms = df_filtered_only_dwellings['FIRE_START_LOCATION'].tolist()



types_of_casualties = df_filtered_only_dwellings['CASUALTY_TOTAL'].unique().tolist()
all_casualties = df_filtered_only_dwellings['CASUALTY_TOTAL'].tolist()

room_counts = dict(Counter(all_start_rooms))
number_of_incidents = sum(room_counts.values())
room_weights = {key: round(value / number_of_incidents, 2) for key, value in room_counts.items()}

keys = list(room_weights.keys())
values = list(room_weights.values())
print(values)

# # Plot the bar graph with an inverted gradient of colors
# plt.figure(figsize=(10, 6))
# colors = plt.cm.RdYlGn_r(mcolors.Normalize()(values))  # Applying RdYlGn_r (inverted) colormap
# bars = plt.bar(keys, values, color=colors)

# # Adding labels and title
# plt.xlabel('Type of Room')
# plt.ylabel('Values')
# plt.title('Room of Fire Origin Likelihood')

# # Rotate x-axis labels to avoid overlap
# plt.xticks(rotation=45, ha='right')

# # Adding color bar
# sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn_r, norm=plt.Normalize(vmin=min(values), vmax=max(values)))
# cbar = plt.colorbar(sm)
# cbar.set_label('Likelihood')

# # Show the plot
# plt.tight_layout()
# plt.show()
