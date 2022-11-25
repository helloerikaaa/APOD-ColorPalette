import streamlit as st

from consts.paths import APODPaths
from image.image_handler import ImageHandler
from color.color_extractor import ColorExtractor
from api.api_handler import download_apod_image

st.set_page_config(layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: white;'>NASA's APOD Color Palette Generator</h1>",
    unsafe_allow_html=True,
)


def spaces(url, bg_color):
    st.markdown(
        f'<p style="background-color:{bg_color};color:#fff;font-size:24px;border-radius:2%;">{url}</p>',
        unsafe_allow_html=True,
    )


st.markdown(
    """
        <style>
            .css-18e3th9 {
                padding-top: 1rem;
                padding-bottom: 10rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
            .css-1d391kg {
                padding-top: 3.5rem;
                padding-right: 1rem;
                padding-bottom: 3.5rem;
                padding-left: 1rem;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

img = download_apod_image()
image = ImageHandler().resize_img(img)
color_extractor = ColorExtractor(image)
colors = color_extractor.get_color_list()

with st.container():
    h1, h2, h3 = st.columns(3)
    with h1:
        st.write(" ")
    with h2:
        st.image(image, caption="Credits: NASA", width=500)
    with h3:
        st.write(" ")

with st.container():
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        spaces(f"{colors[0]}", colors[0])
    with a2:
        spaces(f"{colors[1]}", colors[1])
    with a3:
        spaces(f"{colors[2]}", colors[2])
    with a4:
        spaces(f"{colors[3]}", colors[3])
with st.container():
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        spaces(f"{colors[4]}", colors[4])
    with b2:
        spaces(f"{colors[5]}", colors[5])
    with b3:
        spaces(f"{colors[6]}", colors[6])
    with b4:
        spaces(f"{colors[7]}", colors[7])
with st.container():
    c1, c2, c3 = st.columns(3)
    with b1:
        spaces(f"{colors[8]}", colors[8])
    with b2:
        spaces(f"{colors[9]}", colors[9])
    with b3:
        spaces(f"{colors[10]}", colors[10])
