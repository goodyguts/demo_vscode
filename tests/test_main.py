from demo_vscode.main import combine_names


def test_combine_names():
    assert combine_names("John", "Doe") == "JohnDoe"


def test_combine_other_names():
    assert combine_names("Foo", "Bar") == "FooBar"
