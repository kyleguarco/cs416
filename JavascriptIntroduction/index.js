alert("Hello, world!");

var p = document.getElementsByTagName("h1");

for (var x = 0; x < p.length; x++) {
    p.item(x).textContent = x;
}
