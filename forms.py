from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField


class NewTeamData(FlaskForm):
    class Meta():
        csrf = False

    teamNum = StringField('Enter new Team Number')
    teamName = StringField('Enter new Team Name')
    # match1Num = StringField('Enter Match 1')
    # match2Num = StringField('Enter Match 2')
    # match3Num = StringField('Enter Match 3')
    newDataSubmit = SubmitField('Submit New Team Entry')


class pitScout(FlaskForm):
    class Meta():
        csrf = False

    autoBalance = BooleanField('Automatic Balance')
    coneIntake = BooleanField('Cone Intake')
    cubeIntake = BooleanField('Cube Intake')
    typeOfAuton = StringField('Type of Auton')
    extrapit = TextAreaField('Extra Pit', render_kw={"rows": 6, "cols": 40})
    submitPit = SubmitField('Submit Data')


class MatchForm(FlaskForm):
    class Meta:
        csrf = False

    def __init__(self, match_num: int, **kwargs):
        # self.autonPoints = StringField(f'Auton Points #{match_num}')
        # self.conesPlaced = StringField(f'Cones Placed #{match_num}')
        # self.boxesPlaced = StringField(f'Boxes Placed #{match_num}')
        # self.numOfLinks = StringField(f'Number of Links #{match_num}')
        # self.coopGrid = BooleanField(f"3+ Game Pieces in Coop Grid? #{match_num}")
        # self.balanced = StringField(f'Balanced (level, unlevel, none)')
        # self.extra = TextAreaField(f'Extra Notes', render_kw={"rows": 6, "cols": 40})
        # self.submit = SubmitField(f'Submit Data')
        setattr(self, "autonPoints", StringField(f'Auton Points #{match_num}'))
        setattr(self, "conesPlaced", StringField(f'Cones Placed #{match_num}'))
        setattr(self, "boxesPlaced", StringField(f'Boxes Placed #{match_num}'))
        setattr(self, "numOfLinks", StringField(f'Number of Links #{match_num}'))
        setattr(self, "coopGrid", BooleanField(f"3+ Game Pieces in Coop Grid? #{match_num}"))
        setattr(self, "balanced", StringField(f'Balanced (level, unlevel, none)'))
        setattr(self, "extra", TextAreaField(f'Extra Notes', render_kw={"rows": 6, "cols": 40}))
        setattr(self, "submit", SubmitField(f'Submit Data'))
        self._unbound_fields = self._unbound_fields + [["autonPoints", StringField(f'Auton Points #{match_num}')]]
        self._unbound_fields = self._unbound_fields + [["conesPlaced", StringField(f'Cones Placed #{match_num}')]]
        self._unbound_fields = self._unbound_fields + [["boxesPlaced", StringField(f'Boxes Placed #{match_num}')]]
        self._unbound_fields = self._unbound_fields + [["numOfLinks", StringField(f'Number of Links #{match_num}')]]
        self._unbound_fields = self._unbound_fields + [["coopGrid", BooleanField(f"3+ Game Pieces in Coop Grid? #{match_num}")]]
        self._unbound_fields = self._unbound_fields + [["balanced", StringField(f'Balanced (level, unlevel, none)')]]
        self._unbound_fields = self._unbound_fields + [["extra", TextAreaField(f'Extra Notes', render_kw={"rows": 6, "cols": 40})]]
        self._unbound_fields = self._unbound_fields + [["submit", SubmitField(f'Submit Data')]]
        super(MatchForm, self).__init__(**kwargs)


