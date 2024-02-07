import os

#%% Development information
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

#%% Game configuration

# set working directory to the root of the project
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
WORKING_DIR = os.getcwd()


#Framemode
Iwidth, Iheight = 1280, 720
Cwidth, Cheight = 1280, 720

#Gamerules
STAGE = "home"
FONT_SIZE = 24