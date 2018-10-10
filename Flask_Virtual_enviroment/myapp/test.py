from flask import Flask, render_template
from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SelectField, StringField

from graph import plotting, plotting_2, plotting3, draws, goals
app = Flask(__name__)
app.config['SECRET_KEY'] = 'OurSecretkey'


@app.route('/')
def index():
    return render_template('checkfile.html')

@app.route('/prediction' , methods=['GET'])
def prediction():
    return render_template('prediction.html')

@app.route('/admin' , methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/navbar', methods=['GET'])
def navbar():
    return render_template('navbar.html')

@app.route('/barcapage', methods=['GET'])
def barcapage():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row['awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Barcelona']
    barcaAway = laliga[laliga.awayTeam == 'Barcelona']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Barcelona']
    barcaAway = laliga[laliga.awayTeam == 'Barcelona']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data =plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1=plotting('Result on Away Venue','Home Team','Away Team','Draws',aw,al,ad)
    graph_data_2=plotting('Matches won','Home Team','Away Team','Draws',cp+aw,cp1+al,cp2+ad)
    #graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 =plotting_2('Goals Scored and concede on Home venue','Home Goals','Away Goals',homegoalsScored,homegoalsconcede)
    graph_data_4 =plotting_2('Goals Scored and concede on Away venue','Home Goals','Away Goals',awaygoalsScored,awaygoalsconcede)
    graph_data_5 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession', homePossession / count, 100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7=plotting_2('Total Possession ','Home Possesion','Away Possession',(homePossession+awayPossession)/(count*2),100-((homePossession+awayPossession)/(count*2)))
    graph_data_8 = plotting_2('Fouls in home venue ','Home Fouls','Away Fouls',homeFoulshome,awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ','Home Fouls','Away Fouls',homeFoulsaway,awayFoulsaway)
    graph_data_10 =plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 =plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides, awayOffsides)
    graph_data_12 =plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides, AhomeOffsides)
    return render_template("barca.html", graph_data=graph_data, graph_data_1=graph_data_1,graph_data_2=graph_data_2,graph_data_3=graph_data_3, graph_data_4=graph_data_4,graph_data_5=graph_data_5,graph_data_6=graph_data_6, graph_data_7=graph_data_7,graph_data_8=graph_data_8,graph_data_9=graph_data_9, graph_data_10=graph_data_10,graph_data_11=graph_data_11,graph_data_12=graph_data_12)

@app.route('/madridpage', methods=['GET'])
def madridpage():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row['awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Real Madrid']
    barcaAway = laliga[laliga.awayTeam == 'Real Madrid']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Real Madrid']
    barcaAway = laliga[laliga.awayTeam == 'Real Madrid']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data =plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1=plotting('Result on Away Venue','Home Team','Away Team','Draws',aw,al,ad)
    graph_data_2=plotting('Matches won','Home Team','Away Team','Draws',cp+aw,cp1+al,cp2+ad)
    #graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 =plotting_2('Goals Scored and concede on Home venue','Home Goals','Away Goals',homegoalsScored,homegoalsconcede)
    graph_data_4 =plotting_2('Goals Scored and concede on Away venue','Home Goals','Away Goals',awaygoalsScored,awaygoalsconcede)
    graph_data_5 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession', homePossession / count, 100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7=plotting_2('Total Possession ','Home Possesion','Away Possession',(homePossession+awayPossession)/(count*2),100-((homePossession+awayPossession)/(count*2)))
    graph_data_8 =plotting_2('Fouls in home venue ','Home Fouls','Away Fouls',homeFoulshome,awayFoulshome)
    graph_data_9 =plotting_2('Fouls in away venue ','Home Fouls','Away Fouls',homeFoulsaway,awayFoulsaway)
    graph_data_10 =plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 =plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides, awayOffsides)
    graph_data_12 =plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides, AhomeOffsides)
    return render_template("realmadrid.html", graph_data=graph_data, graph_data_1=graph_data_1,graph_data_2=graph_data_2,graph_data_3=graph_data_3, graph_data_4=graph_data_4,graph_data_5=graph_data_5,graph_data_6=graph_data_6, graph_data_7=graph_data_7,graph_data_8=graph_data_8,graph_data_9=graph_data_9, graph_data_10=graph_data_10,graph_data_11=graph_data_11,graph_data_12=graph_data_12)

