//<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
$(document).ready(function() {
    let draggedElement = null;

    function handleDragStart(e) {
        draggedElement = this;
        e.originalEvent.dataTransfer.effectAllowed = 'move';
        e.originalEvent.dataTransfer.setData('text/html', this.innerHTML);
    }

    function handleDragOver(e) {
        e.preventDefault();
        e.originalEvent.dataTransfer.dropEffect = 'move';
        $(this).addClass('move');
        return false;
    }

    function handleDragLeave(e) {
        $(this).removeClass('move');
    }

    function handleDrop(e) {
        if (draggedElement != this) {
            draggedElement.innerHTML = this.innerHTML;
            this.innerHTML = e.originalEvent.dataTransfer.getData('text/html');
        }
        $(this).removeClass('move');
        return false;
    }

    function removeItem(e) {
        e.preventDefault();
    }

    $('.drag-drop-list > li').each(function() {
        $(this).on({
            dragstart: handleDragStart,
            dragover: handleDragOver,
            dragleave: handleDragLeave,
            drop: handleDrop,
            contextmenu: removeItem
        });
    });
});

