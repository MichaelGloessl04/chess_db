def test_init():
    from chess_csv_exporter import ChessCSVExporter
    wrong_moves = [True, '', "", 2, 3.0, []]
    try:
        for move in wrong_moves:
            cce = ChessCSVExporter(move)
            assert False
    except TypeError as e:
        assert str(e) == f'section is {type(move)} but should be {dict}'  # noqa: E501

    cce = ChessCSVExporter({})  # noqa: F841


def test_export_to_csv():
    from chess_csv_exporter import ChessCSVExporter
    import pandas as pd
    import os

    content = {'1': {0: 1}, '2': {0: 1}, '3': {0: 'test'}, '4': {0: True}}
    cce = ChessCSVExporter(content)

    wrong_paths = [None, 1234, 4.0, True, [], {}]
    for path in wrong_paths:
        try:
            cce.export_to_csv(export_path=path)
            assert False
        except TypeError as e:
            assert str(e) == f'section is {type(path)} but should be {str}'  # noqa: E501

    path = 'tests/test_export.csv'
    cce.export_to_csv(export_path=path)
    df = pd.read_csv(path)
    assert df.to_dict() == content
    os.remove(path)


def test_export_to_csv_increment():
    from chess_csv_exporter import ChessCSVExporter
    import os

    cce = ChessCSVExporter({})
    test_path = 'tests/test_export'

    for i in range(10):
        cce.export_to_csv(export_path=test_path + '.csv', overwrite=False)
        if i == 0:
            assert os.path.exists(test_path + '.csv')
        else:
            assert os.path.exists(test_path + f"({i}).csv")

    for i in range(0, 10):
        if i == 0:
            os.remove(test_path + '.csv')
        else:
            os.remove(f"tests/test_export({i}).csv")
