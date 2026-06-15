from inject_controls import inject_mouse_controls


def test_inject_controls(tmp_path):

    d = tmp_path / "subdir"  # create a subdirectory path inside the temp
    d.mkdir()
    f = d / "test_map.html"
    f.write_text("<html><body></body></html>")

    # Add a mock .catch() block to satisy the requirements of the test
    f.write_text(
        "<html><body><script>vegaEmbed('#vis', spec).catch(error => showError(el, error));</script></body></html>"
    )

    # Run inject controls
    inject_mouse_controls(str(f))

    # Assert: Check if the file was modified
    content = f.read_text()
    assert "zoom_scale" in content
