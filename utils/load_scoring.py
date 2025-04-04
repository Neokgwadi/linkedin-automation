def calculate_lead_score(profile):
    score = 0
    
    # Score based on connections
    if profile.get('connections', 0) > 500:
        score += 3
    elif profile.get('connections', 0) > 100:
        score += 1
        
    # Score based on activity
    if profile.get('last_post_days', 999) < 7:
        score += 2
        
    return score
