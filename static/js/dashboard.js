document.addEventListener('DOMContentLoaded', function() {
    const refreshBtn = document.getElementById('refreshBtn');
    const portsTable = document.getElementById('portsTable');
    const loadingSpinner = document.getElementById('loadingSpinner');
    let autoRefreshInterval;

    // Function to update the table with new data
    function updateTable(ports) {
        portsTable.innerHTML = '';
        ports.forEach(port => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${port.name}</td>
                <td>
                    <span class="status-indicator ${port.status === 'connected' ? 'status-up' : 'status-down'}">
                        ${port.status}
                    </span>
                </td>
                <td>${port.vlan}</td>
                <td>${port.speed}</td>
                <td>${port.duplex}</td>
                <td>${port.description}</td>
            `;
            portsTable.appendChild(row);
        });
    }

    // Function to fetch and update port status
    async function refreshPorts() {
        loadingSpinner.classList.remove('d-none');
        try {
            const response = await fetch('/api/ports');
            const data = await response.json();
            
            if (data.success) {
                updateTable(data.data);
            } else {
                throw new Error(data.error);
            }
        } catch (error) {
            console.error('Error fetching ports:', error);
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert alert-danger';
            alertDiv.textContent = `Failed to fetch port status: ${error.message}`;
            portsTable.parentNode.insertBefore(alertDiv, portsTable);
        } finally {
            loadingSpinner.classList.add('d-none');
        }
    }

    // Manual refresh button click handler
    refreshBtn.addEventListener('click', refreshPorts);

    // Setup auto-refresh
    autoRefreshInterval = setInterval(refreshPorts, 60000); // 60 seconds

    // Clean up interval on page unload
    window.addEventListener('unload', () => {
        clearInterval(autoRefreshInterval);
    });
});
