from wand.image import Image
from wand.display import display
from wand.color import Color
from wand.drawing import Drawing

image_background = "./scorebola.jpg"
filename_output = "./TEST2.png"
# filename_logo = "./liverpool.png"
# filename_logo1 = "./totenham2.png"

font_text = "./oswald.ttf"


with Image(filename=image_background) as img_background:
    with Drawing() as context:
        context.font = font_text
        context.fill_color = Color('#FF9999')
        context.font_size = 150
        #metrics = context.get_font_metrics(img_background, body_text, multiline=True)
        body_text = "DAWONG"
        context.text(
            x=150,
            y=400,
            body=body_text)
        context(img_background)
        metrics = context.get_font_metrics(img_background,body_text,multiline=True)
        print(metrics)
    
    # with Drawing() as context:
    #     context.font = font_text
    #     context.fill_color = Color('#00FF80')
    #     context.font_size = 300
    #     #metrics = context.get_font_metrics(img_background, body_text, multiline=True)
    #     context.text(
    #         x=750,
    #         y=1450,
    #         body="2")
    #     context(img_background)
    # with Image(filename=filename_logo) as logo_liverpool:
    #     img_background.composite(logo_liverpool, left=180, top=1200)
    # with Image(filename=filename_logo1) as logo_totenham:
    #     logo_totenham.resize(400,400)
    #     img_background.composite(logo_totenham, left=110, top=600)
    display(img_background)
    img_background.format = "png"
    img_background.save(filename=filename_output)