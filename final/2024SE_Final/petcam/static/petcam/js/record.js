document.getElementById("record-btn").addEventListener("click", function () {
    fetch('/petcam/start-recording/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ duration: 10 }) // 10초 동안 녹화
    })
    .then(response => response.json())
    .then(data => {
        alert("녹화가 완료되었습니다.");
    })
    .catch(error => {
        console.error('녹화 요청 실패:', error);
    });
});