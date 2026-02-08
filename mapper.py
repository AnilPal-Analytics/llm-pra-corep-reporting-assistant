def map_to_template(data):
    fields = data.get("fields", {})

    template = f"""
    COREP TEMPLATE – OWN FUNDS

    CET1 Capital      : {fields.get("CET1_Capital", "N/A")}
    AT1 Capital       : {fields.get("AT1_Capital", "N/A")}
    Tier 2 Capital    : {fields.get("Tier2_Capital", "N/A")}
    Total Own Funds   : {fields.get("Total_Own_Funds", "N/A")}
    """

    return template
