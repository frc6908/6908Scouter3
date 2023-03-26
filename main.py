"""!DOCTYPE python"""

import pickle
from flask import Flask, render_template, redirect, url_for
#from flask_wtf.csrf import CSRFProtect
from database import getAllTeams, newTeam, teamPitScout, enterMatch, getTeamMatchNums
from forms import NewTeamData, match_One, match_Two, match_Three, match_Four, match_Five, match_Six, match_Seven, match_Eight, match_Nine, match_Ten, match_Eleven, match_Twelve, match_Thirteen, match_Fourteen, match_Fifteen, pitScout


app = Flask(__name__)
app.app_context().push()

@app.route("/", methods=['GET', 'POST'])
def home():
  teamList = getAllTeams()
  form = NewTeamData()
  if form.validate_on_submit():
      print('data submitted')
      newTeam(form.teamNum.data, form.teamName.data)
      return redirect(url_for('home'))
  return render_template('home.html', form=form, teamList=teamList)


@app.route("/<team>", methods=['GET', 'POST'])
def team_one(team):
    form_one = match_One()
    form_two = match_Two()
    form_three=match_Three()
    form_four=match_Four()
    form_five=match_Five()
    form_six=match_Six()
    form_seven=match_Seven()
    form_eight=match_Eight()
    form_nine=match_Nine()
    form_ten=match_Ten()
    form_eleven=match_Eleven()
    form_twelve=match_Twelve()
    form_thirteen=match_Thirteen()
    form_fourteen=match_Fourteen()
    form_fifteen=match_Fifteen()
    pit_scout = pitScout()
    teamnums = getTeamMatchNums(team)
    if form_one.submit.data and form_one.validate_on_submit():
        print("form one!")
        enterMatch(team, form_one.autonPoints.data, form_one.conesPlaced.data, form_one.boxesPlaced.data, form_one.numOfLinks.data, form_one.coopGrid.data, form_one.balanced.data, form_one.extra.data, '1')
        return redirect("https://6908scouter.ahanjaiswal.repl.co/" + team)
    if form_two.submit2.data and form_two.validate_on_submit():
        print("form two!")
        print(form_two.autonPoints2.data)
        enterMatch(team, form_two.autonPoints2.data, form_two.conesPlaced2.data, form_two.boxesPlaced2.data, form_two.numOfLinks2.data, form_two.coopGrid2.data, form_two.balanced2.data, form_two.extra2.data, '2')
        return redirect("https://6908scouter.ahanjaiswal.repl.co/" + team)
    if form_three.submit3.data and form_three.validate_on_submit():
        enterMatch(team, form_three.autonPoints3.data, form_three.conesPlaced3.data, form_three.boxesPlaced3.data, form_three.numOfLinks3.data, form_three.coopGrid3.data, form_three.balanced3.data, form_three.extra3.data, '3')
        return redirect("https://6908scouter.ahanjaiswal.repl.co/" + team)
    if form_four.submit4.data and form_four.validate_on_submit():
      enterMatch(team, form_four.autonPoints4.data, form_four.conesPlaced4.data, form_four.boxesPlaced4.data, form_four.numOfLinks4.data, form_four.coopGrid4.data, form_four.balanced4.data, form_four.extra4.data, '4')
    if form_five.submit5.data and form_five.validate_on_submit():
      enterMatch(team, form_five.autonPoints5.data, form_five.conesPlaced5.data, form_five.boxesPlaced5.data, form_five.numOfLinks5.data, form_five.coopGrid5.data, form_five.balanced5.data, form_five.extra5.data, '5')
    if form_six.submit6.data and form_six.validate_on_submit():
      enterMatch(team, form_six.autonPoints6.data, form_six.conesPlaced6.data, form_six.boxesPlaced6.data, form_six.numOfLinks6.data, form_six.coopGrid6.data, form_six.balanced6.data, form_six.extra6.data, '6')
    if form_seven.submit7.data and form_seven.validate_on_submit():
      enterMatch(team, form_seven.autonPoints7.data, form_seven.conesPlaced7.data, form_seven.boxesPlaced7.data, form_seven.numOfLinks7.data, form_seven.coopGrid7.data, form_seven.balanced7.data, form_seven.extra7.data, '7')
    if form_eight.submit8.data and form_eight.validate_on_submit():
      enterMatch(team, form_eight.autonPoints8.data, form_eight.conesPlaced8.data, form_eight.boxesPlaced8.data, form_eight.numOfLinks8.data, form_eight.coopGrid8.data, form_eight.balanced8.data, form_eight.extra8.data, '8')
    if form_nine.submit9.data and form_nine.validate_on_submit():
      enterMatch(team, form_nine.autonPoints9.data, form_nine.conesPlaced9.data, form_nine.boxesPlaced9.data, form_nine.numOfLinks9.data, form_nine.coopGrid9.data, form_nine.balanced9.data, form_nine.extra9.data, '9')
    if form_ten.submit10.data and form_ten.validate_on_submit():
      enterMatch(team, form_ten.autonPoints10.data, form_ten.conesPlaced10.data, form_ten.boxesPlaced10.data, form_ten.numOfLinks10.data, form_ten.coopGrid10.data, form_ten.balanced10.data, form_ten.extra10.data, '10')
    if form_eleven.submit11.data and form_eleven.validate_on_submit():
      enterMatch(team, form_eleven.autonPoints11.data, form_eleven.conesPlaced11.data, form_eleven.boxesPlaced11.data, form_eleven.numOfLinks11.data, form_eleven.coopGrid11.data, form_eleven.balanced11.data, form_eleven.extra11.data, '11')
    if form_twelve.submit12.data and form_twelve.validate_on_submit():
      enterMatch(team, form_twelve.autonPoints12.data, form_twelve.conesPlaced12.data, form_twelve.boxesPlaced12.data, form_twelve.numOfLinks12.data, form_twelve.coopGrid12.data, form_twelve.balanced12.data, form_twelve.extra12.data, '12')
    if form_thirteen.submit13.data and form_thirteen.validate_on_submit():
      enterMatch(team, form_thirteen.autonPoints13.data, form_thirteen.conesPlaced13.data, form_thirteen.boxesPlaced13.data, form_thirteen.numOfLinks13.data, form_thirteen.coopGrid13.data, form_thirteen.balanced13.data, form_thirteen.extra13.data, '13')
    if form_fourteen.submit14.data and form_fourteen.validate_on_submit():
      enterMatch(team, form_fourteen.autonPoints14.data, form_fourteen.conesPlaced14.data, form_fourteen.boxesPlaced14.data, form_fourteen.numOfLinks14.data, form_fourteen.coopGrid14.data, form_fourteen.balanced14.data, form_fourteen.extra14.data, '14')
    if form_fifteen.submit15.data and form_fifteen.validate_on_submit():
      enterMatch(team, form_fifteen.autonPoints15.data, form_fifteen.conesPlaced15.data, form_fifteen.boxesPlaced15.data, form_fifteen.numOfLinks15.data, form_fifteen.coopGrid15.data, form_fifteen.balanced15.data, form_fifteen.extra15.data, '15')
    if pit_scout.submitPit.data and pit_scout.validate_on_submit():
        print("pitscout!")
        teamPitScout(team, pit_scout.autoBalance.data, pit_scout.coneIntake.data, pit_scout.cubeIntake.data, pit_scout.typeOfAuton.data, pit_scout.extrapit.data)
        return redirect("https://6908scouter.ahanjaiswal.repl.co/" + team)
      
    return render_template('base.html', form1=form_one, form2=form_two, form3 = form_three, form4 = form_four, form5 = form_five, form6 = form_six, form7 = form_seven, form8 = form_eight, form9 = form_nine, form10 = form_ten, form11 = form_eleven, form12 = form_twelve, form13 = form_thirteen, form14 = form_fourteen, form15 = form_fifteen, pitscout = pit_scout, teamNum=team, teamnums = teamnums)


if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )