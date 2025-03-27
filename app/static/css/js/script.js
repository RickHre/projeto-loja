// Exibir uma mensagem de boas-vindas na página inicial
document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessage = document.querySelector('#welcomeMessage');
    if (welcomeMessage) {
        welcomeMessage.textContent = 'Bem-vindo à Minha Loja!';
    }
});

// Confirmação ao excluir cliente
const deleteLinks = document.querySelectorAll('a[href^="/excluir/"]');
deleteLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        const confirmDelete = confirm('Tem certeza que deseja excluir este cliente?');
        if (!confirmDelete) {
            event.preventDefault();
        }
    });
});