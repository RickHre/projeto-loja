// Este arquivo JavaScript é responsável por exibir mensagens de flash usando SweetAlert2


//Aqui será utilizado o SweetAlert2 para exibir mensagens de flash na parte superior da tela
document.addEventListener('DOMContentLoaded', function () {
    const messages = JSON.parse(document.getElementById('flash-messages-data').textContent);

    if (messages.length > 0) {
        messages.forEach(({ category, message }) => {
            let swalIcon;
            switch (category) {
                case 'success':
                    swalIcon = 'success';
                    break;
                case 'info':
                    swalIcon = 'info';
                    break;
                case 'warning':
                    swalIcon = 'warning';
                    break;
                case 'danger':
                    swalIcon = 'error'; // 'danger' geralmente indica um erro
                    break;
                default:
                    swalIcon = 'info'; // Ícone padrão caso a categoria não seja mapeada
            }

            Swal.fire({
                icon: swalIcon,
                title: message,
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true
            });
        });
    }

    // Aqui adicionamos um evento de clique para os botões de exclusão
    // Isso é útil para confirmar a exclusão de um cliente antes de redirecionar
    const deleteButtons = document.querySelectorAll('.delete-client');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Impede o redirecionamento imediato

            const deleteUrl = this.getAttribute('data-url');

            Swal.fire({
                title: 'Tem certeza?',
                text: 'Esta ação não pode ser desfeita!',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sim, excluir!',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = deleteUrl; // Redireciona para a URL de exclusão
                }
            });
        });
    });
});