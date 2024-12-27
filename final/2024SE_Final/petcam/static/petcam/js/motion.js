// Function to fetch and update motion status
function updateStatus() {
    fetch('/petcam/get-motion-status/')
        .then(response => response.json())
        .then(data => {
            // Update button text based on motion status
            if (data.status === "running") {
                document.getElementById('toggle-btn').textContent = "자동녹화중지";
            } else {
                document.getElementById('toggle-btn').textContent = "자동녹화시작";
            }
        });
}

// Update status on page load
updateStatus();

// Toggle motion and update status
document.getElementById('toggle-btn').addEventListener('click', () => {
    fetch('/petcam/toggle-motion/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = data.status;
            updateStatus(); // Refresh the button text
        });
});