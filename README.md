# PI_URFU_2023 

## Команда 1.5
* Пахомов Д.Е.
* Болотов М.В.
* Шибакова А.А.
* Султанов Э.М.

## Программная инженерия. Итоговый проект (PJ)

[![Tests](https://github.com/sultanovemil/PI_URFU_2023/actions/workflows/python-app.yml/badge.svg)](https://github.com/sultanovemil/PI_URFU_2023/actions/workflows/python-app.yml)

Цель проекта: разработать Web приложение машинного обучения и развернуть его в облаке. 
В проекте используется предварительно обученная модель [`blanchefort/rubert-base-cased-sentiment`](https://huggingface.co/blanchefort/rubert-base-cased-sentiment).

### Итоговый проект (PJ) доступен по ссылке: 
https://huggingface.co/spaces/Emil25/pi_project
или https://piurfu2023project.streamlit.app/


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

**Описание:** Чат-бот моделирует разговор с пользователем. Либо бот может создавать темы для диалога, либо пользователь

### `s.sultanov.py`
**Задача:**  Анализ эмоциональной окраски текста на русском языке

**Описание:** Данный скрипт анализирует эмоциональную окраску текста с использованием модели "seara/rubert-tiny2-ru-go-emotions". Он запрашивает у пользователя текст для анализа и выводит результаты, показывая эмоцию, которая была обнаружена в тексте, а также уверенность модели в этой эмоции.



## Практическое задание №2 (pz2)
Создание Streamlit приложений на основе первого практического задания.

### `d.pakhomov_2.py`
Данное веб-приложение конвертирует текст с семантическими аннотациями в аудио человеческой речи с помощью модели [`suno/bark-small`](https://huggingface.co/suno/bark-small).

#### Используемые библиотеки
* [PyTorch](https://pytorch.org)
* [Transformers (HuggingFace)](https://huggingface.co)
* [Streamlit](https://streamlit.io)

#### Примеры
##### Скриншоты
![Приложение после запуска](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/632656d9-2093-44b4-93e6-8bfb23232041)
![Генерация аудио](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/4e558c07-db17-4d47-9dcf-3812be38d872)
![Готовое аудио](https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/146ae83f-9e78-4569-b25c-81a8a70a043a)
##### Аудио
https://github.com/sultanovemil/PI_URFU_2023/assets/32728173/d2b44601-238d-4c5b-a176-ba77dde3b440



### `a.shibakova_2.py`
Веб-приложение моделирует переписку и предлагает различные темы для общения. 

#### Используемые библиотеки
* [Streamlit](https://streamlit.io)
* [streamlit_chat](https://streamlit.io)
* [Transformers (HuggingFace)](https://huggingface.co)



### `e.sultanov_2.py`
Веб-приложение анализирует и распознает изображения с помощью модели [`apple/mobilevit-small`](https://huggingface.co/apple/mobilevit-small).
#### Используемые библиотеки
* [PyTorch](https://pytorch.org)
* [Transformers (HuggingFace)](https://huggingface.co)
* [Streamlit](https://streamlit.io)

#### Описание
Веб-приложение основано на модели "apple/mobilevit-small" и предоставляет возможность распознавания объектов на загруженных изображениях. Чтобы воспользоваться этой функцией, следуйте инструкциям ниже:
#### Шаг 1: Загрузите изображение
* На главной странице вебсайта вы увидите форму загрузки изображения.
* Нажмите на кнопку "Выбрать файл" или "Обзор", чтобы выбрать изображение с вашего компьютера.
* После выбора изображения, оно будет загружено на вебсайт.
#### Шаг 2: Распознавание объектов
* После загрузки изображения вы увидите кнопку "Распознать" или "Recognize".
* Нажмите на эту кнопку, чтобы запустить процесс распознавания объектов на изображении.
* Подождите несколько секунд, пока модель "apple/mobilevit-small" анализирует изображение.
#### Шаг 3: Просмотр результатов
* После завершения процесса распознавания, вы увидите результаты на боковой панели.
* Результаты могут включать список объектов, обнаруженных на изображении.
* Учтите, что точность распознавания может варьироваться в зависимости от сложности изображения и обученной модели.



## Практическое задание №3 (pz3)
Создание API для модели машинного обучения с помощью библиотеки FastAPI  на Python.


### `sultanov_3`
API для перевода текста с мультиязычного (mul) на английский язык (en) с помощью модели [`Helsinki-NLP/opus-mt-mul-en`](https://huggingface.co/Helsinki-NLP/opus-mt-mul-en). 


### `pakhomov_3`
API для определения эмоций в англоязычном тексте с помощью модели [`SamLowe/roberta-base-go_emotions`](https://huggingface.co/SamLowe/roberta-base-go_emotions).

#### Установка
1. Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/sultanovemil/PI_URFU_2023.git
```

2. Перейдите в директорию с приложением, создайте виртуальную среду и активируйте её:
```bash
cd pz3/pakhomov_3
python -m venv .venv
.venv/scripts/activate
```

3. Установите требования указанные в `pz3/pakhomov_3/requirements.txt`:
```bash
pip install -r requirements.txt
```

4. Запустите приложение с помощью команды:
```bash
uvicorn main:app --host localhost
```

5. Документация Swagger будет доступна по ссылке: http://localhost:8000/docs


### `shibakova`
API для чатбота с помощью модели [`facebook/blenderbot-400M-distill`](https://huggingface.co/facebook/blenderbot-400M-distill?text=Hey+my+name+is+Clara%21+How+are+you%3F). 



## Практическое задание №4 (pz4)
Развертывание Web или API приложения в облаке для доступа пользователей через интернет.


### `sultanov`
Веб-приложение, которое предсказывает тип цветка Ириса на основе его характеристик. Приложение использует библиотеку машинного обучения scikit-learn для обучения модели классификации и предсказания типа цветка.
Приложение доступно по ссылке: https://piurfu2023project4.streamlit.app 




## Практическое задание №5
Развертывание Web или API приложения в облаке для доступа пользователей через интернет.
Цель задания: научиться создавать тесты для  API модели машинного обучения и настраивать автоматический запуск тестов на GitHub. 


### `sultanov` https://github.com/sultanovemil/pz5
Тесты для API модели машинного обучения ['blanchefort/rubert-base-cased-sentiment'](https://huggingface.co/blanchefort/rubert-base-cased-sentiment), которое классифицирует эмоциональную окраску коротких текстов на русском языке.





