import torch
import clip


def load_clip_model():
    """
    Load CLIP model only once.
    """

    device = "cuda" if torch.cuda.is_available() else "cpu"

    model, preprocess = clip.load(
        "ViT-B/32",
        device=device
    )

    return model, preprocess, device