async function storeInput() {
  console.log("Storing input in local storage...");
  const input = document.getElementById("promptInput").value;

  try {
    const response = await fetch("http://127.0.0.1:8000/get_gemini_response", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: input }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    document.getElementById("responseOutput").innerText = JSON.stringify(data);
    console.log("Response has been printed on the page.");
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
  }
}
