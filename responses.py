def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'nam vu' in lowered:
        return "TatcataiNamVu"
    else:
        return "Deo hieu"
