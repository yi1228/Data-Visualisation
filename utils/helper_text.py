from htmltools import TagList, tags

about_text = TagList(
    tags.h3("About"),
    tags.br(),
    tags.p(
        """
        This application provides a visual overview of
        malaria and dengue diseases in Malaysia over the
        years and their potential relationships in prevalence.
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

slider_text_map = tags.p(
    """
    Please use the slider below to choose the year. The map will
    reflect data for the input
    """,
    tags.br(),
    style="""
    text-align: justify;
    word-break:break-word;
    hyphens: auto;
    """,
)

slider_text_plot = tags.p(
    """
    Please use the slider below to change the years as well as the
    dropdown to select the countries to compare. By default, the mean
    data for the World is plotted.
    """,
    style="""
    text-align: justify;
    word-break:break-word;
    hyphens: auto;
    """,
)

dataset_information = TagList(
    tags.strong(tags.h3("Dataset Information")),
    tags.p(
        """
        For the app, we have chosen data from the World Bank and
        Organisation for Economic Co-operation and Development (OECD).
        Also, for the data regarding the Death Rate, we relied on
        Our World in Data. References
        to all three can be found below.
        """,
        style="""
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
    tags.ul(
        tags.li(
            tags.a(
                "World Bank",
                href=(
                    "https://data.worldbank.org/indicator/"
                    + "EN.ATM.PM25.MC.M3"
                ),
            )
        ),
        tags.li(
            tags.a(
                "OECD",
                href=(
                    "https://stats.oecd.org/"
                    + "Index.aspx?DataSetCode=EXP_PM2_5"
                ),
            )
        ),
        tags.li(
            tags.a(
                "Our World in Data",
                href=(
                    "https://ourworldindata.org/"
                    + "grapher/respiratory-disease-death-rate"
                ),
            )
        ),
    ),
)

missing_note = TagList(
    tags.br(),
    
    tags.p(


        tags.strong("Note: "),
        """


        Note: Dengue and malaria data are collected every year from 2010 to
        2021. That is, dengue fever only provides data after 2010, but dengue
        fever data in 2014 is missing. Malaria data only provide data after
        2011, but malaria data in 2016 are missing.

        """,
        style="""
        font-size: 17px;
        text-align: justify;
        word-break:break-word;
        hyphens: auto;
        """,
    ),
)