# class match_One(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints = StringField('Auton Points #1')
#     conesPlaced = StringField('Cones Placed #1')
#     boxesPlaced = StringField('Boxes Placed #1')
#     numOfLinks = StringField('Number of Links #1')
#     coopGrid = BooleanField("3+ Game Pieces in Coop Grid? #1")
#     balanced = StringField('Balanced (level, unlevel, none)')
#     extra = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit = SubmitField('Submit Data')
#
#
# class match_Two(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints2 = StringField('Auton Points #2')
#     conesPlaced2 = StringField('Cones Placed #2')
#     boxesPlaced2 = StringField('Boxes Placed #2')
#     numOfLinks2 = StringField('Number of Links #2')
#     coopGrid2 = BooleanField("3+ Game Pieces in Coop Grid? #2")
#     balanced2 = StringField('Balanced (level, unlevel, none)')
#     extra2 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit2 = SubmitField('Submit Data')
#
#
# class match_Three(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints3 = StringField('Auton Points #3')
#     conesPlaced3 = StringField('Cones Placed #3')
#     boxesPlaced3 = StringField('Boxes Placed #3')
#     numOfLinks3 = StringField('Number of Links #3')
#     coopGrid3 = BooleanField("3+ Game Pieces in Coop Grid? #3")
#     balanced3 = StringField('Balanced (level, unlevel, none)')
#     extra3 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit3 = SubmitField('Submit Data')
#
#
# class match_Four(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints4 = StringField('Auton Points #4')
#     conesPlaced4 = StringField('Cones Placed #4')
#     boxesPlaced4 = StringField('Boxes Placed #4')
#     numOfLinks4 = StringField('Number of Links #4')
#     coopGrid4 = BooleanField("3+ Game Pieces in Coop Grid? #4")
#     balanced4 = StringField('Balanced (level, unlevel, none)')
#     extra4 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit4 = SubmitField('Submit Data')
#
#
# class match_Five(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints5 = StringField('Auton Points #5')
#     conesPlaced5 = StringField('Cones Placed #5')
#     boxesPlaced5 = StringField('Boxes Placed #5')
#     numOfLinks5 = StringField('Number of Links #5')
#     coopGrid5 = BooleanField("3+ Game Pieces in Coop Grid? #5")
#     balanced5 = StringField('Balanced (level, unlevel, none)')
#     extra5 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit5 = SubmitField('Submit Data')
#
#
# class match_Six(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints6 = StringField('Auton Points #6')
#     conesPlaced6 = StringField('Cones Placed #6')
#     boxesPlaced6 = StringField('Boxes Placed #6')
#     numOfLinks6 = StringField('Number of Links #6')
#     coopGrid6 = BooleanField("3+ Game Pieces in Coop Grid? #6")
#     balanced6 = StringField('Balanced (level, unlevel, none)')
#     extra6 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit6 = SubmitField('Submit Data')
#
#
# class match_Seven(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints7 = StringField('Auton Points #7')
#     conesPlaced7 = StringField('Cones Placed #7')
#     boxesPlaced7 = StringField('Boxes Placed #7')
#     numOfLinks7 = StringField('Number of Links #7')
#     coopGrid7 = BooleanField("3+ Game Pieces in Coop Grid? #7")
#     balanced7 = StringField('Balanced (level, unlevel, none)')
#     extra7 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit7 = SubmitField('Submit Data')
#
#
# class match_Eight(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints8 = StringField('Auton Points #8')
#     conesPlaced8 = StringField('Cones Placed #8')
#     boxesPlaced8 = StringField('Boxes Placed #8')
#     numOfLinks8 = StringField('Number of Links #8')
#     coopGrid8 = BooleanField("3+ Game Pieces in Coop Grid? #8")
#     balanced8 = StringField('Balanced (level, unlevel, none)')
#     extra8 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit8 = SubmitField('Submit Data')
#
#
# class match_Nine(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints9 = StringField('Auton Points #9')
#     conesPlaced9 = StringField('Cones Placed #9')
#     boxesPlaced9 = StringField('Boxes Placed #9')
#     numOfLinks9 = StringField('Number of Links #9')
#     coopGrid9 = BooleanField("3+ Game Pieces in Coop Grid? #9")
#     balanced9 = StringField('Balanced (level, unlevel, none)')
#     extra9 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit9 = SubmitField('Submit Data')
#
#
# class match_Ten(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints10 = StringField('Auton Points #10')
#     conesPlaced10 = StringField('Cones Placed #10')
#     boxesPlaced10 = StringField('Boxes Placed #10')
#     numOfLinks10 = StringField('Number of Links #10')
#     coopGrid10 = BooleanField("3+ Game Pieces in Coop Grid? #10")
#     balanced10 = StringField('Balanced (level, unlevel, none)')
#     extra10 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit10 = SubmitField('Submit Data')
#
#
# class match_Eleven(FlaskForm):
#     autonPoints11 = StringField('Auton Points #11')
#     conesPlaced11 = StringField('Cones Placed #11')
#     boxesPlaced11 = StringField('Boxes Placed #11')
#     numOfLinks11 = StringField('Number of Links #11')
#     coopGrid11 = BooleanField("3+ Game Pieces in Coop Grid? #11")
#     balanced11 = StringField('Balanced (level, unlevel, none)')
#     extra11 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit11 = SubmitField('Submit Data')
#
#
# class match_Twelve(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints12 = StringField('Auton Points #12')
#     conesPlaced12 = StringField('Cones Placed #12')
#     boxesPlaced12 = StringField('Boxes Placed #12')
#     numOfLinks12 = StringField('Number of Links #12')
#     coopGrid12 = BooleanField("3+ Game Pieces in Coop Grid? #12")
#     balanced12 = StringField('Balanced (level, unlevel, none)')
#     extra12 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit12 = SubmitField('Submit Data')
#
#
# class match_Thirteen(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints13 = StringField('Auton Points #13')
#     conesPlaced13 = StringField('Cones Placed #13')
#     boxesPlaced13 = StringField('Boxes Placed #13')
#     numOfLinks13 = StringField('Number of Links #13')
#     coopGrid13 = BooleanField("3+ Game Pieces in Coop Grid? #13")
#     balanced13 = StringField('Balanced (level, unlevel, none)')
#     extra13 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit13 = SubmitField('Submit Data')
#
#
# class match_Fourteen(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints14 = StringField('Auton Points #14')
#     conesPlaced14 = StringField('Cones Placed #14')
#     boxesPlaced14 = StringField('Boxes Placed #14')
#     numOfLinks14 = StringField('Number of Links #14')
#     coopGrid14 = BooleanField("3+ Game Pieces in Coop Grid? #14")
#     balanced14 = StringField('Balanced (level, unlevel, none)')
#     extra14 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit14 = SubmitField('Submit Data')
#
#
# class match_Fifteen(FlaskForm):
#     class Meta():
#         csrf = False
#
#     autonPoints15 = StringField('Auton Points #15')
#     conesPlaced15 = StringField('Cones Placed #15')
#     boxesPlaced15 = StringField('Boxes Placed #15')
#     numOfLinks15 = StringField('Number of Links #15')
#     coopGrid15 = BooleanField("3+ Game Pieces in Coop Grid? #15")
#     balanced15 = StringField('Balanced (level, unlevel, none)')
#     extra15 = TextAreaField('Extra Notes', render_kw={"rows": 6, "cols": 40})
#     submit15 = SubmitField('Submit Data')
