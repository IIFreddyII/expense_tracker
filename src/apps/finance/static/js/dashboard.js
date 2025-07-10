document.addEventListener("DOMContentLoaded", () => {
    const token = localStorage.getItem("access");


    if (!token) {
        window.location.href = "";
        return;
    }

    const form = document.getElementById("transaction-form");
    const container = document.getElementById("transaction-list");

    // get user info
    const user_id = localStorage.getItem("user")

    // Load existing transactions on page load
    loadTransactions();

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const payload = Object.fromEntries(formData.entries());

        // Parse user info and add the ID to the payload

        if (user_id) {
            payload.user = user_id;
        }

        try {
            const response = await fetch("/api/v1/transactions/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`,
                },
                body: JSON.stringify(payload),
            });

            if (response.ok) {
                form.reset();
                loadTransactions();
            } else if (response.status === 401) {
                window.location.href = "";
            } else {
                alert("Failed to save transaction.");
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });


    async function loadTransactions() {
        // Asegúrate de que tu HTML tenga elementos con estos IDs
        const incomeContainer = document.getElementById("income-list");
        const expenseContainer = document.getElementById("expense-list");

        // Si los contenedores no existen, muestra un error en la consola y detiene la ejecución.
        if (!incomeContainer || !expenseContainer) {
            console.error("Por favor, añade elementos con los IDs 'income-list' y 'expense-list' a tu HTML.");
            return;
        }

        try {
            const response = await fetch("/api/v1/transactions/", {
                method: "GET",
                headers: {
                    "Authorization": `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                const results = data.results || [];

                // Filtramos las transacciones en dos arrays: ingresos y gastos.
                // Asumo que los tipos son 'income' y 'expense'. Ajústalo si usan otros valores.
                const incomes = results.filter(tx => tx.type === 'income');
                const expenses = results.filter(tx => tx.type === 'expense');

                // Renderizar la lista de ingresos
                if (incomes.length === 0) {
                    incomeContainer.innerHTML = "<p>No se encontraron ingresos.</p>";
                } else {
                    // Usamos map y join para generar el HTML de forma más eficiente
                    const incomeHTML = incomes.map(tx => `
                    <p class="${tx.type}">
                      ${tx.date} — ${tx.description} — $${tx.amount}
                    </p>
                `).join('');
                    incomeContainer.innerHTML = incomeHTML;
                }

                // Renderizar la lista de gastos
                if (expenses.length === 0) {
                    expenseContainer.innerHTML = "<p>No se encontraron gastos.</p>";
                } else {
                    const expenseHTML = expenses.map(tx => `
                    <p class="${tx.type}">
                      ${tx.date} — ${tx.description} — $${tx.amount}
                    </p>
                `).join('');
                    expenseContainer.innerHTML = expenseHTML;
                }

            } else if (response.status === 401) {
                window.location.href = "";
            } else {
                incomeContainer.innerHTML = ""; // Limpiar en caso de error
                expenseContainer.innerHTML = "<p>Fallo al cargar las transacciones.</p>";
            }
        } catch (error) {
            console.error("Error al cargar las transacciones:", error);
            incomeContainer.innerHTML = ""; // Limpiar en caso de error
            expenseContainer.innerHTML = "<p>Error inesperado.</p>";
        }
    }


    // Obtener los elementos del DOM que necesitamos
    const modal = document.getElementById('transaction-modal');
    const openModalBtn = document.getElementById('open-modal-btn');
    const closeModalBtn = document.querySelector('.close-button');

    // Función para abrir el modal
    function openModal() {
        modal.style.display = 'block';
    }

    // Función para cerrar el modal
    function closeModal() {
        modal.style.display = 'none';
    }

    // --- ASIGNAR EVENTOS ---

    // 1. Abrir el modal al hacer clic en el botón "Registrar"
    if (openModalBtn) {
        openModalBtn.addEventListener('click', openModal);
    }

    // 2. Cerrar el modal al hacer clic en la 'x'
    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    }

    // 3. Cerrar el modal si el usuario hace clic fuera de la caja de contenido
    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            closeModal();
        }
    });

    // 4. (Opcional) Cerrar el modal con la tecla 'Escape'
    window.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            closeModal();
        }
    });
});
