function loaded() {
  var elem = document.querySelector("body");
  var style = window.getComputedStyle(elem, "");
  var width_page = style.width;
  var x = parseInt(width_page);
  console.log(x);

  function test(x) {
    var y = 3000/x;
    return 100 - y;
  }
  var z = test(x);
  function csschange(z) {
    document.querySelectorAll("li", "").style.padding = "z%"";
  }
}
