from Flask import Flask, send_from_directory
import os

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour servir les fichiers GeoParquet
@app.route('/serve-geo-parquet/<filename>')
def serve_geo_parquet(filename):
    # Répertoire où vous stockez vos fichiers GeoParquet
    directory = '/path/to/your/geo_parquet_files'  # Modifiez ce chemin
    return send_from_directory(directory, filename)

# Démarrer le serveur web
if __name__ == "__main__":
    app.run(debug=True)
