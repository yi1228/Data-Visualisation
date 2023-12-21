from shiny import ui, module, reactive ,render
from shinywidgets import (
    output_widget,
    render_widget
)
from utils.helper_text import (
    missing_note,
)
from utils.plot_utils import create_line,create_histogram,create_bar,create_area
from data import plot_data_denggi, plot_data_malaria,age_group_mapping


state_choices = plot_data_denggi["State"].unique().tolist()

@module.ui
def plot_ui():
    
    return ui.tags.div(
        ui.tags.div(
            ui.input_slider(
                id="years_value",
                label="", # add this line
                min=2010,
                max=2021,
                value=[2012, 2015],
                sep="",
            ),
            ui.input_select(
                id="graph_type",
                label="Select Graph Type:",
                choices=["Year", "Age"],
                selected="Year",  
            ),
            ui.input_selectize(
                id="state_select",
                label="Select State:",
                choices=state_choices,
                selected="",
                multiple=True,
            ),
            ui.input_selectize(
                id="age_select",
                label="Select Age Groups:",
                choices=age_group_mapping,
                selected="",
                multiple=True,
            ),

            ui.tags.hr(),
            missing_note,
            ui.tags.br(),
            class_="main-sidebar card-style",
        ),
        ui.tags.div(
            output_widget("line_plot"),
            ui.tags.hr(),
            output_widget("area_plot"),
            class_="main-main card-style",
        ),
        class_="main-layout",    
    )
    

    


@module.server
def plot_server(input, output, session, is_ds_data):
    @reactive.Calc
    def data():
        if is_ds_data():
            return plot_data_malaria
        return plot_data_denggi

    graph_type = reactive.Calc(lambda: input.graph_type())
    selected_graph_type = reactive.Effect(lambda: input.graph_type())

    @reactive.Effect
    def slider_ui():
        ui.update_slider(
            id = "years_value",
            label="Select year",
            min=2010,
            max=2021,
            value=[2015,2020],
        )

        

    @reactive.Calc
    def fig_one():
        if graph_type() == "Year":
            return create_line(
                data=data(),
                year_range=input.years_value(),
                state=input.state_select(),
                y_from="Grand Total",
                title="Line",
                labels={
                    "Year": "Year",
                    "Grand Total": "Grand Total"
                },
            )
        else:
            return create_histogram(
                data=data(),
                year=input.years_value(),
                state=input.state_select(),
                y_from="Num_of_Age",
                title="Histogram",
                labels={
                    "Age": "Age",
                    "Num_of_Age": "Num_of_Age"
                },
                age_group_mapping=age_group_mapping,
                selected_ages=input.age_select()
            )

    @reactive.Calc
    def fig_two():
        if graph_type() == "Year":
            return create_area(
                data=data(),
                year_range=input.years_value(),
                state=input.state_select(),
                y_from="Grand Total",
                title="Area",
                labels={
                    "Year": "Year",
                    "Grand Total": "Grand Total"
                },
            )
        else:
            return create_bar(
                data=data(),
                year=input.years_value(),
                state=input.state_select(),
                y_from="Num_of_Age",
                title="Bar",
                labels={
                    "Age": "Age",
                    "Num_of_Age": "Num_of_Age"
                },
                age_group_mapping=age_group_mapping,
                selected_ages=input.age_select()
            )

    @output(suspend_when_hidden=False)
    @render_widget
    def line_plot():
        return fig_one()

    @output(suspend_when_hidden=False)
    @render_widget
    def area_plot():
        return fig_two()
    

        
    