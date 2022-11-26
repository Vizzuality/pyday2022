from branca.element import Figure
import folium


def convert_bounds(bbox, invert_y=False):
    """
    Helper method for changing bounding box representation to leaflet notation

    ``(lon1, lat1, lon2, lat2) -> ((lat1, lon1), (lat2, lon2))``
    """
    x1, y1, x2, y2 = bbox
    if invert_y:
        y1, y2 = y2, y1
    return (y1, x1), (y2, x2)


def image_on_map(image, bbox):
    fig = Figure(width="600px", height="600px")
    m = folium.Map()
    fig.add_child(m)
    image.odc.add_to(m)
    m.fit_bounds(bounds=convert_bounds(bbox))
    folium.LayerControl().add_to(m)
    return m
