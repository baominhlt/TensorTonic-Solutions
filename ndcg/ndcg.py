import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    k = k if k <= len(relevance_scores) else len(relevance_scores)
    sorted_relevance_scores = sorted(relevance_scores, reverse=True)

    if all([score == 0 for score in relevance_scores]):
        return 0

    dcg_k = 0
    idcg_k = 0
    for i in range(k):
        dcg_k += (math.pow(2, relevance_scores[i]) - 1) / math.log(i + 1 + 1, 2)
        idcg_k += (math.pow(2, sorted_relevance_scores[i]) - 1) / math.log(i + 1 + 1, 2)
    return dcg_k / max(idcg_k, 1e-8)
    