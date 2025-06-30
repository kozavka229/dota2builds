(() => {

function createInputs(form, prefix, items, infos) {
    const build = infos[0]?.dataset.build || '';
    let total_forms = 0;

    const make = (i, name, value) => {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = `${prefix}-${i}-${name}`;
        input.value = value;
        return input;
    };

    const makeAll = (index, el, del) => {
        form.appendChild(make(index, 'item', el.dataset.item));
        form.appendChild(make(index, 'description', el.dataset.desc));
        form.appendChild(make(index, 'ORDER', index));
        form.appendChild(make(index, 'build', build));

        const pk = infos[index]?.dataset.pk || '';
        form.appendChild(make(index, 'id', pk));

        if (del) form.appendChild(make(index, 'DELETE', 'on'));

        total_forms++;
    };

    items.forEach((el, index) => {
        makeAll(index, el, false);
    });

    infos.forEach((el, index) => {
        if (index < items.length) return;
        makeAll(index, el, true);
    });

    return total_forms;
}

function handleForm(form) {
    const items = document.querySelectorAll("#selected-items .d2mi");
    const infos = document.querySelectorAll(".forminfo");

    const total_forms = document.querySelector("input[name$=TOTAL_FORMS]");
    total_forms.value = createInputs(form, form.dataset.prefix, items, infos);

    form.submit();
    return false;
}

document.addEventListener("DOMContentLoaded", () => {
    const selectedItems = document.getElementById('selected-items');
    const items = document.getElementById('items');

    const sortable1 = new Sortable(selectedItems, {
        group: 'sharedGroup',
        animation: 50
    });

    const sortable2 = new Sortable(items, {
        group: 'sharedGroup',
        animation: 50
    });

    document.querySelectorAll(".forminfo").forEach((el, index) => {
        const item = document.querySelector(`.d2mi[data-item="${el.dataset.item}"]`);
        item.dataset.desc = el.dataset.desc;
        selectedItems.appendChild(item);
    });
});

document.querySelectorAll("#all-items i").forEach((el) => {
    el.addEventListener("click", (e) => {
        el.dataset.desc = prompt("Введите описание предмета " + el.dataset.name, el.dataset.desc || '').slice(0, 300);
        el.title = el.dataset.desc;
    });
});

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    handleForm(e.target);
});
})()