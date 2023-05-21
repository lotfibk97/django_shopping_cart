$(document).ready(function () {
  var refreshTotal = function () {
    var totalPrice = 0;
    $(".order_item").each(function () {
      var linePrice = parseFloat($(this).find(".line_price").text());
      totalPrice += linePrice;
    });
    $("#total_price").text(totalPrice.toFixed(2));
  };
  refreshTotal();
  $(".form-control").on("input", function () {
    var quantity = $(this).val();
    var price = $(this).closest("tr").find(".price").text();
    var linePrice = quantity * price;
    $(this).closest("tr").find(".line_price").text(linePrice.toFixed(2));
    refreshTotal();
  });
});
