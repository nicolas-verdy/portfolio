import streamlit as st
import pandas as pd
from datetime import date, time


# ========================
# Barre latérale
# ========================


st.sidebar.image("LOGO_VERDY_DATA.jpg")


    # Choix de l'affichage : 
affichage_sel  = st.sidebar.radio(
        "Sommaire",
        ["Accueil", "Mon CV", "Mes Projets Ecole", "Mes Projets Perso", "Contacts et Liens"]
    )
st.sidebar.image("Photo_NV_recentree.jpg", width=300)
st.sidebar.caption("© 2025 Nicolas VERDY")
st.sidebar.caption("Tous droits réservés")

if affichage_sel == "Accueil":
        st.title("Portfolio de Nicolas VERDY")
        st.write(" ")
        st.write(" ")
        st.write("Après 20 années passées dans les achats alimentaires dans le monde du Retail (POMONA 6 ans et AUCHAN RETAIL 15 ans), j'ai suivi un bootcamp intensif de 5 mois en Data Analyst entre Septembre 2024 et Février 2025.")
        st.write(" ")
        st.write("Mon objectif est de poursuivre en alternance pour devenir chef de projet en intelligence artificielle et ingénieur data, en combinant mes compétences techniques avec une approche stratégique pour mener à bien des projets innovants.")
        st.write(" ")
        st.write(" ")
        
        colA, colB = st.columns(2)
        with colA:
                st.image("bigdata.jpg",width=300) 
        with colB:
                st.image("bigdata2.jpg",width=1200) 


if affichage_sel == "Mon CV":
        st.image("CV_NVERDY_DATA_IA_ENGINEER.jpg")

        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://github.com/nicolas-verdy/CV/raw/main/CV%20NVERDY%20DATA%20IA%20ENGINEER.pdf" target="_blank" style="text-decoration: none; color: blue;">'
        'Lien vers le CV à télécharger'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )

        
