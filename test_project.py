#Your test functions must be in a file called test_project.py, which should also be in the “root” of your project.
# Be sure they have the same name as your custom functions, prepended with test_ (test_custom_function, for example,
import project
import pytest

   
def test_get_list():
    with pytest.raises(SystemExit):
        project.get_list("https://www.imdb.com/user/ur41041927/ratings?ref_=nv_usr_rt_4")
    with pytest.raises(SystemExit):
        project.get_list("https://www.imdb.com/user/ur41041927/watchlist?ref_=nv_usr_wl")
def test_store_source_data():
    with pytest.raises(SystemExit):
        project.store_source_data([])
def test_read_source_data():
    assert project.read_source_data()==""
def test_build_wordcloud():
    with pytest.raises(ValueError):
        project.build_wordcloud("")