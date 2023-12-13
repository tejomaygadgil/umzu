$(document).click(function (event) {
  var element = $(event.target).parent().closest('.flowchart-label')
  if (element.length > 0) {
    node = element[0].id.split('-')[1]
    document.getElementById("node").innerHTML = node
  }
});

function updateState() {
  document.getElementById("state").innerHTML = document.getElementById("state_select").value
}
