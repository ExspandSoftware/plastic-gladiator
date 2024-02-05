import os

#%% Rahmeninfos ----------------------------------------------------------------
__author__ = "palo.niemann@t-online.de"
__version__ = "1.1.0"
__CIO__ = "Yannick Braune"
__moderators__ = "Karen Iwamya, Paul Niemann"
__team__ = "Paul Niemann, Yannick Braune, Karen Iwamya, Louisa Krieger, Dana Brandis, Clemens Brandhoff, Jakob Pfeiffer, Phillipp Relogio Stauber, Vincent Winter, Mats Parlov, Franz Overlack, Leonard Hosie, Maximilian Bolt"
__head__ = "Wilhelm Gymnasium Hamburg"
__supervisor__ = "Nicole Kind (Chemie S4, Abiturjahrgang 2024)"
__sound__ = "Vincent Winter"
__concept__ = "..."
__graphics__ = "..."
__quality_assurance__ = "Linus Horn (linus@linushorn.dev)"
EXPORT_VARS = [__author__, __version__, __CIO__, __moderators__, __team__, __head__, __supervisor__, __sound__, __concept__, __graphics__, __quality_assurance__]

#Konstante, in Form eines Paths, der zum Arbeitsverzeichnis führt
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
WORKING_DIR = os.getcwd()
#Konstante, in Form eines Paths, der zum Source Code führt
#CURRENT_DIR = os.path.curdir()

#Framemode
Iwidth, Iheight = 1280, 720
Cwidth, Cheight = 1280, 720

#Gamerules
STAGE = "home"
FONT_SIZE = 24