@app.route('/atletico', methods=['GET'])
def atletico():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row['awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Atletico']
    barcaAway = laliga[laliga.awayTeam == 'Atletico']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Atletico']
    barcaAway = laliga[laliga.awayTeam == 'Atletico']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession', homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides, awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides, AhomeOffsides)
    return render_template("atletico.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/sevilla', methods=['GET'])
def sevilla():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Sevilla']
    barcaAway = laliga[laliga.awayTeam == 'Sevilla']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Atletico']
    barcaAway = laliga[laliga.awayTeam == 'Atletico']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("sevilla.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/valencia' , methods=['GET'])
def valencia():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Valencia']
    barcaAway = laliga[laliga.awayTeam == 'Valencia']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Valencia']
    barcaAway = laliga[laliga.awayTeam == 'Valencia']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("Valencia.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/betis', methods=['GET'])
def betis():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Real Betis']
    barcaAway = laliga[laliga.awayTeam == 'Real Betis']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Real Betis']
    barcaAway = laliga[laliga.awayTeam == 'Real Betis']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("betis.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/athletic' , methods=['GET'])
def athletic():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Real Betis']
    barcaAway = laliga[laliga.awayTeam == 'Real Betis']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Athletic Club']
    barcaAway = laliga[laliga.awayTeam == 'Athletic Club']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored
    totalConcede = homegoalsconcede + awaygoalsconcede
    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("athletic.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/villareal' , methods=['GET'])
def villareal():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Villareal']
    barcaAway = laliga[laliga.awayTeam == 'Villareal']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Villareal']
    barcaAway = laliga[laliga.awayTeam == 'Villareal']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)

    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("villareal.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)

@app.route('/getafe' , methods=['GET'])
def getafe():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')
    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row[
            'awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    barcelona = laliga[laliga.homeTeam == 'Getafe']
    barcaAway = laliga[laliga.awayTeam == 'Getafe']
    x = pd.DataFrame(barcelona)
    cp = 0
    cp1 = 0
    cp2 = 0
    tot = 0
    for index, row in x.iterrows():
        tot += 1
        if (row['local_team_won'] == 1):
            cp = cp + 1
        elif (row['visitor_team_won'] == 1):
            cp1 = cp1 + 1
        elif (row['draw'] == 1):
            cp2 = cp2 + 1
    print('Total no of home games are', tot)
    print('Total no of home wins are', cp)
    print('Total no of home looses are', cp1)
    print('Total no of home draws are', cp2)
    x = pd.DataFrame(barcaAway)
    aw = 0
    al = 0
    ad = 0
    at = 0
    for index, row in x.iterrows():
        at += 1
        if (row['local_team_won'] == 1):
            al = al + 1
        elif (row['visitor_team_won'] == 1):
            aw = aw + 1
        elif (row['draw' == 1]):
            ad = ad + 1
    print('Total no of away games are', at)
    print('Total no of away wins are', aw)
    print('Total no of away looses are', al)
    print('Total no of away draws are', ad)
    print('Average won draw and loose are')
    print('Total     wins         looses        draws')
    print(tot + at, '      ', cp + aw, '        ', cp2 + al, '          ', cp2 + ad)
    barcelona = laliga[laliga.homeTeam == 'Villareal']
    barcaAway = laliga[laliga.awayTeam == 'Villareal']
    x = pd.DataFrame(barcelona)
    homegoalsScored = 0
    homegoalsconcede = 0
    awaygoalsScored = 0
    awaygoalsconcede = 0

    for index, row in x.iterrows():
        homegoalsScored = homegoalsScored + row['homeGoalFT']
        homegoalsconcede = homegoalsconcede + row['awayGoalFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awaygoalsScored = awaygoalsScored + row['awayGoalFT']
        awaygoalsconcede = awaygoalsconcede + row['homeGoalFT']
    print('Home Goals scored are ', homegoalsScored)
    print('Home Goals concede are ', homegoalsconcede)
    print('Away Goals scored are ', awaygoalsScored)
    print('Away Goals concede are ', awaygoalsconcede)

    totalGoals = homegoalsScored + awaygoalsScored

    totalConcede = homegoalsconcede + awaygoalsconcede

    print('Total:    Scored      Concede')
    print('         ', totalGoals, '     ', totalConcede)
    x = pd.DataFrame(barcelona)
    homePossession = 0
    awayPossession = 0
    totalPossession = 0
    count = 0
    for index, row in x.iterrows():
        count += 1
        homePossession += row['homePossessionFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        awayPossession += row['awayPossessionFT']
    print('Home possesion average', homePossession / count)
    print('Away possesion average', awayPossession / count)
    print('Total possesion average', (homePossession + awayPossession) / (count * 2))
    x = pd.DataFrame(barcelona)
    homeFoulshome = 0
    awayFoulshome = 0
    homeFoulsaway = 0
    awayFoulsaway = 0
    totalFouls = 0
    for index, row in x.iterrows():
        homeFoulshome += row['homeFoulsCommitedFT']
        awayFoulshome += row['awayFoulsCommitedFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        homeFoulsaway += row['awayFoulsCommitedFT']
        awayFoulsaway += row['homeFoulsCommitedFT']
    print('Home fouls in home ground = ', homeFoulshome)
    print('away fouls in home ground = ', awayFoulshome)
    print('Home fouls in away ground = ', homeFoulsaway)
    print('away fouls in away ground = ', awayFoulsaway)
    totalFoulsHome = homeFoulshome + homeFoulsaway
    totalFoulsAway = awayFoulshome + awayFoulsaway
    print('Total Fouls done = ', totalFoulsHome)
    print('Total Fouls suffer = ', totalFoulsAway)
    x = pd.DataFrame(barcelona)
    homeShots = 0
    awayShots = 0

    homeShotsOnTarget = 0
    awayShotsOnTarget = 0

    AhomeShots = 0
    AawayShots = 0

    AhomeShotsOnTarget = 0
    AawayShotsOnTarget = 0

    for index, row in x.iterrows():
        homeShots += row['homeShotsTotalFT']
        homeShotsOnTarget += row['homeShotsOnTargetFT']
        awayShots += row['awayShotsTotalFT']
        awayShotsOnTarget += row['awayShotsOnTargetFT']
    x = pd.DataFrame(barcaAway)
    for index, row in x.iterrows():
        AhomeShots += row['awayShotsTotalFT']
        AhomeShotsOnTarget += row['awayShotsOnTargetFT']
        AawayShots += row['homeShotsTotalFT']
        AawayShotsOnTarget += row['homeShotsOnTargetFT']
    print('Home shots attempt on home venue = ', homeShots)
    print('Home shots on target on home venue = ', homeShotsOnTarget)
    print('Away shots attempt on home venue = ', awayShots)
    print('Away shots on target on home venue = ', awayShotsOnTarget)
    print('Home shots attempt on away venue = ', AhomeShots)
    print('Home shots on target on away venue = ', AhomeShotsOnTarget)
    print('Away shots attempt on away venue = ', AawayShots)
    print('Away shots on target on away venue = ', AawayShotsOnTarget)
    x = pd.DataFrame(barcelona.head(50))
    homeOffsides = 0
    awayOffsides = 0
    AhomeOffsides = 0
    AawayOffsides = 0
    totalOffsides = 0
    for index, row in x.iterrows():
        homeOffsides += row['homeOffsidesCaughtFT']
        awayOffsides += row['awayOffsidesCaughtFT']

    x = pd.DataFrame(barcaAway.head(50))
    for index, row in x.iterrows():
        AhomeOffsides += row['awayOffsidesCaughtFT']
        AawayOffsides += row['homeOffsidesCaughtFT']
    print('Home offsides in home venue ', homeOffsides)
    print('Away offsides in home venue ', awayOffsides)
    print('Home offsides in away venue ', AawayOffsides)
    print('Away offsides in away venue ', AhomeOffsides)
    graph_data = plotting('Result on Home Venue', 'Home Team', 'Away Team', 'Draws', cp, cp1, cp2)
    graph_data_1 = plotting('Result on Away Venue', 'Home Team', 'Away Team', 'Draws', aw, al, ad)
    graph_data_2 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    # graph_data_3 = plotting('Matches won', 'Home Team', 'Away Team', 'Draws', cp + aw, cp1 + al, cp2 + ad)
    graph_data_3 = plotting_2('Goals Scored and concede on Home venue', 'Home Goals', 'Away Goals', homegoalsScored,
                              homegoalsconcede)
    graph_data_4 = plotting_2('Goals Scored and concede on Away venue', 'Home Goals', 'Away Goals', awaygoalsScored,
                              awaygoalsconcede)
    graph_data_5 = plotting_2('Total goals Scored and concede ', 'Total Goals Scored', 'Total Goals Concede',
                              totalGoals, totalConcede)
    graph_data_6 = plotting_2('Possesion in home venue ', 'Home Possesion', 'Away Possession',
                              homePossession / count,
                              100 - (homePossession / count))
    # graph_data_6 =plotting_2('Total goals Scored and concede ','Total Goals Scored','Total Goals Concede',totalGoals,totalConcede)
    graph_data_7 = plotting_2('Total Possession ', 'Home Possesion', 'Away Possession',
                              (homePossession + awayPossession) / (count * 2),
                              100 - ((homePossession + awayPossession) / (count * 2)))
    graph_data_8 = plotting_2('Fouls in home venue ', 'Home Fouls', 'Away Fouls', homeFoulshome, awayFoulshome)
    graph_data_9 = plotting_2('Fouls in away venue ', 'Home Fouls', 'Away Fouls', homeFoulsaway, awayFoulsaway)
    graph_data_10 = plotting_2('Total Fouls ', 'Home Fouls', 'Away Fouls', totalFoulsHome, totalFoulsAway)
    graph_data_11 = plotting_2('Offsides  in home venue ', 'homeOffsides', 'awayOffsides', homeOffsides,
                               awayOffsides)
    graph_data_12 = plotting_2('Offsides  in away venue ', 'homeOffsides', 'awayOffsides', AawayOffsides,
                               AhomeOffsides)
    return render_template("getafe.html", graph_data=graph_data, graph_data_1=graph_data_1,
                           graph_data_2=graph_data_2, graph_data_3=graph_data_3, graph_data_4=graph_data_4,
                           graph_data_5=graph_data_5, graph_data_6=graph_data_6, graph_data_7=graph_data_7,
                           graph_data_8=graph_data_8, graph_data_9=graph_data_9, graph_data_10=graph_data_10,
                           graph_data_11=graph_data_11, graph_data_12=graph_data_12)
@app.route('/club', methods=['GET'])
def club():
    return render_template('club.html')

@app.route('/compareteams', methods = ['GET'])
def compareteams():
    laliga = pd.read_csv('F:\\Python Projects\\Flask_Virtual_enviroment\\Talha_app\\FootballEurope.csv')

    laliga['winner'] = laliga.apply(
        lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 2 if row['homeGoalFT'] < row['awayGoalFT'] else 0,
        axis=1)
    laliga = laliga[laliga.division == 'La_Liga']
    laliga['local_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] > row['awayGoalFT'] else 0, axis=1)
    laliga['visitor_team_won'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] < row['awayGoalFT'] else 0, axis=1)
    laliga['draw'] = laliga.apply(lambda row: 1 if row['homeGoalFT'] == row['awayGoalFT'] else 0, axis=1)
    ElClassico = laliga
    Barcelona = ElClassico[((ElClassico.homeTeam == 'Barcelona') | (ElClassico.awayTeam == 'Barcelona'))]
    Madrid = ElClassico[((ElClassico.homeTeam == 'Real Madrid') | (ElClassico.awayTeam == 'Real Madrid'))]
    BarcaHome = Barcelona[Barcelona.homeTeam == 'Barcelona']
    BarcaAway = Barcelona[Barcelona.awayTeam == 'Barcelona']
    MadridHome = Madrid[Madrid.homeTeam == 'Real Madrid']
    MadridAway = Madrid[Madrid.awayTeam == 'Real Madrid']

    # In[4]:

    BarcaWins = BarcaHome['local_team_won'].sum() + BarcaAway['visitor_team_won'].sum()
    BarcaLooses = BarcaAway['local_team_won'].sum() + BarcaHome['visitor_team_won'].sum()
    MadridWins = MadridHome['local_team_won'].sum() + MadridAway['visitor_team_won'].sum()
    MadridLooses = MadridAway['local_team_won'].sum() + MadridHome['visitor_team_won'].sum()
    barcahomeGoals = BarcaHome['homeGoalFT'].sum()
    barcaawaygoals = BarcaAway['awayGoalFT'].sum()
    madridhomeGoals = MadridHome['homeGoalFT'].sum()
    madridawaygoals = MadridAway['awayGoalFT'].sum()

    barcaPossesion =  (BarcaAway['homePossessionFT'].sum()/len(laliga)*100) + (BarcaAway['awayPossessionFT'].sum()/len(laliga)*100)
    madridpossesion = (MadridHome['homePossessionFT'].sum()/len(laliga)*100 )+ (MadridAway['awayPossessionFT'].sum()/len(laliga)*100)



    # MadridWins=MadridHome['local_team_won'].sum() + MadridAway['visitor_team_won'].sum()
    BarcaDraws = Barcelona['draw'].sum()
    MadridDraws = Madrid['draw'].sum()
    print('Barcelona win = ', BarcaWins)
    print('Barcelona looses = ', BarcaLooses)
    print('BarcaDraws draws = ', BarcaDraws)
    print('Madrid win = ', MadridWins)
    print('Madrid looses = ', MadridLooses)
    print('Madrid draws = ', MadridDraws)
    graph_data = plotting3('Number of Wins', 'Barcelona', 'RealMadrid', BarcaWins, MadridWins)
    graph_data1 = plotting3('Number of Loses', 'Barcelona', 'RealMadrid', BarcaLooses, MadridLooses)
    graph_data2 = draws('Number of Draws', 'Barcelona', 'RealMadrid', BarcaDraws, MadridDraws)
    graph_data_goals = goals('Number of Aways Goals' , 'Barcelona ' , 'RealMadrid' , barcaawaygoals , madridawaygoals)
    graph_data_homegoals = plotting3('Number of Home Goals', 'Barcelona', 'RealMadrid', barcahomeGoals, madridhomeGoals)
    possesion = goals('Possesion in Percentage %', 'Barcelona', 'RealMadrid', barcaPossesion, madridpossesion)

    return render_template('compare.html', graph_data=graph_data, graph_data1=graph_data1, graph_data2=graph_data2 , graph_data_goals = graph_data_goals , graph_data_homegoals = graph_data_homegoals,possesion = possesion)


if __name__ == "__main__":
    app.run(debug=True)
