import torch
import torch.nn.functional as F

print("EVALUATE.PY STARTED")
def pll_score(
    context: str,
    continuation: str,
    tokenizer,
    model,
    device: torch.device = None
) -> float:
    """
    Computes pseudo-log-likelihood (PLL) score of a continuation given a context.

    Args:
        context (str): Context sentence
        continuation (str): Candidate continuation sentence
        tokenizer: HuggingFace tokenizer
        model: HuggingFace masked language model
        device (torch.device): cpu or cuda

    Returns:
        float: PLL score (higher = more preferred)
    """

    if device is None:
        device = next(model.parameters()).device

    # ---- Tokenize context and continuation separately (NO special tokens) ----
    context_ids = tokenizer(
        context,
        add_special_tokens=False,
        return_tensors="pt"
    )["input_ids"][0]

    cont_ids = tokenizer(
        continuation,
        add_special_tokens=False,
        return_tensors="pt"
    )["input_ids"][0]

    # ---- Manually construct full input ----
    # [CLS] context continuation [SEP]
    input_ids = torch.cat(
        [
            torch.tensor([tokenizer.cls_token_id]),
            context_ids,
            cont_ids,
            torch.tensor([tokenizer.sep_token_id]),
        ]
    ).to(device)

    context_len = 1 + len(context_ids)  # CLS + context tokens

    score = 0.0

    # ---- PLL: mask ONE continuation token at a time ----
    for i in range(context_len, context_len + len(cont_ids)):
        masked_ids = input_ids.clone()
        masked_ids[i] = tokenizer.mask_token_id

        with torch.no_grad():
            outputs = model(masked_ids.unsqueeze(0))
            logits = outputs.logits[0, i]

        log_probs = F.log_softmax(logits, dim=-1)
        token_id = input_ids[i]

        score += log_probs[token_id].item()

    return score
