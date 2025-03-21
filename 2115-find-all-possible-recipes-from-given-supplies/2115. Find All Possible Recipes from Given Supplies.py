class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        makeable = set() # Anything in here is able to be made

        for supply in supplies:
            makeable.add(supply)
        
        recipe_to_ingredients = {} # Given a recipe, give me all required ingredients
        for i in range(len(recipes)):
            recipe_to_ingredients[recipes[i]] = ingredients[i]

        # @cache
        def dfs(recipe, visited): # Returns True if its able to be made
            if recipe in makeable:
                return True
            if recipe not in recipe_to_ingredients or recipe in visited:
                return False
            visited.add(recipe)
            
            res = True
            for required_ingredient in recipe_to_ingredients[recipe]:
                res = res and dfs(required_ingredient, visited)
            if res: 
                makeable.add(recipe)

            return res
        for i in range(len(recipes)):
            if dfs(recipes[i], set()):
                makeable.add(recipes[i])

        res = []
        for recipe in recipes:
            if recipe in makeable:
                res.append(recipe)
        return res