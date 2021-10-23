var taskList = document.getElementById("tasklist");
var reorderForm = document.getElementById("reorderForm");
var positionInput = document.getElementById("positionInput");

let sortable = Sortable.create(taskList, {
  handle: ".handle",
  ghostClass: "dropArea",
  chosenClass: "selectedTask",
});

function reordering() {
  const rows = document.getElementsByClassName("task-wrapper");
  let pos = [];
  for (let row of rows) {
    pos.push(row.dataset.position);
  }
  console.log(pos.join(","));
  positionInput.value = pos.join(",");
  reorderForm.submit();
}

document.ondrop = reordering;
