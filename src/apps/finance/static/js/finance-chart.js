const financeChart = {
    chartInstance: null,

    /**
     * Crea o actualiza la gráfica de pie con los totales de ingresos y gastos.
     * @param {number} totalIncomes - El total de ingresos.
     *@param {number} totalExpenses - El total de gastos.
     */
    update(totalIncomes, totalExpenses) {
        const ctx = document.getElementById('transactionChart')?.getContext('2d');

        // Si el canvas no existe, no hacemos nada.
        if (!ctx) {
            console.error("El elemento canvas 'transactionChart' no fue encontrado.");
            return;
        }

        // Si ya existe una gráfica, la destruimos para evitar conflictos.
        if (this.chartInstance) {
            this.chartInstance.destroy();
        }

        const data = {
            labels: ['Ingresos', 'Gastos'],
            datasets: [{
                label: 'Distribución de Transacciones',
                data: [totalIncomes, totalExpenses],
                backgroundColor: [
                    'rgb(40,167,69)',
                    'rgb(255,0,49)'
                ],
                borderColor: [
                    'rgb(40,167,69)',
                    'rgb(255,0,49)'
                ],
                borderWidth: 1
            }]
        };

        const config = {
            type: 'pie',
            data: data,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Distribución de Ingresos y Gastos'
                    }
                }
            }
        };

        // Creamos y guardamos la nueva instancia de la gráfica.
        this.chartInstance = new Chart(ctx, config);
    }
};