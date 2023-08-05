import streamlit as st
from PIL import Image 


st.title("AESTHETIC SHOTS")

cc1, cc2 ,cc3 = st.columns(3)

def bttn():
	ans_1 = st.button("want to see more")
	if ans_1 == True:
		return True

with cc3:
	st.subheader("_Shots by Sai Likith_")

st.write("_Passionate about automobile photography_")

c1, c2 ,c3 = st.columns(3)

g11 = Image.open('python/Showcase/Aesthetic/325575177_1216507902615616_5191955527552643508_n_564611968922794.jpg')
g21 = Image.open('python/Showcase/Aesthetic/IMG_0003.jpg')
g31 = Image.open('python/Showcase/Aesthetic/SUN09745.jpg')
g41 = Image.open('python/Showcase/Aesthetic/IMG_1769.jpg')

g12 = Image.open('python/Showcase/Aesthetic/32323 (7 of 9).jpg')
g22 = Image.open('python/Showcase/Aesthetic/IMG_1728.jpg')
g32 = Image.open('python/Showcase/Aesthetic/IMG_6191-43.jpg')
g42 = Image.open('python/Showcase/Aesthetic/IMG_0478.JPG')
g52 = Image.open('python/Showcase/Aesthetic/IMG_1498.jpg')

g13 = Image.open('python/Showcase/Aesthetic/IMG_20230124_204445-2.jpg')
g23 = Image.open('python/Showcase/Aesthetic/32323 (25 of 30).jpg')
g33 = Image.open('python/Showcase/Aesthetic/IMG_1652.jpg')
g43 = Image.open('python/Showcase/Aesthetic/IMG_6153-29.jpg')


with c1:
	st.image(g11)
	st.image(g21)
	st.image(g31)



with c2:
	st.image(g12)
	st.image(g22)
	st.image(g32)
	st.image(g42)
		


with c3:
	st.image(g13)
	st.image(g23)
	st.image(g33)

	

if bttn() == True:
	with c1:
		st.image(g41)
	with c2:
		st.image(g52)
	with c3:
		st.image(g43)



contact_form = """
<form action="https://formsubmit.co/shravyarinky29@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your em@il" required>
     <textarea name="message" placeholder="your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form , unsafe_allow_html=True)

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

st_style = """
                <style>
                #MainMenu{visibility: hidden;}
                footer {visibility: hidden;}
				footer:after{
					content:'by saathvik';
					display:block;
					position:relative;
					color:tamoto;
					padding:5px;
					top:3px;}
                header {visibility: hidden}
                </style>
                """

st.markdown(st_style , unsafe_allow_html=True)
