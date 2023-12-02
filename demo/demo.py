import torch
import streamlit as st
import googleapiclient.discovery
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Анализатор комментариев :red[YouTube] :sunglasses:')


# Инициализируем модель Hugging Face для анализа тональности текста
cls_sent = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

st.markdown('***')

# Получаем YouTube API KEY видеоролика для отправки запроса
API_key = st.sidebar.text_input('YouTube API KEY')

# Получаем id видеоролика для отправки запроса
vidID = st.sidebar.text_input('Video Id')
st.sidebar.write('Вы ввели... ', vidID )

<<<<<<< HEAD
btn_start = st.sidebar.button('Загрузить')
if btn_start:
    # Запрос к YouTube API для получения комментариев к видео
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = API_key
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=vidID,
        maxResults=100
    )
    response = request.execute()
    comments = []
=======
# Запрос к YouTube API для получения комментариев к видео
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = ""
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)
request = youtube.commentThreads().list(
    part="snippet",
    videoId="KJA9A1q9l7E",
    maxResults=100
)
response = request.execute()
comments = []
>>>>>>> d9679a209182f11cf4882c86239465f49ecec016

    # Преобразуем полученные комментарии в DataFrame
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['updatedAt'],
            comment['likeCount'],
            comment['textDisplay']
        ])
    comments_df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])

    # Выводим таблицу с комментариями на странице
    st.markdown('## Комментарии из YouTube')
    st.write(comments_df)
    st.markdown('***')

    # Проходим по каждому комментарию в датафрейме
    # Анализируем тональность комментария с помощью модели Hugging Face
    # Добавляем результат в список
    res_list = []
    with st.spinner('Идет процесс обработки данных ...'):
        for comment in comments_df['text']:
            result = cls_sent(comment)
            res_list.append(result[0])
    st.success('Готово!')

    # Выводим таблицу с результатами на странице
    res_df = pd.DataFrame(res_list)
    st.write(res_df)
    st.markdown('***')

    # Создаем круговую диаграмму
    data = res_df['label'].value_counts()
    fig, ax = plt.subplots()
    plt.title("Эмоциональная окраска комментариев на YouTube")
    label = res_df['label'].unique()
    ax.pie(data, labels=label, autopct='%1.1f%%')
    st.pyplot(fig)



    
