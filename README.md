# Basement Crowd - Coffee Shop ☕ #

At Basement Crowd we have a microservice architecture and have many RESTful HTTP Webservices.

For the coding challenge, we would like you to build a RESTful API as per the details below. Our stack is Scala and Akka-Http, so would be great if you can use these, but you are welcome to complete the challenge in Java and any web framework of your choice (or no framework at all).

You should think about how the solution might be deployed (to an app server or embedded server), and should approach it as though you are building a real service, keeping in mind best practices, design patterns, concurrency and RESTful API principles.

## Task: The Shop ##
We’re looking for a RESTful JSON API for a coffee shop that can handle the below functions:

1. Get a list of available coffees (name, price).
2. Add / update / delete a coffee from the menu.
3. Purchase one or more coffees using a credit card (card number, expiry date) (expired credit cards should be declined). Reply with a receipt containing the cost or appropriate error response.
4. Get a summary of sales made. Quantity of each coffee purchased and the total money made per coffee (coffee, quantity, revenue).


## Notes ##
* We do not expect any data to be persisted, for the sake of this challenge all data can simply be managed in memory of the application. Please provide a README with details of decisions or assumptions made during the test.
* We are not expecting to have the perfect solution. But you should also be prepared to discuss the limitations and shortcuts.
* We understand that as an engineer you will be getting inspiration from multiple sources. We’re fine with that, but we wouldn’t like to get something largely copied from an existing project. We want to have a project from you.
* We understand some people may want to publish the solution as a showcase, but we ask you to refrain from including this description in the solution and from sharing this assignment with other people.