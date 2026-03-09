"""Tests for Pip and the Magic Code — Flask web application."""

import pytest
from app import app, BOOK_PAGES, TOTAL_PAGES


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_total_pages():
    assert TOTAL_PAGES == 8
    assert len(BOOK_PAGES) == 8


def test_cover_page(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.data.decode()
    assert "Pip and the Magic Code" in data
    assert "Start Reading" in data


def test_all_book_pages_return_200(client):
    for i in range(1, TOTAL_PAGES + 1):
        response = client.get(f"/page/{i}")
        assert response.status_code == 200, f"Page {i} returned {response.status_code}"


def test_book_page_content(client):
    response = client.get("/page/1")
    data = response.data.decode()
    assert "Chapter 1" in data
    assert "Meet Pip" in data
    assert "print" in data


def test_page_out_of_range_returns_404(client):
    assert client.get("/page/0").status_code == 404
    assert client.get("/page/999").status_code == 404
    assert client.get(f"/page/{TOTAL_PAGES + 1}").status_code == 404


def test_first_page_has_no_previous(client):
    response = client.get("/page/1")
    data = response.data.decode()
    assert "Back to Cover" in data


def test_last_page_has_finish_button(client):
    response = client.get(f"/page/{TOTAL_PAGES}")
    data = response.data.decode()
    assert "Finish" in data


def test_middle_page_has_prev_and_next(client):
    response = client.get("/page/4")
    data = response.data.decode()
    assert "Previous" in data
    assert "Next" in data


def test_each_page_has_code_example(client):
    for i, page_data in enumerate(BOOK_PAGES, start=1):
        assert page_data["code_example"], f"Page {i} has no code example"
        assert page_data["code_result"] is not None, f"Page {i} has no code result"


def test_page_data_required_fields():
    required = ["number", "title", "emoji", "color", "bg_color",
                "content", "story", "lesson_title", "lesson",
                "code_example", "code_result", "fun_fact"]
    for page_data in BOOK_PAGES:
        for field in required:
            assert field in page_data, f"Page {page_data.get('number')} missing field '{field}'"
