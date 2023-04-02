const form = document.getElementById('form');

form.addEventListener("submit", submitHandler);

function submitHandler(e) {
    e.preventDefault();
    fetch(
        form.action,
        {
            method: 'POST',
            body: new FormData(form)
        }
    )
    .then(
        response => response.json()
    )
    .then(data=>{
        if (data.message === 'success') {
            alert('Success!');
            form.reset()
        }
    });
}