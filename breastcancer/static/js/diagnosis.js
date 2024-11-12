// Envío del formulario para obtener el diagnóstico
document.getElementById('diagnosis-form').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch(diagnosisUrl, {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": csrfToken
        }
    });
    const data = await response.json();
    document.getElementById('result').innerText = "El diagnóstico es: " + data.diagnosis;
};
