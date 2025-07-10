document.addEventListener("DOMContentLoaded", () => {
    const token = localStorage.getItem("access");

    if (!token) {
        window.location.href = "";
        return;
    }

    const form = document.getElementById("transaction-form");
    const incomeContainer = document.getElementById("income-list");
    const expenseContainer = document.getElementById("expense-list");
    const totalIncomesEl = document.getElementById('total-incomes');
    const totalExpensesEl = document.getElementById('total-expenses');
    const modal = document.getElementById('transaction-modal');
    const openModalBtn = document.getElementById('open-modal-btn');
    const closeModalBtn = document.querySelector('.close-button');


    /**
     * Formatea un número a una cadena de moneda (ej. $1,234.56).
     * @param {number} amount - La cantidad a formatear.
     * @returns {string} La cantidad formateada como moneda.
     */
    const formatCurrency = (amount) => {
        const numberAmount = Number(amount) || 0;
        return new Intl.NumberFormat('es-MX', {
            style: 'currency',
            currency: 'MXN'
        }).format(numberAmount);
    };


    /**
     * Obtiene los totales de ingresos y gastos desde la API y actualiza el DOM.
     */
    async function updateTotals() {
        totalIncomesEl.textContent = 'Cargando...';
        totalExpensesEl.textContent = 'Cargando...';

        const headers = {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json",
        };

        try {
            const [incomesRes, expensesRes] = await Promise.all([
                fetch('/api/v1/transactions/total-incomes/', {headers}),
                fetch('/api/v1/transactions/total-expenses/', {headers})
            ]);

            if (incomesRes.status === 401 || expensesRes.status === 401) {
                window.location.href = "";
                return;
            }

            if (!incomesRes.ok || !expensesRes.ok) {
                throw new Error('No se pudieron obtener los totales.');
            }

            const incomesData = await incomesRes.json();
            const expensesData = await expensesRes.json();

            totalIncomesEl.textContent = formatCurrency(incomesData.total_incomes);
            totalExpensesEl.textContent = formatCurrency(expensesData.total_expenses);

            financeChart.update(incomesData.total_incomes, expensesData.total_expenses)

        } catch (error) {
            console.error('Error en updateTotals:', error);
            totalIncomesEl.textContent = 'Error';
            totalExpensesEl.textContent = 'Error';
        }
    }

    /**
     * Carga la lista de transacciones (ingresos y gastos) y las muestra en el DOM.
     */
    async function loadTransactions() {
        if (!incomeContainer || !expenseContainer) {
            console.error("Contenedores de lista no encontrados.");
            return;
        }

        try {
            const response = await fetch("/api/v1/transactions/", {
                method: "GET",
                headers: {"Authorization": `Bearer ${token}`},
            });
            console.log(response.status)
            if (response.status === 401 || response.status === 404) {
                window.location.href = "";
                return;
            }

            if (!response.ok) {
                throw new Error("Fallo al cargar las transacciones.");
            }

            const data = await response.json();
            const results = data.results || [];

            const incomes = results.filter(tx => tx.type === 'income');
            const expenses = results.filter(tx => tx.type === 'expense');

            incomeContainer.innerHTML = incomes.length === 0
                ? "<p>No se encontraron ingresos.</p>"
                : incomes.map(tx => `
                    <p class="${tx.type}">
                        <span>${new Date(tx.date).toLocaleDateString('es-MX')} - ${tx.description}</span>
                        <span>${formatCurrency(tx.amount)}</span>
                    </p>
                `).join('');

            expenseContainer.innerHTML = expenses.length === 0
                ? "<p>No se encontraron gastos.</p>"
                : expenses.map(tx => `
                    <p class="${tx.type}">
                        <span>${new Date(tx.date).toLocaleDateString('es-MX')} - ${tx.description}</span>
                        <span>${formatCurrency(tx.amount)}</span>
                    </p>
                `).join('');

        } catch (error) {
            console.error("Error al cargar transacciones:", error);
            incomeContainer.innerHTML = `<p>${error.message}</p>`;
            expenseContainer.innerHTML = "";
        }
    }

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const payload = Object.fromEntries(formData.entries());

        const user_id = localStorage.getItem("user")

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
                closeModal();         // Cierra el modal
                loadTransactions();   // Recarga la lista de transacciones
                updateTotals();       // ¡Actualiza los totales!
            } else if (response.status === 401) {
                window.location.href = "/login/";
            } else {
                const errorData = await response.json();
                console.error("Error al guardar:", errorData);
                alert("Fallo al guardar la transacción. Revisa los datos.");
            }
        } catch (error) {
            console.error("Error de red:", error);
        }
    });

    function openModal() {
        modal.style.display = 'block';
    }

    function closeModal() {
        modal.style.display = 'none';
    }

    if (openModalBtn) openModalBtn.addEventListener('click', openModal);
    if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);

    window.addEventListener('click', (event) => {
        if (event.target == modal) closeModal();
    });

    window.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && modal.style.display === 'block') closeModal();
    });

    loadTransactions();
    updateTotals();
});