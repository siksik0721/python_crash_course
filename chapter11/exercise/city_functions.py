def get_formatted_name(city, country, population=""):
    formatted_name = f"{city}, {country}".title()
    if population:
        formatted_name += f" - population {population}"
    return formatted_name
