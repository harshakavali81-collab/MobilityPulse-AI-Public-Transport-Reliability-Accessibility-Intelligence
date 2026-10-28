import json
def test_static_snapshot_export(tmp_path):
    from scripts.export_static_api import build
    build(tmp_path)
    assert (tmp_path/"overview.json").is_file()
    overview=json.loads((tmp_path/"overview.json").read_text())
    assert overview["metadata"]["data_mode"]=="synthetic"
    assert overview["metadata"]["observations_are_real"] is False
    assert (tmp_path/"analytics"/"reliability.json").is_file()
    assert json.loads((tmp_path/"feed"/"status.json").read_text())["live_tracking"] is False
