def test_readme_import_line_works():
    """The README's quick-start imports these names from the package root."""
    from gateway import Gateway, Request

    assert Gateway.__name__ == "Gateway"
    assert Request(prompt="hi").prompt == "hi"
