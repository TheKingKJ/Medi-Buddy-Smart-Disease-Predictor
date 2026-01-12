// JavaScript for Heart Disease Prediction page

document.addEventListener('DOMContentLoaded', function() {
    const heartForm = document.getElementById('heartForm');
    
    if (heartForm) {
        heartForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            
            fetch('/predict/heart', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                const resultDiv = document.getElementById('result');
                const resultText = document.getElementById('resultText');
                
                if (data.error) {
                    resultText.textContent = 'Error: ' + data.error;
                    resultDiv.classList.remove('alert-success', 'alert-danger');
                    resultDiv.classList.add('alert-warning');
                } else {
                    resultText.textContent = data.result;
                    resultDiv.classList.remove('alert-warning');
                    
                    if (data.result.includes('does not have')) {
                        resultDiv.classList.remove('alert-danger');
                        resultDiv.classList.add('alert-success');
                    } else {
                        resultDiv.classList.remove('alert-success');
                        resultDiv.classList.add('alert-danger');
                    }
                }
                
                resultDiv.style.display = 'block';
                
                // Scroll to result
                resultDiv.scrollIntoView({ behavior: 'smooth' });
            })
            .catch(error => {
                console.error('Error:', error);
                const resultDiv = document.getElementById('result');
                const resultText = document.getElementById('resultText');
                resultText.textContent = 'An error occurred. Please try again.';
                resultDiv.classList.remove('alert-success', 'alert-danger');
                resultDiv.classList.add('alert-warning');
                resultDiv.style.display = 'block';
            });
        });
    }
}); 