from datasets import load_dataset
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STEREOSET_DIR = PROJECT_ROOT / "stereoset" / "intersentence"


def load_stereoset(split: str = "validation"):
    """
    Loads local StereoSet (intersentence) dataset from parquet files.

    Args:
        split (str): Only 'validation' exists for StereoSet

    Returns:
        HuggingFace Dataset
    """

    data_files = {
        split: str(STEREOSET_DIR / "validation-00000-of-00001.parquet")
    }

    dataset = load_dataset(
        "parquet",
        data_files=data_files
    )

    return dataset[split]
