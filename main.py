import os
import data
from dotenv import load_dotenv
from discord import Intents, Client, Message, Member, app_commands
from discord.ext import commands, tasks
import responses
import random
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
intents.members = True
client = Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

aura_data = {}

@client.event
async def on_ready():
    guild = client.guilds[0]
    members = guild.members
    data.initialize_aura_data(members)
    print(f'{client.user} has connected to Discord!')
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

async def send_message(message, user_message):
    if not user_message:
        print("Message is empty because intents are disabled")
        return
    
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]
        
    try:
        response = responses.get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@client.tree.command(name="salut", description="Saluer le bot")
async def hello(interaction):
    await interaction.response.send_message(f'Salut mon sauce {interaction.user.name}!')
    
@client.tree.command(name="dire", description="Faire dire quelque chose au bot")
@app_commands.describe(chose = "Qu'est ce que je dois dire ?")
async def say(interaction, chose: str):
    await interaction.response.send_message(f'{interaction.user.name} dit {chose}')

@client.tree.command(name="my_aura", description="Voir votre aura")
async def my_aura(interaction):
    aura_data = data.load_aura_data()
    aura_user = None
    for _, database in aura_data.items():
        if database['username'] == interaction.user.name:
            aura_user = database['aura']
            break

    if aura_user is not None:
        await interaction.response.send_message(f"Votre aura est de {aura_user}")
    else:
        await interaction.response.send_message("Votre aura n'existe pas")

@client.tree.command(name="aura", description="Voir l'aura d'un utilisateur")
@app_commands.describe(user = "L'utilisateur dont on veut voir l'aura")
async def aura(interaction, user: str):
    aura_data = data.load_aura_data()
    aura_user = None
    for _, database in aura_data.items():
        if database['username'] == user:
            aura_user = database['aura']
            break
        
    if aura_user is not None:
        await interaction.response.send_message(f"L'aura de {user} est de {aura_user}")
    else:
        await interaction.response.send_message(f"L'utilisateur {user} n'existe pas")
        
@client.tree.command(name="total_aura", description="Voir le total des auras de tous les utilisateurs")
async def total_aura(interaction):
    aura_data = data.load_aura_data()
    total = 0
    for _, database in aura_data.items():
        if database['username'] != "Aura Meter":
            total += database['aura']
    
    await interaction.response.send_message(f"Le total des auras est de {total}")
    
@client.tree.command(name="give_aura", description="Donner de l'aura à un utilisateur")
@app_commands.describe(user = "L'utilisateur à qui donner l'aura")
@app_commands.describe(montant = "Le montant d'aura à donner")
async def give_aura(interaction, user: str, montant: int):
    aura_data = data.load_aura_data()
    aura_user_give = interaction.user.name
    aura_user_receive = user
    aura_amount = montant
    
    for _, database in aura_data.items():
        if database['username'] == aura_user_receive:
            database['aura'] += aura_amount
            aura_user_receive = None
        
        elif database['username'] == aura_user_give:
            database['aura'] -= aura_amount
            aura_user_give = None
        
    if aura_user_give is None and aura_user_receive is None:
        data.save_aura_data()
        await interaction.response.send_message(f"{aura_amount} d'aura ont été donnés à {aura_user_receive} par {interaction.user.name}")
    else:
        await interaction.response.send_message("L'utilisateur n'existe pas")
    
@client.tree.command(name="vote_aura", description="Voter pour augmenter ou diminuer l'aura des utilisateurs")
async def weekly_vote(interaction):
    channel = client.get_channel(1275181918996140165)
    aura_data = data.load_aura_data()
    await channel.send("Préparez-vous à voter pour augmenter ou diminuer l'aura des utilisateurs. Réagissez avec 👍 pour augmenter ou 👎 pour diminuer.")
    
    messages = []
    for _, member_data in aura_data.items():
        if member_data['username'] != "Aura Meter":
            message = await channel.send(f"Votez pour augmenter ou diminuer l'aura de {member_data['username']}.")
            await message.add_reaction("👍")
            await message.add_reaction("👎")
            messages.append((message, member_data))
    
    await asyncio.sleep(300)
    
    for message, member_data in messages:
        message = await channel.fetch_message(message.id)
        upvotes = 0
        downvotes = 0
        for reaction in message.reactions:
            if str(reaction.emoji) == "👍":
                upvotes = reaction.count - 1
            elif str(reaction.emoji) == "👎":
                downvotes = reaction.count - 1
        
        member_data['aura'] += (upvotes * 10) - (downvotes * 10)
    
    data.save_aura_data()
    await channel.send("Le vote hebdomadaire est terminé et les auras ont été mises à jour.")

@client.tree.command(name="show_aura", description="Voir l'aura de tous les utilisateurs")
async def show_aura(interaction):
    channel = client.get_channel(1275181918996140165)
    aura_data = data.load_aura_data()
    await channel.send("Préparez-vous à visionner tous les auras des utilisateurs.")
    
    for _, member_data in aura_data.items():
        if member_data['username'] != "Aura Meter":
            await channel.send(f"L'aura totale de {member_data['username']} est de {member_data['aura']}.")
        else:
            await channel.send(f"L'aura totale est de Aura Meter est de ∞")
    await channel.send("Pour toute reclamations, veuillez contacter Allah.")

@client.tree.command(name="vote_massive", description="Initier un vote massif pour augmenter ou diminuer l'aura d'un utilisateur")
@app_commands.describe(user = "L'utilisateur dont on veut initier le vote")
@app_commands.describe(amount = "Le montant d'aura à retirer ou ajouter")
@app_commands.describe(reason = "La raison du vote massif")
async def vote_massive(interaction, user: str, amount: int, reason: str):
    channel = client.get_channel(1275181918996140165)
    guild = interaction.guild
    total_members = len([member for member in guild.members if not member.bot])
    aura_data = data.load_aura_data()
    if amount >= 0:
        message = await channel.send(f"{interaction.user.name} a initié un vote massif pour {user} afin d'ajouter {amount} d'aura pour la raison suivante : {reason}. Réagissez avec ✅ pour voter pour ou ❌ pour voter contre.")
    else:
        message = await channel.send(f"{interaction.user.name} a initié un vote massif pour {user} afin de retirer {amount} d'aura pour la raison suivante : {reason}. Réagissez avec ✅ pour voter pour ou ❌ pour voter contre.")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    await asyncio.sleep(300)
    message = await channel.fetch_message(message.id)
    upvotes = 0
    downvotes = 0
    for reaction in message.reactions:
        if str(reaction.emoji) == "👍":
            upvotes = reaction.count - 1
        elif str(reaction.emoji) == "👎":
            downvotes = reaction.count - 1
    
    if upvotes > total_members / 3:
        if user in aura_data:
            aura_data[user]['aura'] += amount
            data.save_aura_data()
            await channel.send(f"Le vote massif pour {user} est passé. L'aura a été mise à jour.")
        else:
            await channel.send(f"Utilisateur {user} non trouvé dans les données d'aura.")
    else:
        await channel.send(f"Le vote massif pour {user} n'est pas passé.")
    
def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()