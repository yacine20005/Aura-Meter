import csv

def load_aura_data():
    global aura_data
    with open('aura_data.csv', mode='r') as file:
        reader = csv.reader(file)
        aura_data = {rows[0]: {'username': rows[1], 'aura': int(rows[2])} for rows in reader}
        return aura_data

def save_aura_data():
    with open('aura_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for user_id, data in aura_data.items():
            writer.writerow([user_id, data['username'], data['aura']])
            
def initialize_aura_data(members):
    aura_data = load_aura_data()
    with open('aura_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for member in members:
            if str(member.id) not in aura_data:
                writer.writerow([member.id, member.name, 0])
            else:
                writer.writerow([member.id, aura_data[str(member.id)]['username'], aura_data[str(member.id)]['aura']])