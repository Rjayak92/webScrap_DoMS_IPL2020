import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
from webscrap import team1_points,team2_points,team3_points,team4_points,team5_points,team6_points,team7_points,team8_points

#creating seperate cards for each team players individual scores
card1 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Pitch Smashers", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team1_points.columns],
                    data=team1_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card2 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Ground Breakers", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team2_points.columns],
                    data=team2_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)


card3 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Blazing Strikers", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team3_points.columns],
                    data=team3_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card4 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Kings Guard", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team4_points.columns],
                    data=team4_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card5 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("DOMinatorS", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team5_points.columns],
                    data=team5_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card6 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Dragon Hearts", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team6_points.columns],
                    data=team6_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card7 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Brijesh", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team7_points.columns],
                    data=team7_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)

card8 = dbc.Card(
    [
        dbc.CardBody(
            [

                html.H5("Karandeep", className="card-title"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in team8_points.columns],
                    data=team8_points.to_dict('records'),
                    style_cell_conditional=[
                            {
                                'if': {'column_id': 'Player Name'},
                                'textAlign': 'left'
                            }
                        ],
                )

            ]
        ),
    ],
)