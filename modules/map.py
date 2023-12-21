from typing import cast
from pandas import DataFrame
from shiny import ui, module, reactive
from shinywidgets import output_widget, register_widget

from ipywidgets import Layout
from ipyleaflet import Map, LayerGroup, basemaps
from utils.helper_text import (
    about_text,
    missing_note,
    slider_text_map,
)
from utils.map_utils import add_circles, add_polygons, filter_data
from data import polygon_data, map_data_denggi3, map_data_malaria3

basemap = cast(dict, basemaps)

@module.ui
def map_ui():
    return ui.tags.div(
        ui.tags.div(
            about_text,
            ui.tags.hr(),
            slider_text_map,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select year",
                min=2010,
                max=2021,
                value=2011,
                sep="",
            ),
            ui.tags.hr(),
            missing_note,
            ui.tags.br(),
        ),
        ui.tags.div(
            output_widget("map",width="auto",height="auto"),
            class_="main-main card-style no-padding",
        ),
        class_="main-layout",
    )

@module.server
def map_server(input,output,session,is_ds_data):
    map = Map(
        basemap=basemaps.CartoDB.Positron,
        center=(3.7,109),
        zoom=6,
        scroll_wheel_zoom=True,
        min_zoom=3,
        max_zoom=18,
        no_wrap=True,
        layout = Layout(width="100%",height="100%",)
    )
    map.panes = {"circles": {"zIndex":650}, "choropleth" : {"zIndex": 750}}
    register_widget("map",map)

    circle_markers_layer = LayerGroup()
    circle_markers_layer.pane = "circles"
    map.add_layer(circle_markers_layer)

    choropleth_layer = LayerGroup()
    choropleth_layer.pane = "choropleth"
    map.add_layer(choropleth_layer)

    @reactive.Calc
    def point_data() -> DataFrame:
        if is_ds_data():
            return filter_data(map_data_malaria3,input.years_value())
        return filter_data(map_data_denggi3,input.years_value())
    
    @reactive.Effect
    def _() -> None:
        add_circles(point_data(),circle_markers_layer)

    @reactive.Effect()
    def _() -> None:
        add_polygons(polygon_data, point_data(), choropleth_layer)
    

