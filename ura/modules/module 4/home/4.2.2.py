def assess_collapse(mass,astral_body='Earth'):
    GRAVITY = {
    "Earth": 9.8,
    "Jupiter": 24.79,
    "Moon": 1.63,
    }
    CRITICAL = 1000
    if mass * GRAVITY[astral_body] <CRITICAL:
        return False
    else:
        return True