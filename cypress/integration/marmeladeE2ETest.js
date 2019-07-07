describe('My First Test', function() {
	it('Visits the marmelade homepage', function() {
    	cy.visit('http://127.0.0.1:8000/marmeladenladen/')
    	cy.contains('Create your own recipe').click()
  	})
})