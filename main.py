import os
import sys
from streamlit.web import cli as stcli

# Ce script permet de lancer l'application avec la commande 'python main.py'
# au lieu de 'streamlit run app.py'

if __name__ == "__main__":
    # On définit les arguments comme si on les tapait dans le terminal
    sys.argv = ["streamlit", "run", "app.py"]
    
    # On appelle le lanceur de Streamlit
    sys.exit(stcli.main())
