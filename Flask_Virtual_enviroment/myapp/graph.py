import pygal
from pygal.style import Style
custom_style = Style(
legend_font_size =22.0,
value_font_size =22.0,
tooltip_font_size =22.0,
major_label_font_size =22.0,
label_font_sioze =22.0, plot_background='#f9f9f9',
value_label_font_size =22.0,
title_font_size =26.0,
    colors=('#0ba0e5', '#e8102d', '#df34f9'))
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

def plotting(title, arg1, arg2, arg3, val1, val2, val3):

    pie_chart = pygal.Pie(half_pie=True,  style=custom_style)
    pie_chart.title = title
    pie_chart.add(arg1, val1)
    pie_chart.add(arg2, val2)
    pie_chart.add(arg3, val3)
    return pie_chart.render_data_uri()


def plotting_2(title, arg1, arg2, val1, val2):
    pie_chart = pygal.Pie(inner_radius=.3, style=custom_style)
    pie_chart.title = title
    pie_chart.add(arg1, val1)
    pie_chart.add(arg2, val2)
    return pie_chart.render_data_uri()


# plotting('Wins, looses and Draws on home venue','Home Team','Away Team','Draws',cp,cp1,cp2)
# plotting('Wins, looses and Draws on away venue','Home Team','Away Team','Draws',aw,al,ad)
# plotting('Total Wins, looses and Draws','Home Team','Away Team','Draws',cp+aw,cp1+al,cp2+ad)
# plotting_2('Goals Scored and concede on home venue','Home Goals','Away Goals',homegoalsScored,homegoalsconcede)
# plotting_2('Goals Scored and concede on away venue','Home Goals','Away Goals',awaygoalsScored,awaygoalsconcede)
# plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)
# plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)
# plotting_2('Possesion by home team in home venue ','Home Possesion','Away Possession',homePossession/count,100-(homePossession/count))
# plotting_2('Total Possession ','Home Possesion','Away Possession',(homePossession+awayPossession)/(count*2),100-((homePossession+awayPossession)/(count*2)))
# plotting_2('Fouls by home team in home venue ','Home Fouls','Away Fouls',homeFoulshome,awayFoulshome)
# plotting_2('Fouls by home team in away venue ','Home Fouls','Away Fouls',homeFoulsaway,awayFoulsaway)
# plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
# plotting_2('Offsides by home team in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides, awayOffsides)
# plotting_2('Offsides by home team in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides, AhomeOffsides)