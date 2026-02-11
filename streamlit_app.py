import streamlit as st
import time 

# --- IMAGE LINKS ---
IMAGE_OPEN = "https://i.postimg.cc/B6WZ1krv/Cartoon-courtroom-judge-with-gavel.png"
IMAGE_THINKING = "https://i.postimg.cc/6p9MBQTw/Chat-GPT-Image-Jan-12-2026-11-32-25-AM.png"
IMAGE_GAVEL = "https://i.postimg.cc/wMq17nNh/Chat-GPT-Image-Jan-12-2026-11-36-42-AM.png"

st.title("⚖️ ROBOT Judge")

# We create a placeholder at the top so the image stays in one spot
image_placeholder = st.empty()

# 1. Setup Logic for Image Cycling
image_to_show = IMAGE_OPEN 

# 2. Input UI
st.subheader("1. Set your Rule")
col1, col2 = st.columns(2)
condition = col1.text_input("If it is...", placeholder="ex: raining").lower().strip()
result = col2.text_input("Then it must be...", placeholder="ex: cloudy").lower().strip()

# Logic to switch to "Thinking"
if condition and result:
    image_to_show = IMAGE_THINKING

# 3. Statement UI
if condition and result:
    st.divider()
    st.subheader("2. Enter your Statement")
    
    col3, col4 = st.columns(2)
    # Using horizontal=True makes it look a bit cleaner for Yes/No
    s_cond = col3.radio(f"Is it {condition}?", ["No", "Yes"], horizontal=True)
    s_res = col4.radio(f"Is it {result}?", ["No", "Yes"], horizontal=True)

    if st.button("Judge Me!"):
        # Update image to Gavel
        image_to_show = IMAGE_GAVEL
        
        # We display the image inside the button logic to ensure it updates immediately
        image_placeholder.image(image_to_show, width=250)
        
        # Logic check
        if s_cond == "Yes" and s_res == "No":
            st.error("### Result: INVALID!")
            st.write(f"Reason: You said if it's **{condition}**, it MUST be **{result}**!")
        else:
            st.success("### Result: VALID")
            st.write("Reason: No logical contradiction found.")
            st.balloons()
    else:
        # If button not clicked, show the Thinking/Open image
        image_placeholder.image(image_to_show, width=250)
else:
    # If inputs are empty, show the Open Mouth image
    image_placeholder.image(image_to_show, width=250)
