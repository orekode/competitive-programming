def finalValueAfterOperations(self, operations: List[str]) -> int:
    
    value = 0

    for opp in operations:
        if "-" in opp:
            value -= 1
        elif "+" in opp:
            value += 1
