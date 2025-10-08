# Lancement du projet en local

## Lancer Mysql
Dans un terminal :
```net start MySQL80```

## Ouvrir Mysql Workbench
- créer une nouvelle connexion, si pas déjà fait.
- se connecter à la BDD (id: root, mdp: admin)
- si ce n'est pas fait créer un schéma

## Lancer le serveur Django
- création d'un .venv avec la bonne version de python et l'activé
  ``` .venv\Scripts\activate```
- lancer Django
  ``` python manage.py runserver```
- lancer les migrations
  ``` python manage.py migrate ```
- création d'un superuser pour se connecter à l'admin
 ``` python manage.py createsuperuser ```
