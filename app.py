from flask import Flask

# Création de l'application Flask
app = Flask(__name__)


# Définition de la route principale
@app.route('/')
def home():
    return "Bienvenue sur mon application Flask !"


# Route additionnelle
@app.route('/about')
def about():
    return "Ceci est une page 'À propos'."


# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)