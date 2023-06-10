import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

data = pd.read_csv('./assets/CSV/Students.csv')
data.sort_values('FIO', inplace=True)

external_stylesheets = [
    {
        'href': 'https://fonts.googleapis.com/css2?'
        'family=Lato:wght@400;700&display=swap',
        'rel': 'stylesheet',
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#2A335E',
    'text': 'White',
    'color': '#4878FB',
    'gridColor': '#3F4670',
}

pie = px.pie(data, labels=[1, 2, 3, 4, 5], values=data['Math'])

line = px.line(data, x=data['FIO'],
               y=data['Math'], hover_name=data['FIO'])

line.update_xaxes(visible=True, fixedrange=True, gridcolor=colors['gridColor'])
line.update_yaxes(visible=True, fixedrange=True, gridcolor=colors['gridColor'])

line.update_layout(
    title='Оценки по курсу "Математика"',
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    font_size=14,
    font_family='Monospace',
)


app.layout = html.Div(

    children=[
        html.Nav(
            children=[
                html.Img(src='./assets/icons/user.png', className='Img'),
                html.Img(src='./assets/icons/course.png', className='Img'),
                html.Img(src='./assets/icons/settings.png', className='Img'),
            ],
            id="nav"
        ),
        html.Div(
            children=[
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
                html.Div(children=dcc.Graph(figure=line), className='Graph'),
            ],
            id='graphBlocks'
        )
    ],
    id='main'
)


if __name__ == '__main__':
    app.run_server(debug=True)
