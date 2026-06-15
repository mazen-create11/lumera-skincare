document.addEventListener('DOMContentLoaded', () => {
    // --- Header Scroll Effect ---
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // --- Mobile Burger Menu ---
    const burger = document.getElementById('navBurger');
    if (burger) {
        burger.addEventListener('click', () => document.body.classList.toggle('menu-open'));
        document.querySelectorAll('.nav-links a').forEach(a =>
            a.addEventListener('click', () => document.body.classList.remove('menu-open'))
        );
    }

    // --- Intersection Observer for Scroll Animations ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Run once
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
    animatedElements.forEach(el => observer.observe(el));

    // --- Cart Drawer Logic ---
    const cartBtns = document.querySelectorAll('.cart-btn');
    const closeCartBtn = document.querySelector('.close-cart');
    const cartDrawer = document.querySelector('.cart-drawer');
    const cartOverlay = document.querySelector('.cart-overlay');
    const addToCartBtns = document.querySelectorAll('.add-to-cart');
    const cartItemsContainer = document.querySelector('.cart-items');
    
    // Minimal Cart State
    let cart = [];

    function openCart() {
        cartDrawer.classList.add('active');
        cartOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeCart() {
        cartDrawer.classList.remove('active');
        cartOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    cartBtns.forEach(btn => btn.addEventListener('click', (e) => {
        e.preventDefault();
        openCart();
    }));
    
    if(closeCartBtn) closeCartBtn.addEventListener('click', closeCart);
    if(cartOverlay) cartOverlay.addEventListener('click', closeCart);

    // Simple Add to Cart Simulation
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const product = btn.dataset.product || 'Produit LUMÉRA';
            const price = btn.dataset.price || '0';
            
            cart.push({ title: product, price: parseInt(price) });
            updateCartUI();
            openCart();
        });
    });

    function updateCartUI() {
        if (cart.length === 0) {
            cartItemsContainer.innerHTML = '<p class="cart-empty">Votre panier est vide.</p>';
            return;
        }

        let html = '';
        let total = 0;
        cart.forEach(item => {
            html += `
                <div style="display:flex; justify-content:space-between; margin-bottom:1rem; padding-bottom:1rem; border-bottom:1px solid #efefef;">
                    <div>
                        <h4 style="font-family:'Playfair Display', serif; font-size:1.1rem;">${item.title}</h4>
                        <p style="font-size:0.9rem; color:#666;">Quantité: 1</p>
                    </div>
                    <div style="font-weight:600;">${item.price}€</div>
                </div>
            `;
            total += item.price;
        });
        
        cartItemsContainer.innerHTML = html;
        const totalEl = document.querySelector('.cart-total span:last-child');
        if(totalEl) totalEl.innerText = total + '€';
    }

    // --- FAQ Accordion Logic ---
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const faqItem = question.parentElement;
            const isActive = faqItem.classList.contains('active');
            
            // Close all other FAQs
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('active');
            });

            if (!isActive) {
                faqItem.classList.add('active');
            }
        });
    });
});
