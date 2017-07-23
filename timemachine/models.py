# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Season(models.Model):
    seasonid = models.IntegerField(primary_key=True)
    seasontype = models.CharField(max_length=4)
    gp = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    evg = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    shg = models.IntegerField(blank=True, null=True)
    a = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    s = models.IntegerField(blank=True, null=True)
    g_gp = models.FloatField(blank=True, null=True)
    evg_gp = models.FloatField(blank=True, null=True)
    ppg_gp = models.FloatField(blank=True, null=True)
    shg_gp = models.FloatField(blank=True, null=True)
    a_gp = models.FloatField(blank=True, null=True)
    pim_gp = models.FloatField(blank=True, null=True)
    s_gp = models.FloatField(blank=True, null=True)
    def __str__(self):
        return "%s %s" % (self.seasonid, self.gp)

    class Meta:
        managed = False
        db_table = 'season'


class Game(models.Model):
    gameid = models.IntegerField(primary_key=True)
    seasonid = models.ForeignKey(Season, on_delete=models.CASCADE, db_column='seasonid')
    seasontype = models.CharField(max_length=255, blank=True, null=True)
    gamedate = models.DateField(blank=True, null=True)
    awayteam = models.IntegerField(blank=True, null=True)
    hometeam = models.IntegerField(blank=True, null=True)
    awayside = models.CharField(max_length=255, blank=True, null=True)
    homeside = models.CharField(max_length=255, blank=True, null=True)
    ot = models.CharField(max_length=255, blank=True, null=True)
    so = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (self.gameid, self.seasonid, self.seasontype, self.gamedate, self.awayteam, self.hometeam, self.awayside, self.homeside, self.ot, self.so)

    class Meta:
        managed = False
        db_table = 'game'


class Player(models.Model):
    playerid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    playername = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    hand = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (self.playerid, self.firstname, self.lastname, self.playername, self.birthdate, self.country, self.height, self.weight, self.hand, self.position)

    class Meta:
        managed = False
        db_table = 'player'


class Team(models.Model):
    teamid = models.IntegerField(primary_key=True)
    teamname = models.CharField(max_length=255, blank=True, null=True)
    abbreviation = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    franchiseid = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return "%s %s %s %s %s" % (self.teamid, self.teamname, self.abbreviation, self.nickname, self.franchiseid)

    class Meta:
        managed = False
        db_table = 'team'


class Playersummary(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column='gameid')
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='playerid')
    jerseyno = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppa = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    fow = models.IntegerField(blank=True, null=True)
    fot = models.IntegerField(blank=True, null=True)
    ta = models.IntegerField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    shg = models.IntegerField(blank=True, null=True)
    sha = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    plusminus = models.IntegerField(blank=True, null=True)
    evtoi = models.FloatField(blank=True, null=True)
    pptoi = models.FloatField(blank=True, null=True)
    shtoi = models.FloatField(blank=True, null=True)
    def __str__(self):
        return "%s %s %s %s" % (self.playerid, self.goals, self.assists, self.toi)

    class Meta:
        managed = False
        db_table = 'playersummary'


class Teamsummary(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, primary_key=True, db_column='gameid')
    awayteam = models.IntegerField(blank=True, null=True)
    hometeam = models.IntegerField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    awaypim = models.IntegerField(blank=True, null=True)
    homepim = models.IntegerField(blank=True, null=True)
    awayshots = models.IntegerField(blank=True, null=True)
    homeshots = models.IntegerField(blank=True, null=True)
    awayppg = models.IntegerField(blank=True, null=True)
    homeppg = models.IntegerField(blank=True, null=True)
    awayppopp = models.IntegerField(blank=True, null=True)
    homeppopp = models.IntegerField(blank=True, null=True)
    awayblocks = models.IntegerField(blank=True, null=True)
    homeblocks = models.IntegerField(blank=True, null=True)
    awayta = models.IntegerField(blank=True, null=True)
    hometa = models.IntegerField(blank=True, null=True)
    awayga = models.IntegerField(blank=True, null=True)
    homega = models.IntegerField(blank=True, null=True)
    awayhits = models.IntegerField(blank=True, null=True)
    homehits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamsummary'

class Goalieseasons(models.Model):
    id = models.IntegerField(primary_key=True)
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='playerid')
    seasonid = models.ForeignKey(Season, on_delete=models.CASCADE, db_column='seasonid')
    playername = models.CharField(max_length=255, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    sa = models.IntegerField(blank=True, null=True)
    sv = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    sow = models.IntegerField(blank=True, null=True)
    sol = models.IntegerField(blank=True, null=True)
    otw = models.IntegerField(blank=True, null=True)
    otl = models.IntegerField(blank=True, null=True)
    t = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goalieseasons'

class Skaterseasons(models.Model):
    id = models.IntegerField(primary_key=True)
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='playerid')
    seasonid = models.ForeignKey(Season, on_delete=models.CASCADE, db_column='seasonid')
    playername = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=5, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    plusminus = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppa = models.IntegerField(blank=True, null=True)
    shg = models.IntegerField(blank=True, null=True)
    sha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skaterseasons'

class Convertedsseasons(models.Model):
    id = models.AutoField(primary_key=True)
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, db_column='playerid')
    playername = models.CharField(max_length=255, blank=True, null=True)
    seasonid = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    a = models.IntegerField(blank=True, null=True)
    p = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    s = models.IntegerField(blank=True, null=True)
    evg = models.IntegerField(blank=True, null=True)
    eva = models.IntegerField(blank=True, null=True)
    evp = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    ppa = models.IntegerField(blank=True, null=True)
    ppp = models.IntegerField(blank=True, null=True)
    shg = models.IntegerField(blank=True, null=True)
    sha = models.IntegerField(blank=True, null=True)
    shp = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return "%s %s %s %s" % (self.playerid, self.playername, self.seasonid, self.gp)

    class Meta:
        managed = False
        db_table = 'convertedsseasons'

