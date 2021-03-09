function massage_show(text) {
    const massage = document.querySelector("#massage");

    massage.querySelector('p').innerText = text;
    massage.style.display = "block";

    setTimeout(() => {
        massage.style.display = "none";
    }, 5 * 1000);
}

function hitelesit(input) {
    return input.toString().replace(/&/g, ' ').replace(/</g, ' ').replace(/>/g, ' ').replace(/"/g, ' ').trim()
}

const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const om_azonosito = parseInt(hitelesit(formData.get("om_azonosito")));
    const csrftoken = hitelesit(formData.get('csrfmiddlewaretoken'));

    if (!isNaN(om_azonosito) && csrftoken !== "") {
        if (om_azonosito.toString().length === 11 && om_azonosito.toString()[0]==="7") {
            const json = {
                om_azonosito
            }

            fetch("./", {
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
                    form.reset()
                    if (data.massage === "OK") {
                        const {
                            lista
                        } = data;

                        lista.sort(function(a, b){
                            if(a.tagozat < b.tagozat) { return -1; }
                            if(a.tagozat > b.tagozat) { return 1; }
                            return 0;
                        })

                        const modal = document.querySelector("#modal");

                        window.onclick = (event) => {
                            if (event.target == modal) {
                                modal.style.display = "none";
                                body.innerHTML = "";
                            }
                        }

                        modal.querySelector(".nev").innerText = lista[0].nev;
                        modal.querySelector(".om_azonosito").innerText = `OM-Azonosító: ${lista[0].om_azonosito}`;

                        const body = modal.querySelector(".body");

                        lista.forEach(adat => {
                            const elem = document.createElement("div");
                            elem.setAttribute("class", `elem ${adat.dontes === "igen" ? "zold" : "piros"}`);

                            const tagozat = document.createElement("span");
                            tagozat.appendChild(document.createTextNode(`Tagozat: ${adat.tagozat}`));
                            tagozat.setAttribute("class", "tagozat");
                            elem.appendChild(tagozat);

                            const dontes = document.createElement("span");
                            dontes.appendChild(document.createTextNode(`Döntés: ${adat.dontes}`));
                            dontes.setAttribute("class", "dontes");
                            elem.appendChild(dontes);

                            body.appendChild(elem);
                        });

                        modal.setAttribute("style", "display: block;")

                    } else {
                        massage_show(data.massage)
                    }
                })
        } else {
            massage_show("Nem megfelelő az OM-Azonosító formátuma!")
        }
    } else {
        massage_show("Add meg az OM-Azonosítót!")
    }
})