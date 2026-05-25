# Search Engine From Scratch 🔍

A fully functional search engine built from scratch in Python — no search libraries used.
Every component is implemented from first principles using core Computer Science concepts.

## Architecture
Web Crawler → HTML Parser → Indexer → Ranker → Query Engine → Web UI

## Modules

| Module | Description | CS Concept |
|--------|-------------|------------|
| Crawler | Visits web pages using BFS | Graph Traversal |
| Indexer | Builds inverted index | Hash Maps |
| Ranker | Scores pages with TF-IDF + PageRank | Algorithms |
| Query Engine | Processes user queries | String Matching |
| Web Interface | Flask-based search UI | Client-Server |

## Tech Stack
- Language: Python 3.10+
- Libraries: requests, BeautifulSoup4, NLTK, Flask

## Setup

```bash
git clone https://github.com/YOURUSERNAME/searchengine-from-scratch.git
cd searchengine-from-scratch
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Progress
Building this project module by module. Daily commits tracking progress, learning exploring.
