from replit import db
if db is None:
    db = {}


def newTeam(teamNum, teamName):
    db[f"{teamNum} info"] = {
        "Team Number": teamNum,
        "Team Name": teamName
    }


def getAllTeams():
    nums = []
    for key in db.keys():
        if ("info" in key) and (key != "None") and (key != "info"):
            print(key.replace("info", ""))
            nums.append(key.replace("info", ""))
    nums.sort()
    return nums


def getTeamMatchNums(team):
    playedArr = []
    # print("called")
    keys = db.keys()
    print(keys)
    for x in range(1, 16):
        if (team + "Match" + str(x)) in keys:
            playedArr.append("Played")
        else:
            playedArr.append("Not Played")
    return playedArr


def teamPitScout(teamNum, autoBalance, coneIntake, cubeIntake, typeOfAuton, extraPit):
    db[f"{teamNum} pit"] = {
        "Auto Balance": autoBalance,
        "Cone Intake": coneIntake,
        "Cube Intake": cubeIntake,
        "Type of Auton": typeOfAuton,
        "Extra Pit Stuff": extraPit
    }


def enterMatch(teamNum, autonPoints, conesPlaced, boxesPlaced, numOfLinks, CoopGrid, isBalanced, extra, matchNum):
    db[f"{teamNum} Match {matchNum}"] = {
        "AutonPTS": autonPoints,
        "Cones Placed": conesPlaced,
        "Cubes Placed": boxesPlaced,
        "Number of Links": numOfLinks,
        "At least 3 pcs in Coop Grid": CoopGrid,
        "Is Balanced": isBalanced,
        "Extra": extra
    }


print(getTeamMatchNums('6908')[14])
