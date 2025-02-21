document.getElementById("search-button").addEventListener("click", async () => {
    const queryText = document.getElementById("search-input").value;
    
    if (!queryText) {
        alert("Please enter a search query.");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query_embedding: [/* Your query embedding here */] })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        displayResults(data.results);
    } catch (error) {
        console.error("Error:", error);
        alert(`An error occurred: ${error.message}`);
    }
});

function displayResults(results) {
    const resultsContainer = document.getElementById("results-container");
    resultsContainer.innerHTML = "";

    if (results.length === 0) {
        resultsContainer.innerHTML = "<p>No results found.</p>";
        return;
    }

    results.forEach((result, idx) => {
        const imgElement = document.createElement("img");
        imgElement.src = `http://localhost:5000/images/${result.path}`;
        imgElement.alt = `Result ${idx + 1}`;
        imgElement.style.width = "200px";

        resultsContainer.appendChild(imgElement);
    });
}