class Block(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    blocker = models.ForeignKey(Player, on_delete=models.CASCADE)
    shooter = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'


class Decision(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, primary_key=True)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)
    loser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decision'


class Faceoff(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)
    loser = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faceoff'


class Giveaway(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    culprit = models.ForeignKey(Player, on_delete=models.CASCADE)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'giveaway'


class Goal(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    scorer = models.ForeignKey(Player, on_delete=models.CASCADE)
    primary = models.IntegerField(blank=True, null=True)
    secondary = models.IntegerField(blank=True, null=True)
    goalie = models.IntegerField(blank=True, null=True)
    shot = models.CharField(max_length=255, blank=True, null=True)
    situation = models.CharField(max_length=255, blank=True, null=True)
    gwg = models.IntegerField(blank=True, null=True)
    en = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)
    v1 = models.IntegerField(blank=True, null=True)
    v2 = models.IntegerField(blank=True, null=True)
    v3 = models.IntegerField(blank=True, null=True)
    v4 = models.IntegerField(blank=True, null=True)
    v5 = models.IntegerField(blank=True, null=True)
    v6 = models.IntegerField(blank=True, null=True)
    h1 = models.IntegerField(blank=True, null=True)
    h2 = models.IntegerField(blank=True, null=True)
    h3 = models.IntegerField(blank=True, null=True)
    h4 = models.IntegerField(blank=True, null=True)
    h5 = models.IntegerField(blank=True, null=True)
    h6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goal'


class Goaliequal20102016(models.Model):
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, primary_key=True)
    playername = models.CharField(max_length=255, blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    sa = models.IntegerField(blank=True, null=True)
    tsq = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    sqps = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    xgala = models.FloatField(blank=True, null=True)
    sgps = models.FloatField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    gs = models.FloatField(blank=True, null=True)
    svpct = models.FloatField(blank=True, null=True)
    xsvpct = models.FloatField(blank=True, null=True)
    sv_plus = models.FloatField(blank=True, null=True)
    gaa = models.FloatField(blank=True, null=True)
    xgaa = models.FloatField(blank=True, null=True)
    gaaplus = models.FloatField(blank=True, null=True)
    gs_60 = models.FloatField(blank=True, null=True)
    locstadjs = models.FloatField(blank=True, null=True)
    locstadj_s = models.FloatField(blank=True, null=True)
    locstadjxsv_field = models.FloatField(db_column='locstadjxsv_', blank=True, null=True)  # Field renamed because it ended with '_'.
    locstadjsv_plus = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goaliequal20102016'


class Goaliesummary(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, db_column="gameid")
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE, db_column="playerid")
    jerseyno = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    ppsv = models.IntegerField(blank=True, null=True)
    shsv = models.IntegerField(blank=True, null=True)
    evsv = models.IntegerField(blank=True, null=True)
    shsa = models.IntegerField(blank=True, null=True)
    evsa = models.IntegerField(blank=True, null=True)
    ppsa = models.IntegerField(blank=True, null=True)
    decision = models.CharField(max_length=255, blank=True, null=True)
    svpct = models.FloatField(blank=True, null=True)
    evsvpct = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goaliesummary'


