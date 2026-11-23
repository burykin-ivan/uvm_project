# Учебная виртуальная машина (УВМ)

Реализация ассемблера и интерпретатора согласно спецификации варианта №6.

## Язык ассемблера

* `CONST [addr], #value`
* `LOAD [dst], [[src]]`
* `STORE [src], [[dst]] + offset`
* `POW [dst], [base], [exp] + offset`

## Сборка и запуск

```bash
make setup
make test
