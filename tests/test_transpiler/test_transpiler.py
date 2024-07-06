from subprocess import run

def test_transpiler(capfd):
    run(["khomputer", "thai2khom", "-i", "input", "-o", "output"])
    captured = capfd.readouterr()
    assert captured.out.rstrip() == "Namespace(mode='thai2khom', input='input', output='output')"
