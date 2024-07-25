
import streamlit as st
import google.generativeai as genai

def generate_ad_script(product):
    """Generates an advertising script based on the given product.

    Args:
        product: The product to advertise.

    Returns:
        The generated advertising script.
    """

    try:
        # Configure API key
        genai.configure(api_key="AIzaSyBZKWOxPAaF357psP9I2hYToZIW6kzqi_0")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are a marketing expert. Create engaging advertising scripts tailored to the given product.",
        )

        # Construct the prompt
        prompt = f"Create an engaging advertising script for the product: {product}. The script should be persuasive and include key features and benefits."

        # Generate the advertising script
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit application
st.set_page_config(page_title="Advertisement Script Generator", page_icon=":sparkles:")

st.title("Advertisement Script Generator :sparkles:")

st.write("""
    Welcome to the Advertisement Script Generator! This tool helps you create engaging and persuasive advertising scripts 
    for your products in just a few seconds. Simply enter the product name and let our AI do the magic!
""")

product = st.text_input("Enter the product name:", placeholder="e.g., SuperWidget 3000")

if st.button("Generate Advertisement Script"):
    if product:
        with st.spinner("Generating your advertisement script..."):
            script = generate_ad_script(product)
        st.subheader("Generated Advertisement Script:")
        st.write(script)
    else:
        st.error("Please enter a product name.")

st.markdown("""
    ---
    *Need help?* Contact our support team or visit our [documentation](https://www.example.com/docs).
""")