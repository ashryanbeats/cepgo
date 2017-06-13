/*
  CSInterface
*/
var csInterface = new CSInterface();

/*
  UI Elements
*/
var greetingButton = document.querySelector("#greeting-button");

/*
  Event listeners
*/
greetingButton.addEventListener("click", alertGreeting);

/*
  Helper methods
*/
function alertGreeting() {
  csInterface.evalScript("sayHello()");
}
