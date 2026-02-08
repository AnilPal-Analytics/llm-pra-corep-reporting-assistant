def validate(data):
    errors = []

    fields = data.get("fields", {})

    cet1 = fields.get("CET1_Capital")
    at1 = fields.get("AT1_Capital")
    tier2 = fields.get("Tier2_Capital")
    total = fields.get("Total_Own_Funds")

    # Basic validation rules
    if cet1 is None:
        errors.append("CET1 Capital is missing")

    if total is not None and cet1 is not None and at1 is not None and tier2 is not None:
        if total != cet1 + at1 + tier2:
            errors.append("Total Own Funds does not equal CET1 + AT1 + Tier2")

    return errors
