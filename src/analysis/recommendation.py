#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

def create_recommendation(
    problem,
    evidence,
    recommendation,
    priority
):
    """
    Build recommendation dictionary.
    """

    return {
        "Problem": problem,
        "Evidence": evidence,
        "Recommendation": recommendation,
        "Priority": priority
    }