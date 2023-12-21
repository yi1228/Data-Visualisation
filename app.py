from pathlib import Path
from shiny import App, ui, reactive, Session

from modules import map, plot
page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="layout.css"),
    ui.tags.link(rel="stylesheet", type="text/css", href="style.css"),
    ui.tags.script(src="index.js"),

)

page_header = ui.tags.div(
    ui.tags.div(
        ui.tags.a(
            ui.tags.img(
                src="static/img/DMW.png", height="120px"
            ),
        ),
        id="logo-top",
        class_="navigation-logo",
    ),
    ui.tags.div(
        ui.tags.div(
            ui.input_action_button(
                id="tab_map",
                label="Map",
                class_="navbar-button",
            ),
            id="div-navbar-map",
        ),
        ui.tags.div(
            ui.input_action_button(
                id="tab_plot",
                label="Graph",
                class_="navbar-button",
            ),
            id="div-navbar-plot",
        ),
        id="div-navbar-tabs",
        class_="navigation-menu",
    ),
    ui.tags.div(
        ui.input_switch(
            id="dataset",label="Malaria",value=False
        ),
        id="div-navbar-selector",
        class_="navigation-dataset",
    ),
    id="div-navbar",
    class_="navbar-top page-header card-style",
)

map_ui= ui.tags.div(
    map.map_ui("map"),
    id="map-container",
    class_="page-main main-visible",
)

plot_ui= ui.tags.div(
    plot.plot_ui("plot"),
    id="plot-container",
    class_="page-main",
)


page_layout=ui.tags.div(
    page_header,
    map_ui,
    plot_ui,
    class_="page-layout"
)

app_ui= ui.page_fluid(
    page_dependencies,
    page_layout,
    title="Disease App",
)

def server(input,output,session:Session):
    current_tab = "map"

    @reactive.Calc
    def is_ds_data():
        return input.dataset()
    
    map.map_server("map",is_ds_data)
    plot.plot_server("plot",is_ds_data)

    @reactive.Effect
    @reactive.event(input.tab_map)
    async def switch_to_map():
        nonlocal current_tab
        if current_tab != "map":
            await session.send_custom_message("toggleActiveTab", {"activeTab": "map"})
            current_tab = "map"

    @reactive.Effect
    @reactive.event(input.tab_plot)
    async def switch_to_plot():
        nonlocal current_tab
        if current_tab != "plot":
            await session.send_custom_message("toggleActiveTab", {"activeTab": "plot"})
            current_tab = "plot"

www_dir=Path(__file__).parent/"www"
app=App(app_ui,server,static_assets=www_dir)