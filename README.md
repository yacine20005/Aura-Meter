# Aura-Meter

## Description
Aura-Meter est un bot Discord pour suivre et gérer l'aura des utilisateurs. Le bot permet aux utilisateurs d'interagir avec des commandes pour voir, donner et voter pour l'aura des autres utilisateurs.

## Installation
Pour installer et configurer le bot, suivez les étapes ci-dessous :

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances requises en utilisant la commande suivante :
   ```
   pip install -r requirements.txt
   ```
3. Créez un fichier `.env` dans le répertoire racine du projet et ajoutez votre jeton Discord :
   ```
   DISCORD_TOKEN=VotreJetonDiscord
   ```
4. Remplacez `channel_id` dans `main.py` par l'ID de votre canal Discord.

## Utilisation
Pour utiliser le bot, démarrez-le en exécutant la commande suivante :
```
python main.py
```
Une fois le bot en ligne, vous pouvez utiliser les commandes suivantes pour interagir avec lui :

- `/salut` : Saluer le bot.
- `/dire <message>` : Faire dire quelque chose au bot.
- `/my_aura` : Voir votre aura.
- `/aura <utilisateur>` : Voir l'aura d'un utilisateur spécifique.
- `/total_aura` : Voir le total des auras de tous les utilisateurs.
- `/give_aura <utilisateur> <montant>` : Donner de l'aura à un utilisateur.
- `/vote_aura` : Voter pour augmenter ou diminuer l'aura des utilisateurs.
- `/show_aura` : Voir l'aura de tous les utilisateurs.
- `/vote_massive <utilisateur> <montant> <raison>` : Initier un vote massif pour augmenter ou diminuer l'aura d'un utilisateur.

## Remarque
Ce projet a été initialement créé pour s'amuser avec des amis sur un serveur Discord.
