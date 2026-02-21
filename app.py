import streamlit as st
import json
import os

# configuration de l'application
st.set_page_config(
    page_title="générateur de prompts universel",
    page_icon="🤖",
    layout="wide"
)

# fonction de chargement des données harmonisées
@st.cache_data
def charger_donnees():
    # Rafraîchissement forcé du chargement des données
    base_path = os.path.dirname(__file__)
    logic_path = os.path.join(base_path, 'views/prompt_logic/logic_data.json')
    vision_path = os.path.join(base_path, 'views/prompt_vision/vision_data.json')
    video_path = os.path.join(base_path, 'views/prompt_video/video_data.json')
    audio_path = os.path.join(base_path, 'views/prompt_audio/audio_data.json')
    
    logic = {}
    vision = {}
    video = {}
    audio = {}
    
    if os.path.exists(logic_path):
        with open(logic_path, 'r', encoding='utf-8') as f:
            logic = json.load(f)
    
    if os.path.exists(vision_path):
        with open(vision_path, 'r', encoding='utf-8') as f:
            vision = json.load(f)
            
    if os.path.exists(video_path):
        with open(video_path, 'r', encoding='utf-8') as f:
            video = json.load(f)
            
    if os.path.exists(audio_path):
        with open(audio_path, 'r', encoding='utf-8') as f:
            audio = json.load(f)
            
    return logic, vision, video, audio

logic_data, vision_data, video_data, audio_data = charger_donnees()


# barre latérale pour la navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Outil", [
    "🏠 Accueil et guide", 
    "📝 Générateur de texte", 
    "📸 Générateur d'image",
    "🎥 Générateur de vidéo",
    "🎵 Générateur de musique"
], label_visibility="collapsed")

# Injection CSS
st.markdown("""
    <style>
    /* Améliorations Mobile (évite le zoom iOS, ajuste padding) */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        font-size: 16px !important;
    }
    /* Ajout d'une touche de couleur aux titres */
    h1 { color: #1e40af; }
    h2, h3 { color: #3b82f6; }
    </style>
""", unsafe_allow_html=True)

if page == "🏠 Accueil et guide":
    st.title("Bienvenue sur le générateur de prompts 🤖")
    st.markdown("---")
    
    st.header("💡 Pourquoi structurer ses prompts ?")
    st.markdown("""
    Communiquer avec une intelligence artificielle (comme ChatGPT, Claude, Gemini, Perplexity ou Mistral) demande de la précision. 
    Un "prompt" (la requête que vous envoyez) brouillon donnera une réponse brouillonne.
    
    **Un prompt bien structuré permet de :**
    - **Cibler l'expertise :** En donnant un rôle à l'IA, elle mobilise le bon vocabulaire.
    - **Éviter les hallucinations :** Plus le contexte est clair, moins l'IA invente d'informations.
    - **Gagner du temps :** En imposant un format de sortie (tableau, synthèse, code), vous n'avez pas à reformuler la réponse.
    """)
    
    st.markdown("---")
    
    col_g1, col_g2 = st.columns(2, gap="large")
    
    with col_g1:
        with st.container(border=True):
            st.subheader("📝 Le générateur textuel")
            st.markdown("""
            Cet outil est conçu pour les IA de texte (ChatGPT, Claude, Gemini, Perplexity, Mistral...). 
            
            **Comment l'utiliser ?**
            1. **Choisissez un métier** (ex: Achats, Développement) pour orienter l'IA.
            2. **Chargez un modèle** pré-existant ou créez votre prompt de zéro.
            3. Remplissez la **mission** et le **contexte** pour détailler votre besoin.
            4. Dépliez les options avancées pour imposer un ton (Professionnel, Amical) et un format (Tableau, Liste à puces).
            5. Copiez le résultat généré et collez-le dans votre IA !
            """)
            
    with col_g2:
        with st.container(border=True):
            st.subheader("📸 / 🎥 Le générateur visuel et vidéo")
            st.markdown("""
            Cet outil est conçu pour les générateurs d'images (Midjourney, DALL-E) et vidéos (Sora, Runway, Gemini).
            
            **Comment l'utiliser ?**
            1. **Choisissez le style global** de l'image ou de la vidéo (Cinématique, Animation).
            2. Décrivez avec vos mots la **scène principale**.
            3. Paramétrez les aspects techniques (Type de lentille, éclairage, ou **mouvement de caméra**) dans les options avancées.
            4. Utilisez les **exclusions** (Prompt négatif) pour indiquer ce que vous ne voulez *absolument pas* voir.
            5. Le résultat technique généré peut être envoyé directement au moteur de rendu.
            """)
            
        with st.container(border=True):
            st.subheader("🎵 Le générateur de musique")
            st.markdown("""
            Cet outil est conçu pour les générateurs d'audio (Suno, Udio, Gemini).
            
            **Comment l'utiliser ?**
            1. **Choisissez le genre musical** (Pop, Cinématique...).
            2. Paramétrez le **tempo** et les **voix**.
            3. L'outil structure une requête optimisée pour le générateur audio.
            """)
    
    st.info("👈 Utilisez le menu de gauche pour démarrer la génération !")

