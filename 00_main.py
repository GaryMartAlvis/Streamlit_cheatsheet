import streamlit as st 
from streamlit_option_menu import option_menu 

import home, cheatsheet, code_ref, home_app, app1, app2

st.set_page_config(
    page_title = 'Cheatsheet-Streamlit',
    page_icon = '⭐'
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })

    def run(self):  # Add self parameter here
        with st.sidebar:
            app = option_menu(
                menu_title='Streamlit',
                options=['Home','Cheatsheet', 'Code reference', 'Aplicaciones'],
                icons=['house-fill','bookmark-check-fill', 'file-code-fill', 'inbox-fill'],
                menu_icon='book-fill',
                default_index=0
            )

        if app == 'Aplicaciones':
                other_app = st.selectbox("Menú de aplicaciones:", ["App 1", "App 2"])
                if other_app == "App 1":
                    app1.app()
                elif other_app == "App 2":
                    app2.app()
        else:
            for item in self.apps:
                if item['title'] == app:
                    item['function']()

if __name__ == '__main__':
    multi_app = MultiApp()
    multi_app.add_app("Home", home.app)
    multi_app.add_app("Cheatsheet", cheatsheet.app)
    multi_app.add_app("Code reference", code_ref.app)
    multi_app.run()
