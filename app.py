from flask import Flask, jsonify, request
from database import db
from repository import Pokemon
import config


from service import fetch_and_save_pokemons

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/process_pokemons', methods=['POST'])
def process_pokemons():
    try:
        data = request.get_json()

        if not data or 'pokemon_names' not in data or not isinstance(data['pokemon_names'], list):
            print('error: Invalid data. Expected a JSON with a list of Pokémon names.')
            return jsonify({'error': 'Invalid data. Expected a JSON with a list `pokemon_names`'}), 400

        pokemon_names = data['pokemon_names']

        name, error = fetch_and_save_pokemons(pokemon_names)
        
        if name and error:
            return jsonify({'message': f"Error Processing '{name}': {error}"}), 500

        return jsonify({'message': 'Pokémons processed successfully.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    try:
        pokemons = db.session.query(Pokemon).all()

        result = []
        for pokemon in pokemons:
            abilities = [ability.name for ability in pokemon.abilities]
            types = [type.name for type in pokemon.types]
            result.append({
                'id': pokemon.id,
                'name': pokemon.name,
                'base_experience': pokemon.base_experience,
                'height': pokemon.height,
                'weight': pokemon.weight,
                'abilities': abilities,
                'types': types
            })

        return jsonify(result), 200

    except Exception as e:
        print(f'error: {str(e)}')
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)
