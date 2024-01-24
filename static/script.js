document.querySelectorAll('.film').forEach((button) => {
    button.addEventListener('click', ()=>{
        fetch(`/search/${button.id}`, {
                method: 'POST',
                body: JSON.stringify({"title":button.id}),
            });
    });
})