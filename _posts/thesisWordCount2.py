import plotly.graph_objects as go
import plotly.offline as offline
import pandas as pd
import matplotlib.dates as mdates

title = 'Word count'
labels = ['Total', 'Introduction', 'Theory', 'Methods', 'Chp1', 'Chp2', 'Conc']
colors = ['rgb(57,106,177)', 'rgb(218,124,48)', 'rgb(62,150,81)', 'rgb(204,37,41)', 'rgb(83,81,84)', 'rgb(107,76,154)', 'rgb(146,36,40)', 'rgb(148,139,61)', 'rgb(189,189,189)']


mode_size = 12
line_size = 2.5
labelpos = [20480, 1200, 7930, 2334, 4600, 3400, 100]


# Read in data
file = 'thesisWordCount.csv'
dat = pd.read_csv(file)

# Convert dates to something that matplotlib can handle better
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
months_fmt = mdates.DateFormatter('%b')
#dat['Date'] = mdates.datestr2num(dat['Date'])

fig = go.Figure()

for i in range(0, 7):
    fig.add_trace(go.Scatter(x=dat['Date'], y=dat[labels[i]], mode='lines',
        name=labels[i],
        line=dict(color=colors[i], width=line_size),
        connectgaps=True,
    ))

    ## endpoints
    # fig.add_trace(go.Scatter(
        #x=[dat['Date'][0], dat['Date'][35]],
        #y=[dat['Total'][0], dat['Total'][35]],
        #mode='markers',
        #marker=dict(color=colors[i], size=mode_size)
    #))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=16,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        #title='Word count',
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=16,
            color='rgb(82, 82, 82)',
        ),
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=40,
        r=145,
        t=50,
    ),
    showlegend=False,
    legend=dict(y=0.5, font_size=16),
    plot_bgcolor='white'
)

annotations = []

# Adding labels
for y_trace, label, color, pos in zip(dat, labels, colors, labelpos):
    # labeling the right_side of the plot
    annotations.append(dict(xref='paper', x=1, y=pos,
                                  xanchor='left', yanchor='middle',
                                  text=label,
                                  font=dict(family='Arial',
                                            size=16,
                                            color=color),
                                  showarrow=False))
# Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                  xanchor='left', yanchor='bottom',
                                  text=title,
                                  font=dict(family='Arial',
                                            size=24,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))

fig.update_layout(annotations=annotations)

# fig.show()
offline.plot(fig, filename='thesisWordCount.html')
