---
id: formats
language: ru
version: 1.0.1
title: Спецификации и открытые форматы
---


# Спецификации и открытые форматы

| Область | Нормативное описание |
| --- | --- |
| Погодные коллекции | [Обзор API](weather-api.md), [полный контракт 1.7](weather-client-contract.md) |
| Динамические обои | [Правила композиции и автомат 0.2](dynamic-wallpapers.md), [доставка и история](dynamic-api.md) |
| Числовые входы | [Все поля, единицы и диапазоны](numeric-fields.md) |
| Музыка | [JSON, идентичность и URL](music-api.md), [акустический подбор](music-similarity.md) |
| Пакеты оформления | [Контракт r11](theme-packages.md) |
| Клиенты | [Роли и подключение](clients.md) |
| Лаборатория | [Отдельная документация проекта](laboratory.md) |
| Документация | [Редакции и актуализация](documentation.md) |

## Схемы динамической темы 0.2

- [Коллекция](../schemas/dynamic/collection.schema.json).
- [Тема устройства](../schemas/dynamic/v0.2/theme.schema.json).
- [Входы](../schemas/dynamic/v0.2/inputs.schema.json).
- [Рецепт](../schemas/dynamic/v0.2/recipe.schema.json).
- [Текущий кадр](../schemas/dynamic/v0.2/state.schema.json).
- [Результат сборки](../schemas/dynamic/v0.2/build.schema.json).
- [Состояние бытового автомата](../schemas/dynamic/v0.2/life-state.schema.json).
- [Коды](../schemas/dynamic/v0.2/codes.json) и [числовые поля](../schemas/dynamic/v0.2/numeric-fields.json).

Схемы скопированы из действующего серверного контракта без изменения ограничений. Текст объясняет их смысл, но не отменяет обязательные поля. Примеры: [коллекция](../examples/collection.json), [тема](../examples/theme.json), [входы](../examples/inputs.json). Пример использует условные имена рисунков и не поставляется как готовая коллекция.

Полные исходные описания отдельных приложений и лаборатории находятся в их репозиториях. Общая документация связывает их, не меняя собственные версии этих проектов.

Порядок чтения: [Оглавление](../README.md) · Назад: [Композиция, глубина и свет чайной](composition.md) · Далее: [Форматы на границах системы](contracts.md)
