def get_keywords():
    """
    Returns a list of all keywords available in the EMODIA database
    :return:
    """
    negative_words = [
        "abhorrent", "abrasive", "abrupt", "absurd", "abusive", "accidental", 
        "accusatory", "acerbic", "adverse", "aggressive", "alarmist", "alienating", 
        "angry", "annoyed", "annoying", "anxious", "apathetic", "appalling", 
        "arrogant", "ashamed", "awful", "awkward", "bad", "belligerent", 
        "bitter", "bizarre", "blame", "boring", "bothersome", "burdensome", 
        "callous", "chaotic", "clumsy", "coarse", "cold", "complacent", 
        "complaint", "complicated", "concerned", "confused", "contemptible", 
        "cruel", "crushing", "cynical", "damaging", "dangerous", "dark", 
        "deadly", "deceitful", "deceptive", "degrading", "dejected", "delinquent", 
        "deplorable", "depressed", "depressing", "desolate", "desperate", 
        "destructive", "detached", "detrimental", "devastating", "difficult", 
        "disappointing", "disastrous", "disdainful", "disgraceful", "disgusting", 
        "dishonest", "disillusioned", "dismissive", "displeased", "disruptive", 
        "dissatisfied", "distasteful", "distraught", "distressed", "disturbed", 
        "doubtful", "dreary", "dull", "dysfunctional", "embarrassing", "enraged", 
        "envy", "erratic", "evil", "excessive", "exhausting", "fearful", 
        "fearsome", "flawed", "foolish", "frantic", "frightening", "frustrating", 
        "futile", "gloomy", "grave", "greedy", "grim", "guilty", "harmful", 
        "hateful", "haunting", "hazardous", "helpless", "hopeless", "hostile"
    ]
    positive_words = [
        "admirable", "adorable", "adventurous", "agreeable", "amazing", "ambitious", 
        "amiable", "amusing", "appealing", "appreciative", "articulate", "artistic", 
        "astonishing", "astute", "attentive", "attractive", "auspicious", "authentic", 
        "awesome", "beautiful", "beneficial", "blissful", "bountiful", "brave", 
        "bright", "brilliant", "bubbly", "calm", "capable", "captivating", "careful", 
        "charismatic", "charming", "cheerful", "cherished", "clever", "comforting", 
        "compassionate", "competent", "confident", "congenial", "considerate", 
        "content", "convivial", "courageous", "courteous", "creative", "cute", 
        "dazzling", "decent", "dedicated", "delightful", "dependable", "determined", 
        "diligent", "diplomatic", "dynamic", "eager", "earnest", "easygoing", 
        "ebullient", "educated", "effective", "efficient", "elegant", "eloquent", 
        "empathetic", "enchanting", "encouraging", "energetic", "engaging", 
        "enjoyable", "entertaining", "enthusiastic", "excellent", "exceptional", 
        "exciting", "exemplary", "exquisite", "extraordinary", "exuberant", 
        "fabulous", "fair", "faithful", "fantastic", "fascinating", "fearless", 
        "fine", "flourishing", "focused", "forgiving", "fortunate", "friendly", 
        "fun", "funny", "generous", "genial", "gentle", "genuine", "gifted", 
        "glorious", "good", "gracious", "grateful", "great", "happy", "harmonious", 
        "helpful", "hilarious", "honest", "honorable", "hopeful", "hospitable", 
        "humorous", "idealistic", "illustrious", "imaginative", "impressive", 
        "incredible", "independent", "industrious", "innovative", "insightful", 
        "inspiring", "intelligent", "intuitive", "inventive", "joyful", "jubilant", 
        "keen", "kind", "knowledgeable", "laudable", "lively", "lovable", "lovely", 
        "loving", "loyal", "lucky", "magnificent", "marvelous", "masterful", 
        "meticulous", "mindful", "miraculous", "modest", "motivated", "optimistic", 
        "outstanding", "passionate", "patient", "peaceful", "perfect", "persevering", 
        "persistent", "philanthropic", "playful", "pleasant", "pleasing", "poised", 
        "polished", "popular", "positive", "powerful", "praiseworthy", "precious", 
        "precise", "preeminent", "prestigious", "productive", "professional", 
        "proficient", "profound", "prolific", "prominent", "prosperous", "protective", 
        "proud", "prudent", "punctual", "purposeful", "qualified", "quintessential", 
        "radiant", "rational", "realistic", "reassuring", "receptive", "remarkable", 
        "resilient", "resolute", "resourceful", "respectable", "respectful", 
        "resplendent", "responsible", "responsive", "revered", "rewarding", "rich", 
        "righteous", "robust", "romantic", "sagacious", "satisfying", "savvy", 
        "scholarly", "scrupulous", "self-assured", "self-reliant", "sensible", 
        "sensitive", "serene", "sharp", "shining", "sincere", "skillful", "smart", 
        "smiling", "smooth", "sociable", "solid",
        "sophisticated", "spirited", "splendid", "steadfast", "stimulating",
        "stupendous", "stunning", "stupendous", "sturdy", "stylish", "suave",
        "sublime", "successful", "succinct", "super", "superb", "supportive",
        "surprising", "sustained", "sweet", "talented", "tenacious", "terrific",
        "thankful", "thoughtful", "thriving", "timely", "tireless", "tolerant",
        "top", "tranquil", "trusting", "truthful", "ultimate", "unbiased",
        "uncommon", "understanding", "unequaled", "unflappable", "unique"]
    


    keywords_example = positive_words + negative_words

    return keywords_example
