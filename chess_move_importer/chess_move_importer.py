import psycopg2 as psy
from configparser import ConfigParser


class ChessMoveImporter:
    """Import chess data from a postgesql db."""

    def __init__(self, section: str) -> None:
        """Initialize the ChessMoveImporter.

        Args:
            section (str): the section which should be used from the ini file.

        Raises:
            TypeError: raised if section is not a str.
        """
        if type(section) is not str:
            raise TypeError(
                f'section is {type(section)} but should be {str}'
            )
        self._section = section

    def config(self, filename='database.ini') -> dict:
        """Get the db config from a .ini file.

        Args:
            filename (str, optional): path to the .ini file.
                                      Defaults to 'database.ini'.

        Raises:
            Exception: raised if the member _section is not found
                       in the .ini file.

        Returns:
            dict: configuration for the db connection.
        """
        db = {}
        parser = ConfigParser()
        parser.read(filename)

        if parser.has_section(self._section):
            params = parser.items(self._section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception(
                f'Section {self._section} not found in the {filename} file')

        return db

    def extract_game(self) -> dict:
        """Extract game moves from a db.

        Returns:
            dict: a dict containing chess moves.
        """
        game = {
            'id': [],
            'move': [],
            'game_id': []
        }
        try:
            params = self.config()
            with psy.connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM chess_move')
                    db_version = cur.fetchall()
                    for entry in db_version:
                        game['id'].append(entry[0])
                        game['move'].append(entry[2])
                        game['game_id'].append(entry[3])
        except (Exception, psy.DatabaseError) as error:
            print(error)

        return game
