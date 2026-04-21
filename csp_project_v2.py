import pygame
import sys
import random

# setup
pygame.init()

width, height = 1200, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("WPM Tracker")

# clock
clock = pygame.time.Clock()
fps = 60

# colors
bg_color = (30, 30, 30)
text_dim = (80, 80, 80)           # untyped letters
text_correct = (200, 100, 200)
text_wrong = (200, 50, 50)
text_cursor = (230, 180, 80)
text_ui = (100, 100, 100)         # WPM/accuracy labels
text_highlight = (230, 180, 80)   # WPM numbers and results

#fonts
font_large = pygame.font.SysFont("consolas", 40)
font_medium = pygame.font.SysFont("consolas", 25)
font_small = pygame.font.SysFont("consolas", 18)

# list of possible words to type
word_data = [
    {"word": "apple", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "lantern", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "velocity", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "carpet", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "glacier", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "melody", "category": "music", "difficulty": 2, "miss_count": 0},
    {"word": "shadow", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "circuit", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "ocean", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "ladder", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "candle", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "mirror", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "thunder", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "pebble", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "forest", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "rocket", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "silver", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "galaxy", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "pillow", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "magnet", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "compass", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "desert", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "blossom", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "fountain", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "dragon", "category": "fantasy", "difficulty": 2, "miss_count": 0},
    {"word": "spiral", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "hammer", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "crystal", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "river", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "planet", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "meadow", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "sunrise", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "breeze", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "anchor", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "mosaic", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "canyon", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "orchard", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "valley", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "horizon", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "comet", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "meteor", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "eclipse", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "aurora", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "harbor", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "voyage", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "prism", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "marble", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "whisper", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "summit", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "jungle", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "coral", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "echo", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "ripple", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "shimmer", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "cascade", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "orbit", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "nebula", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "asteroid", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "cosmos", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "starlight", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "moonlight", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "daylight", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "twilight", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "throughout", "category": "common", "difficulty": 3, "miss_count": 0},
    {"word": "heaven", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "and", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "earth", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "I", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "alone", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "am", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "the", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "honored", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "one", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "midnight", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "sunset", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "storm", "category": "weather", "difficulty": 1, "miss_count": 0},
    {"word": "drizzle", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "rainfall", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "snowfall", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "blizzard", "category": "weather", "difficulty": 3, "miss_count": 0},
    {"word": "lightning", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "rainbow", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "tornado", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "cyclone", "category": "weather", "difficulty": 2, "miss_count": 0},
    {"word": "hurricane", "category": "weather", "difficulty": 3, "miss_count": 0},
    {"word": "gust", "category": "weather", "difficulty": 1, "miss_count": 0},
    {"word": "windmill", "category": "objects", "difficulty": 2, "miss_count": 0},
    {"word": "engine", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "turbine", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "piston", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "cylinder", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "battery", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "voltage", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "current", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "diode", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "resistor", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "capacitor", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "transistor", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "sensor", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "signal", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "frequency", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "amplitude", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "waveform", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "algorithm", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "program", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "software", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "hardware", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "server", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "network", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "protocol", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "packet", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "bandwidth", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "router", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "modem", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "database", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "query", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "schema", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "index", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "cache", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "memory", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "processor", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "kernel", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "thread", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "socket", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "compile", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "debug", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "deploy", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "script", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "library", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "module", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "function", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "variable", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "those", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "who", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "abandon", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "their", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "friends", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "are", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "worse", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "than", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "scum", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "constant", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "integer", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "decimal", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "fraction", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "vector", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "matrix", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "tensor", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "flow", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "equation", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "theorem", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "proof", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "logic", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "paradox", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "axiom", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "hypothesis", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "theory", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "model", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "system", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "structure", "category": "tech", "difficulty": 3, "miss_count": 0},
    {"word": "symmetry", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "geometry", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "algebra", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "calculus", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "ratio", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "derivative", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "integral", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "limit", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "series", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "probability", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "statistic", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "variance", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "median", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "average", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "pattern", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "scale", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "measure", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "metric", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "noise", "category": "tech", "difficulty": 1, "miss_count": 0},
    {"word": "filter", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "channel", "category": "tech", "difficulty": 2, "miss_count": 0},
    {"word": "spectrum", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "photon", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "electron", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "proton", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "neutron", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "atom", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "molecule", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "compound", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "element", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "reaction", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "catalyst", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "enzyme", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "protein", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "genome", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "neuron", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "synapse", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "cortex", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "muscle", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "tendon", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "ligament", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "artery", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "vein", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "oxygen", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "adoration", "category": "common", "difficulty": 3, "miss_count": 0},
    {"word": "is", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "the", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "state", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "furthest", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "from", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "understanding", "category": "common", "difficulty": 3, "miss_count": 0},
    {"word": "hydrogen", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "nitrogen", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "helium", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "lithium", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "sodium", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "potassium", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "calcium", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "iron", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "copper", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "gold", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "platinum", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "mercury", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "lead", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "zinc", "category": "science", "difficulty": 1, "miss_count": 0},
    {"word": "cobalt", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "nickel", "category": "science", "difficulty": 2, "miss_count": 0},
    {"word": "titanium", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "soil", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "dust", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "sand", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "gravel", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "stone", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "boulder", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "hill", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "mountain", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "silicon", "category": "science", "difficulty": 3, "miss_count": 0},
    {"word": "quartz", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "granite", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "basalt", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "shale", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "sandstone", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "limestone", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "clay", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "plateau", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "plain", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "tundra", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "prairie", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "savanna", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "rainforest", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "wetland", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "swamp", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "marsh", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "lagoon", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "delta", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "estuary", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "reef", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "kelp", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "algae", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "plankton", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "dolphin", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "whale", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "shark", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "octopus", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "squid", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "turtle", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "penguin", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "eagle", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "hawk", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "falcon", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "owl", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "sparrow", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "robin", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "crow", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "raven", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "swan", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "goose", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "duck", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "heron", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "crane", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "if", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "you", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "don't", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "like", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "your", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "destiny", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "accept", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "it", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "flamingo", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "peacock", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "parrot", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "toucan", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "macaw", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "hummingbird", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "butterfly", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "dragonfly", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "beetle", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "ant", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "termite", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "spider", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "scorpion", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "centipede", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "millipede", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "worm", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "snail", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "slug", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "crab", "category": "animals", "difficulty": 1, "miss_count": 0},
    {"word": "lobster", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "shrimp", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "barnacle", "category": "animals", "difficulty": 3, "miss_count": 0},
    {"word": "starfish", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "urchin", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "sponge", "category": "animals", "difficulty": 2, "miss_count": 0},
    {"word": "moss", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "fern", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "bamboo", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "oak", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "maple", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "pine", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "cedar", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "spruce", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "birch", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "willow", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "elm", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "ash", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "palm", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "cactus", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "aloe", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "ivy", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "vine", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "grass", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "clover", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "rose", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "tulip", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "lily", "category": "nature", "difficulty": 1, "miss_count": 0},
    {"word": "orchid", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "daisy", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "sunflower", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "lavender", "category": "nature", "difficulty": 3, "miss_count": 0},
    {"word": "jasmine", "category": "nature", "difficulty": 2, "miss_count": 0},
    {"word": "mint", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "basil", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "thyme", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "oregano", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cinnamon", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "ginger", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "nutmeg", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "vanilla", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cocoa", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "coffee", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tea", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "sugar", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "honey", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "syrup", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "butter", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "somebody", "category": "common", "difficulty": 3, "miss_count": 0},
    {"word": "told", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "me", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "i'm", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "a", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "failure", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "i'll", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "prove", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "them", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "wrong", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "cheese", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "yogurt", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cream", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "bread", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "pasta", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "rice", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "wheat", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "barley", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "oats", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "corn", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "potato", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tomato", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "onion", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "garlic", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "carrot", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cucumber", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "lettuce", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "spinach", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "broccoli", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cabbage", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pumpkin", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "squash", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "zucchini", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "eggplant", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "mushroom", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "bean", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "pea", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "lentil", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "chickpea", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "almond", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "walnut", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "peanut", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cashew", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pistachio", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "hazelnut", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "coconut", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "banana", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "orange", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "lemon", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "lime", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "grapefruit", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "mango", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pineapple", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "papaya", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "kiwi", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "strawberry", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "blueberry", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "raspberry", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "blackberry", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cherry", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "peach", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "plum", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "apricot", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "fig", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "date", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "raisin", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "melon", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "watermelon", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cantaloupe", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "honeydew", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "pomegranate", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "guava", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "when", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "give", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "up", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "dreams", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "everything", "category": "common", "difficulty": 3, "miss_count": 0},
    {"word": "they're", "category": "common", "difficulty": 2, "miss_count": 0},
    {"word": "gone", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "lychee", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "passionfruit", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "dragonfruit", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "starfruit", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "avocado", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "olive", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "saffron", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "turmeric", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "paprika", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cumin", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "coriander", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "fennel", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cardamom", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "clove", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "leaf", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "dill", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "chive", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "parsley", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cilantro", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "rosemary", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "sage", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "marjoram", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "tarragon", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "horseradish", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "mustard", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "ketchup", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "mayonnaise", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "vinegar", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pickle", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "jam", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "jelly", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "marmalade", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "caramel", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "toffee", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "chocolate", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "candy", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "biscuit", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cookie", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "brownie", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "muffin", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cupcake", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pastry", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pie", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "tart", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "pudding", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "custard", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "cream", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "gelato", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "sorbet", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "smoothie", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "milkshake", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "latte", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "espresso", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cappuccino", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "mocha", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "macchiato", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "americano", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "frappe", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "soda", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "lemonade", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "juice", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "nectar", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tonic", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "nah", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "I'd", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "win", "category": "common", "difficulty": 1, "miss_count": 0},
    {"word": "cider", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "kombucha", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "broth", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "soup", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "stew", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "salad", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "sandwich", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "burger", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pizza", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "burrito", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "quesadilla", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "nachos", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "dumpling", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "noodle", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "ramen", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "sushi", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tempura", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "curry", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "kebab", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "falafel", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "hummus", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "shawarma", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "paella", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "risotto", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "gnocchi", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "lasagna", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "ravioli", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "tortellini", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "baguette", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "croissant", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "pretzel", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "pancake", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "waffle", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "omelet", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "sausage", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "bacon", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "steak", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "salmon", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tuna", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "sardine", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "anchovy", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "cod", "category": "food", "difficulty": 1, "miss_count": 0},
    {"word": "trout", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "herring", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "swordfish", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "snapper", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "grouper", "category": "food", "difficulty": 2, "miss_count": 0},
    {"word": "tilapia", "category": "food", "difficulty": 3, "miss_count": 0},
    {"word": "mackerel", "category": "food", "difficulty": 3, "miss_count": 0},
]
    
# typing setup (variables + booleans)
word_count = 0
state = "menu"
typed_text = ""
target_text = "" 
start_time = None
test_active = False
test_done = False
elapsed = 0

def evaluate_performance(typed, target, elapsed_seconds, word_data):
    if elapsed_seconds == 0:
        wpm = 0
    else:
        minutes = elapsed_seconds / 60
        wpm = round((len(typed) / 5) / minutes)
    if len(typed) == 0:
        accuracy = 100
    else:
        correct_chars = 0
        for i in range(len(typed)):
            if i < len(target) and typed[i] == target[i]:
                correct_chars += 1
        accuracy = round((correct_chars / len(typed)) * 100)
    typed_words = typed.split(" ")
    target_words = target.split(" ")
    missed_words = []
    for i in range(len(target_words)):
        if i < len(typed_words) and typed_words[i] != target_words[i]:
            missed_words.append(target_words[i])
            for entry in word_data:
                if entry["word"] == target_words[i]:
                    entry["miss_count"] += 1
    return {"wpm": wpm, "accuracy": accuracy, "missed_words": missed_words}

def get_weighted_words(word_data, count):
    weighted_pool = []
    for entry in word_data:
        weight = 1 + entry["miss_count"]
        for i in range(weight):
            weighted_pool.append(entry["word"])
    if count > len(weighted_pool):
        count = len(weighted_pool)
    return random.sample(weighted_pool, count)

# menu screen
def draw_menu():
    screen.fill(bg_color)

    title = font_large.render("WPM TRACKER", True, text_highlight)
    screen.blit(title, (width // 2 - title.get_width() // 2, height // 2 - 120))

    subtitle = font_small.render("select a mode to begin", True, text_dim)
    screen.blit(subtitle, (width // 2 - subtitle.get_width() // 2, height // 2 - 60))

    mode10w = font_medium.render("[1] 10 words", True, text_correct if word_count == 10 else text_dim)
    mode25w = font_medium.render("[2] 25 words", True, text_correct if word_count == 25 else text_dim)
    start = font_medium.render("[ENTER]", True, text_highlight)

    screen.blit(mode10w, (width // 2 - mode10w.get_width() // 2, height // 2))
    screen.blit(mode25w, (width //2 - mode25w.get_width() // 2, height //2 + 50)) # 50 = placeholder
    screen.blit(start, (width // 2 - start.get_width() // 2, height // 2 + 120))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if state == "menu":
                if event.key == pygame.K_1:
                    word_count = 10
                if event.key == pygame.K_2:
                    word_count = 25
                if event.key == pygame.K_RETURN:
                    current_words = get_weighted_words(word_data, word_count)
                    target_text = " ".join(current_words)
                    typed_text = ""
                    start_time = None
                    test_active = False
                    test_done = False
                    elapsed = 0
                    state = "game"
            elif state == "game":
                if test_done:
                    if event.key == pygame.K_r:
                        state = "menu"
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                if not test_done:
                    if start_time == None:
                        start_time = pygame.time.get_ticks()
                        test_active = True
                    if event.key == pygame.K_BACKSPACE:
                        typed_text = typed_text[:-1]
                    elif event.unicode and event.unicode.isprintable():
                        if len(typed_text) < len(target_text):
                            typed_text += event.unicode
                    if typed_text[:len(target_text)] == target_text:
                        elapsed = (pygame.time.get_ticks() - start_time) / 1000
                        test_done = True
    screen.fill(bg_color)
    # drawing section
    if state == "menu":
        draw_menu()
    elif state == "game":
    # shows live WPM and accuracy on screen while typing
        if test_done:
            results = evaluate_performance(typed_text, target_text, elapsed, word_data)
            final_wpm = results["wpm"]
            final_acc = results["accuracy"]
            missed = results["missed_words"]

            title_surface = font_large.render("Test Complete!", True, (255, 255, 100))
            wpm_surface = font_large.render(f"WPM: {final_wpm}", True, (255, 255, 255))
            acc_surface = font_large.render(f"Accuracy: {final_acc}%", True, (255, 255, 255))
            retry_surface = font_small.render("Press R to retry or Q to quit", True, (150, 150, 150))

            screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, 180))
            screen.blit(wpm_surface, (width // 2 - wpm_surface.get_width() // 2, 250))
            screen.blit(acc_surface, (width // 2 - acc_surface.get_width() // 2, 300))
            screen.blit(retry_surface, (width // 2 - retry_surface.get_width() // 2, 380))

        elif test_active:
            elapsed = (pygame.time.get_ticks() - start_time) / 1000
            results = evaluate_performance(typed_text, target_text, elapsed, word_data)
            wpm = results["wpm"]
            accuracy = results["accuracy"]
            wpm_surface = font_medium.render(f"WPM: {wpm}", True, (255, 255, 100))
            acc_surface = font_medium.render(f"Accuracy: {accuracy}%", True, (255, 255, 100))
            screen.blit(wpm_surface, (50,30))
            screen.blit(acc_surface, (200, 30))

        # draw letters one by one
        words_in_target = target_text.split(" ")
        current_text_width = 0
        current_line = []
        completed_lines = []
        for word in words_in_target:
            word_width = font_large.size(word + " ")[0]
            if current_text_width + word_width > width:
                completed_lines.append(current_line)
                current_line = []
                current_text_width = 0
            current_line.append(word)
            current_text_width += word_width
        completed_lines.append(current_line)

        total_height = len(completed_lines) * 55
        y = height // 2 - total_height // 2
        list_position = 0
        for idx, line in enumerate(completed_lines):
            line_text = " ".join(line)
            x = width // 2 - font_large.size(line_text)[0] // 2
            for char in line_text:
                if list_position < len(typed_text):
                    color = text_correct if typed_text[list_position] == char else text_wrong
                else:
                    color = text_dim
                char_surface = font_large.render(char, True, color)
                screen.blit(char_surface, (x, y))
                x += char_surface.get_width()
                list_position += 1
            y += 55
            list_position += 1
        # draw small direction
        action_surface = font_small.render("Start typing to begin...", True, (150, 150, 150))
        screen.blit(action_surface, (50, height - 40))
    pygame.display.flip()
    clock.tick(60)