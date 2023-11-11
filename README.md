# PI_URFU_2023

## Команда
* Пахомов Д.Е.
* Болотов М.В.
* Шибакова А.А.
* Султанов Э.М.

## Практическое задание №1 (pz1)
Создание базовых приложений, использующие готовые библиотеки машинного обучения.

### `d.pakhomov.py`
**Задача:** Генерировать голос из текста с метатагами для таких звуков как смех, плач и т.д.

**Описание:** Text-to-Speech с помощью модели `suno/bark-small`. Переменная `text_prompt` принимает текст, аудиозаписи сохраняются в папке `bark-outputs`.

### `m.bolotov.py`
**Задача:** Получить ответ на вопрос, заданный пользователем.

**Описание:** Пользователь описывает ситуацию модели `deepset/roberta-base-squad2` в вопросе/подсказке и просит модель сгенерировать ответ с учетом предоставленной информации. 
В этом сценарии модель выбирает соответствующие части информации из подсказки и возвращает результаты.

### `a.shibakova.py`
**Задача:** Создание чат-бота, который предлагает различные темы для последующего диалога.

**Описание:** чат-бот моделирует разговор с пользователем. Либо чат-бот может создавать темы для диалога, либо пользователь. 

### `s.sultanov.py`
**Задача:**  Анализ эмоциональной окраски текста на русском языке

**Описание:** Данный скрипт анализирует эмоциональную окраску текста с использованием модели "seara/rubert-tiny2-ru-go-emotions". Он запрашивает у пользователя текст для анализа и выводит результаты, показывая эмоцию, которая была обнаружена в тексте, а также уверенность модели в этой эмоции.



## Практическое задание №2 (pz2)
Создание Streamlit приложений на основе первого практического задания.

### `d.pakhomov.py`
Данное веб-приложение конвертирует текст с семантическими аннотациями в аудио человеческой речи с помощью модели [`suno/bark-small`](https://huggingface.co/suno/bark-small).

#### Используемые библиотеки
* [PyTorch](https://pytorch.org)
* [Transformers (HuggingFace)](https://huggingface.co)
* [Streamlit](https://streamlit.io)

#### Примеры
![Приложение после запуска](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/632656d9-2093-44b4-93e6-8bfb23232041)
![Генерация аудио](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/4e558c07-db17-4d47-9dcf-3812be38d872)
![Готовое аудио](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/146ae83f-9e78-4569-b25c-81a8a70a043a)




### `a.shibakova_2.py`
Веб-приложение моделирует переписку и предлагает различные темы для общения. 


#### Используемые библиотеки
streamlit
streamlit_chat
from transformers
