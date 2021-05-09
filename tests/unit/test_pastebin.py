"""
This file contains the unit tests for the pastebin model
"""
from web.models.pastebin import Pastebin
from datetime import datetime

def test_new_pastebin():
    """
    GIVEN a Pastebin model
    WHEN a new Pastebin is created
    THEN check that title, content and paste_type are correct
    """

    pastebin = Pastebin("test content", "text", None, "test title", None, None)

    assert pastebin.content == "test user"
    assert pastebin.title == "test title"
    assert pastebin.paste_type == "text"
    assert pastebin.is_valid()

def test_new_pastebin_extended():
    """
    GIVEN a Pastebin model
    WHEN a new Pastebin is created
    THEN check that title, content, paste_type are correct
    """
    pastebin = Pastebin("test content", "text", 2, "test title", datetime.utcnow(), "password")

    assert pastebin.content == "test content"
    assert pastebin.title == "test title"
    assert pastebin.paste_type == "text"
    assert pastebin.user_id == 2
    assert not pastebin.password == "password"
    assert pastebin.check_password("password")
    assert pastebin.date == datetime.utcnow().replace(microsecond=0)
    assert not pastebin.is_expired()
    
def test_pastebin_setting_password(new_pastebin):
    """
    GIVEN an existing Pastebin
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_pastebin.set_password("password")
    assert new_pastebin.password != "password"
    assert new_pastebin.check_password("password")
    assert not new_pastebin.check_password("new password")
