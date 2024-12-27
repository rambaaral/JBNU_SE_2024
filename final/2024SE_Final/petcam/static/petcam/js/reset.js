document.addEventListener("DOMContentLoaded", () => {
    const resetBtn = document.querySelector(".btn.btn-outline-danger.btn-sm");

    const resetSystem = () => {
        fetch("/petcam/reset/")
            .then((response) => response.json())
            .then((data) => console.log(data.status))
            .catch((error) => console.error("Error:", error));
    };

    resetBtn.addEventListener("click", resetSystem);
});