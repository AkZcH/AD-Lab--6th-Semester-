# src/config.py

MODELS = {
    "bert-base": "bert-base-uncased",
    "roberta-base": "roberta-base",
    "distilbert-base": "distilbert-base-uncased"
}

# Optional controls (useful later)
MAX_EXAMPLES = 10    # set to None for full dataset
DEVICE = "auto"      # "auto", "cpu", or "cuda"
