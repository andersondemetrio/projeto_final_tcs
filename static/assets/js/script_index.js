document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById("searchForm");
    const modal = document.getElementById("myModal");

    modal.addEventListener("click", function(event) {
        if (event.target === modal) {
            event.preventDefault();
            event.stopPropagation();
        }
    });

    searchForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(searchForm);

        fetch(searchForm.action + '?' + new URLSearchParams(formData), {
            method: 'GET'
        })
        .then(response => response.text())
        .then(data => {
            const searchResultsTable = document.getElementById("searchResultsTable");
            searchResultsTable.innerHTML = data; // Atualiza a tabela de resultados
        })
        .catch(error => {
            console.error('Erro na busca:', error);
        });
    });

    // Intercepta o clique nos links de paginação
    const paginationLinks = document.querySelectorAll(".pagination a");
    paginationLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // Impede o comportamento padrão do link
            const pageUrl = this.getAttribute("href");

            // Carrega os resultados da próxima página via AJAX
            fetch(pageUrl, {
                method: 'GET'
            })
            .then(response => response.text())
            .then(data => {
                const searchResultsTable = document.getElementById("searchResultsTable");
                searchResultsTable.innerHTML = data; // Atualiza a tabela de resultados
            })
            .catch(error => {
                console.error('Erro na paginação:', error);
            });
        });
    });
});