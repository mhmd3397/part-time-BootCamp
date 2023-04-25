function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
var crustTypes = ["Stuffed Crust", "Cracker Crust", "Flat Bread Crust", "Thin Crust", "Cheese Crust Pizza", "Thick Crust Pizza", "Wrapping It Up"];
var sauceTypes = ["Marinara Sauce", "Spicy Red Sauce", "BBQ Sauce", "Buffalo Sauce", "Alfredo Sauce", "Pesto Sauce", "Chocolate Sauce"];
var cheesess = ["Mozzarella", "Provolone", "Cheddar", "Parmesan", "Gouda", "Goat Cheese", "Gruyere", "Ricotta"];
var toppingss = ["PEPPERONI", "Extra Cheese", "Mushrooms", "Onions", "Sausage", "Black Olives", "Green Peppers", "Pineapple"];
function getRandomItem(arr) {

    // get random index value
    const randomIndex = Math.floor(Math.random() * arr.length);

    // get random item
    const item = arr[randomIndex];
    return item;
}

var s1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var s2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var s3 = pizzaOven(getRandomItem(crustTypes), getRandomItem(sauceTypes), [getRandomItem(cheesess), getRandomItem(cheesess)], [getRandomItem(toppingss), getRandomItem(toppingss)]);
var s4 = pizzaOven(getRandomItem(crustTypes), getRandomItem(sauceTypes), [getRandomItem(cheesess), getRandomItem(cheesess)], [getRandomItem(toppingss), getRandomItem(toppingss)]);
console.log(s1);
console.log(s2);
console.log(s3);
console.log(s4);
