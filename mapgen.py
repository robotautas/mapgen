import folium
from geopy.geocoders import ArcGIS
nom = ArcGIS()


def coords(address):

    if nom.geocode(address) == None:
        pass
    else:
        lonlat = list(nom.geocode(address)[-1])
        return lonlat


def run():

    coordlist = []
    user_input = None
    print('\nPlease provide some geographical data of the point you want to generate on the map\n(e.g. "Mount Rushmore, USA", "..some address, ..city", '
          'etc.) Enter "s" to save the map.\nYour map will be saved as "map.html" in the same folder, where this script is located.\n')
    while user_input != 's':


        user_input = input("Enter a place:")
        coordlist.append([coords(user_input), user_input])

        for i in coordlist:
            if i[0] == None:
                coordlist.remove(i)
                print("..found nothing, try again.")

    coordlist.pop()
    return coordlist


def apply_list():

    map = folium.Map(location=[54.729042, 25.223920], zoom_start=6)
    x = run()
    for i in x:
        map.add_child(folium.Marker(location=i[0], popup=i[1], icon=folium.Icon(color='green')))
    map.save("Map.html")


apply_list()


