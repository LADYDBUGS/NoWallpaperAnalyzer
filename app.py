import streamlit as st
import requests
import base64

# Remplace par ta clé API xAI (obtiens-la sur https://x.ai/api)
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.x.ai/v1/chat/completions"  # Vérifie dans les docs xAI

st.title("Analyse de Personnalité par Fond d'Écran Grok 🚀")
st.markdown("Upload ton capture d'écran de home screen, et Grok analysera ta personnalité de manière fun !")

uploaded_file = st.file_uploader("Choisis ta capture d'écran", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Ton écran uploadé", use_column_width=True)
    if st.button("Analyse Ma Personnalité !"):
        image_bytes = uploaded_file.getvalue()
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        prompt = f"""
        Analyse ce fond d'écran et interface de téléphone pour déduire la personnalité de l'utilisateur de manière fun et détaillée—comme un profil psychologique. 
        Inclu des sections sur le profil global, les détails clés (wallpaper, widgets, apps), forces/faiblesses, et un résumé. 
        Rends-le engageant et subjectif pour rigoler. Voici l'image en base64 : data:image/png;base64,{base64_image}
        """
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "grok-4", "messages": [{"role": "user", "content": prompt}], "max_tokens": 1000}
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                analysis = response.json()["choices"][0]["message"]["content"]
                st.markdown("### Analyse de Grok :")
                st.write(analysis)
            else:
                st.error(f"Erreur API : {response.text}")
        except Exception as e:
            st.error(f"Oups : {str(e)}")

st.markdown("Propulsé par Grok de xAI. Pour les détails API, visite [x.ai/api](https://x.ai/api).")
