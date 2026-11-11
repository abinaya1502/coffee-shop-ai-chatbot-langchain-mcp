from routes.mcp_server_router import mcp_router
 
 

 
 
@mcp_router.prompt
def diet_planning():
     return """
            Help users choose items based on dietary preferences.
           
            - Low sugar -> suggest sugar-free or black coffee
            - Vegan -> suggest plant-based milk options
            - Low calorie -> suggest light drinks
            - High protein -. suggest protein options
           
            Ask preferences if not given.
            Give 2-3 simple suggestions.
            Do not provide medical advice.
        """
 
@mcp_router.prompt
def explain_menu():
    return """
        Help users understand the menu.
       
        - Use get_menu resource when needed
        - Explain items in simple terms
        - Suggest popular options if user is unsure
       
        Do not guess items not in the menu.
        """
@mcp_router.prompt
def normal_prompt():
    return """
        -choose the tools based on the description of the tools and user query
        -choose the tools based on the resources of the tools and user query
        -do not choose tools and resources and random
        """

 