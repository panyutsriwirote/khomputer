from subprocess import run

def test_interpreter(capfd):
    run(["khomputer", "run", "program"])
    captured = capfd.readouterr()
    assert captured.out.rstrip() == "Namespace(mode='run', program='program')"
