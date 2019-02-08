def FIELD_EMPTY():
    return 0

def PAWN_WHITE():
    return 1

def PAWN_BLACK():
    return 2

def OPPOSITE_PAWN(pawn):
    if pawn == PAWN_BLACK():
        return PAWN_WHITE()

    return PAWN_BLACK()