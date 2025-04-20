const getCookie = (cookieName) => {
    const cookieString = document.cookie.match('(^|;) ?' + cookieName + '=([^;]*)(;|$)');
    return cookieString ? decodeURIComponent(cookieString[2]) : null;
};

const autocomplete_datalist = document.querySelector("#autocomplete-datalist");
const hero_name_input = document.querySelector("#id_hero_name");
const build_name_input = document.querySelector("#id_build_name");
var last_result = [];

const params = new URLSearchParams(document.location.search);
if (params.has("heroname")) hero_name_input.value = decodeURIComponent(params.get("heroname"));
if (params.has("buildname")) build_name_input.value = decodeURIComponent(params.get("buildname"));

hero_name_input.setAttribute("list", "autocomplete-datalist");
hero_name_input.addEventListener("input", async () => {
	const value = hero_name_input.value.trim();
	if (value.length == 0) {	
		autocomplete_datalist.innerHTML = "";
		return;
	}
	
	try {
		const response = await fetch("api/complete-hero-name", {
			method: "POST",
			body: `text=${encodeURIComponent(value)}`,
			headers: { 
				"Content-type": "application/x-www-form-urlencoded; charset=UTF-8", 
				"X-CSRFToken": getCookie("csrftoken") 
			}
		});
		
		if (!response.ok) throw new Error();
		
		const { result } = await response.json();
		if (!result || !result.trim()) return;
		
		last_result = result.split(',');
		autocomplete_datalist.innerHTML = last_result
			.map((opt) => `<option value="${opt.trim()}">`)
			.join("");
	}
	catch (err) {
		console.error(err);
	}
});
hero_name_input.addEventListener("focusout", () => {
	if (!last_result.includes(hero_name_input.value.trim()))
		hero_name_input.value = "";
});
