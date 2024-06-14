#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gradio as gr
import stylecloud
from PIL import Image
import os


# In[3]:


def create_stylecloud(file, text_input, language, icon):
    # Dosya veya text inputtan gelen metni kullan
    if file:
        text = file.decode('utf-8')
    elif text_input:
        text = text_input
    else:
        return None  # Eğer ikisi de yoksa None döner
    
    output_file = 'stylecloud.png'
    stylecloud.gen_stylecloud(
        text=text,
        icon_name=icon,
        size=500,
        output_name=output_file
    )
    
    image = Image.open(output_file)
    image = image.resize((300, 300))
    return image

with gr.Blocks() as demo:
    gr.Markdown('Kelime Bulutu Oluşturucu')
    
    with gr.Row():
        input_choice = gr.Radio(choices=['Dosya Yükle', 'Metin Gir'], label='Girdi Seçimi', value='Dosya Yükle')
    
    with gr.Row(visible=True) as file_input_row:
        file_input = gr.File(label='Metin Dosyası Yükle', type='binary')
        
    with gr.Row(visible=False) as text_input_row:
        text_input = gr.Textbox(label='Metin Gir')

    with gr.Row():
        language = gr.Radio(choices=['TR', 'EN'], label='Dil Seçimi', value='TR')
    
    with gr.Row():
        icon = gr.Dropdown(choices=["fas fa-car", "fas fa-star-and-crescent", "fas fa-trophy", "fas fa-heart"],
                           label='İkon Seçimi', value='fas fa-star-and-crescent')
    
    with gr.Row():
        create_button = gr.Button('Oluştur')
        output_image = gr.Image(label='Kelime Bulutu')

        # butona basıldığında
        create_button.click(
            create_stylecloud,
            inputs=[file_input, text_input, language, icon],
            outputs=output_image
        )

    def update_input_visibility(choice):
        if choice == 'Dosya Yükle':
            return gr.update(visible=True), gr.update(visible=False)
        else:
            return gr.update(visible=False), gr.update(visible=True)
    
    input_choice.change(
        update_input_visibility,
        inputs=[input_choice],
        outputs=[file_input_row, text_input_row]
    )
    
demo.launch(share=True)


# In[ ]:




