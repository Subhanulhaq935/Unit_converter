// Client-side UX enhancements
document.addEventListener('DOMContentLoaded', () => {
    // 1. Swap Units Functionality
    const swapBtn = document.getElementById('swapUnitsBtn');
    const fromSelect = document.getElementById('from_unit');
    const toSelect = document.getElementById('to_unit');

    if (swapBtn && fromSelect && toSelect) {
        const doSwap = () => {
            const tempVal = fromSelect.value;
            fromSelect.value = toSelect.value;
            toSelect.value = tempVal;

            // Trigger subtle rotation animation
            swapBtn.style.transform = 'rotate(180deg)';
            setTimeout(() => {
                swapBtn.style.transform = 'none';
            }, 250);
        };

        swapBtn.addEventListener('click', doSwap);
        swapBtn.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                doSwap();
            }
        });
    }

    // 2. Add Copy Button to Result Header if result exists
    const resultHeader = document.querySelector('.result-header');
    const resultTo = document.querySelector('.result-to');

    if (resultHeader && resultTo) {
        const copyBtn = document.createElement('button');
        copyBtn.type = 'button';
        copyBtn.className = 'btn-copy';
        copyBtn.innerHTML = '📋 Copy Result';
        copyBtn.title = 'Copy converted value to clipboard';

        copyBtn.addEventListener('click', async () => {
            const textToCopy = resultTo.textContent.trim().replace(/\s+/g, ' ');
            try {
                await navigator.clipboard.writeText(textToCopy);
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '✅ Copied!';
                copyBtn.classList.add('copied');
                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                    copyBtn.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy: ', err);
            }
        });

        resultHeader.appendChild(copyBtn);
    }
});

