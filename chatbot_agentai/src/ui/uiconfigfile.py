from configparser import ConfigParser


class Config:
    def __init__(self, config_file="uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE")
    
    def get_page_icon(self):
        return self.config.get("DEFAULT", "PAGE_ICON")
    
    def get_page_layout(self):
        return self.config.get("DEFAULT", "PAGE_LAYOUT")
    
    def get_page_initial_state(self):
        return self.config.get("DEFAULT", "PAGE_INITIAL_STATE")
    
    def get_llm_options(self):
        return self.config.get("DEFAULT", "LLM_OPTIONS").split(",")
    
    def get_llm_default(self):
        return self.config.get("DEFAULT", "LLM_DEFAULT")
    
    def get_usecase_options(self):
        return self.config.get("DEFAULT", "USECASE_OPTIONS").split(",")
    
    def get_usecase_default(self):
        return self.config.get("DEFAULT", "USECASE_DEFAULT")
    
    def get_groq_model_options(self):
        return self.config.get("DEFAULT", "GROQ_MODEL_OPTIONS").split(",")
    
    def get_groq_model_default(self):
        return self.config.get("DEFAULT", "GROQ_MODEL_DEFAULT")