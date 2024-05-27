# code pour la classe Character
import pandas as pd


class Character:
    # attributs de classe
    all_character_objects = []  # une liste qui contient tous les objets de character
    all_characters_id = []  # une liste de tous les id de character
    all_names_id = []
    all_movies_id = []
    all_genders_id = []
    all_credits_positions_id = []

    def __init__(self, character_id, name_id, movie_id, gender_id, credits_position_id):
        """ Initialise character avec les attributs
                Args :
        character_id : string, ID d'un character en particulier
        name_id : string, ID du nom du personnage
        movie_id : string, ID du film du personnage
        gender_id : string, genre du personnage
        credits_position_id : string, position des crédits du personnage
        """
        self.character_id = character_id  # id d'un character en particulier
        self.name_id = name_id
        self.movie_id = movie_id
        self.gender_id = gender_id
        self.credits_position_id = credits_position_id

    def get_name_id(self, character_id):
        """Retourne un ID de nom associé à un ID de personnage

            Args :
                character_id : un string qui contient l'ID de character.

            Returns :
                Mettre ensemble all_characters_id et all_names_id avec un zip. Ensuite,
                mettre ceci dans un dictionnaire nommé merged_list. Avec cela, on peut
                utiliser l'ID d'un personnage pour chercher son nom correspondant.
        """
        merged_list = dict(zip(self.all_characters_id, self.all_names_id))
        # cherche l'id character donné et retourne l'id name associé
        return merged_list[character_id]

    def get_movie_id(self, character_id):
        """Retourne un ID de movie associée à un ID de character"""
        merged_list = dict(zip(self.all_characters_id, self.all_movies_id))
        return merged_list[character_id]

    def get_gender_id(self, character_id):
        """Retourne un ID de genre associé à un ID de character"""
        merged_list = dict(zip(self.all_characters_id, self.all_genders_id))
        return merged_list[character_id]

    def get_credits_position_id(self, character_id):
        """Retourne un ID de position dans les crédits associée à un ID de character"""
        merged_list = dict(zip(self.all_characters_id, self.all_credits_positions_id))
        return merged_list[character_id]

    # création de @property pour pouvoir accéder aux attributs (avant __init__)
    @property
    def _all_names_id(self):
        """Accéder à l'attribut de classe all_names_id

            Returns :
            La création d'une méthode avec un @property permet d'accéder
            aux attributs de classe
        """
        return self.all_names_id

    @property
    def _all_movies_id(self):
        """Accéder à l'attribut de classe all_movies_id"""
        return self.all_movies_id

    @property
    def _all_genders_id(self):
        """Accéder à l'attribut de classe all_genders_id"""
        return self.all_genders_id

    @property
    def _all_credits_positions_id(self):
        """Accéder à l'attribut de classe all_credits_positions_id"""
        return self.all_credits_positions_id

    @property
    def _all_characters_id(self):
        """Accéder à l'attribut de classe all_characters_id"""
        return self.all_characters_id

    # création de @classmethod
    @classmethod
    def get_all_names(cls, id_list):
        """Une liste d'ID de personnages pour une liste de noms

            Args :
            cls : @classmethod qui accède aux attributs de classe.
            id_list : une liste d'ID de personnages.

            Returns :
            merged_list contient un dictionnaire avec un zip contenant
            tous les ID de personnages et tous les ID de noms. list_all_names est
            une liste vide qui contiendra les noms qui correspondent aux IDs
            dans id_list (les ID de character).
        """
        merged_list = dict(zip(Character._all_characters_id, Character._all_names_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_names = []
        for ids in id_list:
            list_all_names.append(merged_list[ids])
        return list_all_names

    @classmethod
    def get_all_movies_id(cls, id_list):
        """Une liste d'ID de personnages pour une liste de films"""
        merged_list = dict(zip(Character._all_characters_id, Character._all_movies_id))
        list_all_movies = []
        for ids in id_list:
            list_all_movies.append(merged_list[ids])
        return list_all_movies

    @classmethod
    def get_all_genders_id(cls, id_list):
        """Une liste d'ID de personnages pour une liste de genres"""
        merged_list = dict(zip(Character._all_characters_id, Character._all_genders_id))
        list_all_genders = []
        for ids in id_list:
            list_all_genders.append(merged_list[ids])
        return list_all_genders

    @classmethod
    def get_all_credits_positions_id(cls, id_list):
        """Une liste d'ID de personnages pour une liste de positions dans les crédits"""
        merged_list = dict(
            zip(Character._all_characters_id, Character._all_credits_positions_id))  # dictionnaire qui met
        # ensemble les listes all_characters_id and all_names_id
        list_all_credits_positions = []
        for ids in id_list:
            list_all_credits_positions.append(merged_list[ids])
        return list_all_credits_positions

    @staticmethod
    def create_character_dataset(provided_data):
        """Remplir les variables de la classe Character depuis read_data

            Args :
                provided_data : châine de caractères contenant des données
                tabulées où chaque ligne représente un personnage.

            Returns :
                La méthode sépare le string de provided_data en parties et extrait les
                attributs individuels (character_id, name_id, movie_id, gender_id,
                credits_position_id). Ensuite, la méthode essaie de convertir la partie
                credits_position en integer. Si cela est réussie, la méthode vérifie si
                credits_pos = 1000 (une valeur qui a peu de chances de se produire) alors
                credits_pos sera remplacé par ?. 'Except' garantie que même si la ligne
                ne peut pas être convertie ou s'il y a une erreur, 'credits_pos' aura
                tout de même une valeur.
                La méthode instancie de nouveaux objets de Character les ajoutent dans
                une liste nommée 'all_character_objects'. Par cela, la méthode met à jour
                les attributs en gardant des listes séparées pour chaque attribut.
        """
        for line in provided_data.splitlines():  # lignes sont divisées en parties
            line = str(line)
            parts = line.split('\t')

            # essaie de convertir en integer
            try:
                credits_pos = int(parts[5])  # 6ᵉ partie
                if credits_pos == 1000:  # valeur default (qui a peut de chances de se produire)
                    credits_pos = '?'
            except:
                credits_pos = '?'  # si exception (ex : ligne ne peut pas être convertie en int)

            entries = {
                'character_id': parts[0],
                'name_id': parts[1],
                'movie_id': parts[2],
                'gender_id': parts[4],
                'credits_position_id': credits_pos,
            }

            Character.all_character_objects.append(
                Character(**entries)
            )

            Character.all_characters_id.append(entries['character_id'])
            Character.all_names_id.append(entries['name_id'])
            Character.all_movies_id.append(entries['movie_id'])
            Character.all_genders_id.append(entries['gender_id'])
            Character.all_credits_positions_id.append(entries['credits_position_id'])
        return
