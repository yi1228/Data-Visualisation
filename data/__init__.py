from pandas import read_csv


polygon_data = read_csv("data/countries.csv")
polygon_data["coordinates"] = polygon_data["coordinates"].apply(eval)
points_from_polygons = read_csv("data/points_malaysia.csv")

map_data_malaria3 = (
    read_csv("data/map_data_malaria.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)
map_data_denggi3 = (
    read_csv("data/map_data_denggi.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)

plot_data_malaria = read_csv("data/plot_data_malaria.csv")
plot_data_denggi = read_csv("data/plot_data_denggi.csv")

age_group_mapping = {
    "0-4": "0-4",
    "5-9": "5-9",
    "10-14": "10-14",
    "15-19": "15-19",
    "20-24": "20-24",
    "25-29": "25-29",
    "30-34": "30-34",
    "35-39": "35-39",
    "40-44": "40-44",
    "45-49": "45-49",
    "50-54": "50-54",
    "55-59": "55-59",
    "60-64": "60-64",
    "65-69": "65-69",
    "70-74": "70-74",
    ">75": ">75"
}

