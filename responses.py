def get_response(user_input):
    lowered = user_input.lower()
    if lowered.startswith("vote"):
        return handle_vote(lowered)
    
    elif lowered.startswith("aura"):
        return handle_aura(lowered)
    
    else:
        return "Jules ntm sah"

def handle_aura(user_input):
    aura_data = main.load_aura_data()
    parts = user_input.split()
    
    if len(parts) < 2:
        return "Usage: aura <user>"
    
    user = parts[1]
    
    for member_id, data in aura_data.items():
        if data['username'] == user:
            return f"L'aura actuelle de {user} est {data['aura']}."
    
    return f"L'utilisateur {user} n'est pas trouvé."

def handle_vote(user_input):
    aura_data = main.load_aura_data()
    parts = user_input.split()
    
    if len(parts) < 3:
        return "Usage: vote <user> <up/down>"
    
    user = parts[1]
    vote_type = parts[2]
    
    for member_id, data in aura_data.items():
        if data['username'] == user:
            user = member_id
            username = data['username']
            break
    else:
        return f"L'utilisateur {user} n'est pas trouvé."
    
    if vote_type == "up":
        aura_data[user]['aura'] += 10
        main.save_aura_data()
        return f"L'aura de {username} a été augmentée à {aura_data[user]['aura']}."
    
    elif vote_type == "down":
        aura_data[user]['aura'] -= 10
        main.save_aura_data()
        return f"L'aura de {username} a été réduite à {aura_data[user]['aura']}."
    
    else:
        return "Type de vote non reconnu. Utilisez 'up' ou 'down'."