def test_init():
    from chess_move_importer import ChessMoveImporter
    try:
        cmi = ChessMoveImporter()
        assert False
    except TypeError as e:
        assert str(e) == "ChessMoveImporter.__init__() missing 1 required positional argument: 'section'"  # noqa: E501

    wrong_sections = [None, 1234, 4.0, True, [], {}]
    for section in wrong_sections:
        try:
            cmi = ChessMoveImporter(section)
            assert False
        except TypeError as e:
            assert str(e) == f'section is {type(section)} but should be {str}'  # noqa: E501

    cmi = ChessMoveImporter('chess')  # noqa: F841


def test_extract_game():
    from chess_move_importer import ChessMoveImporter
    cmi = ChessMoveImporter('testchessdb')
    game = cmi.extract_game()
    assert game == {
        'id': [0, 1, 2, 3, 4],
        'move': ['e4', 'e5', 'Nf3', 'Nc6', 'Bb5'],
        'game_id': [1, 1, 1, 1, 1]
    }


def test_config():
    from chess_move_importer import ChessMoveImporter
    wrong_section = 'wrong_section'
    filename = 'database.ini'

    cmi = ChessMoveImporter(wrong_section)
    try:
        cmi.config(filename=filename)
    except Exception as e:
        str(e) == f'Section {wrong_section} not found in the {filename} file'
