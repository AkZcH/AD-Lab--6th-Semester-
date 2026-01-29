from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch


def load_model(model_name: str):
    """
    Loads tokenizer and masked language model.

    Args:
        model_name (str): Hugging Face model ID

    Returns:
        tokenizer, model
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForMaskedLM.from_pretrained(model_name)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return tokenizer, model
