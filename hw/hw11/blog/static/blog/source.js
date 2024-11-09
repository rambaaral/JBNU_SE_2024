function time()
{
    const date = new Date();

    const y = date.getFullYear();
    const m = date.getMonth() + 1;
    const d = date.getDate();
    const dd = date.getDay();
    const h = date.getHours();
    const mm = date.getMinutes();
    const s = date.getSeconds();

    const dayNames = ['일', '월', '화', '수', '목', '금', '토'];

    const result = `${y}년 ${m}월 ${d}일 (${dayNames[dd]}) ${h}시 ${String(mm).padStart(2, '0')}분 ${String(s).padStart(2, '0')}초`;

    document.getElementById('clock').innerText = result;
}

setInterval(time, 1000);

time()