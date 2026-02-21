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


# ---------------------------------------------------------
# GESTION DES LANGUES (Page Accueil Uniquement)
# ---------------------------------------------------------
HOME_TRANSLATIONS = {
    'fr': {
        'nav_home': '🏠 Accueil et guide', 'nav_text': '📝 Générateur de texte', 'nav_image': '📸 Générateur d\'image', 'nav_video': '🎥 Générateur de vidéo', 'nav_audio': '🎵 Générateur de musique',
        'sidebar_lang': '🌐 Langue (Language)',
        'sidebar_theme': '🎨 Thème',
        'theme_light': '☀️ Clair', 'theme_dark': '🌙 Sombre',
        'welcome_title': 'Bienvenue sur le générateur de prompts 🤖',
        'why_structure_title': '💡 Pourquoi structurer ses prompts ?',
        'why_desc': 'Communiquer avec une intelligence artificielle (ChatGPT, Claude, Gemini) demande de la précision. Un prompt brouillon donnera une réponse brouillonne.',
        'benefit_1_title': '🎯 Cibler l\'expertise', 'benefit_1_desc': 'En donnant un rôle à l\'IA, elle mobilise le bon vocabulaire.',
        'benefit_2_title': '🛡️ Réduire les hallucinations', 'benefit_2_desc': 'Plus le contexte est clair, moins l\'IA invente d\'informations.',
        'benefit_3_title': '⏱️ Gagner du temps', 'benefit_3_desc': 'En imposant un format de sortie, vous n\'avez pas à reformuler.',
        'card_text_title': '📝 Le générateur textuel',
        'card_text_desc': 'Orientez l\'IA en choisissant un **métier**, une **mission** et un **format** de sortie (Tableau, Synthèse...).',
        'card_img_vid_title': '📸 / 🎥 Le générateur visuel et vidéo',
        'card_img_vid_desc': 'Définissez non seulement la scène, mais aussi les **mouvements de caméra**, le **framerate** et les **exclusions**.',
        'card_audio_title': '🎵 Le générateur de musique',
        'card_audio_desc': 'Gérérez des "tags" musicaux parfaits en paramétrant le **genre**, le **tempo** et les **voix**.',
        'footer_start': '👈 Utilisez le menu de gauche pour démarrer la génération !'
    },
    'en': {
        'nav_home': '🏠 Home & Guide', 'nav_text': '📝 Text Generator', 'nav_image': '📸 Image Generator', 'nav_video': '🎥 Video Generator', 'nav_audio': '🎵 Music Generator',
        'sidebar_lang': '🌐 Language',
        'sidebar_theme': '🎨 Theme',
        'theme_light': '☀️ Light', 'theme_dark': '🌙 Dark',
        'welcome_title': 'Welcome to the Prompt Generator 🤖',
        'why_structure_title': '💡 Why structure your prompts?',
        'why_desc': 'Communicating with an AI (ChatGPT, Claude, Gemini) requires precision. A messy prompt gives a messy answer.',
        'benefit_1_title': '🎯 Target Expertise', 'benefit_1_desc': 'Assigning a role helps the AI use the right vocabulary.',
        'benefit_2_title': '🛡️ Reduce Hallucinations', 'benefit_2_desc': 'A clear context stops the AI from inventing facts.',
        'benefit_3_title': '⏱️ Save Time', 'benefit_3_desc': 'Force an output format so you don\'t have to rewrite it.',
        'card_text_title': '📝 Text Generator',
        'card_text_desc': 'Guide the AI by choosing a **profession**, a **mission**, and an **output format**.',
        'card_img_vid_title': '📸 / 🎥 Image & Video Generator',
        'card_img_vid_desc': 'Define the scene along with **camera motions**, **framerates**, and **negative prompts**.',
        'card_audio_title': '🎵 Music Generator',
        'card_audio_desc': 'Generate perfect musical "tags" by tweaking **genre**, **tempo**, and **vocals**.',
        'footer_start': '👈 Use the left menu to start generating!'
    },
    'es': {
        'nav_home': '🏠 Inicio y Guía', 'nav_text': '📝 Generador de Texto', 'nav_image': '📸 Generador de Imagen', 'nav_video': '🎥 Generador de Video', 'nav_audio': '🎵 Generador de Música',
        'sidebar_lang': '🌐 Idioma (Language)',
        'sidebar_theme': '🎨 Tema',
        'theme_light': '☀️ Claro', 'theme_dark': '🌙 Oscuro',
        'welcome_title': 'Bienvenido al Generador de Prompts 🤖',
        'why_structure_title': '💡 ¿Por qué estructurar tus prompts?',
        'why_desc': 'Comunicarse con una IA requiere precisión. Un prompt desordenado da una respuesta desordenada.',
        'benefit_1_title': '🎯 Enfocar la Experiencia', 'benefit_1_desc': 'Asignar un rol ayuda a la IA a usar el vocabulario adecuado.',
        'benefit_2_title': '🛡️ Evitar Alucinaciones', 'benefit_2_desc': 'Un contexto claro evita que la IA invente información.',
        'benefit_3_title': '⏱️ Ahorrar Tiempo', 'benefit_3_desc': 'Imponga un formato de salida para no tener que reelaborarlo.',
        'card_text_title': '📝 El Generador Textual',
        'card_text_desc': 'Guía a la IA eligiendo una **profesión**, una **misión** y un **formato**.',
        'card_img_vid_title': '📸 / 🎥 El Generador Visual',
        'card_img_vid_desc': 'Define la escena junto con **movimientos de cámara**, **FPS** y **exclusiones**.',
        'card_audio_title': '🎵 El Generador de Música',
        'card_audio_desc': 'Genera etiquetas musicales perfilando el **género**, **tempo** y **voces**.',
        'footer_start': '👈 ¡Usa el menú de la izquierda para comenzar!'
    },
    'de': {
        'nav_home': '🏠 Start & Hilfe', 'nav_text': '📝 Text-Generator', 'nav_image': '📸 Bild-Generator', 'nav_video': '🎥 Video-Generator', 'nav_audio': '🎵 Musik-Generator',
        'sidebar_lang': '🌐 Sprache (Language)',
        'sidebar_theme': '🎨 Design',
        'theme_light': '☀️ Hell', 'theme_dark': '🌙 Dunkel',
        'welcome_title': 'Willkommen beim Prompt-Generator 🤖',
        'why_structure_title': '💡 Warum Prompts strukturieren?',
        'why_desc': 'Die Kommunikation mit KI erfordert Präzision. Ein chaotischer Prompt liefert eine chaotische Antwort.',
        'benefit_1_title': '🎯 Expertise anvisieren', 'benefit_1_desc': 'Eine Rolle hilft der KI, das richtige Vokabular zu nutzen.',
        'benefit_2_title': '🛡️ Halluzinationen reduzieren', 'benefit_2_desc': 'Klarer Kontext hindert die KI am Erfinden von Fakten.',
        'benefit_3_title': '⏱️ Zeit sparen', 'benefit_3_desc': 'Geben Sie ein Format vor, um Nacharbeiten zu vermeiden.',
        'card_text_title': '📝 Text-Generator',
        'card_text_desc': 'Leiten Sie die KI an: Wählen Sie **Beruf**, **Mission** und **Format**.',
        'card_img_vid_title': '📸 / 🎥 Bild- & Video-Generator',
        'card_img_vid_desc': 'Definieren Sie Szenen mit **Kamerabewegungen**, **Framerate** und **Ausschlüssen**.',
        'card_audio_title': '🎵 Musik-Generator',
        'card_audio_desc': 'Erstellen Sie musikalische Tags per **Genre**, **Tempo** und **Stimmen**.',
        'footer_start': '👈 Nutzen Sie das Menü links, um zu starten!'
    }
}

