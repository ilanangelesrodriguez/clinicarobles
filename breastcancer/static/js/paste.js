// Función para pegar datos desde el portapapeles
document.getElementById('paste-button').onclick = async function() {
    try {
        // Obtiene el texto del portapapeles
        const clipboardText = await navigator.clipboard.readText();

        // Divide el texto en valores usando comas, espacios o saltos de línea como separadores
        const values = clipboardText.split(/[\s,]+/).filter(Boolean);

        // Asigna cada valor a los campos de entrada en orden
        values.forEach((value, index) => {
            const input = document.getElementById(`feature${index + 1}`);
            if (input) {
                input.value = value.trim();
            }
        });
    } catch (error) {
        alert("No se pudo acceder al portapapeles. Asegúrate de que el navegador permita el acceso.");
    }
};