if affichage_sel == "Mes Projets Ecole":

        st.subheader("Les outils utilisés")
        st.write(" ")
        st.write(" ")
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        outils = [("Airtable", "Logo Airtable.jpg"), ("Scikit-Learn", "sklearn_logo.png"), ("Slack", "logo-Slack-1.webp"), ("Streamlit", "Logo streamlit.jpg"),("Python", "Logo Python-Symbole.jpg") , ("Pandas", "Pandas_logo.svg.png"), ("Canva", "Canva-Nouveau-Logo.jpg") ]   
        for col, (nom, image) in zip([col1, col2, col3, col4, col5, col6, col7], outils):
                with col:
                    st.image(image, width=400)   

        col8, col9, col10, col11, col12, col13, col14 = st.columns(7)
        outils = [("Github", "Logo_github.jpg"), ("Matplotlib", "matplotlib.png"), ("PowerBI", "Power-B.jpg"), ("Seaborn", "seaborn.png"),("SQL", "sql.jpg") , ("My SQL", "my_sql.png"), ("VS CODE", "VS_CODE_LOGO.jpg") ]   
        for col, (nom, image) in zip([col8, col9, col10, col11, col12, col13, col14], outils):
                with col:
                    st.image(image, width=400)  




        st.header("------------------------------------------------------------")

        st.header("Projet 1 - Toys and Models (Oct-24)")
        st.image("toys_model.jpg", width=100)
        st.write("🔍 Contexte du projet : L’objectif était de développer un outil automatisé pour visualiser les indicateurs clés, facilitant ainsi le pilotage stratégique de l’entreprise. 📊 Étapes principales : Analyse des données : Exploration approfondie du schéma de base de données afin d’identifier les structures et relations utiles. Requêtes SQL : Conception de requêtes performantes pour relier les différentes tables et extraire des informations pertinentes. Développement d’un tableau de bord interactif : Création sous Power BI pour présenter les indicateurs stratégiques, couvrant : la performance financière, les résultats commerciaux, les aspects logistiques et les indicateurs RH. 💡 Résultats obtenus : Cet outil a simplifié l’accès aux données, accéléré la prise de décision et optimisé la gestion globale grâce à des visualisations dynamiques et intuitives.")

        st.subheader("Les KPI demandés")
        st.write("Ventes : Le Nombre de produits vendus par catégorie et par mois, avec comparaison et taux de variation par rapport au même mois de l'année précédente.")
        st.write("Finances : Le chiffre d'affaires des commandes des deux derniers mois par pays.")
        st.write("Finances : Les commandes qui n'ont pas encore été payées.")
        st.write("Logistique : Le stock des 5 produits les plus commandés.")
        st.write("Ressources Humaines : Chaque mois, les 2 vendeurs ayant réalisé le plus de chiffres d'affaires")

        col15, col16 = st.columns(2)
        outils = [("KPI1", "KPI1.jpg"), ("KPI2", "KPI2.jpg")]   
        for col, (nom, image) in zip([col15, col16], outils):
                with col:
                    st.image(image, width=400)  

        col17, col18 = st.columns(2)
        outils = [("KPI3", "KPI3.jpg"), ("KPI4", "kpi4.jpg")]   
        for col, (nom, image) in zip([col17, col18], outils):
                with col:
                    st.image(image, width=400)        

        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://github.com/nicolas-verdy/Toys_and_models_WCS" target="_blank" style="text-decoration: none; color: blue;">'
        'Lien vers le repo Github'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )



        st.header("------------------------------------------------------------")

        st.header("Projet 2 - Cinéma dans la Creuse (Déc-24)")
        st.write(" ")
        st.write(" ")
        st.write("🔍 Contexte du projet : Un cinéma de la Creuse souhaitait se moderniser et m'a demandé de créer un moteur de recommandations de films personnalisé, basé sur les bases de données IMDb et TMDB. 📊 Étapes clés réalisées : Une étude de marché locale a permis d'identifier les préférences des spectateurs. Les bases de données ont été analysées pour extraire des tendances clés, comme les genres populaires et les acteurs récurrents. Un moteur de recommandations utilisant des algorithmes de machine learning a ensuite été développé, avec l’intégration des affiches de films dans l’interface utilisateur pour une expérience immersive. 💡 Impact : Le projet a posé les bases d'une stratégie numérique moderne, offrant une expérience personnalisée et interactive, permettant au cinéma d'attirer un public plus large et de fidéliser ses clients.")

        col22, col23 = st.columns(2)
        outils = [("Cine1", "CineCreuse1.jpg"), ("Cine2", "CineCreuse2.jpg")]   
        for col, (nom, image) in zip([col22, col23], outils):
                with col:
                    st.image(image, width=400)    


        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://creusecinewcs-zens.streamlit.app/" target="_blank" style="text-decoration: none; color: blue;">'
        'Lien vers le site de recommandation'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )

        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://github.com/nicolas-verdy/Creuse_cine_WCS" target="_blank" style="text-decoration: none; color: blue;">'
        'Lien vers le repo Github'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )

        st.header("------------------------------------------------------------")

        st.header("Mission DATA - Création Dashboard en accord avec les KPI Clients (Jan-25)")

        st.write(" ")
        st.write("🔍 Contexte du projet : Le client nous a fourni un jeu de données (issu de Kaggle, au format csv) et nous a donné 24h pour lui fournir un dashboard mettant en avant les KPI demandés. 📊 Étapes clés réalisées : Nettoyage de la base de données, choix des graphes en accord avec les KPI clients et analyse. 💡 Réalisation : Dashboard interactif, permettant de filtrer les informations selon les KPI.")

        col19, col20, col21 = st.columns(3)
        outils = [("Missiondata1", "Mission_data1.jpg"), ("Missiondata2", "Mission_data2.jpg"), ("Missiondata3", "Mission_data3.jpg")]   
        for col, (nom, image) in zip([col19, col20, col21], outils):
                with col:
                    st.image(image, width=400)  

        st.markdown(
                '<p style="font-size:20px;">'
                '<a href="https://github.com/nicolas-verdy/WCS_Mission_Data" target="_blank" style="text-decoration: none; color: blue;">'
                'Lien vers le repo Github'
                '</a>'
                '</p>',
                unsafe_allow_html=True
                )


if affichage_sel == "Mes Projets Perso":
        st.header("")
        st.image("Site-en-construction.jpg")
  

if affichage_sel == "Contacts et Liens":

        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://github.com/nicolas-verdy" target="_blank" style="text-decoration: none; color: blue;">'
        'Visitez mon Github pour découvrir mes différents projets ---> ICI'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )
        st.image("Logo_github.jpg", width=200)
        st.write(" ")
        st.write(" ")
        st.write(" ")

        st.markdown(
        '<p style="font-size:20px;">'
        '<a href="https://www.linkedin.com/in/verdy-nicolas-989b90112/" target="_blank" style="text-decoration: none; color: blue;">'
        'Lien vers mon LinkedIn ---> ICI'
        '</a>'
        '</p>',
        unsafe_allow_html=True
        )
        st.image("Logo_linkedin.jpg", width=200)
  




#    Pour lancer Streamlit, copier dans le terminal le code suivant  -->>>       streamlit run portfolio_NV.py