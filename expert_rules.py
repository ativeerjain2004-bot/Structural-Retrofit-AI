def recommend_using_rules(data):

    scores = {
        "CFRP Wrap": 0,
        "GFRP Wrap": 0,
        "Steel Plate Bonding": 0,
        "Concrete Jacketing": 0
    }

    loss = data["Capacity_Loss_Pct"]
    crack = data["Max_Crack_Width_mm"]
    damage = data["Damage_Type"]
    exposure = data["Exposure_Condition"]
    settlement = data["Differential_Settlement"]
    budget = data["Budget_Constraint"]

    if settlement == "Yes":
        return "Concrete Jacketing"

    if loss >= 35:
        return "Concrete Jacketing"

    if damage == "Shear":
        return "Concrete Jacketing"

    if crack > 3:
        scores["Concrete Jacketing"] += 40

    if damage == "Flexural":
        scores["CFRP Wrap"] += 35

    if damage == "Corrosion":
        scores["Steel Plate Bonding"] += 30
        scores["GFRP Wrap"] += 20

    if exposure == "Aggressive":
        scores["CFRP Wrap"] += 20
        scores["Steel Plate Bonding"] -= 20

    elif exposure == "Fire-prone":
        scores["Concrete Jacketing"] += 35
        scores["CFRP Wrap"] -= 50
        scores["GFRP Wrap"] -= 40

    if budget == "High":
        scores["CFRP Wrap"] += 25

    elif budget == "Medium":
        scores["GFRP Wrap"] += 25

    else:
        scores["Steel Plate Bonding"] += 30

    return max(scores, key=scores.get)
