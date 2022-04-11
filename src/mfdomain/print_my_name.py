

def say_hi(message) -> str:
    if isinstance(message, str):
        return message
    else:
        return "INVALID"
