# CoursDocker
Cours de docker de M2 Admin Sys


Notes personnelles :
Introduction a Docker :
Il s'agit de gérer des conteneur, virtualisation sans OS, augmentation des capacités récursivement, rendre les applications élastiques pouvant accumuler de la charge et être augmentés en capacités

Autant dev que ops
SysOps GitOps, automatisations de tache DevOps, automatisation de l’infrastructure (Infrastructure as code IaaC)


Cloud Apps et DevOps :
Migration vers le cloud
de Monolithe (Un seul serveur avec toute les fonctionnalités) en 2000
- 20 % du CPU et Complexité de mise à jours, pb = généralisé

à MicroServices : Chaque Brique de l’appli est séparé sur un serveur dédié avec une techno adapté qui peuvent communiquer ensemble
+ élastique, indépendant et « stateless »(ne stocke pas de session car dans un
token JWT ) → Header(jwt) + Payload(json + login) + Sign(clé publique)

Permet de faire de l’Agile et amène une meilleurs communication entre Dev et Ops

Docker crée en 2013 à partir d’un dev fait en 2004, et est devenu indispensable dans les projets Dev d’aujourd’hui

Serveur  monolithique = application + OS + Serveur physique

Ensemble de brique applicative qui standardise les package et dépendances
Isole les appli 
Partage le même noyau
Marche sur la majorité des OS


Docker (Container)
IntelliJ (Environnement de dev)
Ligne de commande 








Installer wls2
https://docs.microsoft.com/fr-fr/windows/wsl/install-manual#step-3---enable-virtual-machine-feature
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
Installation de wsl_update_x64.msi
wsl --set-version Ubuntu-20.04 2
wsl --set-default-version 2
docker run -d -p 80:80 docker/getting-started
docker pull nginx


Image = ensemble de calques 
Créer un dockerfile pour lancer une image = 

dockerfile 
FROM « template de dockerhub» 
ENV « variable à créer»
RUN «commande linux pour intégrer une configuration à la création de l’image»
COPY « fichier local» « répertoire du conteneur»		
ADD ‘’ ‘’
EXPOSE «ouvrir un port de connexion»
WORKDIR «Répertoire par défaut de connexion»
CMD «Commande qui se lance au lancement du contener»

Créer une image = 
docker build -t utilisateur/projet:nomPush ./repertoire

Lancer un contener :
docker run –port portLocal/portContener -d Conterner

arrêter :
docker stop contener
docker exec -it contener commande
docker ps

arrêt de tout kes conteneurs :
docker-compose up
docker-compose stop


Création de compte https://hub.docker.com/
Création d’un repository en publique : https://hub.docker.com/repositories
Créations de fichiers registery et index sous C:\Users\Guyle\OneDrive\Guy\Travail\Itescia M2I\M2\Kubernets\GitDocker\Register selon https://hub.docker.com/_/nginx (fichiers static-html-directory et Dockerfile
Push :
cd C:\Users\Guyle\OneDrive\Guy\Travail\Itescia M2I\M2\Kubernets\GitDocker\Register
docker build -t guy0b/docker:latest .
docker push guy0b/docker
