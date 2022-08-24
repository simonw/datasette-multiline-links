from datasette import hookimpl
from datasette.utils import is_url
from markupsafe import Markup, escape


@hookimpl
def render_cell(value):
    if not isinstance(value, str):
        return
    output = []
    for line in value.split("\n"):
        stripped = line.strip()
        if is_url(stripped):
            output.append('<a href="{url}">{url}</a>'.format(url=escape(stripped)))
        else:
            output.append(escape(line))
    return Markup("\n".join(output))
