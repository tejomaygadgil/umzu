import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

$(document).click(function (event) {
  var element = $(event.target).parent().closest('.flowchart-label');
  if (element.length > 0) {
    var node = element[0].id.split('-')[1];
    document.getElementById("node").innerHTML = node;
  };
});

$("#state_select").change(function () {
  var selectedState = this.value;
  document.getElementById("state").innerHTML = selectedState;
});

// https://github.com/mermaid-js/mermaid/issues/2162 
mermaid.initialize({ startOnLoad: false });
const drawDiagram = async function () {
  const element = document.querySelector('#graph');
  // Read from file
  const response = await fetch('graph.txt')
  const graphText = await response.text();
  const graphDefinition = graphText;
  
  const nodeSet = new Set(graphText.split('\n').slice(2).flatMap(text => text.split(' --> ')));
  console.log(nodeSet);

  const { svg } = await mermaid.render('mySvgId', graphDefinition);
  element.innerHTML = svg;
};
await drawDiagram();

