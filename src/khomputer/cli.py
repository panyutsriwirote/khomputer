from argparse import ArgumentParser
from .interpreter import interpret
from .transpiler import transpile

__VERSION__ = "0.0.1a"

def main():
    # Common argument parser
    parser = ArgumentParser(description="The Khomputer programming language")
    parser.add_argument("-v", "--version", action="version", version=f"Khomputer {__VERSION__}")
    sub_parsers = parser.add_subparsers(dest="mode", required=True)
    # Transpiler arguments (khomputer thai2khom ...)
    transpiler_parser = sub_parsers.add_parser("thai2khom")
    transpiler_parser.add_argument("-i", "--input", required=True)
    transpiler_parser.add_argument("-o", "--output", required=True)
    # Interpreter arguments (khomputer run ...)
    interpreter_parser = sub_parsers.add_parser("run")
    interpreter_parser.add_argument("program")
    # Main program
    args = parser.parse_args()
    print(args)
    if args.mode == "thai2khom":
        transpile(input_dir=args.input, output_dir=args.output)
    else:
        interpret(prog_dir=args.program)
