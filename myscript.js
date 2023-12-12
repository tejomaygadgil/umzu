
$(document).click(function(event) {
    var element = $(event.target).parent().closest('.flowchart-label')
    if (element.length > 0) {
        node = element[0].id.split('-')[1]
        console.log(node)
        }
});

