def verify_otp_while(correct_otp: str, entries: list[str]) -> str:
    attempts = 0
    max_attempts = 3
    idx = 0

    while attempts < max_attempts:
        if idx >= len(entries):
            pass
            break
        entered = entries[idx].strip()
        idx += 1

        if entered == "":
            continue

        attempts += 1
        if entered == correct_otp:
            return f"OTP verified in {attempts} attempt(s)."
    else:
        return "Account locked for 30 minutes (3 wrong attempts)."

    return "Session ended without verification."


def verify_otp_for(correct_otp: str, entries: list[str]) -> str:
    idx = 0
    for attempt in range(1, 4):
        while idx < len(entries) and entries[idx].strip() == "":
            idx += 1
            continue

        if idx >= len(entries):
            pass
            return "Session ended."

        entered = entries[idx].strip()
        idx += 1

        if entered == correct_otp:
            return f"OTP verified on attempt {attempt}."
    else:
        return "Account locked for 30 minutes (3 wrong attempts)."


def verify_otp_with_security_bonus(
    correct_otp: str,
    entries: list[str],
    security_answer_correct: bool = False,
) -> str:
    attempts = 0
    max_attempts = 3
    bonus_used = False
    idx = 0

    while attempts < max_attempts:
        if idx >= len(entries):
            break
        entered = entries[idx].strip()
        idx += 1

        if entered == "":
            continue

        attempts += 1
        if entered == correct_otp:
            return f"OTP verified in {attempts} attempt(s)."

        if attempts == max_attempts and not bonus_used and security_answer_correct:
            bonus_used = True
            max_attempts += 2
    else:
        return f"Account locked for 30 minutes ({attempts} wrong attempts)."

    return "Session ended."


def verify_otp_recursive(
    correct_otp: str,
    entries: list[str],
    idx: int = 0,
    attempts_left: int = 3,
) -> str:
    if attempts_left == 0:
        return "Account locked for 30 minutes."
    if idx >= len(entries):
        return "Session ended."

    entered = entries[idx].strip()
    if entered == "":
        return verify_otp_recursive(correct_otp, entries, idx + 1, attempts_left)
    if entered == correct_otp:
        return "OTP verified (recursive)."
    return verify_otp_recursive(correct_otp, entries, idx + 1, attempts_left - 1)


if __name__ == "__main__":
    otp = "4829"
    print("1. Valid on 2nd attempt (with blank):", verify_otp_while(otp, ["", "1111", "4829"]))
    print("2. Lock after 3 wrong (for loop):    ", verify_otp_for(otp, ["1111", "", "2222", "3333"]))
    print("3. Bonus 2 attempts (security OK):   ", verify_otp_with_security_bonus(otp, ["1", "2", "3", "4", "4829"], True))
    print("4. Recursive lock:                   ", verify_otp_recursive(otp, ["1111", "2222", "3333"]))
      
