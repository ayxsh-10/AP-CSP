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
    "amplitude", "waveform", "algorithm", "program", "software", "hardware", "server",
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
    "flamingo", "peacock", "parrot", "toucan", "macaw", "hummingbird", "butterfly",
    "dragonfly", "beetle", "ant", "termite", "spider", "scorpion", "centipede",
    "millipede", "worm", "snail", "slug", "crab", "lobster", "shrimp", "barnacle",
    "starfish", "urchin", "sponge", "moss", "fern", "bamboo", "oak", "maple", "pine",
    "cedar", "spruce", "birch", "willow", "elm", "ash", "palm", "cactus", "aloe", "ivy",
    "vine", "grass", "clover", "rose", "tulip", "lily", "orchid", "daisy", "sunflower",
    "lavender", "jasmine", "mint", "basil", "thyme", "oregano", "cinnamon", "ginger",
    "nutmeg", "vanilla", "cocoa", "coffee", "tea", "sugar", "honey", "syrup", "butter",
    "somebody", "told", "me", "i'm", "a", "failure", "i'll", "prove", "them", "wrong",
    "cheese", "yogurt", "cream", "bread", "pasta", "rice", "wheat", "barley", "oats",
    "corn", "potato", "tomato", "onion", "garlic", "carrot", "cucumber", "lettuce", 
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
    "gelato", "sorbet", "smoothie", "milkshake", "latte", "espresso", "cappuccino", "mocha",
    "macchiato", "americano", "frappe", "soda", "lemonade", "juice", "nectar", "tonic",
    "nah", "I'd", "win",
    "cider", "kombucha", "broth", "soup", "stew", "salad", "sandwich", "burger", "pizza",
    "burrito", "quesadilla", "nachos", "dumpling", "noodle", "ramen", "sushi", "tempura",
    "curry", "kebab", "falafel", "hummus", "shawarma", "paella", "risotto", "gnocchi",
    "lasagna", "ravioli", "tortellini", "baguette", "croissant", "pretzel", "pancake",
    "waffle", "omelet", "sausage", "bacon", "steak", "salmon", "tuna", "sardine", "anchovy",
    "cod", "trout", "herring", "swordfish", "snapper", "grouper", "tilapia", "mackerel" 
]
    
# typing setup (variables + booleans)
current_words = random.sample(words,10)
target_text = " ".join(current_words)
typed_text = "" 
start_time = None
test_active = False
test_done = False
elapsed = 0

# wpm calculation
def calculate_wpm(chars_typed, elapsed_seconds):
    if elapsed_seconds == 0:
        return 0
    minutes = elapsed_seconds / 60
    wpm = (chars_typed / 5) / minutes
    return round(wpm)

# accuracy calculation
def calculate_accuracy(typed, target):
    if len(typed) == 0:
        return 0
    correct = 0
    for i in range(len(typed)):
        if i < len(target) and typed[i] == target[i]:
            correct += 1
    return round((correct / len(typed)) * 100)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if test_done:
                if event.key == pygame.K_r:
                    current_words = random.sample(words, 10)
                    target_text = " ".join(current_words)
                    typed_text = ""
                    start_time = None
                    test_active = False
                    test_done = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if not test_done:
                if start_time == None:
                    start_time = pygame.time.get_ticks()
                    test_active = True
                if event.key == pygame.K_BACKSPACE:
                    typed_text = typed_text[:-1]
                else:
                    typed_text += event.unicode
                if typed_text == target_text:
                    elapsed = (pygame.time.get_ticks() - start_time) / 1000
                    test_done = True
    screen.fill(bg_color)
    # shows live WPM and accuracy on screen while typing
    if test_done:
        final_wpm = calculate_wpm(len(typed_text), elapsed)
        final_acc = calculate_accuracy(typed_text, target_text)

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
        wpm = calculate_wpm(len(typed_text), elapsed)
        accuracy = calculate_accuracy(typed_text, target_text)
        wpm_surface = font_medium.render(f"WPM: {wpm}", True, (255, 255, 100))
        acc_surface = font_medium.render(f"Accuracy: {accuracy}%", True, (255, 255, 100))
        screen.blit(wpm_surface, (50,30))
        screen.blit(acc_surface, (200, 30))

    # draw target text
    target_surface = font_large.render(target_text, True, (255, 255, 255))
    screen.blit(target_surface, (50, height // 2 - 60))
    # draw what the user has typed so far
    typed_surface = font_large.render(typed_text, True, (100, 255, 100))
    screen.blit(typed_surface, (50, height // 2))
    # draw small direction
    action_surface = font_small.render("Start typing to begin...", True, (150, 150, 150))
    screen.blit(action_surface, (50, height - 40))
    pygame.display.flip()
    clock.tick(60)