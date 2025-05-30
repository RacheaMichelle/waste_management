// This is a backup in case the inline script doesn't work
function initializePasswordToggles() {
    document.querySelectorAll('.toggle-password').forEach(button => {
        // Only add listener if not already present
        if (!button.dataset.listenerAdded) {
            button.addEventListener('click', function() {
                const input = this.previousElementSibling;
                const icon = this.querySelector('i');
                
                if (input && icon) {
                    if (input.type === 'password') {
                        input.type = 'text';
                        icon.classList.replace('fa-eye', 'fa-eye-slash');
                    } else {
                        input.type = 'password';
                        icon.classList.replace('fa-eye-slash', 'fa-eye');
                    }
                }
            });
            button.dataset.listenerAdded = 'true';
        }
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializePasswordToggles);

// Also expose function to window for debugging
window.togglePassword = initializePasswordToggles;

// Password strength indicator (for registration forms)
document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    if (passwordInput) {
        passwordInput.addEventListener('input', function(e) {
            const password = e.target.value;
            const strengthBar = document.querySelector('.strength-bar');
            const strengthText = document.querySelector('.strength-text');
            
            if (!strengthBar || !strengthText) return;
            
            let strength = 0;
            if (password.length >= 8) strength += 1;
            if (/[A-Z]/.test(password)) strength += 1;
            if (/[0-9]/.test(password)) strength += 1;
            if (/[^A-Za-z0-9]/.test(password)) strength += 1;
            
            const colors = ['bg-red-500', 'bg-yellow-500', 'bg-blue-500', 'bg-green-500'];
            const texts = ['Very Weak', 'Weak', 'Medium', 'Strong'];
            
            strengthBar.className = `h-full ${colors[strength]} strength-bar`;
            strengthBar.style.width = `${(strength + 1) * 25}%`;
            strengthText.textContent = texts[strength] || '';
        });
    }
});