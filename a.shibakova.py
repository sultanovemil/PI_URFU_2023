#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch


# In[2]:


from transformers import pipeline, Conversation


# In[4]:


chatbot = pipeline(model="facebook/blenderbot-400M-distill")


# In[ ]:


while True:
    user = input("User: ")

    if user.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    conversation = Conversation()
    conversation.add_user_input(user)
    conversation = chatbot(conversation)

    # Получение ответа от Chatbot
    chatbot_response = conversation.generated_responses[-1]
    print("Chatbot:", chatbot_response)


# In[ ]:




