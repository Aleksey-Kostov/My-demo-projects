// Load external JavaScript files dynamically
function loadScript(src) {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = src;
    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
}

async function loadAllScripts() {
  try {
    // Load external libraries
    await loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js");
    await loadScript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js");
    await loadScript("https://code.jquery.com/jquery-3.5.1.min.js");
    await loadScript("https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js");

    // Correct path for CurrentDateTime.js
    // await loadScript("/static/style/JavaScript/CurrentDateTime.js");  // Update path as needed

    // Load other scripts
    await loadScript("/static/style/JavaScript/DinamicBackground.js");

    await loadScript("https://cdn.jsdelivr.net/npm/chart.js");
    await loadScript("/static/style/JavaScript/widgets.js");

    await loadScript("/static/style/JavaScript/PhotoPreview.js");
    await loadScript("/static/style/JavaScript/FilterMessages.js");

    console.log("All scripts loaded successfully");
  } catch (error) {
    console.error("Error loading scripts:", error);
  }
}

loadAllScripts();

  