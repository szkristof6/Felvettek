function hitelesit(input) {
	return input.toString().replace(/&/g, ' ').replace(/</g, ' ').replace(/>/g, ' ').replace(/"/g, ' ').trim()
}

const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const om_azonosito = parseInt(hitelesit(formData.get("om_azonosito")));
    const csrftoken = hitelesit(formData.get('csrfmiddlewaretoken'));

    if(!isNaN(om_azonosito) && csrftoken !== ""){
        const json = {
            om_azonosito
        }

        fetch("/kereses/", {
            method: "POST",
            body: JSON.stringify(json),
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken
            },
            credentials: 'same-origin'
        }).then(response => response.json())
        .then((data) => {
            console.log(data);
        })
    } else {
        console.log("ures");
    }
})