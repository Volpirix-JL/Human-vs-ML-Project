'''
if ripeness > 1.5 and sweetness > 0: Good
if ripeness > 1.5 and sweetness < 0: Bad
if ripeness < 1.5 and sweetness < 0: Good
if ripeness < 1.5 and sweetness > 0: Bad
'''
def human_checker(r_s):
    if r_s[0] > 1.5 and r_s[1] > 0:
        return "good"
    elif r_s[0] > 1.5 and r_s[1] < 0:
        return "bad"
    elif r_s[0] < 1.5 and r_s[1] < 0:
        return "good"
    elif r_s[0] < 1.5 and r_s[1] > 0:
        return "bad"
