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

    const makeAll = (el, del) => {
        form.appendChild(make(total_forms, 'item', el.dataset.item));
        form.appendChild(make(total_forms, 'description', el.dataset.desc || ''));
        form.appendChild(make(total_forms, 'id', el.dataset.pk || ''));
        form.appendChild(make(total_forms, 'ORDER', total_forms));
        form.appendChild(make(total_forms, 'build', (el.dataset.pk) ? build : ''));

        if (del) form.appendChild(make(total_forms, 'DELETE', 'on'));

        total_forms++;
    };

    let used_pk = [];
    items.forEach((el) => {
        let pk = el.dataset.pk;
        if (pk)
            used_pk.push(pk)

        makeAll(el, false);
    });

    infos.forEach((el) => {
        if (!used_pk.includes(el.dataset.pk))
            makeAll(el, true);
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
        item.dataset.pk = el.dataset.pk;
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