# Initialisation de la session
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'fr'
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'light'

# ---------------------------------------------------------
# BARRE LATÉRALE (SIDEBAR) & STYLING DYNAMIQUE
# ---------------------------------------------------------
st.sidebar.title("🧭 Navigation")

# Sélecteurs de configuration dans la sidebar (pour l'accueil)
lang_options = {'fr': '🇫🇷 Français', 'en': '🇬🇧 English', 'es': '🇪🇸 Español', 'de': '🇩🇪 Deutsch'}
t = HOME_TRANSLATIONS[st.session_state['lang']]

st.sidebar.markdown("---")
new_lang = st.sidebar.selectbox(t['sidebar_lang'], options=list(lang_options.keys()), format_func=lambda x: lang_options[x], index=list(lang_options.keys()).index(st.session_state['lang']))
if new_lang != st.session_state['lang']:
    st.session_state['lang'] = new_lang
    st.rerun()

theme_options = {'light': t['theme_light'], 'dark': t['theme_dark']}
new_theme = st.sidebar.selectbox(t['sidebar_theme'], options=['light', 'dark'], format_func=lambda x: theme_options[x], index=0 if st.session_state['theme']=='light' else 1)
if new_theme != st.session_state['theme']:
    st.session_state['theme'] = new_theme
    st.rerun()
