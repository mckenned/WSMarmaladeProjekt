describe('Marmeladen End to End Tests', function() {

	it('Add all fruit ingredients and check presence in recipe', function() {
		for(var i=1;i<=26;i++){
    	cy.visit('/')
        cy.log('Click on the create your own recipe button')
    	cy.get('[data-cy=createYourRecipeButton').click()
    	cy.get('label>input[value='+i+']').then(($label)=>{
    		var ingredientName=$label.parent().text().toLowerCase()
    		$label.click()
            cy.log('Submit the fruitbasket containing '+ingredientName)
    		cy.contains('Submit').click()
            cy.log('Assert that recipe contains '+ingredientName)
    		cy.get('[data-cy=ingredientsFruit').contains(ingredientName)
    		cy.get('[data-cy=recipeText').contains(ingredientName)
    	})
	    }
  	})

    it('Add all spice ingredients and check presence in recipe', function() {
        for(var i=35;i<=50;i++){
        cy.visit('/')
        cy.log('Click on the create your own recipe button')
        cy.get('[data-cy=createYourRecipeButton').click()
        cy.get('label>input[value='+i+']').then(($label)=>{
            var ingredientName=$label.parent().text().toLowerCase()
            $label.click()
            cy.log('Submit the fruitbasket containing '+ingredientName)
            cy.contains('Submit').click()
            cy.log('Assert that recipe contains '+ingredientName)
            cy.get('[data-cy=ingredientsSpice').contains(ingredientName)
            cy.get('[data-cy=recipeText').contains(ingredientName)
        })
        }
    })

    it('Add 2 fruit and check presence of both in recipe', function(){
        cy.visit('/')
        cy.get('[data-cy=createYourRecipeButton').click()
        cy.get('label>input[value=5]').then(($label1)=>{
            var ingredientName1=$label1.parent().text().toLowerCase()
            $label1.click()
            cy.get('label>input[value=17]').then(($label2)=>{
                var ingredientName2=$label2.parent().text().toLowerCase()
                $label2.click()
                cy.log('Submit the fruitbasket containing '+ingredientName1+' and '+ingredientName2)
                cy.contains('Submit').click()
                cy.log('Assert that recipe contains '+ingredientName1 +' and '+ingredientName2)
                cy.get('[data-cy=ingredientsFruit').contains(ingredientName1)
                cy.get('[data-cy=recipeText').contains(ingredientName1)
                cy.get('[data-cy=ingredientsFruit').contains(ingredientName2)
                cy.get('[data-cy=recipeText').contains(ingredientName2)
                cy.get('[data-cy=recipeText').contains('For a great experience and rich taste we added some ingredients')
            })
        })
    })

    it('Add 3 fruit and check presence of all in recipe', function(){
        cy.visit('/')
        cy.get('[data-cy=createYourRecipeButton').click()
        cy.get('label>input[value=5]').then(($label1)=>{
            var ingredientName1=$label1.parent().text().toLowerCase()
            $label1.click()
            cy.get('label>input[value=17]').then(($label2)=>{
                var ingredientName2=$label2.parent().text().toLowerCase()
                $label2.click()
                cy.get('label>input[value=1]').then(($label3)=>{
                    var ingredientName3=$label3.parent().text().toLowerCase()
                    $label3.click()
                    cy.log('Submit the fruitbasket containing '+ingredientName1+', '+ingredientName2+' and '+ingredientName3)
                    cy.contains('Submit').click()
                    cy.log('Assert that recipe contains '+ingredientName1 +', '+ingredientName2+' and '+ingredientName3)
                    cy.get('[data-cy=ingredientsFruit').contains(ingredientName1)
                    cy.get('[data-cy=recipeText').contains(ingredientName1)
                    cy.get('[data-cy=ingredientsFruit').contains(ingredientName2)
                    cy.get('[data-cy=recipeText').contains(ingredientName2)
                    cy.get('[data-cy=ingredientsFruit').contains(ingredientName3)
                    cy.get('[data-cy=recipeText').contains(ingredientName3)
                    cy.get('[data-cy=recipeText').contains('For a great experience and rich taste we added some ingredients')
            })
            })
        })
    })

    it('Add 4 fruit and check presence of all except last in recipe', function(){
        cy.visit('/')
        cy.get('[data-cy=createYourRecipeButton').click()
        cy.get('label>input[value=5]').then(($label1)=>{
            var ingredientName1=$label1.parent().text().toLowerCase()
            $label1.click()
            cy.get('label>input[value=17]').then(($label2)=>{
                var ingredientName2=$label2.parent().text().toLowerCase()
                $label2.click()
                cy.get('label>input[value=1]').then(($label3)=>{
                    var ingredientName3=$label3.parent().text().toLowerCase()
                    $label3.click()
                    cy.get('label>input[value=14]').then(($label4)=>{
                        var ingredientName4=$label4.parent().text().toLowerCase()
                        $label4.click()
                        cy.log('Submit the fruitbasket containing '+ingredientName1+', '+ingredientName2+', '+ingredientName3+', and '+ingredientName4)
                        cy.contains('Submit').click()
                        cy.log('Assert that recipe contains '+ingredientName1 +', '+ingredientName2+', '+ingredientName3+', and '+ingredientName4)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName1)
                        cy.get('[data-cy=recipeText').contains(ingredientName1)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName2)
                        cy.get('[data-cy=recipeText').contains(ingredientName2)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName3)
                        cy.get('[data-cy=recipeText').contains(ingredientName3)
                        cy.get('[data-cy=ingredientsFruit').should('not.contain', ingredientName4)
                        cy.get('[data-cy=recipeText').should('not.contain',ingredientName4)
                     })
                })
            })
        })
    })

    it('Add 3 fruit and 1 spice and check presence of all in recipe', function(){
        cy.visit('/')
        cy.get('[data-cy=createYourRecipeButton').click()
        cy.get('label>input[value=5]').then(($label1)=>{
            var ingredientName1=$label1.parent().text().toLowerCase()
            $label1.click()
            cy.get('label>input[value=17]').then(($label2)=>{
                var ingredientName2=$label2.parent().text().toLowerCase()
                $label2.click()
                cy.get('label>input[value=1]').then(($label3)=>{
                    var ingredientName3=$label3.parent().text().toLowerCase()
                    $label3.click()
                    cy.get('label>input[value=50]').then(($label4)=>{
                        var ingredientName4=$label4.parent().text().toLowerCase()
                        $label4.click()
                        cy.log('Submit the fruitbasket containing '+ingredientName1+', '+ingredientName2+', '+ingredientName3+', and '+ingredientName4)
                        cy.contains('Submit').click()
                        cy.log('Assert that recipe contains '+ingredientName1 +', '+ingredientName2+', '+ingredientName3+', and '+ingredientName4)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName1)
                        cy.get('[data-cy=recipeText').contains(ingredientName1)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName2)
                        cy.get('[data-cy=recipeText').contains(ingredientName2)
                        cy.get('[data-cy=ingredientsFruit').contains(ingredientName3)
                        cy.get('[data-cy=recipeText').contains(ingredientName3)
                        cy.get('[data-cy=ingredientsSpice').contains(ingredientName4)
                        cy.get('[data-cy=recipeText').contains(ingredientName4)
                        cy.get('[data-cy=recipeText').contains('Great! Here is your special recipe.')
                     })
                })
            })
        })
    })
})
