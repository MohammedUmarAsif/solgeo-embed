"""Low-label, model-agnostic embedding utilities for Earth observation."""

from .features import (
    FeatureStandardizer,
    PrototypeClassifier,
    cosine_similarity,
    extract_patches,
    feature_cache_key,
)

__all__ = [
    "FeatureStandardizer",
    "PrototypeClassifier",
    "cosine_similarity",
    "extract_patches",
    "feature_cache_key",
]
