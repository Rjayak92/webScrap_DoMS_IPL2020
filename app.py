import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
import pandas as pd
from dash.exceptions import PreventUpdate
from card_contents import card1, card2, card3, card4, card5, card6, card7, card8
import dash_table
from webscrap import standing
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_core_components as dcc



app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

#copying standing dataframe for finding the top three
leader_standing = standing.copy()

#assets bar chart data points for leader board
leaderboard_datapoints = pd.DataFrame({'x':['Second','First','Third'],'y':[70,100,50]})

#returing first, second, third standings
idx = leader_standing['Scores'].idxmax()
First_Stand = '💥 ' + leader_standing.loc[idx][0]

#dropping the first top team from table to get second top
leader_standing.drop(index=idx,inplace = True)

idx2 = leader_standing['Scores'].idxmax()
Second_Stand = '💥 ' +  leader_standing.loc[idx2][0]
leader_standing.drop(index=idx2,inplace = True)

idx3 = leader_standing['Scores'].idxmax()
Third_Stand = '💥 ' + leader_standing.loc[idx3][0]

#storing the top 3 teams to send as labels for bar chart
List_table_toppers = [Second_Stand,First_Stand,Third_Stand]


#app body and layout
header = html.Div([
    dbc.Row(dbc.Col()),
    dbc.Row(dbc.Col(html.Div(html.H1("DoMS IPL Fantasy 2020 ")),style={'color': 'rgb(96, 64, 32)'},width={"offset": 4})),
    # dbc.Row(dbc.Col(html.Div(html.H4("E Sala Cuppu Namde, RCB")),width={"size":12,"offset": 1})),
])

#layout for the app
row1 = html.Div(
    [
        dbc.CardDeck(
            [
                card1,
                card2,
                card3,
                card4
            ]
        ),
    ], style={'padding': '25px'}
)
row2 = html.Div(
    [
        dbc.CardDeck(
            [
                card5,
                card6,
                card7,
                card8
            ]
        ),
    ], style={'padding': '25px'}
)
row3 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div([
                        html.Div(html.H6("Scores Table"),style={'color': 'Black'}),

                        dash_table.DataTable(
                            columns=[{"name": i, "id": i} for i in standing.columns],
                            data=standing.to_dict('records'),
                            style_cell_conditional=[
                                {
                                    'if': {'column_id': 'Team Name'},
                                    'textAlign': 'left'
                                }
                            ],
                            style_header = {'backgroundColor': 'rgb(40, 40, 164)',
                                            'border': '1px solid blue',
                                            'color': 'white'
                                            },
                            style_cell = {
                                                'backgroundColor': 'white',
                                                'color': 'black'
                                            },
                            style_data={'border': '1px solid blue'},
                        )
                    ]),width={"size":2,"offset": 2},
                ),
                dbc.Col(
                    html.Div([

                            dcc.Location(id='url', refresh=False),
                            dcc.Graph(
                                id='page-content',
                            ),
                ]),width={"size":3,"offset": 1},
                ),
            ],align="center",
        )
    ]
)
app.layout = html.Div([
    header,
    row3,
    row1,
    row2
])

#call back for dynamically updating leaderboard on load
@app.callback(Output('page-content', 'figure'),
              [Input('url', 'pathname')])

def update_page(path):
    if path is None: raise PreventUpdate
    else:
        fig = go.Figure(data=[go.Bar(
            x=leaderboard_datapoints['x'], y=leaderboard_datapoints['y'],
            text=List_table_toppers,
            textposition='auto',
            hoverinfo = 'skip',
        )])
        # fig.update_traces(textposition='outside')

        fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False,
                          xaxis_zeroline=False, yaxis_zeroline=False, bargap=.05)
        fig.update_yaxes(showticklabels=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_layout(
            # hovermode=False,
            font_family="Arial",
            title_font_color="Black",
            title = {'text':'Leader Board',
                    'y':0.9,
                    'x':0.5,
                     },
            font=dict(
                size=14,
            ),
            plot_bgcolor='white',
            autosize=False,
            width=700,
            height=450, )
        fig.update_traces(marker_color='rgb(179, 0, 0)', marker_line_color='rgb(8,48,107)',
                          marker_line_width=1.5)
        return fig




if __name__ == "__main__":
    app.run_server(debug=False)