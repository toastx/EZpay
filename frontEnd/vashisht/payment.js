var userInput1;
console.log("User input: " + userInput1);
var userInput2;
console.log("User input: " + userInput2);
var userInput3;
console.log("User input: " + userInput3);















// var outside = document.getElementById("body-container");
// var toPrice = document.getElementById("to-currency-price");
// var fromBasis = document.getElementById("from-basis");
// var toMenu = document.getElementById("to-menu");
// var fromMenu = document.getElementById("from-menu");
// var toSelect = document.getElementsByClassName("to-currency");
// var fromSelect = document.getElementsByClassName("from-currency");

// var toCurrency = "USD";
// var fromCurrency = "BTC";

// var retrievePrice = function() {
//     var XHR = new XMLHttpRequest();
    
//     XHR.onreadystatechange = function(){
//       if(XHR.readyState == 4 && XHR.status == 200) {
//         var val = JSON.parse(XHR.responseText)[fromCurrency][toCurrency];
//         var price = val.toLocaleString('en');
//         toPrice.textContent = price + " " + toCurrency;
//         fromBasis.textContent = fromCurrency;
//       }
//     }
    
//     XHR.open("GET","https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + fromCurrency + "&tsyms=" + toCurrency);
//     XHR.send();
// }

// for(var i = 0; i < toSelect.length; i++) {
//     toSelect[i].addEventListener("click", function() {
//         toMenu.classList.remove("expand");
//         toCurrency = this.textContent;
//         retrievePrice();
//     });
// }

// for(var i = 0; i < fromSelect.length; i++) {
//     fromSelect[i].addEventListener("click", function() {
//         fromMenu.classList.remove("expand");
//         fromCurrency = this.textContent;
//         retrievePrice();
//     });
// }

// toPrice.addEventListener("click", function() {
//     if(toMenu.classList.contains("expand")) {
//         toMenu.classList.remove("expand");
//     } else {
//         toMenu.classList.add("expand");
//     }
// });

// fromBasis.addEventListener("click", function() {
//     if(fromMenu.classList.contains("expand")) {
//         fromMenu.classList.remove("expand");
//     } else {
//         fromMenu.classList.add("expand");
//     }
// });

// //Execute
// setInterval(function() {
//     retrievePrice();
// }, 10000);

// retrievePrice();