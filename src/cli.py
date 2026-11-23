import argparse
from pathlib import Path
from assembler.parser import AssemblerParser

def main() -> None:
    parser = argparse.ArgumentParser(description="УВМ: Ассемблер")
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    asm = AssemblerParser()
    # На данном этапе просто читаем файл, чтобы не было ошибок импорта
    _ = args.input.read_text(encoding='utf-8')
    instructions = asm.parse("")
    
    if args.test:
        print("IR: []")

if __name__ == '__main__':
    main()
