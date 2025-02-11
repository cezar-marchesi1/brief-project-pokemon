from database import db


pokemon_type = db.Table('pokemon_type',
                        db.Column('pokemon_id', db.Integer, db.ForeignKey(
                            'pokemon.id'), primary_key=True),
                        db.Column('type_id', db.Integer, db.ForeignKey(
                            'type.id'), primary_key=True)
                        )


class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    base_experience = db.Column(db.Integer)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    abilities = db.relationship(
        'Ability', backref='pokemon', lazy=True, cascade='all, delete-orphan')

    types = db.relationship('Type', secondary=pokemon_type,
                            backref=db.backref('pokemons', lazy=True))


class Ability(db.Model):
    __tablename__ = 'ability'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    pokemon_id = db.Column(db.Integer, db.ForeignKey(
        'pokemon.id'), nullable=False)


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
