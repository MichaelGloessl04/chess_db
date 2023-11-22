from chess_move_importer import ChessMoveImporter
from chess_csv_exporter import ChessCSVExporter


def main():
    ccge = ChessMoveImporter('chessdb')
    cccsv = ChessCSVExporter(ccge.extract_game())
    cccsv.export_to_csv('export.csv')


if __name__ == "__main__":
    main()
