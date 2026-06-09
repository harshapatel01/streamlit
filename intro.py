import streamlit as st
from PIL import Image
import pandas as pd
import random
import altair as alt

st.title("📊📊hiiii.. This is Harsha") 

st.header("I am the main heading")

st.subheader("I am ur sub Heading")

st.text("hi i am learning the streamlit from today can i learn streamlit in 30 days completely and profisionaly ")

st.markdown("> Hello world")

st.markdown(" ---")

st.markdown("1.Harsha 2.Nani 3.Vardhan")

st.markdown("[Google](https://google.com)")

st.markdown("""
1. First item
2. Second item
3. Third item
""")

st.markdown("""
<ul style = "list-style-type:;">
    <li>Harsha</li>
    <li>Nani</li>
    <li>Vardhan</li>
</ul>            
""",unsafe_allow_html=True)

st.markdown("you can run the below code in this website [coderunner](https://www.programiz.com/java-programming/online-compiler/)")


st.markdown("""
📊Java code
``` 
       
class Harsha{
    public static void main(String args[]){
        System.out.println("Harsha");
    }
}     
```
            
""")

st.caption("this is my first website") 

#latex
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}1\\2 \end{pmatrix}")

st.latex(r"\pi^2")


uploaded_file = st.file_uploader("upload the image",type=["jpg","png","jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption="uploaded image",use_container_width=True)
    

st.markdown("---")
data = {"Name":["Harsha","nani"],"Branch":["Aiml","cse"],"ph.no":[9502781403,9573973403]}
st.json(data)
st.dataframe(data=data)

code = """
class Harsha{
    public static void main(String args[]){
        System.out.printl("Harsha");
    }
}
"""

st.code(code,language="java")

st.markdown("---")

def csvfun():
    type = ["csv"]
    uploaded_file1 = st.file_uploader("upload the file to make DataFrame",type)
    if uploaded_file1 is not None:
        data1 = pd.read_csv(uploaded_file1)
        st.dataframe(data1) 
csvfun()

st.markdown("---")

value = random.randint(20000,30000)
delta = random.randint(-50,50)

st.metric("live share prize",value,delta)

st.markdown("---")



data = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "sales": [10, 20, 15, 25, 30],
    "profits":[10,20,11,12,11]
})

chart = alt.Chart(data,title="📊Graph of the sales").mark_bar(color="red",size=30).encode(
    x="day",
    y="profits",
    
)

st.write(chart)
st.table(data=data)

def add(a, b):
    """This function adds two numbers"""
    return a + b

st.help(add)



