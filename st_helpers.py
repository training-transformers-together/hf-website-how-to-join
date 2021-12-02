import streamlit as st
import streamlit.components.v1 as components

with open("static/header.html", 'r', encoding='utf-8') as f:
    header_html = f.read()
with open("static/header_style.css", 'r', encoding='utf-8') as f:
    header_style_css = f.read()
with open("static/header_animate.js") as f:
    header_animate_js = f.read()
with open("static/content_style.css", 'r', encoding='utf-8') as f:
    content_style_css = f.read()
with open("static/meta.html", 'r', encoding='utf-8') as f:
    meta_html = f.read()


def make_header():
    components.html(f"<style>{header_style_css}</style>{header_html}<script>{header_animate_js}</script>", height=260)
    st.markdown(meta_html, unsafe_allow_html=True)
    st.markdown(f"<style>{content_style_css}</style>", unsafe_allow_html=True)  # apply css to the rest of the document


def content_text(text: str, vspace_before: int = 0, vspace_after: int = 0):
    st.markdown(f'<center><div class="padded faded main_text" '
                f'style="padding-top: {vspace_before}px; padding-bottom: {vspace_after}px; text-align: justify;">'
                f'{text}</div><center>',
                unsafe_allow_html=True)


CITATIONS = {}


def cite(tag):
    CITATIONS[tag] = len(CITATIONS) + 1
    return f"&nbsp;[{CITATIONS[tag]}]"