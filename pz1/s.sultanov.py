#Эта модель оптимизирована для классификации эмоций коротких русских текстов.

from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-ru-go-emotions")

res = model(input('Введите cвой текст: '))
print(res)

