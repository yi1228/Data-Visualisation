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

