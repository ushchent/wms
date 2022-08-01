
const update_in_field = artikul => {
	fetch(`/api/code/${artikul}`)
		.then(response => response.json())
		.then(data => {
					console.log(data[0]["in_field"]);
				document.getElementById("in_field_id").textContent = data[0]["in_field"];
})
}

const update_status = artikul => {
			fetch(`/api/code/${artikul}`)
				.then(response => response.json())
				.then(data => document.getElementById("status_id").textContent
						= status_map[data[0]["status"]])
		}
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
	
const close_artikul = artikul => {
			const post_data = {
						"code": artikul,
						"status": true
					}
			fetch("/api/status_update/", {
						"method": "POST",
						"headers": {
								"Content-Type": "application/json",
								"X-CSRFToken": csrftoken
								},
						"body": JSON.stringify(post_data)
					})
	fetch(`/api/code/${artikul}`)
		.then(response => response.json())
		.then(data => {
				document.getElementById("status_id").textContent =
						status_map[data[0]["status"]];
   				document.getElementById("status_id").className =
						status_style_map[data[0]["status"]];
})
}
		const update_field = () => {
				const boxes_found = document.getElementById("number_id").value;
				const artikul_selected = document.getElementById("artikul_id")
						.textContent;
				console.log(artikul_selected);
				const post_data = {
							"code": artikul_selected,
							"in_field": boxes_found,
							"csrftoken": csrftoken
				};
				console.log(post_data);
					fetch("/api/field_update/", {
							"method": "POST",
								"headers": {
									"Content-Type": "application/json",
									"X-CSRFToken": csrftoken 
										},
								"body": JSON.stringify(post_data)
							})
						.then(update_in_field(artikul_selected))
				}

const search_box = document.getElementById("artikul_selector");
const state = { data: null };
//search_box.onfocus = function() {
//    if (search_box.value == "Выбрать артикул") {
//        search_box.value = "";
//    }
//}
//search_box.onblur = function() {
//    if (search_box.value == "") {
//        search_box.value = "Выбрать артикул";
          document.querySelector("#search_results").className="hidden";
//    }
//};

const set_search_type = () => {
    console.log(this.id)
}

const create_search_results_list = data => {
    const target = document.querySelector("#search_results");
    const message = document.getElementById("message");
    if (target.getElementsByTagName("ul")[0]) {
        target.getElementsByTagName("ul")[0].remove();
    }
    const result_list = document.createElement("ul");
    if (data.length == 0) {
        target.className="hidden";
        message.textContent = "Артикул не найден";    
    } else {
        target.className = "";
        message.textContent = "";
    }

    for (var i=0; i<data.length; i++) {
        const code = data[i]["code"];
        const id = data[i]["id"];
        const title = data[i]["title"];
        const list_item = document.createElement("li");
        list_item.setAttribute("data-artikul", data[i].code);
        list_item.setAttribute("data-id", data[i].id);
        list_item.addEventListener("click", display_data, false);
        const li_text = document.createTextNode(`${code} -- ${title}`);
        list_item.appendChild(li_text);
        result_list.appendChild(list_item);
    }
    target.appendChild(result_list);
}

const status_map = {
    false: "Открыто",
    true: "Закрыто" 
}

const status_style_map = {
	false: "open",
	true: "closed"
}

const sector_map = {
	"1": [1, 5, 8],
	"2": [3, 6],
	"3": [2, 4, 7, 9]
	}

const get_sector_number = artikul => {
	const sectors = Object.entries(sector_map);
	var sector_identified;
	sectors.forEach(e => {
			if (artikul[0] in e[1]) {
				console.log("sector identified: ", e[0])
				sector_identified = e[0]
				} 
		});
	return sector_identified;
	}

const display_data = event => {
    const artikul_id = event.target.dataset.id;
    console.log("target.dataset", event.target.dataset);
    console.log("target id:", artikul_id);

    const selected_artikul = state.data.filter(e => e.id == artikul_id);
    console.log("selected artikul:", selected_artikul);
    document.getElementById("artikul_id").textContent = selected_artikul[0].code;
    document.getElementById("title_id").textContent = selected_artikul[0].title;
    document.getElementById("status_id").textContent = status_map[selected_artikul[0].status];
   document.getElementById("status_id").className = status_style_map[selected_artikul[0].status];
 
    const sector = selected_artikul[0].sector == " " ? get_sector_number(selected_artikul[0].code) : selected_artikul[0].sector;
    document.getElementById("sector_id").textContent = sector;
    
    document.getElementById("tag_id").textContent = selected_artikul[0].tag;
    document.getElementById("amount_id").textContent = selected_artikul[0].amount;
    document.getElementById("packaging_id").textContent = selected_artikul[0].packaging;
    document.getElementById("boxes_id").textContent = selected_artikul[0].boxes;
    //document.getElementById("baza_id").textContent = selected_artikul[0].baza;
    //document.getElementById("dop_id").textContent = selected_artikul[0].dop;
    document.getElementById("in_field_id").textContent = selected_artikul[0].in_field;
    document.getElementById("search_results").className = "hidden"; 
	document.getElementById("number_id").value = 0;
}

const url_map = {
    "code": "code",
    "title": "title"
};

const handle_input = value => {
    const radios = document.querySelectorAll("input[type='radio']");
    const search_type = Object.values(radios).filter(e => e.checked)[0].value;
            if (value.length > 3) {
                get_data(search_type, value)
            }        
        }
        
        const get_data = (search_type, value) => {
            const url = `/api/${search_type}/${value}`;
                fetch(url)
                    .then(response => response.json())
                .then(data => {
                    create_search_results_list(data);
                    state.data = data;
                }
                    )
            }
