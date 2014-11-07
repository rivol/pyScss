"""Test the command-line tool from the outside."""
from subprocess import PIPE, Popen

# TODO: this needs way, way, way, way more tests


def test_stdio():
    proc = Popen(['python', '-m', 'scss.tool', '-C'], stdin=PIPE, stdout=PIPE)
    out, _ = proc.communicate(b"""
        $color: red;

        table {
            td {
                color: $color;
            }
        }
    """)

    assert out == b"""\
table td {
  color: red;
}
"""
