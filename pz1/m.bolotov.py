
from transformers import pipeline

test4 = pipeline(model="deepset/roberta-base-squad2")
test4(question="Where do I live?", context='My name is Max and I live in Ekb')