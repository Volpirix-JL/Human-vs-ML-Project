'''
if ripeness > 1.5 and sweetness > 0: Good
if ripeness > 1.5 and sweetness < 0: Bad
if ripeness < 1.5 and sweetness < 0: Good
if ripeness < 1.5 and sweetness > 0: Bad
'''
def human_checker(ripeness, sweetness):
    if ripeness > 1.5 and sweetness > 0:
        return "Good"
    elif ripeness > 1.5 and sweetness < 0:
        return "Bad"
    elif ripeness < 1.5 and sweetness < 0:
        return "Good"
    elif ripeness < 1.5 and sweetness > 0:
        return "Bad"
