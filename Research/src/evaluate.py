from collections import Counter

from src.data_loader import load_stereoset
from src.models import load_model
from src.pll_scoring import pll_score
from src.metrics import compute_stereoset_metrics
from src.config import MODELS


def get_majority_labels(sentence_labels):
    """
    Convert StereoSet human annotations into a single label per sentence
    using majority vote.

    Args:
        sentence_labels (list of dict): each dict contains a "label" list

    Returns:
        list[int]: length-3 list of labels (0=stereotype, 1=anti, 2=unrelated)
    """
    labels = []
    for sent in sentence_labels:
        votes = sent["label"]
        majority_label = Counter(votes).most_common(1)[0][0]
        labels.append(majority_label)
    return labels


def main():
    print("EVALUATE.PY STARTED")

    dataset = load_stereoset()
    print("Dataset size:", len(dataset))

    NUM_EXAMPLES = 10  # increase later (e.g. 500–2000)

    for model_name, model_id in MODELS.items():
        print(f"\nEvaluating model: {model_name}")

        tokenizer, model = load_model(model_id)
        results = []

        for i in range(NUM_EXAMPLES):
            ex = dataset[i]

            context = ex["context"]
            sentences = ex["sentences"]["sentence"]
            raw_labels = ex["sentences"]["labels"]
            bias_type = ex["bias_type"]

            # ✅ correct label aggregation
            labels = get_majority_labels(raw_labels)

            scores = [
                pll_score(context, sent, tokenizer, model)
                for sent in sentences
            ]

            best_idx = scores.index(max(scores))
            best_label = labels[best_idx]

            # Debug only for first few examples
            if i < 5:
                print("Context:", context)
                print("Scores:", scores)
                print("Majority labels:", labels)
                print("Preferred label:", best_label)
                print("-" * 50)

            results.append({
                "scores": scores,
                "labels": labels,
                "bias_type": bias_type
            })

        print("Evaluated examples:", len(results))

        metrics = compute_stereoset_metrics(results)
        print(f"{model_name} metrics:", metrics)


if __name__ == "__main__":
    main()
