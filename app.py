import streamlit as st
from PIL import Image 

#-----------------------menu style start----------------------------------------

st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """

st.markdown(st_style , unsafe_allow_html=True)

#----------------------menu style end-------------------------------------------


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


g11 = Image.open('325575177_1216507902615616_5191955527552643508_n_564611968922794.jpg')
g21 = Image.open('IMG_0003.jpg')
g31 = Image.open('SUN09745.jpg')
g41 = Image.open('IMG_1769.jpg')
g51 = Image.open('PicsArt_21-10-12_11-25-59-780.jpg')
g61 = Image.open('IMG_6146-26_1.jpg')

g12 = Image.open('32323 (7 of 9).jpg')
g22 = Image.open('IMG_1728.jpg')
g32 = Image.open('IMG_6191-43.jpg')
g42 = Image.open('IMG_0478.JPG')
g52 = Image.open('IMG_1498.jpg')
g62 = Image.open('IMG_9870.jpg')
g72 = Image.open('IMG_9916.jpg')
g82 = Image.open('IMG_1713.jpg')

g13 = Image.open('IMG_20230124_204445-2.jpg')
g23 = Image.open('32323 (25 of 30).jpg')
g33 = Image.open('IMG_1652.jpg')
g43 = Image.open('IMG_6153-29.jpg')
g53 = Image.open('32323 (10 of 30).jpg')
g63 = Image.open('IMG_1701.jpg')
g73 = Image.open('IMG_6182-41.jpg')


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
		st.image(g51)
		st.image(g61)

	with c2:
		st.image(g52)
		st.image(g62)
		st.image(g72)
		st.image(g82)

	with c3:
		st.image(g43)
		st.image(g53)
		st.image(g63)
		st.image(g73)

#-----------------------------------------contact form start-----------------------------------------------------

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

local_css("style.css.txt")

#-----------------------------------------contact form end-------------------------------------------------------------

