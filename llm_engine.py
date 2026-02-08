import json

def generate_corep_output(context, scenario):
    """
    Mock LLM output for COREP reporting
    No external API used
    """

    response = {
        "template": "COREP Own Funds",
        "fields": {
            "CET1_Capital": 1200000,
            "AT1_Capital": 300000,
            "Tier2_Capital": 200000,
            "Total_Own_Funds": 1700000
        },
        "audit_log": {
            "CET1_Capital": "Derived from PRA Rulebook Article 26",
            "AT1_Capital": "Derived from PRA Rulebook Article 51",
            "Tier2_Capital": "Derived from PRA Rulebook Article 62",
            "Total_Own_Funds": "Sum of CET1, AT1 and Tier 2"
        }
    }

    return json.dumps(response)
