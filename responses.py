def get_response(user_input: str, user: str) -> str:
    lowered: str = user_input.lower()
    lowered_user: str = user.lower()

    if 'mindlinh' in lowered_user:
        return "Chao buoi toi Mai Linh nhó"
    elif 'godofchoke' in lowered_user:
        return "luv <3"
    elif 'nam vu' in lowered:
        return "TatcataiNamVu"
    else:
        return ""
