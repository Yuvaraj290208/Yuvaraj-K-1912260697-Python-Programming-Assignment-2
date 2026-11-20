import re


def normalise(text: str) -> str:
    """'tn 09 ab 1234' -> 'TN09AB1234' (spaces and hyphens removed, upper case)"""
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg: str) -> bool:
    """Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits (e.g. TN09AB1234)"""
    if len(reg) not in (9, 10):
        return False
    return (
        reg[:2].isalpha()
        and reg[2:4].isdigit()
        and reg[4:-4].isalpha()
        and reg[-4:].isdigit()
    )


def format_receipt(reg: str) -> str:
    if not is_valid(reg):
        return "INVALID"
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"


def is_valid_regex(reg: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg))


if __name__ == "__main__":
    for raw in ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]:
        reg = normalise(raw)
        print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")

    custom_inputs = [
        "mh-12-de-1433",
        "dl 01 c 9999",
        "  ap-39-XY-0001 ",
        "KL07ABC1234",
        "TN09123456",
        "12-AB-CD-1234",
    ]
    for raw in custom_inputs:
        reg = normalise(raw)
        print(f"{raw:18} -> {reg:12} | Receipt: {format_receipt(reg)}")
      
