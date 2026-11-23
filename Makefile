.PHONY: setup test

setup:
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

test:
	@echo "Запуск тестов этапа 1"
	source .venv/bin/activate && python3 src/cli.py asm tests/test_stage1.asm out.ir --test
