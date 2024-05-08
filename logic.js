const CM_TO_PX = 37.795275591;
function drawVolume() {
  var selectedShape = document.getElementById("volume").value;
  var size = document.getElementById("size").value;
  var shapeOutput = document.getElementById("volumeOutput");

  if (size === undefined || size <= 0 || size > 10) {
    alert(
      "Please enter a value greater than 0 and less than or equal to 10 for size."
    );
    return;
  }

  if (selectedShape.toLowerCase() === "cube") {
    shapeOutput.style.borderRadius = "0";
  } else if (selectedShape.toLowerCase() === "cylinder") {
    shapeOutput.style.borderRadius = "50%";
  }

  shapeOutput.style.width = size * CM_TO_PX + "px";
  shapeOutput.style.height = size * CM_TO_PX + "px";
}

document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("volumeForm");
  var usernameInput = document.getElementById("size");

  usernameInput.addEventListener("keypress", function (event) {
    // Check if the Enter key was pressed
    if (event.key === "Enter") {
      // Prevent the default form submission behavior
      event.preventDefault();
    }
  });
});