class Hit(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    hitter = models.ForeignKey(Player, on_delete=models.CASCADE)
    hittee = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hit'


class Missedshot(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    culprit = models.ForeignKey(Player, on_delete=models.CASCADE)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'missedshot'


class Officials(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, primary_key=True)
    referee1id = models.IntegerField(blank=True, null=True)
    referee1name = models.CharField(max_length=255, blank=True, null=True)
    referee2id = models.IntegerField(blank=True, null=True)
    referee2name = models.CharField(max_length=255, blank=True, null=True)
    linesman1id = models.IntegerField(blank=True, null=True)
    linesman1name = models.CharField(max_length=255, blank=True, null=True)
    linesman2id = models.IntegerField(blank=True, null=True)
    linesman2name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'officials'


class Onice(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    situation = models.CharField(max_length=255, blank=True, null=True)
    v1 = models.IntegerField(blank=True, null=True)
    v2 = models.IntegerField(blank=True, null=True)
    v3 = models.IntegerField(blank=True, null=True)
    v4 = models.IntegerField(blank=True, null=True)
    v5 = models.IntegerField(blank=True, null=True)
    v6 = models.IntegerField(blank=True, null=True)
    h1 = models.IntegerField(blank=True, null=True)
    h2 = models.IntegerField(blank=True, null=True)
    h3 = models.IntegerField(blank=True, null=True)
    h4 = models.IntegerField(blank=True, null=True)
    h5 = models.IntegerField(blank=True, null=True)
    h6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onice'


class Penalty(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    taker = models.ForeignKey(Player, on_delete=models.CASCADE)
    drawer = models.IntegerField(blank=True, null=True)
    penalty = models.CharField(max_length=255, blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penalty'


class Playershotquality(models.Model):
    playername = models.CharField(max_length=255, primary_key=True)
    gp = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    evpptoi = models.IntegerField(blank=True, null=True)
    tsq = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    sqps = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    tsg = models.FloatField(blank=True, null=True)
    sgps = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playershotquality'


class Seasongoaliequal20102016(models.Model):
    playername = models.ForeignKey(Player, on_delete=models.CASCADE, primary_key=True)
    seasonid = models.ForeignKey(Season, on_delete=models.CASCADE)
    gp = models.IntegerField(blank=True, null=True)
    toi = models.FloatField(blank=True, null=True)
    sa = models.IntegerField(blank=True, null=True)
    tsq = models.FloatField(blank=True, null=True)
    sqps = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    xgala = models.FloatField(blank=True, null=True)
    sgps = models.FloatField(blank=True, null=True)
    ga = models.IntegerField(blank=True, null=True)
    gs = models.FloatField(blank=True, null=True)
    svpct = models.FloatField(blank=True, null=True)
    xsvpct = models.FloatField(blank=True, null=True)
    sv_plus = models.FloatField(blank=True, null=True)
    gaa = models.FloatField(blank=True, null=True)
    xgaa = models.FloatField(blank=True, null=True)
    gaaplus = models.FloatField(blank=True, null=True)
    gs_60 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasongoaliequal20102016'


class Shootout(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    shooter = models.ForeignKey(Player, on_delete=models.CASCADE)
    goalie = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    shot = models.CharField(max_length=255, blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shootout'


class Shot(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    shooter = models.ForeignKey(Player, on_delete=models.CASCADE)
    goalie = models.IntegerField(blank=True, null=True)
    shot = models.CharField(max_length=255, blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shot'


class Stars(models.Model):
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE, primary_key=True)
    firststar = models.IntegerField(blank=True, null=True)
    secondstar = models.IntegerField(blank=True, null=True)
    thirdstar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stars'


class Takeaway(models.Model):
    tid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    taker = models.ForeignKey(Player, on_delete=models.CASCADE)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    awaygoals = models.IntegerField(blank=True, null=True)
    homegoals = models.IntegerField(blank=True, null=True)
    xcoord = models.FloatField(blank=True, null=True)
    ycoord = models.FloatField(blank=True, null=True)
    adjx = models.IntegerField(blank=True, null=True)
    adjy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'takeaway'


class ApexAcl(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    username = models.CharField(max_length=255)
    priv = models.CharField(max_length=1)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_acl'


class ApexWsFiles(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField(blank=True, null=True)
    row = models.ForeignKey('ApexWsRows', models.DO_NOTHING, blank=True, null=True)
    webpage_id = models.FloatField(blank=True, null=True)
    component_level = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255)
    image_alias = models.CharField(max_length=255, blank=True, null=True)
    image_attributes = models.CharField(max_length=255, blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)
    content_last_update = models.DateField(blank=True, null=True)
    mime_type = models.CharField(max_length=255)
    content_charset = models.CharField(max_length=255, blank=True, null=True)
    content_filename = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_files'


class ApexWsHistory(models.Model):
    row_id = models.FloatField()
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField()
    column_name = models.CharField(max_length=255, blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    new_value = models.CharField(max_length=4000, blank=True, null=True)
    application_user_id = models.CharField(max_length=255, blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_history'


class ApexWsLinks(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField(blank=True, null=True)
    row = models.ForeignKey('ApexWsRows', models.DO_NOTHING, blank=True, null=True)
    webpage_id = models.FloatField(blank=True, null=True)
    component_level = models.CharField(max_length=30, blank=True, null=True)
    tags = models.CharField(max_length=4000, blank=True, null=True)
    show_on_homepage = models.CharField(max_length=1, blank=True, null=True)
    link_name = models.CharField(max_length=255)
    url = models.CharField(max_length=4000)
    link_description = models.CharField(max_length=4000, blank=True, null=True)
    display_sequence = models.FloatField(blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_links'


class ApexWsNotes(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField(blank=True, null=True)
    row = models.ForeignKey('ApexWsRows', models.DO_NOTHING, blank=True, null=True)
    webpage_id = models.FloatField(blank=True, null=True)
    component_level = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_notes'


class ApexWsRows(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField()
    unique_value = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=4000, blank=True, null=True)
    parent_row_id = models.FloatField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    geocode = models.CharField(max_length=512, blank=True, null=True)
    load_order = models.FloatField(blank=True, null=True)
    change_count = models.FloatField(blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)
    c001 = models.CharField(max_length=4000, blank=True, null=True)
    c002 = models.CharField(max_length=4000, blank=True, null=True)
    c003 = models.CharField(max_length=4000, blank=True, null=True)
    c004 = models.CharField(max_length=4000, blank=True, null=True)
    c005 = models.CharField(max_length=4000, blank=True, null=True)
    c006 = models.CharField(max_length=4000, blank=True, null=True)
    c007 = models.CharField(max_length=4000, blank=True, null=True)
    c008 = models.CharField(max_length=4000, blank=True, null=True)
    c009 = models.CharField(max_length=4000, blank=True, null=True)
    c010 = models.CharField(max_length=4000, blank=True, null=True)
    c011 = models.CharField(max_length=4000, blank=True, null=True)
    c012 = models.CharField(max_length=4000, blank=True, null=True)
    c013 = models.CharField(max_length=4000, blank=True, null=True)
    c014 = models.CharField(max_length=4000, blank=True, null=True)
    c015 = models.CharField(max_length=4000, blank=True, null=True)
    c016 = models.CharField(max_length=4000, blank=True, null=True)
    c017 = models.CharField(max_length=4000, blank=True, null=True)
    c018 = models.CharField(max_length=4000, blank=True, null=True)
    c019 = models.CharField(max_length=4000, blank=True, null=True)
    c020 = models.CharField(max_length=4000, blank=True, null=True)
    c021 = models.CharField(max_length=4000, blank=True, null=True)
    c022 = models.CharField(max_length=4000, blank=True, null=True)
    c023 = models.CharField(max_length=4000, blank=True, null=True)
    c024 = models.CharField(max_length=4000, blank=True, null=True)
    c025 = models.CharField(max_length=4000, blank=True, null=True)
    c026 = models.CharField(max_length=4000, blank=True, null=True)
    c027 = models.CharField(max_length=4000, blank=True, null=True)
    c028 = models.CharField(max_length=4000, blank=True, null=True)
    c029 = models.CharField(max_length=4000, blank=True, null=True)
    c030 = models.CharField(max_length=4000, blank=True, null=True)
    c031 = models.CharField(max_length=4000, blank=True, null=True)
    c032 = models.CharField(max_length=4000, blank=True, null=True)
    c033 = models.CharField(max_length=4000, blank=True, null=True)
    c034 = models.CharField(max_length=4000, blank=True, null=True)
    c035 = models.CharField(max_length=4000, blank=True, null=True)
    c036 = models.CharField(max_length=4000, blank=True, null=True)
    c037 = models.CharField(max_length=4000, blank=True, null=True)
    c038 = models.CharField(max_length=4000, blank=True, null=True)
    c039 = models.CharField(max_length=4000, blank=True, null=True)
    c040 = models.CharField(max_length=4000, blank=True, null=True)
    c041 = models.CharField(max_length=4000, blank=True, null=True)
    c042 = models.CharField(max_length=4000, blank=True, null=True)
    c043 = models.CharField(max_length=4000, blank=True, null=True)
    c044 = models.CharField(max_length=4000, blank=True, null=True)
    c045 = models.CharField(max_length=4000, blank=True, null=True)
    c046 = models.CharField(max_length=4000, blank=True, null=True)
    c047 = models.CharField(max_length=4000, blank=True, null=True)
    c048 = models.CharField(max_length=4000, blank=True, null=True)
    c049 = models.CharField(max_length=4000, blank=True, null=True)
    c050 = models.CharField(max_length=4000, blank=True, null=True)
    n001 = models.FloatField(blank=True, null=True)
    n002 = models.FloatField(blank=True, null=True)
    n003 = models.FloatField(blank=True, null=True)
    n004 = models.FloatField(blank=True, null=True)
    n005 = models.FloatField(blank=True, null=True)
    n006 = models.FloatField(blank=True, null=True)
    n007 = models.FloatField(blank=True, null=True)
    n008 = models.FloatField(blank=True, null=True)
    n009 = models.FloatField(blank=True, null=True)
    n010 = models.FloatField(blank=True, null=True)
    n011 = models.FloatField(blank=True, null=True)
    n012 = models.FloatField(blank=True, null=True)
    n013 = models.FloatField(blank=True, null=True)
    n014 = models.FloatField(blank=True, null=True)
    n015 = models.FloatField(blank=True, null=True)
    n016 = models.FloatField(blank=True, null=True)
    n017 = models.FloatField(blank=True, null=True)
    n018 = models.FloatField(blank=True, null=True)
    n019 = models.FloatField(blank=True, null=True)
    n020 = models.FloatField(blank=True, null=True)
    n021 = models.FloatField(blank=True, null=True)
    n022 = models.FloatField(blank=True, null=True)
    n023 = models.FloatField(blank=True, null=True)
    n024 = models.FloatField(blank=True, null=True)
    n025 = models.FloatField(blank=True, null=True)
    n026 = models.FloatField(blank=True, null=True)
    n027 = models.FloatField(blank=True, null=True)
    n028 = models.FloatField(blank=True, null=True)
    n029 = models.FloatField(blank=True, null=True)
    n030 = models.FloatField(blank=True, null=True)
    n031 = models.FloatField(blank=True, null=True)
    n032 = models.FloatField(blank=True, null=True)
    n033 = models.FloatField(blank=True, null=True)
    n034 = models.FloatField(blank=True, null=True)
    n035 = models.FloatField(blank=True, null=True)
    n036 = models.FloatField(blank=True, null=True)
    n037 = models.FloatField(blank=True, null=True)
    n038 = models.FloatField(blank=True, null=True)
    n039 = models.FloatField(blank=True, null=True)
    n040 = models.FloatField(blank=True, null=True)
    n041 = models.FloatField(blank=True, null=True)
    n042 = models.FloatField(blank=True, null=True)
    n043 = models.FloatField(blank=True, null=True)
    n044 = models.FloatField(blank=True, null=True)
    n045 = models.FloatField(blank=True, null=True)
    n046 = models.FloatField(blank=True, null=True)
    n047 = models.FloatField(blank=True, null=True)
    n048 = models.FloatField(blank=True, null=True)
    n049 = models.FloatField(blank=True, null=True)
    n050 = models.FloatField(blank=True, null=True)
    d001 = models.DateField(blank=True, null=True)
    d002 = models.DateField(blank=True, null=True)
    d003 = models.DateField(blank=True, null=True)
    d004 = models.DateField(blank=True, null=True)
    d005 = models.DateField(blank=True, null=True)
    d006 = models.DateField(blank=True, null=True)
    d007 = models.DateField(blank=True, null=True)
    d008 = models.DateField(blank=True, null=True)
    d009 = models.DateField(blank=True, null=True)
    d010 = models.DateField(blank=True, null=True)
    d011 = models.DateField(blank=True, null=True)
    d012 = models.DateField(blank=True, null=True)
    d013 = models.DateField(blank=True, null=True)
    d014 = models.DateField(blank=True, null=True)
    d015 = models.DateField(blank=True, null=True)
    d016 = models.DateField(blank=True, null=True)
    d017 = models.DateField(blank=True, null=True)
    d018 = models.DateField(blank=True, null=True)
    d019 = models.DateField(blank=True, null=True)
    d020 = models.DateField(blank=True, null=True)
    d021 = models.DateField(blank=True, null=True)
    d022 = models.DateField(blank=True, null=True)
    d023 = models.DateField(blank=True, null=True)
    d024 = models.DateField(blank=True, null=True)
    d025 = models.DateField(blank=True, null=True)
    d026 = models.DateField(blank=True, null=True)
    d027 = models.DateField(blank=True, null=True)
    d028 = models.DateField(blank=True, null=True)
    d029 = models.DateField(blank=True, null=True)
    d030 = models.DateField(blank=True, null=True)
    d031 = models.DateField(blank=True, null=True)
    d032 = models.DateField(blank=True, null=True)
    d033 = models.DateField(blank=True, null=True)
    d034 = models.DateField(blank=True, null=True)
    d035 = models.DateField(blank=True, null=True)
    d036 = models.DateField(blank=True, null=True)
    d037 = models.DateField(blank=True, null=True)
    d038 = models.DateField(blank=True, null=True)
    d039 = models.DateField(blank=True, null=True)
    d040 = models.DateField(blank=True, null=True)
    d041 = models.DateField(blank=True, null=True)
    d042 = models.DateField(blank=True, null=True)
    d043 = models.DateField(blank=True, null=True)
    d044 = models.DateField(blank=True, null=True)
    d045 = models.DateField(blank=True, null=True)
    d046 = models.DateField(blank=True, null=True)
    d047 = models.DateField(blank=True, null=True)
    d048 = models.DateField(blank=True, null=True)
    d049 = models.DateField(blank=True, null=True)
    d050 = models.DateField(blank=True, null=True)
    clob001 = models.TextField(blank=True, null=True)
    search_clob = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_rows'


class ApexWsTags(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    data_grid_id = models.FloatField(blank=True, null=True)
    row = models.ForeignKey(ApexWsRows, models.DO_NOTHING, blank=True, null=True)
    webpage_id = models.FloatField(blank=True, null=True)
    component_level = models.CharField(max_length=30, blank=True, null=True)
    tag = models.CharField(max_length=4000, blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_tags'


class ApexWsWebpgSectionHistory(models.Model):
    section_id = models.FloatField()
    ws_app_id = models.FloatField()
    webpage_id = models.FloatField()
    old_display_sequence = models.FloatField(blank=True, null=True)
    new_display_sequence = models.FloatField(blank=True, null=True)
    old_title = models.CharField(max_length=4000, blank=True, null=True)
    new_title = models.CharField(max_length=4000, blank=True, null=True)
    old_content = models.TextField(blank=True, null=True)
    new_content = models.TextField(blank=True, null=True)
    application_user_id = models.CharField(max_length=255)
    change_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'apex$_ws_webpg_section_history'


class ApexWsWebpgSections(models.Model):
    id = models.FloatField(primary_key=True)
    ws_app_id = models.FloatField()
    webpage_id = models.FloatField(blank=True, null=True)
    display_sequence = models.FloatField(blank=True, null=True)
    section_type = models.CharField(max_length=30)
    title = models.CharField(max_length=4000, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_upper = models.TextField(blank=True, null=True)
    nav_start_webpage_id = models.FloatField(blank=True, null=True)
    nav_max_level = models.FloatField(blank=True, null=True)
    nav_include_link = models.CharField(max_length=1, blank=True, null=True)
    data_grid_id = models.FloatField(blank=True, null=True)
    report_id = models.FloatField(blank=True, null=True)
    data_section_style = models.FloatField(blank=True, null=True)
    chart_type = models.CharField(max_length=255, blank=True, null=True)
    chart_3d = models.CharField(max_length=1, blank=True, null=True)
    chart_label = models.CharField(max_length=255, blank=True, null=True)
    label_axis_title = models.CharField(max_length=255, blank=True, null=True)
    chart_value = models.CharField(max_length=255, blank=True, null=True)
    value_axis_title = models.CharField(max_length=255, blank=True, null=True)
    chart_aggregate = models.CharField(max_length=255, blank=True, null=True)
    chart_sorting = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apex$_ws_webpg_sections'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CopyOfOnice(models.Model):
    gameid = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    situation = models.CharField(max_length=255, blank=True, null=True)
    v1 = models.IntegerField(blank=True, null=True)
    v2 = models.IntegerField(blank=True, null=True)
    v3 = models.IntegerField(blank=True, null=True)
    v4 = models.IntegerField(blank=True, null=True)
    v5 = models.IntegerField(blank=True, null=True)
    v6 = models.IntegerField(blank=True, null=True)
    h1 = models.IntegerField(blank=True, null=True)
    h2 = models.IntegerField(blank=True, null=True)
    h3 = models.IntegerField(blank=True, null=True)
    h4 = models.IntegerField(blank=True, null=True)
    h5 = models.IntegerField(blank=True, null=True)
    h6 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copy_of_onice'


class DemoCustomers(models.Model):
    customer_id = models.FloatField(primary_key=True)
    cust_first_name = models.CharField(max_length=20)
    cust_last_name = models.CharField(max_length=20)
    cust_street_address1 = models.CharField(max_length=60, blank=True, null=True)
    cust_street_address2 = models.CharField(max_length=60, blank=True, null=True)
    cust_city = models.CharField(max_length=30, blank=True, null=True)
    cust_state = models.CharField(max_length=2, blank=True, null=True)
    cust_postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number1 = models.CharField(max_length=25, blank=True, null=True)
    phone_number2 = models.CharField(max_length=25, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cust_email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_customers'


class DemoOrderItems(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('DemoOrders', models.DO_NOTHING)
    product = models.ForeignKey('DemoProductInfo', models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'demo_order_items'


class DemoOrders(models.Model):
    order_id = models.FloatField(primary_key=True)
    customer = models.ForeignKey(DemoCustomers, models.DO_NOTHING)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_timestamp = models.DateField(blank=True, null=True)
    user = models.ForeignKey('DemoUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_orders'


class DemoProductInfo(models.Model):
    product_id = models.FloatField(primary_key=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_description = models.CharField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    product_avail = models.CharField(max_length=1, blank=True, null=True)
    list_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    product_image = models.BinaryField(blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=400, blank=True, null=True)
    image_last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_product_info'


class DemoStates(models.Model):
    st = models.CharField(max_length=30, blank=True, null=True)
    state_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_states'


class DemoUsers(models.Model):
    user_id = models.FloatField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=4000, blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    quota = models.FloatField(blank=True, null=True)
    products = models.CharField(max_length=1, blank=True, null=True)
    expires_on = models.DateField(blank=True, null=True)
    admin_user = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_users'


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14, blank=True, null=True)
    loc = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    mgr = models.ForeignKey('self', models.DO_NOTHING, db_column='mgr', blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='deptno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'


class MdAdditionalProperties(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey('MdConnections', models.DO_NOTHING, db_column='connection_id_fk')
    ref_id_fk = models.FloatField()
    ref_type = models.CharField(max_length=4000)
    property_order = models.FloatField(blank=True, null=True)
    prop_key = models.CharField(max_length=4000)
    value = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_additional_properties'


class MdApplicationfiles(models.Model):
    id = models.FloatField(primary_key=True)
    applications_id_fk = models.ForeignKey('MdApplications', models.DO_NOTHING, db_column='applications_id_fk')
    name = models.CharField(max_length=200)
    uri = models.CharField(max_length=4000)
    type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    language = models.CharField(max_length=100, blank=True, null=True)
    loc = models.FloatField(blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=4000, blank=True, null=True)
    updated_on = models.DateField(blank=True, null=True)
    updated_by = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_applicationfiles'


class MdApplications(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=4000, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    base_dir = models.CharField(max_length=4000, blank=True, null=True)
    output_dir = models.CharField(max_length=4000, blank=True, null=True)
    backup_dir = models.CharField(max_length=4000, blank=True, null=True)
    inplace = models.FloatField(blank=True, null=True)
    connection_id_fk = models.ForeignKey('MdConnections', models.DO_NOTHING, db_column='connection_id_fk')
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_applications'


class MdCatalogs(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey('MdConnections', models.DO_NOTHING, db_column='connection_id_fk')
    catalog_name = models.CharField(max_length=4000, blank=True, null=True)
    dummy_flag = models.CharField(max_length=1, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_catalogs'


class MdColumns(models.Model):
    id = models.FloatField(primary_key=True)
    table_id_fk = models.ForeignKey('MdTables', models.DO_NOTHING, db_column='table_id_fk')
    column_name = models.CharField(max_length=4000)
    column_order = models.FloatField()
    column_type = models.CharField(max_length=4000, blank=True, null=True)
    precision = models.FloatField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    nullable = models.CharField(max_length=1, blank=True, null=True)
    default_value = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    datatype_transformed_flag = models.CharField(max_length=1, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateField()
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_columns'


class MdConnections(models.Model):
    id = models.FloatField(primary_key=True)
    project_id_fk = models.ForeignKey('MdProjects', models.DO_NOTHING, db_column='project_id_fk')
    type = models.CharField(max_length=4000, blank=True, null=True)
    host = models.CharField(max_length=4000, blank=True, null=True)
    port = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=4000, blank=True, null=True)
    password = models.CharField(max_length=4000, blank=True, null=True)
    dburl = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    num_catalogs = models.FloatField(blank=True, null=True)
    num_columns = models.FloatField(blank=True, null=True)
    num_constraints = models.FloatField(blank=True, null=True)
    num_groups = models.FloatField(blank=True, null=True)
    num_roles = models.FloatField(blank=True, null=True)
    num_indexes = models.FloatField(blank=True, null=True)
    num_other_objects = models.FloatField(blank=True, null=True)
    num_packages = models.FloatField(blank=True, null=True)
    num_privileges = models.FloatField(blank=True, null=True)
    num_schemas = models.FloatField(blank=True, null=True)
    num_sequences = models.FloatField(blank=True, null=True)
    num_stored_programs = models.FloatField(blank=True, null=True)
    num_synonyms = models.FloatField(blank=True, null=True)
    num_tables = models.FloatField(blank=True, null=True)
    num_tablespaces = models.FloatField(blank=True, null=True)
    num_triggers = models.FloatField(blank=True, null=True)
    num_user_defined_data_types = models.FloatField(blank=True, null=True)
    num_users = models.FloatField(blank=True, null=True)
    num_views = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_connections'


class MdConstraintDetails(models.Model):
    id = models.FloatField(primary_key=True)
    ref_flag = models.CharField(max_length=1, blank=True, null=True)
    constraint_id_fk = models.ForeignKey('MdConstraints', models.DO_NOTHING, db_column='constraint_id_fk')
    column_id_fk = models.ForeignKey(MdColumns, models.DO_NOTHING, db_column='column_id_fk', blank=True, null=True)
    column_portion = models.FloatField(blank=True, null=True)
    constraint_text = models.TextField(blank=True, null=True)
    detail_order = models.FloatField()
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_constraint_details'


class MdConstraints(models.Model):
    id = models.FloatField(primary_key=True)
    delete_clause = models.CharField(max_length=4000, blank=True, null=True)
    name = models.CharField(max_length=4000, blank=True, null=True)
    constraint_type = models.CharField(max_length=4000, blank=True, null=True)
    table_id_fk = models.ForeignKey('MdTables', models.DO_NOTHING, db_column='table_id_fk')
    reftable_id_fk = models.FloatField(blank=True, null=True)
    constraint_text = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=40)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_constraints'


class MdDerivatives(models.Model):
    id = models.FloatField(primary_key=True)
    src_id = models.FloatField()
    src_type = models.CharField(max_length=4000, blank=True, null=True)
    derived_id = models.FloatField()
    derived_type = models.CharField(max_length=4000, blank=True, null=True)
    derived_connection_id_fk = models.ForeignKey(MdConnections, models.DO_NOTHING, db_column='derived_connection_id_fk')
    transformed = models.CharField(max_length=1, blank=True, null=True)
    original_identifier = models.CharField(max_length=4000, blank=True, null=True)
    new_identifier = models.CharField(max_length=4000, blank=True, null=True)
    derived_object_namespace = models.CharField(max_length=40, blank=True, null=True)
    derivative_reason = models.CharField(max_length=10, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_derivatives'


class MdFileArtifacts(models.Model):
    id = models.FloatField(primary_key=True)
    applicationfiles = models.ForeignKey(MdApplicationfiles, models.DO_NOTHING)
    pattern = models.CharField(max_length=4000, blank=True, null=True)
    string_found = models.CharField(max_length=4000, blank=True, null=True)
    string_replaced = models.CharField(max_length=4000, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=4000, blank=True, null=True)
    line = models.FloatField(blank=True, null=True)
    pattern_start = models.FloatField(blank=True, null=True)
    pattern_end = models.FloatField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    db_type = models.CharField(max_length=100, blank=True, null=True)
    code_type = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=4000, blank=True, null=True)
    priority = models.BigIntegerField(blank=True, null=True)
    security_group_id = models.CharField(max_length=20)
    created_on = models.DateField()
    created_by = models.CharField(max_length=4000, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_file_artifacts'


class MdGroupMembers(models.Model):
    id = models.FloatField(primary_key=True)
    group_id_fk = models.ForeignKey('MdGroups', models.DO_NOTHING, db_column='group_id_fk')
    user_id_fk = models.ForeignKey('MdUsers', models.DO_NOTHING, db_column='user_id_fk', blank=True, null=True)
    group_member_id_fk = models.FloatField()
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_group_members'


class MdGroupPrivileges(models.Model):
    id = models.FloatField(primary_key=True)
    group_id_fk = models.ForeignKey('MdGroups', models.DO_NOTHING, db_column='group_id_fk')
    privilege_id_fk = models.ForeignKey('MdPrivileges', models.DO_NOTHING, db_column='privilege_id_fk')
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_group_privileges'


class MdGroups(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey('MdSchemas', models.DO_NOTHING, db_column='schema_id_fk')
    group_name = models.CharField(max_length=4000, blank=True, null=True)
    group_flag = models.CharField(max_length=1, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_groups'


class MdIndexDetails(models.Model):
    id = models.FloatField(primary_key=True)
    index_id_fk = models.ForeignKey('MdIndexes', models.DO_NOTHING, db_column='index_id_fk')
    column_id_fk = models.ForeignKey(MdColumns, models.DO_NOTHING, db_column='column_id_fk')
    index_portion = models.FloatField(blank=True, null=True)
    detail_order = models.FloatField()
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_index_details'


class MdIndexes(models.Model):
    id = models.FloatField(primary_key=True)
    index_type = models.CharField(max_length=4000, blank=True, null=True)
    table_id_fk = models.ForeignKey('MdTables', models.DO_NOTHING, db_column='table_id_fk')
    index_name = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_indexes'


class MdMigrDependency(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey(MdConnections, models.DO_NOTHING, db_column='connection_id_fk')
    parent_id = models.FloatField()
    child_id = models.FloatField()
    parent_object_type = models.CharField(max_length=4000)
    child_object_type = models.CharField(max_length=4000)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_migr_dependency'


class MdMigrParameter(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey(MdConnections, models.DO_NOTHING, db_column='connection_id_fk')
    object_id = models.FloatField()
    object_type = models.CharField(max_length=4000)
    param_existing = models.FloatField()
    param_order = models.FloatField()
    param_name = models.CharField(max_length=4000)
    param_type = models.CharField(max_length=4000)
    param_data_type = models.CharField(max_length=4000)
    percision = models.FloatField(blank=True, null=True)
    scale = models.FloatField(blank=True, null=True)
    nullable = models.CharField(max_length=1)
    default_value = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_migr_parameter'


class MdMigrWeakdep(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey(MdConnections, models.DO_NOTHING, db_column='connection_id_fk')
    schema_id_fk = models.ForeignKey('MdSchemas', models.DO_NOTHING, db_column='schema_id_fk')
    parent_id = models.FloatField()
    child_name = models.CharField(max_length=4000)
    parent_type = models.CharField(max_length=4000)
    child_type = models.CharField(max_length=4000)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_migr_weakdep'


class MdNumrowSource(models.Model):
    numrows = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=4000, blank=True, null=True)
    objid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_numrow$source'


class MdNumrowTarget(models.Model):
    numrows = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=4000, blank=True, null=True)
    objid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_numrow$target'


class MdOtherObjects(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey('MdSchemas', models.DO_NOTHING, db_column='schema_id_fk')
    name = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_other_objects'


class MdPackages(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey('MdSchemas', models.DO_NOTHING, db_column='schema_id_fk')
    name = models.CharField(max_length=4000)
    package_header = models.TextField(blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    language = models.CharField(max_length=40)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_packages'


class MdPartitions(models.Model):
    id = models.FloatField(primary_key=True)
    table_id_fk = models.ForeignKey('MdTables', models.DO_NOTHING, db_column='table_id_fk')
    native_sql = models.TextField(blank=True, null=True)
    partition_expression = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_on = models.DateField()
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_partitions'


class MdPrivileges(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey('MdSchemas', models.DO_NOTHING, db_column='schema_id_fk')
    privilege_name = models.CharField(max_length=4000)
    privelege_object_id = models.FloatField(blank=True, null=True)
    privelegeobjecttype = models.CharField(max_length=4000)
    privelege_type = models.CharField(max_length=4000)
    admin_option = models.CharField(max_length=1, blank=True, null=True)
    native_sql = models.TextField()
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_privileges'


class MdProjects(models.Model):
    id = models.FloatField(primary_key=True)
    project_name = models.CharField(max_length=4000)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_projects'


class MdRegistry(models.Model):
    object_type = models.CharField(primary_key=True, max_length=30)
    object_name = models.CharField(max_length=30)
    desc_object_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_registry'
        unique_together = (('object_type', 'object_name'),)


class MdRepoversions(models.Model):
    revision = models.FloatField()

    class Meta:
        managed = False
        db_table = 'md_repoversions'


class MdSchemas(models.Model):
    id = models.FloatField(primary_key=True)
    catalog_id_fk = models.ForeignKey(MdCatalogs, models.DO_NOTHING, db_column='catalog_id_fk')
    name = models.CharField(max_length=4000, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    character_set = models.CharField(max_length=4000, blank=True, null=True)
    version_tag = models.CharField(max_length=40, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_schemas'


class MdSequences(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    name = models.CharField(max_length=4000)
    seq_start = models.FloatField()
    incr = models.FloatField()
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_sequences'


class MdStoredPrograms(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    programtype = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=4000, blank=True, null=True)
    package_id_fk = models.ForeignKey(MdPackages, models.DO_NOTHING, db_column='package_id_fk', blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    language = models.CharField(max_length=40)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    linecount = models.FloatField(blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_stored_programs'


class MdSynonyms(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    name = models.CharField(max_length=4000)
    synonym_for_id = models.FloatField()
    for_object_type = models.CharField(max_length=4000)
    private_visibility = models.CharField(max_length=1, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_synonyms'


class MdTables(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    table_name = models.CharField(max_length=4000)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    qualified_native_name = models.CharField(max_length=4000)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_tables'


class MdTablespaces(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    tablespace_name = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_tablespaces'


class MdTriggers(models.Model):
    id = models.FloatField(primary_key=True)
    table_or_view_id_fk = models.FloatField()
    trigger_on_flag = models.CharField(max_length=1)
    trigger_name = models.CharField(max_length=4000, blank=True, null=True)
    trigger_timing = models.CharField(max_length=4000, blank=True, null=True)
    trigger_operation = models.CharField(max_length=4000, blank=True, null=True)
    trigger_event = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    language = models.CharField(max_length=40)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    linecount = models.FloatField(blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_triggers'


class MdUserDefinedDataTypes(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    data_type_name = models.CharField(max_length=4000)
    definition = models.CharField(max_length=4000)
    native_sql = models.TextField()
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_user_defined_data_types'


class MdUserPrivileges(models.Model):
    id = models.FloatField(primary_key=True)
    user_id_fk = models.ForeignKey('MdUsers', models.DO_NOTHING, db_column='user_id_fk')
    privilege_id_fk = models.ForeignKey(MdPrivileges, models.DO_NOTHING, db_column='privilege_id_fk', blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_udpated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_user_privileges'


class MdUsers(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    username = models.CharField(max_length=4000)
    password = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_users'


class MdViews(models.Model):
    id = models.FloatField(primary_key=True)
    schema_id_fk = models.ForeignKey(MdSchemas, models.DO_NOTHING, db_column='schema_id_fk')
    view_name = models.CharField(max_length=4000, blank=True, null=True)
    native_sql = models.TextField(blank=True, null=True)
    native_key = models.CharField(max_length=4000, blank=True, null=True)
    language = models.CharField(max_length=40)
    comments = models.CharField(max_length=4000, blank=True, null=True)
    linecount = models.FloatField(blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'md_views'


class MigrDatatypeTransformMap(models.Model):
    id = models.FloatField(primary_key=True)
    project_id_fk = models.ForeignKey(MdProjects, models.DO_NOTHING, db_column='project_id_fk')
    map_name = models.CharField(max_length=4000, blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migr_datatype_transform_map'


class MigrDatatypeTransformRule(models.Model):
    id = models.FloatField(primary_key=True)
    map_id_fk = models.ForeignKey(MigrDatatypeTransformMap, models.DO_NOTHING, db_column='map_id_fk')
    source_data_type_name = models.CharField(max_length=4000)
    source_precision = models.FloatField(blank=True, null=True)
    source_scale = models.FloatField(blank=True, null=True)
    target_data_type_name = models.CharField(max_length=4000)
    target_precision = models.FloatField(blank=True, null=True)
    target_scale = models.FloatField(blank=True, null=True)
    security_group_id = models.FloatField()
    created_on = models.DateField()
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_on = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migr_datatype_transform_rule'


class MigrGenerationOrder(models.Model):
    id = models.FloatField(primary_key=True)
    connection_id_fk = models.ForeignKey(MdConnections, models.DO_NOTHING, db_column='connection_id_fk')
    object_id = models.FloatField()
    object_type = models.CharField(max_length=4000)
    generation_order = models.FloatField()

    class Meta:
        managed = False
        db_table = 'migr_generation_order'


class MigrationReservedWords(models.Model):
    keyword = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'migration_reserved_words'


class Migrlog(models.Model):
    id = models.FloatField(primary_key=True)
    parent_log = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    log_date = models.DateTimeField()
    severity = models.IntegerField()
    logtext = models.CharField(max_length=4000, blank=True, null=True)
    phase = models.CharField(max_length=100, blank=True, null=True)
    ref_object_id = models.FloatField(blank=True, null=True)
    ref_object_type = models.CharField(max_length=4000, blank=True, null=True)
    connection_id_fk = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrlog'


class StageMigrlog(models.Model):
    svrid_fk = models.FloatField(blank=True, null=True)
    dbid_gen_fk = models.FloatField(blank=True, null=True)
    id = models.FloatField(primary_key=True)
    ref_object_id = models.FloatField(blank=True, null=True)
    ref_object_type = models.CharField(max_length=4000, blank=True, null=True)
    log_date = models.DateTimeField()
    severity = models.IntegerField()
    logtext = models.CharField(max_length=4000, blank=True, null=True)
    phase = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stage_migrlog'
