  // Active Sellers Chart
    var ctx1 = document.getElementById('activeSellersChart').getContext('2d');
    var activeSellersChart = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            datasets: [{
                label: 'Active Sellers',
                data: [5, 12, 8, 14, 9],
                backgroundColor: '#007bff',
                borderColor: '#007bff',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Active Buyers Chart
    var ctx2 = document.getElementById('activeBuyersChart').getContext('2d');
    var activeBuyersChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            datasets: [{
                label: 'Active Buyers',
                data: [15, 22, 18, 24, 30],
                borderColor: '#28a745',
                backgroundColor: 'rgba(40, 167, 69, 0.2)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Total Products Chart
    var ctx3 = document.getElementById('totalProductsChart').getContext('2d');
    var totalProductsChart = new Chart(ctx3, {
        type: 'pie',
        data: {
            labels: ['Fruits', 'Vegetables', 'Grains', 'Herbs', 'Dairy'],
            datasets: [{
                label: 'Total Products',
                data: [25, 30, 15, 10, 20],
                backgroundColor: ['#ff5733', '#33ff57', '#3357ff', '#ff33a8', '#a833ff'],
                borderColor: '#fff',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
        }
    });
