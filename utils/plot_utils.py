import plotly.graph_objects as go
import plotly.express as px
from pandas import DataFrame

def create_line(
    data: DataFrame,
    year_range: list[int],
    state: str,
    y_from: str,
    title: str,
    labels: dict,
) -> go.FigureWidget:
    if year_range[0] != year_range[1]:
        title = f"{title} - {year_range[0]} to {year_range[1]}"
    else:
        title = f"{title} - {year_range[0]}"
    plot_data = data[data["Year"].between(year_range[0], year_range[1])]
    plot_data = plot_data[plot_data["State"].isin(state)]

    fig = px.line(
        data_frame=plot_data,
        x="Year",
        y=y_from,
        color="State",
        title=title,
        labels=labels,
        color_discrete_sequence=px.colors.colorbrewer.Blues[1:],
    )

    fig.update_traces(
        mode="markers+lines",
        hovertemplate=None,
        line=dict(width=5),
        marker=dict(size=15),
    )
    fig.update_layout(plot_bgcolor="white", hovermode="x unified")

    fig.update_xaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)
    fig.update_yaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)

    return go.FigureWidget(fig)

def create_area(
    data: DataFrame,
    year_range: list[int],
    state: str,
    y_from: str,
    title: str,
    labels: dict,
) -> go.FigureWidget:
    if year_range[0] != year_range[1]:
        title = f"{title} - {year_range[0]} to {year_range[1]}"
    else:
        title = f"{title} - {year_range[0]}"
    plot_data = data[data["Year"].between(year_range[0], year_range[1])]
    plot_data = plot_data[plot_data["State"].isin(state)]

    fig = px.area(
        data_frame=plot_data,
        x="Year",
        y=y_from,
        color="State",
        title=title,
        labels=labels,
        color_discrete_sequence=px.colors.colorbrewer.Blues[1:],
    )

    fig.update_layout(plot_bgcolor="white", hovermode="x unified")

    fig.update_xaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)
    fig.update_yaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)

    return go.FigureWidget(fig)


def create_histogram(
    data: DataFrame,
    year: list[int],
    state: str,
    y_from: str,
    title: str,
    labels: dict,
    age_group_mapping: dict,
    selected_ages: list[str]
) -> go.FigureWidget:
    if year[0] : title = f"{title} - {year[0]}"
    plot_data = data[data["Year"] == year[0]]
    plot_data = plot_data[plot_data["State"].isin(state)]
    
    plot_data = plot_data.melt(
        id_vars=["State"],
        value_vars=selected_ages,
        var_name="Age",
        value_name="Num_of_Age"
    )
    selected_age_names = [age_group_mapping[age] for age in selected_ages]
    plot_data = plot_data[plot_data['Age'].isin(selected_ages)]
    

    fig = px.histogram(
        data_frame=plot_data,
        x="Age",  
        y="Num_of_Age",
        color="State",
        title=title,
        labels=labels,
        color_discrete_sequence=px.colors.colorbrewer.Blues[1:],
        category_orders={
            "Age": selected_age_names  
        },
    )
    fig.update_layout(plot_bgcolor="white", hovermode="x unified",barmode="group")

    fig.update_xaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)
    fig.update_yaxes(title=labels[y_from],showline=False, gridcolor="#d2d2d2", gridwidth=0.5)

    return go.FigureWidget(fig)

def create_bar(
    data: DataFrame,
    year: list[int],
    state: str,
    y_from: str,
    title: str,
    labels: dict,
    age_group_mapping: dict,
    selected_ages: list[str]  
) -> go.FigureWidget:
    if year[0] : title = f"{title} - {year[0]}"
    plot_data = data[data["Year"] == year[0]]
    plot_data = plot_data[plot_data["State"].isin(state)]
    
    plot_data = plot_data.melt(
        id_vars=["State"],
        value_vars=selected_ages,
        var_name="Age",
        value_name="Num_of_Age"
    )
    selected_age_names = [age_group_mapping[age] for age in selected_ages]
    plot_data = plot_data[plot_data['Age'].isin(selected_ages)]
    

    fig = px.bar(
        data_frame=plot_data,
        x="Age",  
        y="Num_of_Age",
        color="State",
        title=title,
        labels=labels,
        color_discrete_sequence=px.colors.colorbrewer.Blues[1:],
        category_orders={
            "Age": selected_age_names  
        },
    )
    fig.update_layout(plot_bgcolor="white", hovermode="x unified")

    fig.update_xaxes(showline=False, gridcolor="#d2d2d2", gridwidth=0.5)
    fig.update_yaxes(title=labels[y_from],showline=False, gridcolor="#d2d2d2", gridwidth=0.5)

    return go.FigureWidget(fig)