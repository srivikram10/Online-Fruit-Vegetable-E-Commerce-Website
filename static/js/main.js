// Cart functionality
async function addToCart(productId) {
    try {
        const response = await fetch(`/add_to_cart/${productId}`);
        const data = await response.json();
        
        if (data.status === 'success') {
            showToast(data.message, 'success');
            // Optional: update cart count icon
        } else {
            showToast(data.message, 'error');
            if (data.message.includes('login')) {
                window.location.href = '/login';
            }
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('Something went wrong', 'error');
    }
}

async function updateCart(cartId, action) {
    try {
        const response = await fetch(`/update_cart/${cartId}/${action}`);
        const data = await response.json();
        if (data.status === 'success') {
            if (data.removed) {
                const element = document.getElementById(`cart-item-${cartId}`);
                if (element) element.remove();
                // If cart is empty, reload to show empty state
                if (document.querySelectorAll('[id^="cart-item-"]').length === 0) {
                    window.location.reload();
                }
            } else {
                // Update quantity display
                const qtyElement = document.getElementById(`qty-${cartId}`);
                if (qtyElement) qtyElement.innerText = data.new_quantity;
            }
            
            // Update totals
            const subtotalElement = document.getElementById('subtotal');
            const totalElement = document.getElementById('total');
            if (subtotalElement) subtotalElement.innerText = data.new_total.toFixed(2);
            if (totalElement) totalElement.innerText = data.new_total.toFixed(2);
            
            showToast('Cart updated', 'success');
        } else {
            showToast(data.message, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function removeFromCart(cartId) {
    if (!confirm('Are you sure you want to remove this item?')) return;
    try {
        const response = await fetch(`/remove_from_cart/${cartId}`);
        const data = await response.json();
        if (data.status === 'success') {
            const element = document.getElementById(`cart-item-${cartId}`);
            if (element) element.remove();
            
            // Re-calculate total or reload if empty
            if (document.querySelectorAll('[id^="cart-item-"]').length === 0) {
                window.location.reload();
            } else {
                // We could calculate here or fetch totals again, 
                // but for simplicity let's reload or assume it's fine for now.
                // Better yet, just call updateCart with dummy action to get totals?
                // For now, let's just reload to be safe and accurate on totals.
                window.location.reload();
            }
        } else {
            showToast(data.message, 'error');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Simple Toast Notification
function showToast(message, type) {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: ${type === 'success' ? '#27ae60' : '#e74c3c'};
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 9999;
        transition: transform 0.3s ease, opacity 0.3s ease;
        transform: translateY(100px);
    `;
    toast.innerText = message;
    document.body.appendChild(toast);
    
    // Animate in
    setTimeout(() => {
        toast.style.transform = 'translateY(0)';
    }, 100);
    
    // Remove after 3s
    setTimeout(() => {
        toast.style.transform = 'translateY(100px)';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Scroll effects
window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (window.scrollY > 50) {
        nav.style.padding = '0.5rem 5%';
        nav.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
    } else {
        nav.style.padding = '1rem 5%';
        nav.style.boxShadow = 'none';
    }
});

// Category hover animations (CSS handles mostly, but JS can add micro-interactions)
document.querySelectorAll('.category-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.querySelector('i').style.transform = 'scale(1.2) rotate(10deg)';
    });
    card.addEventListener('mouseleave', () => {
        card.querySelector('i').style.transform = 'scale(1) rotate(0deg)';
    });
});
