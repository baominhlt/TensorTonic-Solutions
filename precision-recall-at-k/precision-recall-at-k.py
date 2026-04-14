def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k_true = len([item for item in recommended[:k] if item in relevant])
    return [top_k_true / k, top_k_true / len(relevant)]