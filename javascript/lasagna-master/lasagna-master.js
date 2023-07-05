/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(time) {
   return time == null ? 'You forgot to set the timer.' : time == 0 ? 'Lasagna is done.' : 'Not done, please wait.'
}

export function preparationTime(layers, time=2) {
   return layers.length * time
}

export function quantities(layers) {
   let noodleCount = 0 
   let sauceCount = 0;
   layers.forEach(element => {
      if (element == 'noodles') {
         noodleCount+=50
      }
      else if (element == 'sauce') {
         sauceCount+=0.2
      }
   });

   return {
      noodles: noodleCount, 
      sauce: sauceCount
   }
}

   export function addSecretIngredient(friendsList, myList) {
      myList[myList.length] = friendsList[friendsList.length-1];
   }

   export function scaleRecipe(recipe, portions=2) {
      portions /= 2
      const scaledRecipe = {}
      for (let ingredient in recipe) {
         scaledRecipe[ingredient] = recipe[ingredient]*portions
      }

      return scaledRecipe
   }