elif page == "📝 Générateur de texte":
    st.title("📝 Générateur textuel")
    st.markdown("Créez des prompts précis et efficaces pour vos IA textuelles (ChatGPT, Claude, Gemini, Perplexity, Mistral...).")
    
    if not logic_data:
        st.error("Erreur : le fichier logic_data.json est introuvable dans views/prompt_logic/.")
    else:
        # Sur mobile, col1 et col2 vont s'empiler automatiquement. Sur desktop, ils seront côte à côte.
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            with st.container(border=True):
                st.subheader("⚙️ Configuration")
                # sélection du métier
                job_keys = list(logic_data.keys())
                job_id = st.selectbox(
                    "Domaine d'expertise", 
                    job_keys, 
                    format_func=lambda x: logic_data[x]['translations']['fr']['title']
                )
                
                job = logic_data[job_id]
                templates = job.get('templates', {})
                
                # sélection du modèle
                tpl_list = ["Aucun modèle"] + [templates[t]['fr']['name'] for t in templates]
                selected_tpl_name = st.selectbox("Modèles disponibles", tpl_list)
                
                # pré-remplissage si un modèle est sélectionné
                initial_values = {}
                if selected_tpl_name != "Aucun modèle":
                    for t_key in templates:
                        if templates[t_key]['fr']['name'] == selected_tpl_name:
                            initial_values = templates[t_key]['fr']
                            break
            
            with st.container(border=True):
                st.subheader("✍️ Contenu du prompt")
                role = st.text_input("Rôle (Agis en tant que...)", value=initial_values.get('role', ''))
                task = st.text_area("Mission principale", value=initial_values.get('task', ''), height=100)
                context = st.text_area("Contexte et détails", value=initial_values.get('context', ''), height=100)
                
                with st.expander("Options avancées (ton, format)"):
                    c_a, c_b = st.columns(2)
                    with c_a:
                        tones = [t['label']['fr'] for t in job['options']['tones']]
                        tone = st.selectbox("Ton employé", tones)
                    with c_b:
                        formats = [f['label']['fr'] for f in job['options']['formats']]
                        format_out = st.selectbox("Format attendu", formats)
                        
                    constraints = st.text_input("Contraintes additionnelles", value=initial_values.get('constraints', ''))

        with col2:
            with st.container(border=True):
                st.subheader("🎯 Résultat")
                
                # assemblage du prompt final (logique métier)
                prompt_parts = []
                if role:
                    prompt_parts.append(f"### AGIS EN TANT QUE {role.upper()}")
                    prompt_parts.append("Tu possèdes une expertise approfondie dans ce domaine.\n")
                if task:
                    prompt_parts.append(f"### MISSION\n{task}\n")
                if context:
                    prompt_parts.append(f"### CONTEXTE\n{context}\n")
                
                if tone or format_out or constraints:
                    prompt_parts.append(f"### PARAMÈTRES DE SORTIE")
                    if tone: prompt_parts.append(f"- Ton : {tone}")
                    if format_out: prompt_parts.append(f"- Format : {format_out}")
                    if constraints: prompt_parts.append(f"- Contraintes : {constraints}")
                
                final_text = "\n".join(prompt_parts)
                
                if final_text.strip():
                    st.code(final_text, language="markdown")
                    st.caption("💡 Cliquez sur l'icône de copie en haut à droite du bloc pour l'utiliser.")
                else:
                    st.info("👈 Remplissez le formulaire à gauche pour voir le prompt s'afficher ici.")

elif page == "📸 Générateur d'image":
    st.title("📸 Générateur visuel")
    st.markdown("Paramétrez vos requêtes pour des IA génératives d'images (Midjourney, DALL-E, etc.).")
    
    if not vision_data:
        st.error("Erreur : le fichier vision_data.json est introuvable dans views/prompt_vision/.")
    else:
        col_v1, col_v2 = st.columns([1, 1], gap="large")
        
        with col_v1:
            with st.container(border=True):
                st.subheader("🎨 Paramètres visuels")
                
                modes = vision_data.get('modes', {})
                mode_id = st.selectbox(
                    "Style de l'image ou catégorie", 
                    list(modes.keys()), 
                    format_func=lambda x: modes[x]['translations']['fr']
                )
                
                concept = st.text_area("Description de la scène", placeholder="Ex : Un chat lisant un livre dans l'espace...")
                
                with st.expander("Détails et styles spécifiques", expanded=True):
                    # génération dynamique des champs selon le json
                    fields = modes[mode_id].get('fields', [])
                    selections = {}
                    
                    for field in fields:
                        options_labels = [opt['label']['fr'] for opt in field['options']]
                        choice = st.selectbox(field['label']['fr'], options_labels)
                        # récupération de la valeur technique associée au label
                        val_technique = next(opt['val'] for opt in field['options'] if opt['label']['fr'] == choice)
                        selections[field['id']] = val_technique
                        
                with st.expander("Exclusions (prompt négatif)"):
                    neg_prompt = st.text_input("Éléments à exclure", value="blur, low quality, distorted, bad anatomy")

        with col_v2:
            with st.container(border=True):
                st.subheader("📋 Résultat technique")
                
                # création de la structure de sortie harmonisée
                output_data = {
                    "mode": mode_id,
                    "prompt_principal": concept,
                    "parametres": selections,
                    "negatif": neg_prompt
                }
                
                st.json(output_data)
                st.info("ℹ️ Ce format structuré peut être utilisé par vos scripts ou agents d'automatisation.")