st.sidebar.markdown("---")

# Navigation radio buttons
page_labels = [t['nav_home'], t['nav_text'], t['nav_image'], t['nav_video'], t['nav_audio']]
page_idx = st.sidebar.radio("Outil", range(len(page_labels)), format_func=lambda i: page_labels[i], label_visibility="collapsed")

# Injection CSS pour le thème Material Design 4
bg_color = "#FAFAFA" if st.session_state['theme'] == 'light' else "#141218"
text_color = "#1D1B20" if st.session_state['theme'] == 'light' else "#E6E0E9"
container_bg = "#FFFFFF" if st.session_state['theme'] == 'light' else "#2B2930"
sidebar_bg = "#F3EDF7" if st.session_state['theme'] == 'light' else "#2B2930"

st.markdown(f"""
    <style>
    /* Import de la police Google Sans (remplacée par Roboto si indispo) */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
    
    html, body, p, h1, h2, h3, h4, h5, h6, label, input, textarea, button, li {{
        font-family: 'Roboto', sans-serif;
    }}

    /* Fond Global */
    .stApp, [data-testid="stAppViewContainer"] {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg} !important;
        border-right: none !important;
    }}

    /* Typographie Générale */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown li, label, .stRadio div, .stSelectbox div, .st-emotion-cache-1629p8f p {{
        color: {text_color} !important;
    }}
    
    h1, h2, h3 {{ color: #0A56D1 !important; font-weight: 500 !important; }}

    /* Alertes (Info, Success, Warning) */
    [data-testid="stAlert"] *, [data-testid="stAlert"] p, [data-testid="stAlert"] span {{
        color: {text_color} !important;
    }}

    /* Cartes et Conteneurs (Elevation 1) */
    [data-testid="stVerticalBlockBorderWrapper"] > div {{
        background-color: {container_bg} !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 1rem !important;
        box-shadow: 0 1px 3px 0 rgba(0,0,0,0.12), 0 1px 2px 0 rgba(0,0,0,0.24) !important;
        transition: box-shadow 0.3s cubic-bezier(.25,.8,.25,1);
    }}
    [data-testid="stVerticalBlockBorderWrapper"] > div:hover {{
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.15), 0 4px 6px 0 rgba(0,0,0,0.20) !important;
    }}

    /* Champs de Saisie (Filled Variant) */
    input[type="text"], input[type="number"], textarea, div[data-baseweb="select"] > div {{
        background-color: {"rgba(10, 86, 209, 0.04)" if st.session_state['theme'] == 'light' else "rgba(208, 188, 255, 0.08)"} !important;
        color: {text_color} !important;
        border: 1px solid transparent !important;
        border-bottom: 1px solid #79747E !important;
        border-radius: 4px 4px 0 0 !important;
    }}
    input:focus, textarea:focus, div[data-baseweb="select"] > div:focus-within {{
        border-bottom: 2px solid #0A56D1 !important;
        background-color: {"rgba(10, 86, 209, 0.08)" if st.session_state['theme'] == 'light' else "rgba(208, 188, 255, 0.12)"} !important;
    }}

    /* Boutons (Pilled/Tonal variant) */
    button[kind="primary"], button[kind="secondary"] {{
        border-radius: 100px !important;
        text-transform: none !important;
        font-weight: 500 !important;
        letter-spacing: 0.1px !important;
        padding: 10px 24px !important;
        border: none !important;
        background-color: #0A56D1 !important;
        color: white !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
        transition: all 0.2s ease-in-out !important;
    }}
    button[kind="secondary"] {{
        background-color: {sidebar_bg} !important;
        color: #0A56D1 !important;
    }}
    button[kind="primary"]:hover, button[kind="secondary"]:hover {{
        box-shadow: 0 1px 3px rgba(0,0,0,0.3), 0 4px 8px rgba(0,0,0,0.15) !important;
        transform: translateY(-1px);
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# CORPS DE LA PAGE
# ---------------------------------------------------------
if page_idx == 0:  # Accueil
    st.title(t['welcome_title'])
    st.markdown("---")
    
    st.header(t['why_structure_title'])
    st.write(t['why_desc'])
    
    # 3 colonnes pour aérer la liste à puces "Pourquoi"
    c1, c2, c3 = st.columns(3)
    c1.info(f"**{t['benefit_1_title']}**\n\n{t['benefit_1_desc']}")
    c2.success(f"**{t['benefit_2_title']}**\n\n{t['benefit_2_desc']}")
    c3.warning(f"**{t['benefit_3_title']}**\n\n{t['benefit_3_desc']}")
    
    st.markdown("<br><br>", unsafe_allow_html=True) # Espacement vertical
    
    col_g1, col_g2, col_g3 = st.columns(3, gap="large")
    
    with col_g1:
        with st.container(border=True):
            st.subheader(t['card_text_title'])
            st.write(t['card_text_desc'])
            
    with col_g2:
        with st.container(border=True):
            st.subheader(t['card_img_vid_title'])
            st.write(t['card_img_vid_desc'])

    with col_g3:
        with st.container(border=True):
            st.subheader(t['card_audio_title'])
            st.write(t['card_audio_desc'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.success(t['footer_start'], icon="🚀")

elif page_idx == 1:  # Générateur de Texte
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
                
                example = st.text_area("Exemple attendu (Few-Shot)", value=initial_values.get('example', ''), height=100)
                instructions = st.text_area("Instructions spécifiques", value=initial_values.get('instructions', ''), height=100)
                
                with st.expander("Options avancées (ton, format)"):
                    c_a, c_b = st.columns(2)
                    with c_a:
                        tones = [t['label']['fr'] for t in job['options']['tones']]
                        tone = st.selectbox("Ton employé", tones)
                    with c_b:
                        formats = [f['label']['fr'] for f in job['options']['formats']]
                        format_out = st.selectbox("Format attendu", formats)
                        
                    constraints = st.text_input("Contraintes additionnelles", value=initial_values.get('constraints', ''))
                    
                with st.expander("Méthodologie IA"):
                    interactive = st.checkbox("Mode Interactif (Demander de poser des questions d'abord)")
                    cot = st.checkbox("Réflexion par étapes (Chain of Thought)")

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
                
                if example:
                    prompt_parts.append(f"### EXEMPLE ATTENDU\nVoici un exemple pour guider ta réponse :\n\"\"\"\n{example}\n\"\"\"\n")
                
                criteria = []
                if tone: criteria.append(f"- Ton : {tone}")
                if format_out: criteria.append(f"- Format : {format_out}")
                if constraints: criteria.append(f"- Contraintes : {constraints}")
                
                if instructions:
                    for line in instructions.split('\n'):
                        if line.strip():
                            if not line.strip().startswith('-') and not line.strip().startswith('•'):
                                criteria.append(f"- {line.strip()}")
                            else:
                                criteria.append(line.strip())
                
                if criteria:
                    prompt_parts.append(f"### INSTRUCTIONS & CRITÈRES\nRespecte impérativement ces points :")
                    prompt_parts.append("\n".join(criteria) + "\n")
                    
                if interactive or cot:
                    prompt_parts.append(f"### MÉTHODOLOGIE")
                    if interactive:
                        prompt_parts.append("⚠️ AVANT de répondre, pose-moi 2 ou 3 questions courtes pour clarifier ma demande.")
                    if cot:
                        prompt_parts.append("🧠 Réfléchis étape par étape (Chain of Thought).")

                
                final_text = "\n".join(prompt_parts)
                
                if final_text.strip():
                    st.code(final_text, language="markdown")
                    st.caption("💡 Cliquez sur l'icône de copie en haut à droite du bloc pour l'utiliser.")
                else:
                    st.info("👈 Remplissez le formulaire à gauche pour voir le prompt s'afficher ici.")

elif page_idx == 2:  # Générateur Visuel
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
                    fields = list(modes[mode_id].get('fields', []))
                    
                    # Ajouter les champs communs (action, scene, camera) si applicables
                    groups = modes[mode_id].get('groups', [])
                    common_data = vision_data.get('common', {})
                    for group in groups:
                        if group in common_data:
                            fields.extend(common_data[group])
                    
                    selections = {}
                    
                    for field in fields:
                        if field.get('type') == 'text':
                            choice = st.text_input(field['label']['fr'], value=field.get('default', ''))
                            if choice:
                                selections[field['id']] = choice
                        else:
                            options_labels = [opt['label']['fr'] for opt in field['options']]
                            choice = st.selectbox(field['label']['fr'], ["-- Sélectionner --"] + options_labels)
                            if choice != "-- Sélectionner --":
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

elif page_idx == 3:  # Générateur de vidéo
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

elif page_idx == 4:  # Générateur de musique
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
                
                with st.expander("Tempo, Ambiance et Instruments", expanded=True):
                    fields = genres[genre_id].get('fields', [])
                    selections = {}
                    
                    for field in fields:
                        options_labels = [opt['label']['fr'] for opt in field['options']]
                        choice = st.selectbox(field['label']['fr'], ["-- Sélectionner --"] + options_labels, key=f"aud_{field['id']}")
                        if choice != "-- Sélectionner --":
                            val_technique = next(opt['val'] for opt in field['options'] if opt['label']['fr'] == choice)
                            selections[field['id']] = val_technique
                
                with st.expander("Détails avancés (Optionnel)"):
                    tonalite = st.text_input("Tonalité (ex: C minor, Do Majeur)")
                    langue = st.text_input("Langue des paroles (ex: Français, English)")
                    influence = st.text_input("Influence Artiste ou Lien (ex: Daft Punk, ou lien Spotify/Deezer)")

        with col_a2:
            with st.container(border=True):
                st.subheader("📋 Résultat technique")
                
                prompt_parts = []
                prompt_parts.append(f"[Genre] {genre_id}")
                for k, v in selections.items():
                    prompt_parts.append(f"[{k.capitalize()}] {v}")
                
                if tonalite:
                    prompt_parts.append(f"[Key] {tonalite}")
                if langue:
                    prompt_parts.append(f"[Language] {langue}")
                if influence:
                    prompt_parts.append(f"[Influence] Style of {influence}")
                
                if concept:
                    prompt_parts.append(f"\n{concept}")
                
                final_text = "\n".join(prompt_parts)
                st.code(final_text, language="markdown")
                st.caption("💡 Utilisez ces 'Tags' pour générer votre musique (ex: sur Suno.ai).")