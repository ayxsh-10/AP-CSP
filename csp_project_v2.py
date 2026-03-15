import pygame
import sys
import random

# setup
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("WPM Tracker")

# clock
clock = pygame.time.Clock()
fps = 60

# colors and fonts
bg_color = (15,35,15)
font_large = pygame.font.Font(None, 40)
font_medium = pygame.font.Font(None, 25)
font_small = pygame.font.Font(None, 18)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    pygame.display.flip()
    clock.tick(60)

    words = ["apple", "lantern", "velocity", "carpet", "glacier", "melody", "shadow", "circuit",
             "ocean", "ladder", "candle", "mirror", "thunder", "pebble", "forest", "rocket",
             "silver", "galaxy", "pillow", "magnet", "compass", "desert", "blossom", "fountain",
             "dragon", "spiral", "hammer", "crystal", "river", "planet", "meadow", "sunrise",
             "breeze", "anchor", "mosaic", "canyon", "orchard", "valley", "horizon", "comet",
             "meteor", "eclipse", "aurora", "harbor", "voyage", "prism", "marble", "whisper",
             "summit", "jungle", "coral", "echo", "ripple", "shimmer", "cascade", "orbit",
             "nebula", "asteroid", "cosmos", "starlight", "moonlight", "daylight", "twilight",
             "throughout", "heaven", "and", "earth", "I", "alone", "am", "the", "honored", "one",
             "midnight", "sunset", "storm", "drizzle", "rainfall","snowfall", "blizzard",
             "lightning", "rainbow", "tornado", "cyclone", "hurricane", "gust", "windmill",
             "engine", "turbine", "piston", "cylinder", "battery", "voltage", "current", "diode",
             "resistor", "capacitor", "transistor", "sensor", "signal", "signal", "frequency",
             "amplitude", "waveform", "algorithim", "program", "software", "hardware", "server",
             "network", "protocol", "packet", "bandwidth", "router", "modem", "database", "query",
             "schema", "index", "cache", "memory", "processor", "kernel", "thread", "socket",
             "compile", "debug", "deploy", "script", "library", "module", "function", "variable",
             "those", "who", "abandon", "their", "friends", "are", "worse", "than", "scum",
             "constant", "integer", "decimal", "fraction", "vector", "matrix", "tensor", "flow",
             "equation", "theorem", "proof", "logic", "paradox", "axiom", "hypothesis", "theory",
             "model", "system", "structure", "symmetry", "geometry", "algebra", "calculus", "ratio",
             "derivative", "integral", "limit", "series", "probability", "statistic", "variance",
             "median", "average", "pattern", "scale", "measure", "metric", "noise", "filter", 
             "channel", "spectrum", "photon", "electron", "proton", "neutron", "atom", "molecule",
             "compound", "element", "reaction", "catalyst", "enzyme", "protein", "genome", "neuron",
             "synapse", "cortex", "muscle", "tendon", "ligament", "artery", "vein", "oxygen",
             "adoration", "is", "the", "state", "furthest", "from", "understanding",
             "hydrogen", "nitrogen", "helium", "lithium", "sodium", "potassium", "calcium", "iron",
             "copper", "gold", "platinum", "mercury", "lead", "zinc", "cobalt", "nickel", 
             "titanium", "soil", "dust", "sand", "gravel", "stone", "boulder", "hill", "mountain",
             "silicon", "quartz", "granite", "basalt", "shale", "sandstone", "limestone", "clay",
             "plateau", "plain", "tundra", "prairie", "savanna", "rainforest", "wetland", "swamp",
             "marsh", "lagoon", "delta", "estuary", "reef", "kelp", "algae", "plankton", "dolphin",
             "whale", "shark", "octopus", "squid", "turtle", "penguin", "eagle", "hawk", "falcon",
             "owl", "sparrow", "robin", "crow", "raven", "swan", "goose", "duck", "heron", "crane",
             "if", "you", "don't", "like", "your", "destiny", "don't", 'accept', "it",
             "flamingo", "peacock", "parrot", "toucan", "macaw", "hummingbird", "butterly",
             "butterfly", "dragonfly", "beetle", "ant", "termite", "spider", "scorpion", "centipede",
             "millipede", "worm", "snail", "slug", "crab", "lobster", "shrimp", "barnacle",
             "starfish", "urchin", "sponge", "moss", "fern", "bamboo", "oak", "maple", "pine",
             "cedar", "spruce", "birch", "willow", "elm", "ash", "palm", "cactus", "aloe", "ivy",
             "vine", "grass", "clover", "rose", "tulip", "lily", "orchid", "daisy", "sunflower",
             "lavender", "jasmine", "mint", "basil", "thyme", "oregano", "cinnamon", "ginger",
             "nutmeg", "vanilla", "cocoa", "coffee", "tea", "sugar", "honey", "syrup", "butter",
             "somebody", "told", "me", "i'm", "a", "failure", "i'll", "prove", "them", "wrong",
             "cheese", "yogurt", "cream", "bread", "pasta", "rice", "wheat", "barley", "oats",
             "corn", "potato", "tomato", "onion", "garlic", "carror", "cucumber", "lettuce", 
             "spinach", "broccoli", "cabbage", "pumpkin", "squash", "zucchini", "eggplant",
             "mushroom", "bean", "pea", "lentil", "chickpea", "almond", "walnut", "peanut",
             "cashew", "pistachio", "hazelnut", "coconut", "banana", "orange", "lemon", "lime",
             "grapefruit", "mango", "pineapple", "papaya", "kiwi", "strawberry", "blueberry",
             "raspberry", "blackberry", "cherry", "peach", "plum", "apricot", "fig", "date",
             "raisin", "melon", "watermelon", "cantaloupe", "honeydew", "pomegranate", "guava",
             "when", "you", "give", "up", "your", "dreams", "and", "everything", "they're", "gone",
             "lychee", "passionfruit", "dragonfruit", "starfruit", "avocado", "olive", "saffron",
             "turmeric", "paprika", "cumin", "coriander", "fennel", "cardamom", "clove", "bayleaf",
             "dill", "chive", "parsley", "cilantro", "rosemary", "sage", "marjoram", "tarragon",
             "horseradish", "mustard", "ketchup", "mayonnaise", "vinegar", "pickle", "jam", "jelly",
             "marmalade", "caramel", "toffee", "chocolate", "candy", "biscuit", "cookie", "brownie",
             "muffin", "cupcake", "pastry", "pie", "tart", "pudding", "custard", "icecream", 
             "gelato", "sorbet", "smoothie", "milkshake", "latte", "espresso", "capucchino", "mocha",
             "macchiato", "americano", "frappe", "soda", "lemonade", "juice", "nectar", "tonic",
             "nah", "I'd", "win"
             "cider", "kombucha", "broth", "soup", "stew", "salad", "sandwich", "burger", "pizza",
             "burrito", "quesadilla", "nachos", "dumpling", "noodle", "ramen", "sushi", "tempura",
             "curry", "kebab", "falafel", "hummus", "shawarma", "paella", "risotto", "gnocchi",
             "lasagna", "ravioli", "tortellini", "baguette", "croissant", "pretzel", "pancake",
             "waffle", "omelet", "sausage", "bacon", "steak", "salmon", "tuna", "sardine", "anchovy",
             "cod", "trout", "herring", "swordfish", "snapper", "grouper", "tilaplia", "mackerel" 
            ]