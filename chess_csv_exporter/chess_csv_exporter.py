import pandas as pd
import os


class ChessCSVExporter:
    """Take chess moves and export them to a csv file."""

    def __init__(self, game_data: dict) -> None:
        """Initialize the ChessCSVExporter.

        Args:
            game_data (dict): a dict filled with chess moves.
        """
        if not isinstance(game_data, dict):
            raise TypeError(
                f'section is {type(game_data)} but should be {dict}'
            )
        self._game_data = game_data

    def export_to_csv(self, export_path='export.csv', overwrite=True):
        """Export extracted gamedata to a csv file.

        Args:
            export_path (str, optional): the location of the exported file.
                                         Defaults to 'export.csv'.
            overwrite (bool, optional): if the file should be overwritten if
                                        it already exists.
                                        Defaults to True.
        """
        if not isinstance(export_path, str):
            raise TypeError(
                f'section is {type(export_path)} but should be {str}'
            )

        if not overwrite:
            export_path = self._increment_export_path(export_path)

        df = pd.DataFrame(self._game_data)
        df.to_csv(export_path, index=False)

    def _increment_export_path(self, export_path: str) -> str:
        if not os.path.exists(export_path):
            return export_path
        i = 0
        stripped = export_path[:-4]
        ongoing = stripped

        while os.path.exists(ongoing + '.csv'):
            i += 1
            ongoing = stripped + f"({i})"
        return ongoing + '.csv'
