def update_priority(word, correct):
    if correct:
        word['priority'] -= 1
    else:
        word['priority'] += 2
    
    if word['priority'] < 1:
        word['priority'] = 1
    
    return word