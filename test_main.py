from main import add


def test_add():
    """Test add function in main.py"""
    assert add(2, 2) == 4
    # assert add(2, 3) == 4


if __name__ == "__main__":
    test_add()
