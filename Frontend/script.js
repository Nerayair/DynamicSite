function storeInput() {
  console.log("Storing input in local storage...");
  const input = document.getElementById("promptInput").value;
  localStorage.setItem("promptInput", input);
  console.log("Input has been stored in local storage.");
  console.log("Redirecting to /output...");
}
