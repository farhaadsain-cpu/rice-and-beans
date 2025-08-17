from lib import loaders

def test_load_csv():
    df = loaders.load_csv("data_templates/projects.csv")
    assert not df.empty
