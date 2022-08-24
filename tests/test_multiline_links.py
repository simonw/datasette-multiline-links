from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value,expected",
    (
        (
            "https://example.com",
            '<a href="https://example.com">https://example.com</a>',
        ),
        (
            "https://example.com\nNot a link\nhttps://google.com",
            (
                '<a href="https://example.com">https://example.com</a>\n'
                "Not a link\n"
                '<a href="https://google.com">https://google.com</a>'
            ),
        ),
        (
            "https://<script>alert('xss')</script>",
            '<a href="https://&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;">https://&lt;script&gt;alert(&#39;xss&#39;)&lt;/script&gt;</a>',
        ),
    ),
)
async def test_multiline_links(value, expected):
    datasette = Datasette(memory=True)
    response = await datasette.client.get(
        "/_memory", params={"sql": "select :value", "value": value}
    )
    assert response.status_code == 200
    assert expected in response.text
