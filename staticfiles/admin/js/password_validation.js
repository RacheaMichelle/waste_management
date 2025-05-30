// Password visibility toggle
function togglePassword(button) {
    const input = button.previousElementSibling;
    const icon = button.querySelector('i');
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.replace('fa-eye', 'fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.replace('fa-eye-slash', 'fa-eye');
    }
}

// Password strength indicator
document.addEventListener('DOMContentLoaded', function() {
    const password1 = document.getElementById('id_password1');
    if (password1) {
        password1.addEventListener('input', function(e) {
            const password = e.target.value;
            const strengthBar = document.querySelector('.strength-bar');
            const strengthText = document.querySelector('.strength-text');
            
            if (!password) {
                strengthBar.style.width = '0%';
                strengthText.textContent = '';
                return;
            }
            
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