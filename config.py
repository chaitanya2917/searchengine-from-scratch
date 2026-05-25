# config.py
# Central configuration for the Search Engine project
# All settings for every module are controlled from here

# ─── CRAWLER SETTINGS ─────────────────────────────────────────────────────────

# The starting URL where the crawler begins
SEED_URL = "https://en.wikipedia.org/wiki/Computer_science"

# Maximum number of pages the crawler will visit
MAX_PAGES = 100

# Maximum depth of crawling (how many links deep from seed)
MAX_DEPTH = 3

# Time to wait between requests in seconds (be polite to servers)
CRAWL_DELAY = 1.0

# Only crawl pages from this domain (stay focused)
ALLOWED_DOMAIN = "en.wikipedia.org"

# ─── FILE PATHS ───────────────────────────────────────────────────────────────

# Where crawled page data will be saved
CRAWLED_DATA_PATH = "data/crawled_pages.json"

# Where the inverted index will be saved
INDEX_PATH = "data/inverted_index.json"

# Where PageRank scores will be saved
PAGERANK_PATH = "data/pagerank_scores.json"

# ─── INDEXER SETTINGS ─────────────────────────────────────────────────────────

# Minimum word length to include in index (ignore tiny words like "a", "I")
MIN_WORD_LENGTH = 3

# ─── RANKER SETTINGS ──────────────────────────────────────────────────────────

# PageRank damping factor (standard value used by Google originally)
# Means: 85% chance user follows a link, 15% chance they jump to random page
DAMPING_FACTOR = 0.85

# How many times to iterate PageRank calculation until it stabilizes
PAGERANK_ITERATIONS = 100

# Weight balance between TF-IDF and PageRank in final score
# 0.7 means TF-IDF contributes 70%, PageRank contributes 30%
TFIDF_WEIGHT = 0.7
PAGERANK_WEIGHT = 0.3

# ─── QUERY ENGINE SETTINGS ────────────────────────────────────────────────────

# Number of results to return per search query
TOP_K_RESULTS = 10

# ─── FLASK WEB APP SETTINGS ───────────────────────────────────────────────────

# Port number for the web interface
FLASK_PORT = 5000

# Debug mode (set to False in production)
FLASK_DEBUG = True