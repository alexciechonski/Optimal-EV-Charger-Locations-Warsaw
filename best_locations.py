from minimum_cost import MinimumCost as mc
from get_stations import getStations
import json
import streamlit as st
import folium
from streamlit_folium import folium_static

def minCost(address, power):
    """given an address returns an address of a transformer station that produces the lowest grid connection cost"""
    # convert the address into cords
    y,x = mc.a2c(address)
    start = (x,y)

    # get df around that point
    stations = getStations(x, y)
    df = stations.get_data()

    # list of 5 closest ones
    locs = mc.minimum_distance(df, y, x) #(x-cord, y-cord, haversine distance) for each trafostacja
    
    # get the shortest routes
    shortest_routes = [(loc[0], loc[1], mc.get_route(start, (loc[0],loc[1]))) for loc in locs]
    min_vec = sorted(shortest_routes, key=lambda x: x[2])[0] #(x-cord, y-cord, shortest_routes) for each trafostacja
    cords = (min_vec[1],min_vec[0])
    min_length = min_vec[2]

    if min_length > 200:
            cost = 19.96 * power + 9.49 * min_length
    else:
        cost = 19.96 * power

    # return f"address/cords: {mc.c2a(cords)},\ncost: {cost},\nlength: {min_length}"
    return mc.c2a(cords), cost, min_length

def best_locs(options, parking):
    """returns a dictionary containing the data of the optimal parking lot for EV charger installation"""
    with open('updated_locations.json','r') as f:
        parkings = json.load(f)

    min_diff = float('inf')
    best_data = None

    for key, data in parkings.items():
        if data['address'] in options:
            diff = abs(data['num_roads'] - data['num_chargers'])
            if diff < min_diff:
                min_diff = diff
                best_data = data  # Store the whole data dictionary

    return best_data  # Return the entire data entry


def generate_map(selected_options, parkings, best_data):
    """generates a map of parking lots"""
    map_center = [52.2297, 21.0122]
    folium_map = folium.Map(location=map_center, zoom_start=12)

    for key, data in parkings.items():
        if data['address'] in selected_options:
            folium.Marker(
                location=(data['lat'], data['lon']),
                popup=data['address'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(folium_map)

    if best_data:
        folium.Marker(
            location=(best_data['lat'], best_data['lon']),
            popup=f"Best Location: {best_data['address']}",
            icon=folium.Icon(color='red', icon='star')
        ).add_to(folium_map)

    return folium_map

def main():
    """app for visualizing the most optimal locations for EV charger installation"""
    # Load dataset
    with open('pl2.json', 'r') as f:
        parkings = json.load(f)

    # Title and sidebar
    st.title("Best EV Charger Locations in Warsaw")
    st.sidebar.header('Menu')

    # List of addresses
    options = sorted([data['address'] for data in parkings.values()])

    # Initialize session state for selected options if not already set
    if 'selected_options' not in st.session_state:
        st.session_state.selected_options = set(options)  # Default to all selected

    # Button for selecting all
    if st.sidebar.button('Select All'):
        st.session_state.selected_options = set(options)

    # Button for unselecting all
    if st.sidebar.button('Unselect All'):
        st.session_state.selected_options = set()

    # Search bar in the sidebar
    search_query = st.sidebar.text_input("Search for an address")

    power = st.sidebar.number_input("Enter the desired power of the charger (in kW)")

    # Filter options based on the search query
    if search_query:
        filtered_options = [option for option in options if search_query.lower() in option.lower()]
        # Multi-select widget for deselecting found addresses
        selected_from_search = st.sidebar.multiselect(
            "Selected addresses (deselect to remove):",
            options=filtered_options,
            default=[opt for opt in filtered_options if opt in st.session_state.selected_options]
        )
        # Update session state to reflect changes from the search multiselect
        st.session_state.selected_options = set(selected_from_search).union(
            st.session_state.selected_options.intersection(set(options) - set(filtered_options))
        )

    # Print the number of selected options
    st.write(f"Number of selected options: {len(st.session_state.selected_options)}")

    if st.sidebar.button('Apply'):
        if st.session_state.selected_options:
            best_data = best_locs(st.session_state.selected_options, parkings)
            if best_data:
                folium_map = generate_map(st.session_state.selected_options, parkings, best_data)
                folium_static(folium_map)
                address = best_data['address']
                mc_res = minCost(address, power)
                st.write(f"Cost of grid connection: {mc_res[1]}")
                st.write(f"Closest station: {mc_res[0]}")
            else:
                st.write("No best location found.")
        else:
            st.write("No addresses selected. Please select one or more addresses to display the map.")

if __name__ == "__main__":
    main()
