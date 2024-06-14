words_list = [
    "ability", "about", "account", "achieve", "across", "act", "action",
    "activity", "add", "address", "adult", "affect", "after", "again", "age",
    "agency", "ago", "agree", "ahead", "air", "all", "allow", "almost",
    "alone", "along", "already", "also", "although", "always", "am", "among",
    "amount", "amuse", "and", "angel", "anger", "angle", "animal", "answer",
    "any", "apart", "apologize", "appear", "apple", "apply", "argue", "arm",
    "around", "arrange", "art", "article", "as", "ask", "aspect", "assume",
    "at", "attack", "attempt", "attention", "attract", "avoid", "away", "baby",
    "back", "bad", "bag", "ball", "ban", "base", "basic", "bath", "be",
    "beautiful", "because", "become", "bed", "before", "begin", "behavior",
    "behind", "believe", "benefit", "best", "better", "between", "beyond",
    "big", "bird", "bit", "black", "blue", "board", "body", "book", "both",
    "box", "boy", "break", "bring", "brother", "build", "business", "but",
    "buy", "by", "call", "camera", "can", "capital", "car", "card", "care",
    "carry", "case", "cat", "catch", "center", "certain", "chair", "challenge",
    "chance", "change", "character", "charge", "check", "child", "choice",
    "church", "city", "class", "clean", "clear", "clearly", "close", "coach",
    "cold", "come", "community", "company", "compare", "computer", "concern",
    "condition", "conference", "connect", "consider", "contact", "continue",
    "control", "conversation", "cook", "cool", "corner", "cost", "could",
    "country", "couple", "course", "cover", "create", "culture", "cup", "cut",
    "dad", "dance", "danger", "dark", "data", "daughter", "day", "dead",
    "deal", "death", "decide", "deep", "degree", "deliver", "democrat",
    "department", "design", "detail", "develop", "device", "different",
    "difficult", "dinner", "direct", "discover", "discussion", "distance",
    "divide", "do", "doctor", "dog", "door", "down", "drive", "drop", "drug",
    "dry", "during", "each", "early", "east", "easy", "eat", "edge",
    "education", "effect", "effort", "eight", "either", "enjoy", "enough",
    "enter", "environment", "equal", "especially", "experience", "explain",
    "eye", "face", "fact", "fall", "family", "far", "farm", "fast", "father",
    "fear", "feel", "fight", "figure", "fill", "final", "find", "fine",
    "finish", "fire", "fish", "five", "floor", "fly", "focus", "follow",
    "food", "foot", "for", "force", "forest", "forget", "form", "forward",
    "found", "four", "free", "friend", "from", "front", "full", "fun",
    "future", "game", "garden", "gas", "general", "get", "girl", "give",
    "glass", "goal", "good", "government", "grab", "great", "green", "ground",
    "group", "grow", "guess", "gun", "guy", "hair", "half", "hand", "hang",
    "happen", "happy", "hard", "hat", "have", "he", "health", "hear", "heart",
    "heavy", "help", "her", "here", "high", "hill", "him", "history", "hit",
    "hold", "home", "hope", "hot", "hotel", "house", "how", "human", "hurry",
    "idea", "identify", "if", "image", "important", "include", "information",
    "inside", "instead", "interest", "interview", "into", "investment",
    "involve", "is", "issue", "it", "item", "job", "join", "joy", "judge",
    "jump", "just", "keep", "key", "kid", "kill", "kind", "kitchen", "know",
    "land", "language", "large", "last", "late", "laugh", "law", "lay", "lead",
    "learn", "leave", "left", "legal", "less", "let", "letter", "level", "lie",
    "life", "light", "like", "line", "list", "little", "live", "local", "long",
    "look", "lose", "loss", "love", "low", "machine", "main", "make", "man",
    "manage", "many", "market", "marriage", "matter", "may", "mean", "measure",
    "meat", "media", "meet", "memory", "mention", "message", "middle", "might",
    "military", "mind", "minute", "miss", "model", "modern", "moment", "money",
    "month", "more", "morning", "most", "mother", "move", "music", "my",
    "nation", "near", "need", "network", "new", "news", "nice", "night", "no",
    "none", "not", "note", "now", "number", "occur", "of", "off", "offer",
    "office", "often", "old", "on", "once", "one", "only", "open", "operation",
    "opportunity", "or", "order", "organization", "other", "our", "out",
    "outside", "over", "own", "page", "pain", "pair", "paper", "part", "party",
    "pass", "past", "patient", "pay", "peace", "people", "per", "perform",
    "period", "person", "picture", "piece", "place", "plan", "play", "point",
    "police", "political", "poor", "popular", "possible", "power", "present",
    "price", "problem", "process", "product", "program", "project", "property",
    "protect", "prove", "provide", "public", "pull", "purpose", "push",
    "quality", "question", "quick", "quite", "race", "radio", "raise", "range",
    "rate", "reach", "read", "ready", "real", "reality", "reason", "receive",
    "record", "reduce", "reflect", "region", "remain", "remember", "report",
    "require", "research", "response", "result", "return", "reveal", "right",
    "risk", "road", "rock", "role", "room", "rule", "run", "safe", "same",
    "save", "say", "school", "science", "sea", "season", "seat", "second",
    "section", "see", "sell", "send", "sense", "serve", "set", "seven",
    "share", "she", "short", "show", "side", "sign", "similar", "simple",
    "since", "sing", "sit", "situation", "six", "skill", "small", "social",
    "some", "soon", "sound", "source", "south", "space", "speak", "special",
    "sport", "stand", "start", "state", "stay", "step", "still", "stop",
    "story", "street", "strong", "student", "study", "stuff", "style",
    "subject", "success", "such", "sudden", "summer", "support", "sure",
    "system", "table", "take", "talk", "task", "tax", "teach", "team",
    "technology", "television", "ten", "test", "than", "that", "the", "their",
    "them", "then", "theory", "there", "these", "they", "thing", "think",
    "this", "those", "thought", "three", "time", "to", "today", "together",
    "top", "total", "town", "trade", "training", "travel", "tree", "trial",
    "trip", "true", "trust", "try", "turn", "two", "type", "under", "unit",
    "up", "use", "value", "very", "view", "vote", "wait", "walk", "wall",
    "want", "war", "watch", "way", "we", "weather", "week", "well", "west",
    "what", "when", "where", "which", "while", "white", "who", "whole", "why",
    "wide", "will", "win", "with", "within", "woman", "wonder", "word", "work",
    "world", "write", "year", "yes", "yesterday", "yet", "you", "young"
]

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