elif page == "🎥 Générateur de vidéo":
    st.title("🎥 Générateur vidéo")
    st.markdown("Paramétrez vos requêtes pour des IA génératives de vidéos (Sora, Runway, Gemini, etc.).")
    
    if not video_data:
        st.error("Erreur : le fichier video_data.json est introuvable dans views/prompt_video/.")
    else:
        col_v1, col_v2 = st.columns([1, 1], gap="large")
        
        with col_v1:
            with st.container(border=True):
                st.subheader("🎬 Paramètres vidéo")
                
                modes = video_data.get('modes', {})
                mode_id = st.selectbox(
                    "Style de la vidéo", 
                    list(modes.keys()), 
                    format_func=lambda x: modes[x]['translations']['fr']
                )
                
                concept = st.text_area("Description du plan", placeholder="Ex : Un lent travelling sur une forêt vue du ciel...")
                
                with st.expander("Mouvements et paramètres", expanded=True):
                    fields = modes[mode_id].get('fields', [])
                    selections = {}
                    
                    for field in fields:
                        options_labels = [opt['label']['fr'] for opt in field['options']]
                        choice = st.selectbox(field['label']['fr'], options_labels, key=f"vid_{field['id']}")
                        val_technique = next(opt['val'] for opt in field['options'] if opt['label']['fr'] == choice)
                        selections[field['id']] = val_technique
                        
                with st.expander("Exclusions (prompt négatif)"):
                    neg_prompt = st.text_input("Éléments à exclure (vidéo)", value="bad anatomy, extra limbs, jerky motion")

        with col_v2:
            with st.container(border=True):
                st.subheader("📋 Résultat technique")
                # Format plus adapté aux IA de vidéo (souvent un gros bloc de texte)
                
                prompt_parts = []
                if mode_id:
                    prompt_parts.append(f"Style: {mode_id}")
                if concept:
                    prompt_parts.append(f"Scene: {concept}")
                for k, v in selections.items():
                    prompt_parts.append(f"{k.capitalize()}: {v}")
                if neg_prompt:
                    prompt_parts.append(f"--no {neg_prompt}")
                
                final_text = " | ".join(prompt_parts)
                st.code(final_text, language="markdown")
                st.caption("💡 Copiez cette ligne pour l'utiliser dans Runway ou Sora.")

elif page == "🎵 Générateur de musique":
    st.title("🎵 Générateur de musique")
    st.markdown("Structurez vos requêtes pour les IA musicales (Suno, Udio, Gemini, etc.).")
    
    if not audio_data:
        st.error("Erreur : le fichier audio_data.json est introuvable dans views/prompt_audio/.")
    else:
        col_a1, col_a2 = st.columns([1, 1], gap="large")
        
        with col_a1:
            with st.container(border=True):
                st.subheader("🎼 Paramètres audio")
                
                genres = audio_data.get('genres', {})
                genre_id = st.selectbox(
                    "Genre musical", 
                    list(genres.keys()), 
                    format_func=lambda x: genres[x]['translations']['fr']
                )
                
                concept = st.text_area("Thème de la chanson ou Paroles", placeholder="Ex : Une chanson sur le courage et l'exploration spatiale...")
                
                with st.expander("Tempo et Ambiance", expanded=True):
                    fields = genres[genre_id].get('fields', [])
                    selections = {}
                    
                    for field in fields:
                        options_labels = [opt['label']['fr'] for opt in field['options']]
                        choice = st.selectbox(field['label']['fr'], options_labels, key=f"aud_{field['id']}")
                        val_technique = next(opt['val'] for opt in field['options'] if opt['label']['fr'] == choice)
                        selections[field['id']] = val_technique

        with col_a2:
            with st.container(border=True):
                st.subheader("📋 Résultat technique")
                
                prompt_parts = []
                prompt_parts.append(f"[Genre] {genre_id}")
                for k, v in selections.items():
                    prompt_parts.append(f"[{k.capitalize()}] {v}")
                
                if concept:
                    prompt_parts.append(f"\n{concept}")
                
                final_text = "\n".join(prompt_parts)
                st.code(final_text, language="markdown")
                st.caption("💡 Utilisez ces 'Tags' pour générer votre musique (ex: sur Suno.ai).")