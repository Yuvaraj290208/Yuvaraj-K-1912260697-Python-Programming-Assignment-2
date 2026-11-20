def subsidy_separate_if(units: int, has_ration_card: bool, has_senior_above_80: bool) -> list[str]:
    decisions = []

    if units <= 100:
        decisions.append("Full subsidy (<= 100 units)")

    if units <= 200 and has_ration_card:
        decisions.append("Partial subsidy (ration card)")

    if units > 200 and not has_senior_above_80:
        decisions.append("No subsidy (> 200 units)")

    if has_senior_above_80:
        decisions.append("Special subsidy (member > 80 years)")

    return decisions


def subsidy_if_elif_else(units: int, has_ration_card: bool, has_senior_above_80: bool) -> str:
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if has_ration_card:
            return "Partial subsidy"
        return "No subsidy"
    else:
        if has_senior_above_80:
            return "Special subsidy (senior > 80)"
        return "No subsidy"


def subsidy_match_case(units: int, has_ration_card: bool, has_senior_above_80: bool) -> str:
    match units:
        case u if u <= 100:
            return "Full subsidy"
        case u if 101 <= u <= 200 and has_ration_card:
            return "Partial subsidy"
        case u if 101 <= u <= 200:
            return "No subsidy"
        case _ if has_senior_above_80:
            return "Special subsidy (senior > 80)"
        case _:
            return "No subsidy"


def subsidy_tuple_lookup(units: int, has_ration_card: bool, has_senior_above_80: bool) -> str:
    slabs = [
        (100, lambda card, senior: True, "Full subsidy"),
        (200, lambda card, senior: card, "Partial subsidy"),
        (200, lambda card, senior: not card, "No subsidy"),
        (float("inf"), lambda card, senior: senior, "Special subsidy (senior > 80)"),
        (float("inf"), lambda card, senior: True, "No subsidy"),
    ]
    for limit, condition, decision in slabs:
        if units <= limit and condition(has_ration_card, has_senior_above_80):
            return decision
    return "No subsidy"


if __name__ == "__main__":
    households = [
        ("H1 (80u, card, senior)", 80, True, True),
        ("H2 (100u, no card, no senior)", 100, False, False),
        ("H3 (101u, card, no senior)", 101, True, False),
        ("H4 (101u, no card, senior)", 101, False, True),
        ("H5 (200u, card, no senior)", 200, True, False),
        ("H6 (200u, no card, no senior)", 200, False, False),
        ("H7 (201u, card, no senior)", 201, True, False),
        ("H8 (201u, no card, senior)", 201, False, True),
    ]

    for label, units, card, senior in households:
        sep = ", ".join(subsidy_separate_if(units, card, senior))
        elif_res = subsidy_if_elif_else(units, card, senior)
        match_res = subsidy_match_case(units, card, senior)
        lookup_res = subsidy_tuple_lookup(units, card, senior)
        print(f"{label} | separate_if: [{sep}] | if-elif-else: {elif_res} | match: {match_res} | tuple: {lookup_res}")
      
